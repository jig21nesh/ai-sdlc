'use strict';

// Progressive enhancement only. All content and links exist without JavaScript.
const motionToggle = document.querySelector('#motion-toggle');
const motionNote = document.querySelector('#motion-note');
const diagrams = [...document.querySelectorAll('img[data-gif]')];
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let playing = false;

function setMotion(next) {
  playing = next;
  for (const img of diagrams) img.src = playing ? img.dataset.gif : img.dataset.still;
  motionToggle.textContent = playing ? 'Pause animations' : 'Play animations';
  motionToggle.setAttribute('aria-pressed', String(playing));
  motionNote.textContent = playing
    ? 'Animations are playing. Pause replaces every GIF with its equivalent static diagram.'
    : 'Diagrams are still. Each GIF has an equivalent static diagram and a text explanation.';
}
motionToggle.hidden = false;
motionToggle.addEventListener('click', () => setMotion(!playing));
reduceMotion.addEventListener('change', event => { if (event.matches) setMotion(false); });

const stages = [...document.querySelectorAll('.stage')];
const expandButton = document.querySelector('#expand-stages');
function syncExpanded() {
  const allOpen = stages.every(stage => stage.open);
  expandButton.textContent = allOpen ? 'Collapse all modules' : 'Expand all modules';
  expandButton.setAttribute('aria-expanded', String(allOpen));
}
expandButton.hidden = false;
expandButton.addEventListener('click', () => {
  const open = !stages.every(stage => stage.open);
  stages.forEach(stage => { stage.open = open; });
  syncExpanded();
});
stages.forEach(stage => stage.addEventListener('toggle', syncExpanded));

const query = document.querySelector('#source-query');
const kind = document.querySelector('#source-kind');
const cards = [...document.querySelectorAll('.source-card')];
const count = document.querySelector('#source-count');
document.querySelector('#evidence-tools').hidden = false;
function filterSources() {
  const term = query.value.trim().toLowerCase();
  let shown = 0;
  for (const card of cards) {
    card.hidden = !((kind.value === 'all' || card.dataset.kind === kind.value) && card.dataset.search.includes(term));
    if (!card.hidden) shown++;
  }
  count.textContent = `${shown} of ${cards.length} sources`;
  document.querySelector('#source-empty').hidden = shown > 0;
}
query.addEventListener('input', filterSources);
kind.addEventListener('change', filterSources);

function revealHash() {
  let id;
  try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
  const target = document.getElementById(id);
  if (!target) return;
  if (target.classList.contains('stage')) target.open = true;
  if (target.classList.contains('source-card') && target.hidden) {
    query.value = '';
    kind.value = 'all';
    filterSources();
  }
  // Wait for details/filter layout to settle before following a deep link.
  if (target.classList.contains('stage') || target.classList.contains('source-card')) {
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  }
}
window.addEventListener('hashchange', revealHash);
document.addEventListener('click', event => {
  const link = event.target.closest('a[href^="#"]');
  if (link && link.hash === location.hash) revealHash();
});
revealHash();
