# Prompt Cookbook — v3

This reference explains how to turn a resolved art direction into a strong image-generation instruction **without anchoring the model to repeated literal objects**.

The skill should never copy an example object from this repository just because it exists here.

## Core rule

A good generation instruction describes **relationships, composition, material, hierarchy, atmosphere, and exclusions** — not a shopping list of topic-associated objects.

## Prompt anatomy

A resolved internal generation instruction should usually contain:

1. **format / medium**
2. **one-sentence visual concept**
3. **one hero subject or scene**
4. **composition / crop / focal point**
5. **negative-space zone**
6. **color atmosphere**
7. **lighting / material language**
8. **typography behavior**
9. **quality target**
10. **topic-specific exclusions**

## Neutral template

> Create one premium [format] social key visual. The concept is [single visual metaphor]. Use one unmistakable hero: [subject/scene]. Compose it [position/crop/scale], with intentional negative space in [zone] for a short headline. Use [dominant color family], [controlled secondary], and [restrained accent]. Lighting is [single coherent direction/quality]. Materials feel [tactile/architectural/photographic/sculptural/etc]. Typography should be minimal, integrated, and subordinate to the concept. The result should feel like premium editorial art direction / conceptual advertising, not a generic AI poster. Avoid [4–8 topic-specific clichés].

## Anti-enumeration rule

Do not convert source bullets into visual bullets.

If the brief contains:
- 6 tracks
- 5 benefits
- 4 requirements
- 3 dates
- 2 links

The generation instruction should still normally describe:
- 1 concept
- 1 hero
- 1 headline
- 0–1 micro-line

The other facts remain outside the image unless the user explicitly requests an information poster.

## Event brief transformation

Instead of prompting:

> Show the event title, students, team size, date, registration, GitHub, Devpost, certificate, tracks, prizes, CTA and a futuristic city.

Do this internally:

> Identify what the event *means* emotionally or strategically, invent one metaphor for that meaning, and build a key visual around only that metaphor.

Do not use a portal, city, student group, robot, laptop, or light bulb automatically. Those are not defaults.

## Topic-specific exclusions

Exclusions should be chosen from the brief, not copied mechanically.

Examples of exclusion categories:
- obvious category stereotypes
- redundant props
- UI-like information cards
- decorative technology symbols
- excessive text
- multiple focal points
- duplicate metaphors
- visual effects that do not change meaning

## Quality language that helps

Useful:
- premium editorial key visual
- conceptual advertising
- sculptural studio composition
- cultural poster
- architecture-magazine restraint
- controlled surrealism
- high-end campaign photography
- tactile materials
- coherent single-source lighting
- intentional negative space
- one memorable silhouette
- typography integrated into composition

Weak by itself:
- beautiful
- amazing
- professional
- cool
- modern

These adjectives need concrete art-direction decisions around them.

## Final test

Before sending the internal generation instruction, remove every sentence that merely restates the source brief.

What remains should describe **the image**, not the document.
