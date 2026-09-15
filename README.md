# Human Social Designer

A concept-first ChatGPT skill for creating **one polished social-media visual at a time** with the judgment of a human art director.

The skill is built for users who do not want generic “AI poster” aesthetics. Instead of starting from effects, it starts from the communication problem: What is the message? What should the viewer notice first? What is the strongest visual metaphor? Which words deserve emphasis? What can be removed?

The intended result is a social post that feels **designed**, not merely generated.

## What makes this skill different

Most image prompts describe objects and visual styles. Human Social Designer adds an art-direction layer before generation.

It deliberately controls:

- concept and visual metaphor
- hierarchy
- focal point
- whitespace
- text/image relationship
- Arabic typography behavior
- visual density
- palette discipline
- realism and lighting
- platform format
- brand consistency
- what *not* to include

The default output is **one final image**, not a gallery of half-resolved options.

## Designed for

- social-media announcements
- workshops
- hackathons
- competitions
- scholarships
- AI and robotics news
- educational posts
- awareness campaigns
- quote and idea posts
- editorial visual stories
- brand announcements
- technology campaigns
- event posters
- program promotions
- Telegram / Instagram / Facebook / LinkedIn creatives

## Design philosophy

The central rule is:

> **Idea first. Composition second. Typography third. Effects last.**

A successful post should usually be explainable as one strong visual sentence.

Examples:

- “An idea literally breaks through the box labeled ‘the familiar.’”
- “A robot hand intentionally knocks over a chess piece to represent learning through mistakes.”
- “A procrastination post is staged as a comfortable room filled with physical excuses rather than a generic clock icon.”

The skill avoids adding visual elements merely because they look expensive or futuristic.

## Human-made look

The skill actively avoids common AI-poster clichés:

- glowing robot heads
- generic brains with circuits
- random floating UI
- excessive cyan-purple neon
- meaningless microcopy
- unnecessary 3D spheres
- visually equal clutter everywhere
- dozens of explanatory icons
- random particles and light streaks
- decorative cards without information hierarchy
- repeated center-object poster templates

Instead, it uses restraint, intentional imbalance, negative space, editorial structure, and meaningful visual interaction.

## Arabic-first capability

Human Social Designer is particularly suited to Arabic social design.

It treats Arabic typography as a visual component rather than simply placing Arabic text over an image. Depending on the concept, the headline can:

- stack vertically
- change scale between words
- interact with an object
- appear partially occluded
- become a physical part of the concept
- use outline vs solid contrast
- occupy negative space
- create rhythm through line breaks

The skill favors short, visually strong Arabic headlines and avoids dense generated paragraphs inside images.

## Default output behavior

When the user gives a usable brief, the skill should:

1. understand the message
2. choose the strongest concept internally
3. determine hierarchy and art direction
4. generate one image directly
5. avoid long explanations unless requested

It should not force the user through a design questionnaire when sensible professional assumptions can be made.

## Example usage

```text
@human-social-designer
صمم لي منشور عن ورشة ذكاء اصطناعي للطلاب. أريد عنوانًا عربيًا قصيرًا، وفكرة قوية، ولا أريد الشكل التقني التقليدي.
```

```text
@human-social-designer
حوّل هذا الخبر إلى صورة سوشال ميديا واحدة، 4:5، بهوية تحريرية قوية:
[news text]
```

```text
@human-social-designer
أنشئ بوستر لهاكاثون أونلاين. المعلومات الضرورية: التسجيل مجاني، الموعد 3–10 أكتوبر، والتسليم على Devpost.
```

```text
@human-social-designer
صمم منشورًا عن التسويف. لا تستخدم ساعة عملاقة فقط؛ أريد فكرة أذكى وتحكي قصة بصرية.
```

## Repository structure

```text
human-social-designer/
├── SKILL.md
├── README.md
├── LICENSE
└── references/
    ├── design-philosophy.md
    ├── concept-playbook.md
    └── quality-checklist.md
```

`SKILL.md` is the actual skill instruction file. The reference documents expand the skill's design vocabulary and quality controls.

## Installation / importing

This repository is structured as a ChatGPT-style skill repository, with `SKILL.md` at the root.

Creating the repository alone does **not** automatically make it appear in the Skills page. Use the **+** control in the Skills interface and import/add the skill from the repository or package according to the options available in your ChatGPT UI.

After it is installed, invoke it as:

```text
@human-social-designer
```

## Version

Current skill version: **1.0.0**

## License

MIT
