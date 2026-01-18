# Prompt Engineering Template Library

*January 2026 Edition*

The definitive copy-paste library of production-tested prompts for every major video AI model.

---

## Table of Contents

1. [Universal Prompt Architecture](#universal-prompt-architecture)
2. [Veo 3.1 Templates](#veo-31-templates)
3. [Kling 2.6 Templates](#kling-26-templates)
4. [Sora 2 Pro Templates](#sora-2-pro-templates)
5. [Runway Gen-4.5 Templates](#runway-gen-45-templates)
6. [Wan 2.6 Templates](#wan-26-templates)
7. [Seedance 1.5 Pro Templates](#seedance-15-pro-templates)
8. [LTX-2 Templates](#ltx-2-templates)
9. [Hailuo 02 Templates](#hailuo-02-templates)
10. [Negative Prompt Library](#negative-prompt-library)
11. [Advanced Techniques](#advanced-techniques)
12. [Failure Mode Prevention](#failure-mode-prevention)

---

## Universal Prompt Architecture

### The Five-Layer Structure

All effective video prompts follow this mental model, regardless of model-specific syntax:

```
Layer 1: SUBJECT     → Who/what is the focus?
Layer 2: ACTION      → What movement/behavior occurs?
Layer 3: ENVIRONMENT → Where does this happen?
Layer 4: STYLE       → What aesthetic/mood?
Layer 5: TECHNICAL   → Camera, duration, quality parameters
```

### Quality Modifiers (Universal)

**Resolution Boosters:**
- `highly detailed`, `sharp focus`, `8K resolution`
- `professional quality`, `cinematic`, `masterpiece`

**Motion Enhancers:**
- `smooth motion`, `fluid movement`, `natural dynamics`
- `physically accurate`, `realistic physics`

**Consistency Anchors:**
- `consistent lighting`, `stable composition`
- `coherent style throughout`, `uniform character design`

---

## Veo 3.1 Templates

### JSON Schema

```json
{
  "prompt": {
    "subject": "string - primary focus",
    "action": "string - motion description",
    "scene": "string - environment details",
    "style": "string - aesthetic direction",
    "technical": {
      "camera_motion": ["array of movements"],
      "duration": "number - seconds",
      "aspect_ratio": "16:9 | 9:16 | 1:1",
      "audio": {
        "dialogue": "string - spoken words",
        "sfx": "string - sound effects",
        "music": "string - background score"
      }
    }
  },
  "negative_prompt": "string - what to avoid"
}
```

### Template 1: Cinematic Dialogue Scene

```json
{
  "prompt": {
    "subject": "A weathered detective in a noir trench coat, mid-40s, silver stubble",
    "action": "Leans forward across a steel interrogation table, speaking intensely",
    "scene": "Dimly lit police interrogation room, single overhead lamp casting harsh shadows, one-way mirror reflecting",
    "style": "Neo-noir cinematography, high contrast, desaturated colors with teal highlights, Fincher-esque",
    "technical": {
      "camera_motion": ["slow dolly in", "rack focus from subject to mirror"],
      "duration": 5,
      "aspect_ratio": "2.39:1",
      "audio": {
        "dialogue": "You know exactly where she went. Don't you.",
        "sfx": "Chair scraping, clock ticking, air conditioning hum",
        "music": "Minimal synth drone, building tension"
      }
    }
  },
  "negative_prompt": "cartoon, anime, bright colors, happy mood, daylight, amateur quality"
}
```

### Template 2: Product Hero Shot

```json
{
  "prompt": {
    "subject": "Sleek wireless earbuds, matte black with chrome accents, floating",
    "action": "Rotating slowly, case opening to reveal earbuds which lift out magnetically",
    "scene": "Pure black void with subtle gradient, volumetric light rays from upper left",
    "style": "Apple-style product photography, minimalist, premium feel, studio lighting",
    "technical": {
      "camera_motion": ["orbital 360", "macro zoom on charging contacts"],
      "duration": 6,
      "aspect_ratio": "16:9",
      "audio": {
        "sfx": "Subtle magnetic click, satisfying snap, gentle whoosh",
        "music": "Ambient electronic, clean and modern"
      }
    }
  },
  "negative_prompt": "hands, human presence, dust, scratches, fingerprints, cluttered background"
}
```

### Template 3: Nature Documentary

```json
{
  "prompt": {
    "subject": "Massive humpback whale, barnacles on skin, water streaming off fins",
    "action": "Breaching in slow motion, twisting body mid-air, crashing back into ocean",
    "scene": "Open Pacific Ocean at golden hour, scattered clouds, distant island silhouette",
    "style": "BBC Planet Earth cinematography, 240fps slow motion aesthetic, National Geographic quality",
    "technical": {
      "camera_motion": ["tracking shot following breach", "pull back to reveal scale"],
      "duration": 8,
      "aspect_ratio": "21:9",
      "audio": {
        "sfx": "Massive water explosion, cascading splash, whale exhale",
        "music": "Orchestral swell, Hans Zimmer-style epic"
      }
    }
  },
  "negative_prompt": "boats, humans, pollution, cartoon whale, unrealistic colors"
}
```

---

## Kling 2.6 Templates

### Beats Syntax Format

```
[0:00-0:02] Scene setup description
[0:02-0:04] Action beat one
[0:04-0:06] Action beat two
...

STYLE: aesthetic direction
CAMERA: movement specification
MOTION_SCALE: 1-10
NEGATIVE: what to avoid
```

### Template 1: Action Sequence

```
[0:00-0:01] A masked ninja in black tactical gear crouches on a Tokyo rooftop at night, neon signs glowing below
[0:01-0:03] Ninja leaps across gap between buildings, cape flowing, landing in a roll
[0:03-0:05] Quick draw of katana, blade catching moonlight, defensive stance

STYLE: John Wick cinematography, blue-orange color grade, rain-slicked surfaces
CAMERA: tracking shot following jump, whip pan to sword draw
MOTION_SCALE: 8
NEGATIVE: daylight, cartoon, slow motion, static camera, western buildings
```

### Template 2: Fashion Runway

```
[0:00-0:02] Model emerges from darkness, avant-garde geometric dress in silver, spotlight hitting
[0:02-0:04] Confident stride down white runway, fabric catching light with each step
[0:04-0:05] Dramatic pause and turn at end of runway, dress movement settling

STYLE: Vogue editorial, high fashion photography, Alexander McQueen aesthetic
CAMERA: low angle tracking shot, frontal to three-quarter view
MOTION_SCALE: 5
NEGATIVE: casual clothing, poor posture, audience visible, backstage elements
```

### Template 3: Food Commercial

```
[0:00-0:02] Burger ingredients suspended in air: brioche bun, lettuce, tomato, beef patty with sizzle
[0:02-0:04] Ingredients descend in slow motion, cheese melting as it touches hot patty
[0:04-0:05] Final assembly lands on wooden board, steam rising, sesame seeds falling

STYLE: McDonald's commercial quality, food photography lighting, appetizing color grade
CAMERA: macro orbital shot, slow descent tracking
MOTION_SCALE: 4
NEGATIVE: real restaurant setting, hands, utensils, cold food appearance
```

---

## Sora 2 Pro Templates

### Shot-List Structure

```json
{
  "scenes": [
    {
      "scene_id": 1,
      "duration_frames": 120,
      "description": "scene content",
      "camera": "camera specification",
      "transition_out": "cut | dissolve | wipe"
    }
  ],
  "global_style": "overall aesthetic",
  "aspect_ratio": "16:9",
  "fps": 24
}
```

### Template 1: Multi-Shot Narrative

```json
{
  "scenes": [
    {
      "scene_id": 1,
      "duration_frames": 72,
      "description": "Wide establishing shot: A lone astronaut stands on Mars surface, red dust swirling, Earth visible as small dot in purple sky",
      "camera": "static wide, slight push in",
      "transition_out": "dissolve"
    },
    {
      "scene_id": 2,
      "duration_frames": 48,
      "description": "Medium shot: Astronaut's helmet visor reflects the barren landscape, breath fogging inside",
      "camera": "slow orbital around helmet",
      "transition_out": "cut"
    },
    {
      "scene_id": 3,
      "duration_frames": 72,
      "description": "Close-up: Gloved hand reaches down, picks up a small green plant sprouting from red soil",
      "camera": "tilt up from plant to astronaut face",
      "transition_out": "fade to black"
    }
  ],
  "global_style": "The Martian cinematography, Denis Villeneuve color palette, IMAX quality, emotionally resonant",
  "aspect_ratio": "2.39:1",
  "fps": 24
}
```

### Template 2: Commercial Spot (15-Second)

```json
{
  "scenes": [
    {
      "scene_id": 1,
      "duration_frames": 36,
      "description": "Problem: Person struggling with tangled wired earbuds on crowded subway",
      "camera": "handheld medium shot, slightly chaotic",
      "transition_out": "quick cut"
    },
    {
      "scene_id": 2,
      "duration_frames": 24,
      "description": "Solution reveal: Same person, now in park, puts in sleek wireless earbuds",
      "camera": "smooth dolly, product hero shot",
      "transition_out": "cut"
    },
    {
      "scene_id": 3,
      "duration_frames": 36,
      "description": "Lifestyle: Person jogging freely, music visualization waves emanating from ears",
      "camera": "tracking alongside, golden hour light",
      "transition_out": "cut"
    },
    {
      "scene_id": 4,
      "duration_frames": 24,
      "description": "Logo card: Product floating on white, brand name fades in",
      "camera": "static, subtle zoom",
      "transition_out": "fade"
    }
  ],
  "global_style": "Apple commercial aesthetic, clean transitions, lifestyle aspirational",
  "aspect_ratio": "16:9",
  "fps": 30
}
```

---

## Runway Gen-4.5 Templates

### Timeline Array Format

```json
{
  "prompt": "base description",
  "timeline": [
    {
      "frame_range": [0, 60],
      "keyframe_mode": true,
      "camera_path": {
        "start": {"position": [x,y,z], "rotation": [rx,ry,rz]},
        "end": {"position": [x,y,z], "rotation": [rx,ry,rz]}
      },
      "motion_intensity": 0.0-1.0
    }
  ],
  "style_reference": "URL or description",
  "motion_reference": "URL or description"
}
```

### Template 1: Professional Motion Control

```json
{
  "prompt": "Hyperrealistic CGI dragon perched on medieval castle tower, scales iridescent green-gold, wings folded, breathing visible in cold air, stormy sky background",
  "timeline": [
    {
      "frame_range": [0, 45],
      "keyframe_mode": true,
      "camera_path": {
        "start": {"position": [0, -50, 20], "rotation": [15, 0, 0]},
        "end": {"position": [0, 0, 5], "rotation": [0, 0, 0]}
      },
      "motion_intensity": 0.3,
      "description": "Dramatic push in revealing dragon"
    },
    {
      "frame_range": [45, 90],
      "keyframe_mode": true,
      "camera_path": {
        "start": {"position": [0, 0, 5], "rotation": [0, 0, 0]},
        "end": {"position": [30, 0, 5], "rotation": [0, -20, 0]}
      },
      "motion_intensity": 0.5,
      "description": "Orbital to three-quarter view, dragon turns head"
    },
    {
      "frame_range": [90, 120],
      "keyframe_mode": true,
      "camera_path": {
        "start": {"position": [30, 0, 5], "rotation": [0, -20, 0]},
        "end": {"position": [30, 0, 0], "rotation": [0, -20, 5]}
      },
      "motion_intensity": 0.7,
      "description": "Dragon spreads wings, camera tilts up"
    }
  ],
  "style_reference": "Game of Thrones dragon design, Industrial Light & Magic quality",
  "negative_prompt": "cartoon, cute dragon, bright colors, clear sky, modern elements"
}
```

### Template 2: Music Video Effect

```json
{
  "prompt": "Singer in center frame, black background, neon light trails following hand gestures, 80s synthwave aesthetic",
  "timeline": [
    {
      "frame_range": [0, 30],
      "motion_intensity": 0.4,
      "description": "Hands at rest, lights dimming in"
    },
    {
      "frame_range": [30, 60],
      "motion_intensity": 0.8,
      "description": "Arms raise, light trails explode outward"
    },
    {
      "frame_range": [60, 90],
      "motion_intensity": 1.0,
      "description": "Full choreography, trails create geometric patterns"
    }
  ],
  "style_reference": "The Weeknd Blinding Lights music video, Bruno Mars 24K Magic",
  "motion_reference": "Contemporary dance isolations, tutting"
}
```

---

## Wan 2.6 Templates

### MoE-Aware Multi-Shot Syntax

```
SHOT 1: [description] --expert anime
SHOT 2: [description] --expert anime
TRANSITION: [type]

SUBJECT_ANCHOR: consistent element description
STYLE_TOKENS: comma-separated style hints
NEGATIVE: avoidance terms
```

### Template 1: Anime Action Sequence

```
SHOT 1: Close-up of determined eyes, anime girl with silver hair, wind blowing strands across face, sunset reflection in pupils --expert anime
SHOT 2: Full body, same girl in mecha pilot suit, running toward giant robot silhouette, dust kicking up --expert anime
SHOT 3: Cockpit interior, hands gripping controls, holographic displays activating around her --expert anime
TRANSITION: dynamic cuts, speed lines

SUBJECT_ANCHOR: Silver-haired girl, age 17, violet eyes, angular face, pilot suit with blue accents
STYLE_TOKENS: Makoto Shinkai lighting, Trigger Studio action, high detail animation, 2D with 3D depth
NEGATIVE: 3D render, western cartoon, chibi, deformed hands, static pose, poor anatomy
```

### Template 2: Stylized Landscape

```
SHOT 1: Dawn breaks over floating islands, bioluminescent plants pulsing, waterfalls flowing upward --expert fantasy
SHOT 2: Camera pushes through cloud layer, revealing ancient temple on central island --expert fantasy
SHOT 3: Slow pan across temple interior, light beams through crystal ceiling, dust particles floating --expert fantasy
TRANSITION: smooth dissolves

SUBJECT_ANCHOR: Floating island ecosystem, impossible physics, ancient civilization remnants
STYLE_TOKENS: Studio Ghibli environment design, Breath of the Wild aesthetic, painterly rendering
NEGATIVE: realistic physics, modern elements, human figures, ground-based landscape
```

### Template 3: Character Introduction

```
SHOT 1: Silhouette in doorway, backlit, trench coat flowing, only glowing cybernetic eye visible --expert cyberpunk
SHOT 2: Side profile walking, neon signs reflecting off metallic arm, rain streaming --expert cyberpunk
SHOT 3: Frontal medium shot, face revealed, scarred but confident expression, lighter igniting cigarette --expert cyberpunk
TRANSITION: hard cuts with frame flash

SUBJECT_ANCHOR: Cyberpunk mercenary, late 30s, half-face cybernetic, military-style coat, right arm full chrome
STYLE_TOKENS: Blade Runner 2049 cinematography, Ghost in the Shell character design, volumetric neon
NEGATIVE: bright daylight, clean appearance, fantasy elements, happy expression, anime face
```

---

## Seedance 1.5 Pro Templates

### Four-Layer Structure with Audio Reactivity

```
SUBJECT: [character/object description]
MOTION: [choreography/movement with beat markers]
ENVIRONMENT: [setting with lighting dynamics]
STYLE: [aesthetic direction with audio-reactive elements]

AUDIO_SYNC:
  BPM: number
  DOWNBEAT_ACTIONS: [list of emphasized moves]
  ENERGY_CURVE: description of intensity over time
```

### Template 1: Dance Performance

```
SUBJECT: Professional dancer in flowing white dress, bare feet, athletic build, hair in motion

MOTION:
  [BEAT 1] Arms sweep upward, dress fabric follows
  [BEAT 2] Spin with dress expansion, hair whip
  [BEAT 3] Drop to floor, controlled descent
  [BEAT 4] Rise with body wave, arm extension
  [BEATS 5-8] Repeat pattern with increasing intensity

ENVIRONMENT: Empty white cyclorama studio, soft overhead light, minimal shadow for clean silhouette

STYLE: Contemporary dance film, Sia Chandelier aesthetic, emotional movement, fabric physics emphasis

AUDIO_SYNC:
  BPM: 120
  DOWNBEAT_ACTIONS: [spin initiation, floor contact, rise apex]
  ENERGY_CURVE: Build from controlled to explosive over 8 beats
```

### Template 2: Music Video Choreography

```
SUBJECT: Five dancers in synchronized formation, urban streetwear, diverse casting, confident expressions

MOTION:
  [VERSE] Sharp isolations, head movements on snare hits
  [PRE-CHORUS] Formation shift, ripple effect across group
  [CHORUS] Full energy, jumping, arm choreography in unison
  [BREAKDOWN] Solo dancer center, others freeze as background

ENVIRONMENT: Abandoned warehouse, dramatic side lighting, haze in air, graffiti walls

STYLE: K-pop production quality, BTS choreography precision, high contrast lighting, hip-hop foundation

AUDIO_SYNC:
  BPM: 128
  DOWNBEAT_ACTIONS: [formation changes, unison hits, solo transitions]
  ENERGY_CURVE: 60% verse → 80% pre-chorus → 100% chorus → 40% breakdown
```

---

## LTX-2 Templates

### Paragraph Format with ControlNet

LTX-2 uses natural language with embedded technical parameters:

```
[Main Description Paragraph]

Technical Parameters:
- Control Type: canny | depth | pose
- Control Strength: 0.0-1.0
- Steps: 25-50
- CFG: 6.0-8.0
- Audio: enabled | disabled
- Audio Description: if enabled, describe audio elements
```

### Template 1: Controlled Video-to-Video

```
A professional chef in white jacket prepares sushi in an upscale Japanese restaurant.
The chef's hands move with practiced precision, slicing fresh salmon with a traditional
yanagiba knife. Each cut is deliberate, the blade catching warm pendant lighting overhead.
Steam rises gently from the rice preparation area beside him. The background shows a
minimalist wooden interior with subtle zen garden elements visible through a window.

Technical Parameters:
- Control Type: depth
- Control Strength: 0.7
- Steps: 40
- CFG: 7.0
- Audio: enabled
- Audio Description: Subtle knife on cutting board sounds, ambient restaurant murmur, occasional ceramic clink, soft traditional Japanese instrumental in background
```

### Template 2: Text-to-Video with Audio

```
A vintage record player in a cozy evening living room begins to play. The needle drops
onto black vinyl, arm mechanism moving smoothly. Warm lamp light creates a golden glow
on wooden furniture. Through a rain-streaked window, city lights blur beautifully.
A steaming cup of tea sits beside the record player, small wisps of steam curling upward.
The scene feels nostalgic and peaceful, like a memory of a perfect evening at home.

Technical Parameters:
- Control Type: none
- Steps: 50
- CFG: 7.5
- Audio: enabled
- Audio Description: Vinyl crackle and pop, jazz piano music playing through the record, rain pattering against window, occasional distant thunder, subtle room tone
```

### Template 3: ControlNet Pose-Driven

```
An athlete performs a complex gymnastics floor routine in an Olympic arena.
Starting with a running approach, they launch into a tumbling pass with multiple flips
and twists. The crowd is visible but blurred in the background, blue floor mat prominent.
Competition lighting creates dramatic shadows and highlights on the gymnast's form.
The movement should feel powerful yet graceful, with perfect form throughout.

Technical Parameters:
- Control Type: pose
- Control Strength: 0.85
- Steps: 45
- CFG: 6.5
- Audio: enabled
- Audio Description: Feet impacting mat, crowd gasping then cheering, announcer voice murmur, arena ambience
```

---

## Hailuo 02 Templates

### Camera Control Keywords

Hailuo excels with explicit camera vocabulary:

**Movement Keywords:**
- `DOLLY IN/OUT`, `TRACK LEFT/RIGHT`, `CRANE UP/DOWN`
- `ORBIT CW/CCW`, `ZOOM IN/OUT`, `WHIP PAN`
- `HANDHELD`, `STEADICAM`, `STATIC LOCK`

### Template 1: Camera-Heavy Product Shot

```
SUBJECT: Luxury watch with exposed mechanical movement, rose gold case, black leather strap

CAMERA SEQUENCE:
1. MACRO STATIC on watch face, hands moving
2. SLOW ORBIT CCW revealing case profile
3. RACK FOCUS from dial to crown
4. CRANE UP with simultaneous ZOOM OUT to full watch
5. DOLLY OUT to hero composition

ENVIRONMENT: Black infinite void, single key light from 45 degrees, subtle fill, no reflections on glass

STYLE: Rolex commercial quality, premium product photography, jewelry-grade lighting

DURATION: 8 seconds
NEGATIVE: fingerprints, dust, scratches, visible logos of other brands, human presence
```

### Template 2: Fast Action Camera

```
SUBJECT: Parkour athlete in urban environment, athletic wear, determined expression

CAMERA SEQUENCE:
1. TRACKING SHOT following runner through alley
2. WHIP PAN as athlete vaults over obstacle
3. POV through narrow gap
4. CRANE UP as athlete climbs wall
5. DRONE PULLBACK revealing city rooftop escape

ENVIRONMENT: Gritty urban, fire escapes, concrete, golden hour side lighting, dust particles

STYLE: District B13 chase sequences, Jason Bourne handheld energy, practical stunt aesthetic

DURATION: 10 seconds
NEGATIVE: slow motion, static camera, clean environments, safety equipment visible
```

---

## Negative Prompt Library

### Universal Negatives (Apply to All)

```
blurry, low quality, pixelated, artifacts, compression, watermark, signature,
text overlay, logo, amateur, poorly composed, bad lighting
```

### Human-Focused Negatives

```
deformed hands, extra fingers, missing fingers, fused fingers, mutated hands,
bad anatomy, wrong proportions, extra limbs, cloned face, disfigured,
gross proportions, malformed limbs, missing arms, missing legs, extra arms,
extra legs, fused limbs, too many fingers, long neck, cross-eyed
```

### Style-Specific Negatives

**For Realistic Content:**
```
cartoon, anime, illustration, painting, sketch, drawing, 3D render,
CGI uncanny valley, plastic skin, doll-like, artificial
```

**For Anime/Stylized:**
```
photorealistic, 3D, western cartoon, chibi (unless intended),
inconsistent style, mixed art styles, sketch lines visible
```

**For Product Shots:**
```
dirty, damaged, used, fingerprints, smudges, dust, scratches,
reflections of photographer, tripod visible, background clutter
```

**For Nature/Landscape:**
```
humans, man-made structures, pollution, vehicles, aircraft,
power lines, unnatural colors, oversaturated, HDR artifacts
```

---

## Advanced Techniques

### 1. Multi-Pass Refinement

```
PASS 1 (Draft):
- Lower steps (20-25)
- Focus on composition and motion
- Identify issues

PASS 2 (Enhance):
- Standard steps (35-45)
- Fix identified issues in prompt
- Add detail specifications

PASS 3 (Final):
- Maximum steps (50+)
- Full quality settings
- Final negative refinements
```

### 2. Seed Inheritance for Multi-Shot

```
Shot 1: seed = 12345
Shot 2: seed = 12346 (increment by 1)
Shot 3: seed = 12347

This maintains stylistic coherence while allowing variation.
```

### 3. Expert Mixture Hints (MoE Models)

For Wan 2.6 and similar MoE architectures:
```
Anime content: --expert anime
Realistic content: --expert realistic
3D render: --expert 3d
Hybrid: --expert anime,realistic (weighted blend)
```

### 4. Audio-Visual Synchronization Tokens

For Veo 3.1 and LTX-2:
```
{action} [SYNC: audio_event]
"Door slams open [SYNC: impact_sound]"
"Character speaks [SYNC: dialogue_start]"
```

### 5. Temporal Consistency Anchors

```
Frame 1 anchor: "Establishing reference for: [character description]"
Subsequent frames: "Same [anchor_reference], now [new action]"
```

---

## Failure Mode Prevention

### Problem → Solution Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Hand deformation | Missing negative prompt | Add explicit hand negatives |
| Style drift mid-video | Weak style tokens | Strengthen style anchors, use consistent seed family |
| Motion too slow | Low motion scale | Increase motion_scale or motion_intensity |
| Motion too chaotic | High motion scale without guidance | Reduce scale, add motion description |
| Character changes appearance | No subject anchor | Add SUBJECT_ANCHOR with detailed description |
| Poor composition | Missing camera direction | Explicit camera movement specification |
| Audio-visual mismatch | Generic audio prompt | Specific timing with [SYNC] markers |
| Truncation artifacts | Prompt too long | Prioritize essential elements, split into shots |
| Mode collapse | Conflicting style tokens | Remove contradictory descriptors |
| Aspect ratio issues | Wrong ratio for content | Match ratio to subject (portrait for people, wide for landscape) |

### Quality Checklist Before Generation

- [ ] Subject clearly described with consistent anchors
- [ ] Action/motion explicitly specified with timing
- [ ] Environment set with lighting direction
- [ ] Style tokens non-contradictory
- [ ] Camera movement planned
- [ ] Negative prompts include common failure modes
- [ ] Aspect ratio appropriate for content
- [ ] Duration realistic for model capabilities
- [ ] Audio elements match visual timing (if applicable)

---

*Template Library v1.0 — January 18, 2026*
*Production-tested on: Veo 3.1, Kling 2.6, Sora 2 Pro, Runway Gen-4.5, Wan 2.6, Seedance 1.5 Pro, LTX-2, Hailuo 02*
