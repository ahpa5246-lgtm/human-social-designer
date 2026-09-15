# Human Social Designer

A strict concept-first ChatGPT skill for creating **one premium social-media key visual at a time** with the judgment of a senior human art director.

Version 3 is intentionally opinionated. It is designed to prevent the exact failure mode of dense AI-generated event flyers: title + paragraphs + icon grids + students + futuristic city + CTA + every fact in the brief.

## v3 default behavior

Every brief is reduced to:

- one core message
- one emotional idea
- one visual metaphor
- one dominant hero object / scene
- one short headline
- almost no secondary copy

Then the skill generates **one final image directly**.

The default is **Conceptual Key Visual Mode**, not an informational flyer.

## Hard rule

Unless the user explicitly asks for a detailed information poster or infographic, the image should NOT contain:

- track lists
- requirements lists
- benefits grids
- certificate modules
- tool lists
- multiple CTAs
- rows of icons
- long paragraphs
- every fact from the source brief

Those details belong in the caption.

## What it aims for

- unusual but intelligent imagery
- one unmistakable hero
- editorial negative space
- strong silhouette
- sculptural / photographic / architectural / illustrative art direction chosen per brief
- controlled surrealism
- beautiful Arabic display typography
- one coherent color world
- minimal copy
- Pinterest-worthy campaign quality

## What it rejects

- generic AI-startup visuals
- students + laptops as universal shorthand
- groups staring at a glowing future
- futuristic cities by default
- portals by default
- robots merely because the topic is AI
- icon grids
- glass cards
- glowing brains
- random particles
- walls of text
- literal illustration of every bullet

## Repository structure

```text
human-social-designer/
├── SKILL.md
├── README.md
├── LICENSE
├── examples/
│   ├── README.md
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
    ├── reference-analysis.md
    └── failure-analysis.md
```

The SVG files are visual studies only. They are **not literal prompt templates** and should never be mechanically reused.

## Example invocation

```text
@human-social-designer
حول هذا المنشور إلى key visual واحد. أريد فكرة غريبة وذكية، عنوانًا قصيرًا فقط، ولا تضع التفاصيل في الصورة.
```

```text
@human-social-designer
صمم بوستر عن التسويف بأسلوب editorial / Pinterest. استخدم مشهدًا واحدًا غير متوقع ولا تستخدم أيقونات أو قوائم.
```

## Important: updating the GitHub repo vs updating the installed skill

Editing this GitHub repository does **not necessarily refresh an already imported/installed copy of the skill** inside ChatGPT.

After a major repository update, re-import / reinstall / refresh the skill from the repository in the Skills UI so ChatGPT loads the current `SKILL.md`.

If an old result still behaves like a dense flyer after v3, first verify that the installed skill has been refreshed.

## Version

**3.0.0**

## License

MIT
