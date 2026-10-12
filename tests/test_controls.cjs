// Behavior checks for progressive-enhancement controls. No browser emulation claims.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');

class Element {
  constructor(data = {}, classes = []) {
    this.dataset = data; this.hidden = false; this.open = false; this.value = '';
    this.textContent = ''; this.attrs = {}; this.handlers = {}; this.scrolls = 0;
    this.classList = {contains: name => classes.includes(name)};
  }
  addEventListener(name, callback) { this.handlers[name] = callback; }
  setAttribute(name, value) { this.attrs[name] = value; }
  scrollIntoView() { this.scrolls++; }
  fire(name, payload = {}) { this.handlers[name]?.(payload); }
}
const elements = Object.fromEntries(['motion-toggle','motion-note','expand-stages','source-query','source-kind','source-count','evidence-tools','source-empty'].map(id => [id,new Element()]));
elements['source-kind'].value = 'all';
const stages = JSON.parse(fs.readFileSync(path.join(root, 'data/stages.json'))).map(s => {
  const e = new Element({}, ['stage']); elements[`stage-${s.id}`] = e; return e;
});
const cards = JSON.parse(fs.readFileSync(path.join(root,'research/evidence.json'))).map(s => {
  const e = new Element({kind:s.type,search:JSON.stringify(s).toLowerCase()}, ['source-card']);
  elements[`source-${s.id}`] = e; return e;
});
const diagrams = ['lifecycle','delegation','adaptation'].map(s => new Element({gif:`assets/${s}.gif`,still:`assets/${s}.png`}));
const media = new Element();
const win = new Element(); win.matchMedia = () => media;
const doc = new Element();
doc.querySelector = selector => elements[selector.slice(1)];
doc.querySelectorAll = selector => ({'.stage':stages,'.source-card':cards,'img[data-gif]':diagrams})[selector];
doc.getElementById = id => elements[id] || null;
const location = {hash:''};
vm.runInNewContext(fs.readFileSync(path.join(root,'assets/app.js'),'utf8'), {document:doc,window:win,location,requestAnimationFrame:fn=>fn()});

elements['motion-toggle'].fire('click');
assert.ok(diagrams.every(d => d.src.endsWith('.gif')));
assert.equal(elements['motion-toggle'].attrs['aria-pressed'],'true');
elements['motion-toggle'].fire('click');
assert.ok(diagrams.every(d => d.src.endsWith('.png')));
elements['motion-toggle'].fire('click');
media.fire('change',{matches:true});
assert.ok(diagrams.every(d => d.src.endsWith('.png')));
elements['expand-stages'].fire('click');
assert.ok(stages.every(s => s.open));
elements['expand-stages'].fire('click');
assert.ok(stages.every(s => !s.open));
elements['source-kind'].value = 'repository';
elements['source-kind'].fire('change');
assert.equal(cards.filter(c=>!c.hidden).length,cards.filter(c=>c.dataset.kind==='repository').length);
elements['source-query'].value = '<img src=x onerror=alert(1)>';
elements['source-query'].fire('input');
assert.equal(cards.filter(c=>!c.hidden).length,0);
assert.equal(elements['source-empty'].hidden,false);
location.hash = '#source-O08'; win.fire('hashchange');
assert.equal(elements['source-O08'].hidden,false);
assert.equal(cards.filter(c=>!c.hidden).length,cards.length);
assert.ok(elements['source-O08'].scrolls>0);
location.hash = '#stage-retire'; win.fire('hashchange');
assert.equal(elements['stage-retire'].open,true);
location.hash = '#%E0%A4%A'; assert.doesNotThrow(()=>win.fire('hashchange'));
console.log('PASS: GIF play/pause/reduced-motion change, stage expand/collapse, type filtering, empty results, literal hostile search and deep links.');
