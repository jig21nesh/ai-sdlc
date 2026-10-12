#!/usr/bin/env python3
"""Generate original, local explanatory diagrams and reduced-motion equivalents.

Dependency: Pillow 11.3.0 (Python 3.9+).
Run from any directory:
    uv run --no-project --with pillow==11.3.0 scripts/generate_gifs.py
For a sandbox, add --cache-dir /private/tmp/ai-sdlc-uv-cache after `uv run`.

No downloaded images, external fonts, telemetry, or network calls are used by
this script. The first uv invocation may download the pinned Pillow package.
Font rendering uses installed Arial or DejaVu Sans, or Pillow's bundled font.
Set AI_SDLC_FONT and AI_SDLC_FONT_BOLD to local TTF paths for identical fonts
across machines. Rendered text is 22 px or larger. All semantic content appears
in every frame and in the static PNG; animation only changes emphasis.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
WIDTH, HEIGHT = 1080, 420
SCALE = 2
FRAME_MS = 2400
COLORS = {
    "background": "#f5f9ff",
    "white": "#ffffff",
    "navy": "#112744",
    "body": "#35516f",
    "muted": "#b3c6dc",
    "line": "#8099b5",
    "blue": "#185bd6",
    "cyan": "#087a8c",
    "active": "#e2efff",
    "active_cyan": "#ddf6f7",
    "rule": "#d9e4f1",
}


def font(size: int = 22, bold: bool = False):
    """Use an existing local font; the fallback ships with Pillow."""
    candidates = [
        os.environ.get("AI_SDLC_FONT_BOLD" if bold else "AI_SDLC_FONT", ""),
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
        else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if path and Path(path).is_file():
            return ImageFont.truetype(path, size * SCALE)
    return ImageFont.load_default(size=size * SCALE)


class Diagram:
    def __init__(self, title: str, subtitle: str):
        self.image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), COLORS["background"])
        self.draw = ImageDraw.Draw(self.image)
        self.text(28, 24, title, 29, bold=True)
        self.text(28, 65, subtitle, 22, color="body")
        self.line([(28, 104), (WIDTH - 28, 104)], color="rule", width=1)

    def text(self, x, y, value, size=22, *, bold=False, color="navy", anchor="lt"):
        self.draw.text(
            (round(x * SCALE), round(y * SCALE)), value,
            font=font(size, bold), fill=COLORS[color], anchor=anchor,
        )

    def line(self, points, *, color="line", width=2):
        self.draw.line(
            [(round(x * SCALE), round(y * SCALE)) for x, y in points],
            fill=COLORS[color], width=width * SCALE, joint="curve",
        )

    def arrow(self, points, *, active=False, color=None, width=2):
        color = color or ("blue" if active else "line")
        self.line(points, color=color, width=width)
        end_x, end_y = points[-1]
        start_x, start_y = points[-2]
        angle = math.atan2(end_y - start_y, end_x - start_x)
        tip = (end_x * SCALE, end_y * SCALE)
        wing1 = ((end_x - 8 * math.cos(angle) + 4 * math.sin(angle)) * SCALE,
                 (end_y - 8 * math.sin(angle) - 4 * math.cos(angle)) * SCALE)
        wing2 = ((end_x - 8 * math.cos(angle) - 4 * math.sin(angle)) * SCALE,
                 (end_y - 8 * math.sin(angle) + 4 * math.cos(angle)) * SCALE)
        self.draw.polygon([tip, wing1, wing2], fill=COLORS[color])

    def card(self, x, y, w, h, lines, *, active=False, cyan=False):
        color = "cyan" if cyan else "blue"
        fill = "active_cyan" if cyan else "active"
        self.draw.rounded_rectangle(
            (x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE),
            radius=12 * SCALE,
            fill=COLORS[fill if active else "white"],
            outline=COLORS[color if active else "muted"],
            width=(3 if active else 1) * SCALE,
        )
        for offset, value, size, bold in lines:
            self.text(x + w / 2, y + offset, value, size, bold=bold,
                      color=color if active and bold else "navy", anchor="mt")

    def finish(self):
        return self.image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def lifecycle(step=None):
    diagram = Diagram(
        "Anthropic reference: six stages in a delivery loop",
        "Our layout uses the playbook's stage names; governance applies throughout.",
    )
    model = json.loads((ROOT / "data/reference-model.json").read_text())
    names = [stage["name"] for stage in model["stages"]]
    artifacts = ["intent", "specification", "plan + code", "checks", "review + ship", "operations"]
    active = set(range(6)) if step in (None, 3) else {step * 2, step * 2 + 1}
    card_width, gap, x0 = 154, 20, 28
    for i, (name, artifact) in enumerate(zip(names, artifacts)):
        x = x0 + i * (card_width + gap)
        diagram.card(x, 135, card_width, 112, [
            (17, name, 22, False),
            (62, artifact, 22, False),
        ], active=i in active)
        if i < 5:
            diagram.arrow([(x + card_width + 3, 191), (x + card_width + gap - 3, 191)],
                          active=i in active)
    feedback = step in (None, 3)
    diagram.arrow([(975, 249), (975, 289), (105, 289), (105, 251)],
                  active=feedback, color="cyan" if feedback else "line", width=3)
    # White backing keeps the return-path caption readable without hiding nodes.
    diagram.draw.rectangle((260 * SCALE, 270 * SCALE, 820 * SCALE, 307 * SCALE),
                           fill=COLORS["background"])
    diagram.text(540, 277, "Operations inform the next intent", 22,
                 color="cyan" if feedback else "body", anchor="mt")
    diagram.text(28, 334, "Delivery flow and adoption dependencies are different views.", 24, bold=True)
    diagram.text(28, 377, "The guide maps our detailed work modules onto these six stages.", 22, color="body")
    return diagram.finish()


def delegation(step=None):
    diagram = Diagram(
        "Optional helpers; verification follows the candidate.",
        "An original toolkit example, not Anthropic's adoption-dependency diagram.",
    )
    all_active = step is None
    coord = all_active or step == 0
    workers = all_active or step == 1
    review = all_active or step == 2
    action = all_active or step == 3
    diagram.card(28, 173, 185, 124, [
        (15, "Coordinator", 24, True),
        (55, "scope + budget", 22, False),
        (86, "edit ownership", 22, False),
    ], active=coord)
    diagram.line([(214, 235), (235, 235)], color="blue" if workers else "line")
    diagram.line([(235, 194), (235, 274)], color="blue" if workers else "line")
    for y, label in [(164, "Research"), (244, "Risk analysis")]:
        diagram.arrow([(235, y + 30), (262, y + 30)], active=workers)
        diagram.card(264, y, 175, 60, [(16, label, 22, True)], active=workers)
        diagram.line([(440, y + 30), (470, y + 30)], color="blue" if review else "line")
    diagram.line([(470, 194), (470, 274)], color="blue" if review else "line")
    diagram.arrow([(470, 234), (500, 234)], active=review)
    diagram.card(502, 173, 228, 124, [
        (13, "Build + self-check", 22, True),
        (54, "change + test", 22, False),
        (86, "repeat within scope", 22, False),
    ], active=review)
    diagram.arrow([(733, 235), (783, 235)], active=action)
    diagram.card(786, 173, 266, 124, [
        (15, "Independent review", 22, True),
        (55, "if policy requires", 22, False),
        (86, "candidate + evidence", 22, False),
    ], active=action, cyan=True)
    diagram.text(28, 359, "Dependent checks wait for their inputs. Parallelize only independent work.", 22, color="body")
    diagram.text(28, 393, "Runtime controls enforce access; a role brief cannot grant authority.", 22, color="body")
    return diagram.finish()


def adaptation(step=None):
    diagram = Diagram(
        "Reuse the workflow. Configure the context.",
        "Stable stage contracts travel across organizations, projects and agent tools.",
    )
    columns = [
        (28, 236, "Invariant core", ["stage contracts", "skills + artifacts", "evidence format"]),
        (300, 236, "Org policy", ["risk + data rules", "owners + authority", "retention"]),
        (572, 236, "Project facts", ["stack + commands", "architecture", "environments"]),
        (850, 202, "Runtime", ["permissions", "sandbox + CI", "adapters"]),
    ]
    for i, (x, w, title, details) in enumerate(columns):
        lines = [(18, title, 25, True)] + [
            (65 + j * 34, item, 22, False) for j, item in enumerate(details)
        ]
        diagram.card(x, 136, w, 181, lines,
                     active=step is None or step == i, cyan=i == 3)
        if i in (0, 1):
            diagram.text(x + w + 18, 213, "+", 30, color="body", anchor="mt")
        elif i == 2:
            diagram.arrow([(x + w + 5, 226), (844, 226)], active=step in (None, 3))
    diagram.text(28, 344, "Policy informs agents; runtime controls enforce permissions.", 24, bold=True)
    diagram.text(28, 386, "Change org and project profiles, then validate the tool adapters.", 22, color="body")
    return diagram.finish()


ANIMATIONS = {
    "lifecycle": {
        "title": "Anthropic six-stage reference",
        "alt": "Plan, Design, Build, Test, Deploy and Maintain form a loop. Implementation planning is part of Build. This layout uses the article's stage names, not its adoption graph.",
        "caption": "Reference stage names, original layout. Module assignments and additional governance/retirement coverage are our synthesis.",
        "frames": ["Plan and Design", "Build and Test", "Deploy and Maintain", "Feedback to Plan"],
    },
    "delegation": {
        "title": "Bounded agent delegation",
        "alt": "A coordinator assigns independent research and risk analysis, integrates their results into implementation with continuous checks, then obtains independent candidate review when policy requires it.",
        "caption": "An optional toolkit workflow. Continuous self-checking and independent candidate review serve different purposes; dependent work is sequential.",
        "frames": ["Coordinator sets scope", "Independent helpers investigate", "Implementation checks the change", "Independent candidate review when required"],
    },
    "adaptation": {
        "title": "A portable core with local configuration",
        "alt": "Invariant stage contracts combine with organization policy and project facts. Runtime permissions, sandboxing, CI checks and adapters enforce the configured boundaries.",
        "caption": "Keep the core portable. Configure organization policy and project facts, then enforce boundaries through runtime controls and tool adapters.",
        "frames": ["Invariant core", "Organization policy", "Project facts", "Runtime enforcement and adapters"],
    },
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, render in [("lifecycle", lifecycle), ("delegation", delegation), ("adaptation", adaptation)]:
        frames = [render(step) for step in range(4)]
        # A shared palette avoids changes in antialiased text colors between frames.
        palette = render().quantize(colors=255, method=Image.Quantize.MEDIANCUT)
        indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
        gif_path = OUT / f"{name}.gif"
        png_path = OUT / f"{name}.png"
        indexed[0].save(gif_path, save_all=True, append_images=indexed[1:],
                        duration=FRAME_MS, loop=0, disposal=2, optimize=False)
        render().save(png_path, optimize=True)
        with Image.open(gif_path) as gif:
            assert gif.format == "GIF" and gif.n_frames == 4
            assert gif.size == (WIDTH, HEIGHT) and gif.info.get("loop") == 0
            for frame in range(gif.n_frames):
                gif.seek(frame)
                assert gif.info["duration"] == FRAME_MS
                assert gif.convert("RGB").getbbox() is not None
        with Image.open(png_path) as png:
            assert png.size == (WIDTH, HEIGHT) and png.format == "PNG"
            assert png.getbbox() is not None
        assert gif_path.stat().st_size > 1000 and png_path.stat().st_size > 1000
        ANIMATIONS[name].update({
            "gif": f"assets/{name}.gif", "static": f"assets/{name}.png",
            "width": WIDTH, "height": HEIGHT, "frame_duration_ms": FRAME_MS,
            "loop": True, "semantic_content_identical_in_static": True,
        })
        print(f"Validated {name}: 4 frames, {WIDTH}x{HEIGHT}, looping GIF + static PNG")
    (OUT / "animations.json").write_text(json.dumps(ANIMATIONS, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
