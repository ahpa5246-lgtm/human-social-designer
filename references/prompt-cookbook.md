# Prompt Cookbook

This file describes how to turn a resolved art direction into a strong image-generation instruction.

The goal is not to expose a prompt to the user by default. The goal is to help the skill internally construct better generation language.

## Prompt anatomy

A resolved generation instruction should usually contain these layers:

1. **format / medium**
2. **single visual concept**
3. **hero subject**
4. **composition / crop / focal point**
5. **negative space / typography zone**
6. **color atmosphere**
7. **lighting / material**
8. **typography behavior**
9. **quality target**
10. **explicit exclusions**

## Template

> Create one premium [format] social poster. The concept is [one-sentence metaphor]. Use one unmistakable hero: [subject]. Compose it [framing/crop/position], leaving [negative-space zone] for a short [Arabic/English] headline. Use [dominant palette] with [secondary/accent]. Lighting is [direction/quality]. Materials feel [tactile/architectural/photographic/etc]. Typography should [behavior] and remain minimal. The result should feel like [editorial/cultural/conceptual advertising reference class], not a generic AI poster. Avoid [specific clichés].

## Example: hackathon / opportunity

Weak prompt:

> Make a futuristic AI hackathon poster with students, laptops, icons, city, tracks, GitHub, Devpost and prizes.

Stronger internal direction:

> Create one premium 4:5 conceptual campaign poster about entering an AI hackathon as a threshold into a larger future. Use one monumental dark architectural portal as the hero, opening onto a luminous distant path and a single impossible vertical structure. Deep midnight navy world, restrained warm gold light, quiet teal reflections. Keep most of the left side as negative space. Use only the event title and one very short Arabic hook; no track list, no icon grid, no dense details. Cinematic architectural photography / high-end CGI hybrid, controlled realism, one light direction, strong silhouette. Avoid robots, laptops, holograms, neon startup graphics, floating UI, generic futuristic skyline clutter.

## Example: procrastination

Weak prompt:

> Make a productivity poster with a clock, checklist, laptop, coffee, sticky notes and phone.

Stronger internal direction:

> Create one bold surreal editorial poster about procrastination. One human figure in a monochrome violet suit sits calmly, but their head is replaced by a large vintage alarm clock; they hold a long blade across the shoulder like a ceremonial object. Flat saturated violet environment, very few props, strong silhouette, dramatic negative space, one short Arabic headline integrated beside the figure. Premium fashion-editorial lighting, strange but controlled. Avoid desk scenes, laptops, coffee, floating icons, checklists, visual clutter.

## Example: learning from mistakes

> Create one quiet premium 4:5 editorial poster. A precise robotic hand holds a white chess knight above a board while a black king lies fallen in the foreground. Warm cream architectural space, deep blue typography, subtle teal accent, long shadows, generous empty upper-right area for the headline. The message is that error can be an intentional move in learning. Minimal copy. Avoid circuit graphics, robot faces, holograms, warning icons and generic tech decoration.

## Negative prompting principle

Exclusions should be topic-specific.

Do not dump the same long negative list into every prompt.

Choose the 4–8 clichés most likely to appear for that brief.

## Quality language

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

Less useful by itself:
- beautiful
- amazing
- professional
- cool
- modern

These adjectives need concrete art-direction instructions around them.
