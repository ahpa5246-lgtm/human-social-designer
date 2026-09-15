# Human Social Designer

A concept-first ChatGPT skill for creating **one premium social-media key visual at a time** with the judgment of a senior human art director.

This repository is designed for users who want social images that feel like **Pinterest-worthy editorial posters, conceptual advertising, cultural campaigns, sophisticated brand key visuals, and modern Arabic art direction** — not generic AI posters or dense information flyers.

## What changed in v2

Version 2 shifts the default behavior from “make a nice social poster” to:

> **distill the brief → invent one visual metaphor → suppress information → compose one hero → use minimal typography → generate one memorable image**

This means a hackathon brief with ten facts no longer automatically becomes ten icons and six boxes. A workshop brief no longer automatically becomes a student with a laptop. An AI topic no longer automatically becomes a robot.

The default is now **Conceptual Key Visual Mode**.

## Core philosophy

**Idea first. Composition second. Typography third. Effects last.**

The skill silently reduces every brief to:

- one core message
- one emotional idea
- one metaphor
- one hero object / scene
- one short headline

Then it removes anything that does not earn its place.

## What the skill deliberately avoids

- generic “AI startup” visuals
- people with laptops as a universal solution
- floating app icons
- glowing brains
- robot-human handshakes
- glass cards for decoration
- excessive cyan/purple neon
- random particles
- dense event flyers by default
- walls of text
- icon grids where a visual idea should exist
- multiple focal points
- literal illustration of every bullet in a brief

## What it aims for instead

- strange but intelligent imagery
- one unmistakable hero
- editorial negative space
- sculptural / architectural / photographic art direction
- controlled surrealism
- strong Arabic display typography
- short copy
- coherent color atmosphere
- memorable silhouette
- professional human authorship

## Typical use cases

- Instagram / Telegram / Facebook campaign posts
- hackathon and workshop promotion
- AI / robotics / engineering news visuals
- opportunities and scholarships
- awareness campaigns
- editorial quote posts
- brand announcements
- social campaign key visuals
- premium Arabic poster design

## Repository structure

```text
human-social-designer/
├── SKILL.md
├── README.md
├── LICENSE
├── examples/
│   ├── README.md
│   ├── 01-portal-opportunity.svg
│   ├── 02-time-cuts.svg
│   └── 03-mistake-chess.svg
└── references/
    ├── design-philosophy.md
    ├── concept-playbook.md
    ├── quality-checklist.md
    ├── anti-patterns.md
    ├── poster-modes.md
    ├── arabic-typography.md
    ├── prompt-cookbook.md
    └── reference-analysis.md
```

The SVG examples are **concept diagrams / art-direction references**, not templates to copy literally. Their purpose is to show how one idea, one focal point, and minimal copy can outperform an overloaded flyer.

The reference documents provide the decision system behind the skill: what to reject, how to choose a poster mode, how to treat Arabic typography, how to build a generation prompt, and how to analyze inspiration without copying it.

## Example invocation

```text
@human-social-designer
صمم لي منشور عن ورشة ذكاء اصطناعي للطلاب. أريد صورة غريبة وذكية، أقل قدر ممكن من الكلام، وبدون روبوتات أو لابتوبات بشكل مبتذل.
```

```text
@human-social-designer
حول هذا الهاكاثون إلى key visual واحد. لا أريد كل الشروط داخل التصميم؛ اختر أقوى فكرة واكتب فقط العنوان ومعلومة واحدة أساسية.
```

```text
@human-social-designer
صمم بوستر عن التسويف بأسلوب Pinterest احترافي. استخدم مشهدًا واحدًا غريبًا بدل مجموعة أيقونات.
```

## The key difference

A normal poster generator asks:

> “What objects belong to this topic?”

Human Social Designer asks:

> **“What one image would make this message unforgettable?”**

## Installation

The actual skill instruction is in `SKILL.md` at the repository root.

After importing / installing the repository as a ChatGPT skill, invoke it as:

```text
@human-social-designer
```

## Version

**2.0.0**

## License

MIT
