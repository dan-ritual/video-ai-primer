# Comprehensive Video AI Guide — January 2026

A practitioner's reference for video editors working with AI video generation. Covers prompting best practices, start/stop frame workflows, character consistency, orchestration, and tooling across all major models.

---

## Table of Contents

1. [Model-by-Model Prompting Best Practices](#model-by-model-prompting-best-practices)
2. [Start/Stop Frame (First/Last Frame) Generation](#startstop-frame-generation)
3. [Character Consistency & Reference Images](#character-consistency--reference-images)
4. [Character Sheets & Artifact Management](#character-sheets--artifact-management)
5. [Context Engineering & Structured Prompting](#context-engineering--structured-prompting)
6. [CLI Orchestration & Automation](#cli-orchestration--automation)
7. [Midjourney Niji 7 for Start/Stop Frames](#midjourney-niji-7-for-startstop-frames)
8. [Krea AI & Nano Banana Workflows](#krea-ai--nano-banana-workflows)
9. [Current Benchmarks & Model Selection](#current-benchmarks--model-selection)
10. [Key Resources & Further Reading](#key-resources--further-reading)

---

## Model-by-Model Prompting Best Practices

### Google Veo 3.1

**Core Formula:** `[Shot Composition] + [Subject] + [Action] + [Setting] + [Aesthetics]`

**Key Techniques:**
- **Lead with camera direction.** Veo weights early words heavily. Start with "wide aerial," "medium handheld," or "macro product shot"
- **Use concrete language.** Replace "show a dramatic product reveal" with "tight product macro; slider move left to right; cap twists open and mist rises"
- **Optimal length:** 3–6 sentences (100–150 words)
- **Scope control:** Keep to one scene, one main action per clip
- **Multi-clip sequences:** Structure as "Clip 1 / Clip 2 / Clip 3" with explicit seconds per clip. Keep 2–4 clips to avoid drift
- **Audio prompting:** Use separate sentences to describe audio cues and dialogue
- **Negative prompting:** Supported—exclude unwanted elements explicitly

**Technical Specs:**
- Duration: 4s, 6s, or 8s selectable
- Resolution: 720p or 1080p at 24 FPS
- Aspect ratios: 16:9 or 9:16
- First/last frame: Supported with "ingredients to video" feature
- Up to 3 reference images for character/object/style consistency

**Sources:** [Google Cloud Prompting Guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), [DreamHost Guide](https://www.dreamhost.com/blog/veo-3-1-prompt-guide/)

---

### Kling AI (O1, 2.5 Turbo, 2.6)

**Universal Structure:** `Subject (specific details) + Action (precise movement) + Context (3-5 elements max) + Style (camera, lighting, mood)`

#### Kling O1 (December 2025)

The world's first unified multimodal video model with 18+ video tasks in a single platform.

**Key Features:**
- MVL (Multimodal Visual Language) architecture
- Chain of Thought (CoT) approach for better motion accuracy
- Edit Mode: Modify existing video with text prompts
- Up to 7 image references per generation
- Start/End frame control using `@image1` and `@image2` in prompts

**Prompting Tips:**
- Keep sentences natural and straightforward
- Avoid vague phrases like "beautiful scene"
- Use concrete, action-based language
- Begin with single clear sentence stating goal and visual style

**Example:** "Cinematic 9:16 video of a sneaker landing in slow motion in a puddle, neon reflections, dramatic backlight, 1080p, 5-second shot."

#### Kling 2.5 Turbo Pro

**Strengths:** Better motion accuracy, cinematic lighting, pro-level scene control

**Prompting Tips:**
- Add flowing movement: "glides smoothly" or "jerks to a halt"
- Lighting sets tone: "bathed in sunset gold" or "harsh midday glare"
- Weave in emotion: "serene and hopeful" or "eerie and tense"

#### Kling 2.6 Pro

First Kling model with **native synchronized audio generation** (dialogue, SFX, ambient).

**Key Features:**
- 1080p output with controlled camera movements
- Timing/beats: "Beat 0–5s: walk in; 5–10s: barista pours espresso (SFX); 12s: dialogue starts"
- Structural reasoning for temporal anchors

**Common Failures to Avoid:**
1. Too many elements → overload
2. Missing camera → static shots
3. Open-ended motion → 99% hangs
4. Vague spatial language → distortions

**Always specify:** Camera movement + motion endpoints ("then settles back into place")

**Sources:** [fal.ai Kling 2.6 Guide](https://fal.ai/learn/devs/kling-2-6-pro-prompt-guide), [VEED Kling Guide](https://www.veed.io/learn/kling-ai-prompting-guide)

---

### OpenAI Sora 2 / Sora 2 Pro

**Core Principle:** Structure prompts like a shot list/storyboard.

**Prompt Structure:**
1. Camera framing and depth of field
2. Action described in beats
3. Lighting and palette
4. Subject anchored with distinctive details

**Key Techniques:**
- **Write for the lens, not the idea.** Replace "cinematic" with "wide establishing, eye level, slow push-in"
- **One camera movement + one subject action per shot**
- **Describe timing using beats or counts** for clean motion transitions
- **Encode materials/forces explicitly:** "wet nylon jacket," "8–10 mph crosswind from camera left," "footfalls splashing in shallow puddles"

**Audio & Dialogue:**
- Native audio generation—be explicit about what you want to hear
- Place dialogue in a block below visual description
- Keep exchanges to a few sentences for timing accuracy
- Label speakers consistently for multi-character scenes

**Workflow Best Practices:**
1. Script beat sheet and storyboard
2. Define "style spine" (consistent camera/color language)
3. Generate 3–5 variants at low res/short duration
4. Set acceptance criteria: subject clarity, smooth motion, realistic physics, no artifacts, audio sync

**Common Issues:**
- Motion issues → simplify to one camera move; specify stability
- Lip-sync problems → shorten lines; ADR in post
- Text artifacts → exclude legible text; add overlays later
- Physics glitches → detail surfaces and forces

**Note:** Sora 2 currently ranks 7th on benchmarks (Elo: 1,206) but excels at long-form content (up to 35s on Pro tier) and photorealism.

**Sources:** [OpenAI Cookbook Sora 2 Guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide), [Atlabs Sora 2 Guide](https://www.atlabs.ai/blog/sora-2-prompt-guide)

---

### Runway Gen-4 / Gen-4.5

**Core Philosophy:** Visual detail over conversational prompts. Command-based requests lack needed descriptions.

**Key Principles:**
- Describe what should happen, not what to avoid (no negative prompting)
- Consider each generation as a single scene
- 5s clips for simple actions; 10s for multiple movements
- Translate conceptual ideas into clear, specific physical actions

**Reference System (Gen-4):**
- Up to 3 reference images
- References handle visual consistency; prompts control context/actions/atmosphere
- Let references handle character consistency while prompts guide emotion and creativity

**Gen-4.5 (December 2025):**
- **#1 on Artificial Analysis Video Arena** (1,247 Elo)
- "Autoregressive-to-Diffusion" (A2D) architecture
- Excels at complex sequenced instructions and cause-and-effect relationships
- Supports detailed camera choreography, scene compositions, timing, atmospheric changes in single prompt

**Genre-Specific Tips:**
- Action: dynamism and rapid transitions
- Drama: smooth, intimate framing
- Documentary: naturalism and realism
- Horror: discomfort and suspense

**Sources:** [Runway Gen-4 Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide), [DataCamp Tutorial](https://www.datacamp.com/tutorial/runway-gen-4)

---

### MiniMax Hailuo 2.3 / 2.3 Fast

**Key Features:**
- Improved body movement, facial expressions, physical realism
- Supports anime, illustration, ink-wash painting, game-CG art styles
- 768p or 1080p (1080p limited to 6s)
- Text and image inputs (Fast variant: image inputs only)

**Prompting Best Practices:**
1. **Be specific and detailed**—more specificity = better results
2. **Character development:** "Character X expresses sadness," "Character Y leaps over a wall"
3. **Camera movements:** dolly, zoom, crane shot, tracking shot, POV, roll
4. **Scene details:** backgrounds, weather, lighting, time of day, architecture
5. **Art styles:** "Pixar-style," "3D modeling," "film noir," "cyberpunk"
6. **Color grading:** "muted tones," "vibrant colors," "black and white"

**Limitation:** No last-frame conditioning—videos generated solely from prompt or starting image.

**Sources:** [Higgsfield Hailuo 2.3 Guide](https://higgsfield.ai/blog/Minimax-Hailuo-2.3-A-Creative-Guide), [MiniMax Official](https://www.minimax.io/news/minimax-hailuo-23)

---

### Wan 2.1 / 2.2 / 2.5 / 2.6

#### Wan 2.1 (Open Source)

**Golden Rule:** Be clear and sufficiently detailed. The more precise, the closer to your vision.

**Technical Parameters:**
- Guidance scale: 5-7
- Steps: 20-30 per frame
- 480p for speed, 720p for quality
- Keep camera movement under 5 seconds
- Avoid overly complex camera movements

#### Wan 2.2 (MoE Architecture)

**Prompt Structure (80-120 words):**
1. Shot order (what camera first captures, how shot develops)
2. Standard cinematography terms for camera movements
3. Speed terms: "Slow-motion," "Whip-pan," "Time-lapse"
4. Parallax cues: "Foreground grass sways while mountains remain still"

#### Wan 2.5 (Native Audio)

**Key Features:**
- Native 1080p HD, 10-second clips
- Synchronized audio: multi-voice dialogue, SFX, background music

**Prompting Techniques:**
- Use cinematic terminology (dolly shot, bokeh, three-point lighting)
- Start with wide establishing shots before close-ups
- Maintain lighting/color/style consistency throughout sequences
- Use temporal markers (sunrise, noon, twilight, night)
- Layer audio: dialogue, ambient sounds, music separately
- Use negative prompts to exclude unwanted elements

#### Wan 2.6 (Multi-Shot)

**Key Features:**
- Text-to-video: up to 800 characters, 720p/1080p, 5/10/15 seconds
- `multi_shots` parameter for segmented narratives
- "Clone-level consistency"—exact appearance preservation across shots

**Sources:** [Ambience AI Wan Guide](https://www.ambienceai.com/tutorials/wan-prompting-guide), [Atlabs Wan 2.5 Guide](https://www.atlabs.ai/blog/wan-2-5-prompting-guide), [fal.ai Wan 2.6 Guide](https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes)

---

### ByteDance Seedance 1.5 Pro

**Architecture:** Dual-Branch Diffusion Transformer (DB-DiT), 4.5B parameters

**Key Features:**
- Native audio-video synchronization (generated in parallel)
- Multi-language lip-sync: English, Mandarin, Japanese, Korean, Spanish, Portuguese, Indonesian, Cantonese, Sichuanese
- Advanced camera scheduling: tracking shots, Hitchcock zooms, pans, tilts, handheld motion
- Up to 1080p resolution
- 2-3 minute generation time (10x speedup from Q3 2025 optimizations)

**Prompting Best Practices:**
- Structure like a shot plan: composition → character → camera → mood
- Layer audio elements separately (foreground vs. background)
- Include emotional cues: "angry," "hesitant," "excited," "sad"
- Describe movement with detail and pacing words: "slow," "deliberate," "rhythmic"
- Focus on single performance moments rather than multiple actions

**Best Use Cases:** Dialogue-heavy shorts, multi-language content, talking-head UGC, product explainers, dramatic close-ups

**Limitations:** 15-second max, occasional motion instability, struggles with singing

**Roadmap:** 30s generations Q2 2026, 60s generations late 2026

**Sources:** [ByteDance Official](https://seed.bytedance.com/en/seedance1_5_pro), [Higgsfield Seedance Guide](https://higgsfield.ai/blog/Seedance-1.5-Pro-on-Higgsfield-A-Practical-Creator-Guide)

---

### Lightricks LTX-2 (Open Source)

**Key Differentiator:** Open weights, local execution, no API dependencies

**Best Practices:**
- Keep prompt in single flowing paragraph
- Use present tense verbs for movement/action
- Match detail to shot scale (more precision for closeups)
- Write 4-8 descriptive sentences covering all key aspects
- Focus on camera's relationship to subject for camera movement

**What Works Well:**
- Stylized aesthetics: painterly, noir, analog film, fashion editorial, pixelated animation, surreal
- Lighting/mood control: backlighting, color palettes, soft rim light, flickering lamps
- Characters can talk and sing in various languages

**What to Avoid:**
- Emotional labels without visual cues (use posture, gesture, facial expression)
- Readable text (signage, brand names)
- Complex physics or chaotic motion (except dancing)
- Too many characters/layered actions

**Audio Prompting:**
- Weave sound descriptions into visual prompts
- Explicit cues: "footsteps crunching on gravel," "distant thunder rumbling"
- More specific = better synchronization

**Technical Requirements:**
- Width & height divisible by 32
- Frame count divisible by 8 + 1
- Native 4K (3840×2160) up to 50 fps

**Sources:** [LTX Official Prompting Guide](https://ltx.io/model/model-blog/prompting-guide-for-ltx-2), [GitHub](https://github.com/Lightricks/LTX-2)

---

## Start/Stop Frame Generation

### Overview

First/Last Frame (FLF2V) technology lets you provide two reference images—start and end—and the AI generates intermediate frames automatically. This gives precise control over openings, endings, and transitions.

### Model Support Matrix

| Model | Start Frame | End Frame | Both | Notes |
|-------|-------------|-----------|------|-------|
| Veo 3.1 | ✅ | ✅ | ✅ | "First and last frame" feature with audio |
| Kling O1 | ✅ | ✅ | ✅ | Use `@image1` and `@image2` in prompts |
| Kling 2.1+ | ✅ | ✅ | ✅ | Full director control over transitions |
| Wan 2.1 FLF2V | ✅ | ✅ | ✅ | Open-source, 720p HD output |
| Runway Gen-4 | ✅ | Limited | Limited | Up to 3 reference images |
| Hailuo 2.3 | ✅ | ❌ | ❌ | No last-frame conditioning |
| Seedance 1.5 | ✅ | ❌ | ❌ | Start frame only |
| LTX-2 | ✅ | ✅ | ✅ | ComfyUI workflows available |

### Best Practices

**Frame Selection:**
- First and last frames should be as similar as possible for natural transitions
- Maintain consistent color palette, tone, and settings
- Keep wardrobe and hair consistent across frames
- Simple silhouettes and solid colors reduce frame-to-frame mutation

**Prompt Integration:**
- For Kling O1: Reference frames directly with `@image1` (start) and `@image2` (end)
- Focus motion instructions on what happens between frames
- Specify the transition type: smooth, dramatic, subtle

**Workflow Tips:**
- Generate start/stop frames using image generators (Midjourney, Nano Banana, Flux)
- Ensure both frames are high resolution (1080p+), clear, well-composed
- Remove text overlays or watermarks from reference frames
- Match lighting and contrast between frames

### Wan 2.1 FLF2V Specific

The open-source Wan FLF2V model is particularly powerful for start/stop workflows:
- Generates coherent motion path between first_image and last_image
- Optional text prompt for guidance
- Available via fal.ai API and ComfyUI

**Sources:** [fal.ai Wan FLF2V](https://fal.ai/models/fal-ai/wan-flf2v), [Artlist Start/End Frame Guide](https://artlist.io/blog/ai-video-start-and-end-frame/)

---

## Character Consistency & Reference Images

### Platform-Specific Features

**Veo 3.1:** Up to 3 reference images for character/object/scene consistency across shots

**Kling O1:** Up to 7 image references including character photos, outfits, props, environmental angles

**Runway Gen-4:** Up to 3 reference images—references handle consistency, prompts control context

**Wan 2.6:** "Clone-level consistency"—exact appearance preservation across shots

**Seedream 4.0:** Transforms 3 reference images into perfectly consistent videos

### Best Practices

**Reference Image Preparation:**
1. Curate 6–10 reference images per character per scene
2. Include: front-facing portrait, three-quarter angle, profile
3. Keep wardrobe clean and consistent ("red scarf, leather jacket")
4. Maintain neutral, consistent lighting
5. High resolution (1080p+), clear, well-composed
6. Free of text overlays or watermarks

**Prompt Strategies:**
- Embed consistent visual descriptors in every prompt
- Fix subject description; vary only scene/camera
- Use the same language from your "character bible" every time
- Grab last frame of each finished segment as reference for next prompt

**Technical Methods:**

1. **Anchor Frames:** Create key frames with locked style/pose/emotion as guideposts
2. **Prompt Chaining:** Change only 1–2 elements per frame for believable motion
3. **Frame Conditioning:** Use last frame of shot N to start shot N+1
4. **Latent Reuse:** Preserve character features in latent space across frames

**Common Issues:**

- **Wardrobe mutation:** Favor simple silhouettes, solid colors, minimal distinctive anchors (red jacket, silver pendant)
- **Lighting inconsistency:** Keep single dominant light direction per scene; key flip = identity wobble
- **Multi-shot drift:** Repeat core style cues; use explicit bridge shots

### Tools

- **Midjourney V7 Omni-Reference:** Use `--cref` parameter to guide generation with reference images
- **Google Flow:** Real-time character consistency monitoring with Veo 3/Imagen 4
- **Higgsfield Popcorn:** Builds internal identity model from reference image
- **GoEnhance:** Dedicated consistency engine

**Sources:** [Artlist Character Consistency Guide](https://artlist.io/blog/consistent-character-ai/), [CrePal Character Consistency 2025](https://crepal.ai/blog/aivideo/how-to-keep-characters-consistent-in-ai-videos-2025/)

---

## Character Sheets & Artifact Management

### Creating a Character Bible

Document every defining element:
1. **Core visual identity:** Face shape, skin tone, hair color/style, eye color, body type
2. **Distinctive features:** Scars, tattoos, accessories, signature clothing
3. **Wardrobe palette:** Primary colors, textures, key items
4. **Posture and movement:** How they walk, gesture, emote
5. **Lighting preference:** Key light direction, color temperature

### Multi-View Character Sheets

Generate comprehensive reference sheets showing:
- Front view
- Three-quarter view
- Profile view
- Back view
- Multiple emotional states
- Key poses/actions

**Tools for Generation:**
- Midjourney with `--ar 16:9` and "character turnaround sheet" in prompt
- Niji 7 for anime-style character sheets
- Flux with LoRA for consistent style
- Krea Nano Banana Elements for style/character sets

### Artifact Organization

**Folder Structure:**
```
project/
├── characters/
│   ├── character_a/
│   │   ├── reference_sheet.png
│   │   ├── front.png
│   │   ├── profile.png
│   │   ├── expressions/
│   │   └── character_bible.md
│   └── character_b/
├── scenes/
│   ├── scene_01/
│   │   ├── start_frame.png
│   │   ├── end_frame.png
│   │   ├── prompt.txt
│   │   └── outputs/
│   └── scene_02/
├── style_references/
│   ├── color_palette.png
│   ├── lighting_reference.png
│   └── mood_board.png
└── prompts/
    ├── templates/
    └── shot_list.json
```

### Prompt Templates

Maintain reusable prompt templates with placeholders:
```
[SHOT_TYPE] of [CHARACTER_NAME], [CHARACTER_DESCRIPTION],
[ACTION], [SETTING], [LIGHTING], [CAMERA_MOVEMENT], [STYLE]
```

---

## Context Engineering & Structured Prompting

### JSON Prompting

JSON prompts isolate components to eliminate cross-contamination errors. Native language for AI video models.

**Benefits:**
- Swap parts easily (change lighting without rewriting everything)
- Generate prompts programmatically for batch processing
- Consistent structure across multiple generations
- Speaks directly to each expert network in the model

**Basic Structure:**
```json
{
  "subject": "elderly woman with silver hair, weathered hands",
  "action": "slowly opens antique music box",
  "camera": {
    "shot_type": "extreme close-up",
    "movement": "subtle push-in",
    "angle": "eye level"
  },
  "lighting": {
    "type": "warm practical light",
    "source": "single candle, camera left",
    "mood": "intimate, nostalgic"
  },
  "audio": {
    "dialogue": null,
    "sfx": "music box melody, soft mechanical clicks",
    "ambient": "distant rain on windows"
  },
  "style": {
    "aesthetic": "film noir",
    "color_grade": "desaturated with warm highlights",
    "reference": "Wong Kar-wai cinematography"
  },
  "duration": "6 seconds",
  "aspect_ratio": "16:9"
}
```

### YAML Alternative

More readable syntax, similar structure:
```yaml
subject: elderly woman with silver hair
action: slowly opens antique music box
camera:
  shot_type: extreme close-up
  movement: subtle push-in
lighting:
  type: warm practical light
  source: single candle, camera left
duration: 6 seconds
```

### Tools

- **PixelDojo:** Visual JSON prompt builder with community directory
- **n8n Workflow:** Convert natural language to Veo 3 JSON via GPT/Gemini
- **JsonToVideo:** Structured prompts for Veo 3.1/Sora 2

### Context Engineering Philosophy

Beyond prompt engineering—treat the model as a programmable, context-aware engine:
1. **What data/knowledge/tools/memory** are provided
2. **Structured flows** where prompts, tools, memory are composed programmatically
3. **Multi-agent workflows:** Intent Translator → Literature Retrieval → Synthesis → Generation → Validation

**Sources:** [ImagineArt JSON Prompting](https://www.imagine.art/blogs/json-prompting-for-ai-video-generation), [Atlabs Veo3 JSON Guide](https://www.atlabs.ai/blog/json-prompting-veo3)

---

## CLI Orchestration & Automation

### FFmpeg Integration

FFmpeg remains essential for post-processing AI-generated clips.

**Key Operations:**
```bash
# Concatenate clips
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4

# Add audio track
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4

# Upscale to 4K
ffmpeg -i input.mp4 -vf scale=3840:2160:flags=lanczos output_4k.mp4

# Convert frame rate
ffmpeg -i input.mp4 -r 24 output_24fps.mp4

# Extract frames for reference
ffmpeg -i video.mp4 -vf "select=eq(n\,0)+eq(n\,last)" -vsync vfr frame_%d.png

# Create GIF preview
ffmpeg -i video.mp4 -vf "fps=10,scale=480:-1" output.gif
```

### AI-Powered FFmpeg Tools

- **LLmpeg:** AI companion that generates FFmpeg commands from natural language. Auto-clipboard, command history, pre-built templates
- **AI-FFmpeg:** Web app using FFmpeg.wasm with NLP command generation
- **FFmpegGPT:** Expert advice for complex video/audio operations

### Claude Code Orchestration

**Key Tools:**
- **Claude-Flow:** Leading agent orchestration platform for Claude. Multi-agent swarms, autonomous workflows, MCP protocol support
- **Claude Code Workflow Studio:** VSCode extension for drag-and-drop AI workflow building
- **Slash Commands:** Custom shortcuts for complex operations (e.g., `/commit-push-pr`)
- **Subagents:** Specialized AI personas for different workflow phases

**Example Workflow Architecture:**
```
User Input
    ↓
Intent Analysis (Claude)
    ↓
┌─────────────────────────────────────┐
│  Parallel Generation Tasks          │
│  ├── Generate Start Frame (Flux)    │
│  ├── Generate End Frame (Flux)      │
│  └── Prepare Audio (Seedance)       │
└─────────────────────────────────────┘
    ↓
Video Generation (Kling O1 / Veo 3.1)
    ↓
Post-Processing (FFmpeg)
    ↓
Quality Check (Claude Vision)
    ↓
Output
```

### BuildShip Integration

Connect FFmpeg with AI models via no-code/low-code workflows:
- Overlay audio on videos
- Combine multiple audio files
- Batch video resolution conversion
- Automated social media repurposing

### MCP Servers for AI Agents

Use Model Context Protocol (MCP) servers to let AI agents control FFmpeg programmatically:
- Batch processing via conversational commands
- "For each video in this list, create 1080p and 720p versions"
- Integrate with video generation APIs

**Sources:** [VentureBeat Claude Code 2.1.0](https://venturebeat.com/orchestration/claude-code-2-1-0-arrives-with-smoother-workflows-and-smarter-agents/), [BuildShip FFmpeg](https://buildship.com/integrations/ffmpeg)

---

## Midjourney Niji 7 for Start/Stop Frames

### Overview

Released January 9, 2026. Specialized for Eastern/anime aesthetics, developed with Spellbrush.

### Key Features

- **Improved coherency:** Fine details (eyes, reflections, backgrounds) much clearer
- **Sharper lines:** Better definition in outlines and shapes
- **Enhanced clarity:** Complex elements rendered more clearly
- **Better compositions:** Complex characters/objects more effectively rendered
- **Style Reference (sref):** Replicate specific artistic aesthetics via codes
- **Video Model:** Available on niji・journey app
- **Video End Frame:** Seamlessly loop or specify unique end frame

### Usage

**Discord:** `--niji 7` after prompt
**Web:** Select "Niji 7" from Version dropdown

### Prompting Tips

- Include detailed background descriptions
- Be precise—Niji 7 interprets prompts more literally
- Specify "character turnaround sheet" for multi-view references
- Use `--ar 16:9` or `--ar 9:16` for video-ready frames

### Current Limitations

- **No cref (character reference)** yet—replacement coming as "super special secret surprise"
- Personalization and moodboards features coming soon

### Workflow for Video Generation

1. Generate character sheet in Niji 7
2. Use consistent style reference (sref) codes across frames
3. Generate start frame with character + initial pose/setting
4. Generate end frame with same character + final pose/setting
5. Feed both to FLF2V model (Wan, Kling, Veo)

**Sources:** [Niji V7 Official](https://nijijourney.com/blog/niji-7), [Midjourney Version Docs](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)

---

## Krea AI & Nano Banana Workflows

### Nano Banana Overview

One of 10 editing models on Krea AI. Add/remove objects, merge images, change expressions, lighting.

### Nano Banana Pro

- **Native 4K** image generation and editing
- "World's smartest video model"—add/remove objects, restyle, add consistent characters, change camera angles

### Nano Banana Elements (December 2025)

Build sets of styles, objects, or characters using just a few reference images. Reference them in prompts within Nano Banana tool.

### Krea Nodes

Visual workflow builder:
- Chain AI operations like Blender/Houdini node systems
- Combine all models and features
- Build automated workflows
- Create applications for specific generation types (e.g., exploded-view images)

### Workflow Tips

- Add personalized context: brand guidelines, visual moodboards, personal instructions
- Use Krea's 1000+ styles with Nano Banana
- Native 4K output, 3-second generation time for 1024px Flux at FP16
- Chain image generation → video animation → asset management → video upscaling

**Sources:** [Krea Nano Banana](https://www.krea.ai/nano-banana), [Krea Video](https://www.krea.ai/video)

---

## Current Benchmarks & Model Selection

### January 2026 Rankings (Artificial Analysis Video Arena)

| Rank | Model | Elo Score | Best For |
|------|-------|-----------|----------|
| 1 | Runway Gen-4.5 | 1,247 | VFX, stylized content, cause-and-effect |
| 2 | Google Veo 3 | ~1,230 | Cinematic stability, 4K polish, native audio |
| 3-6 | Kling variants | ~1,210-1,225 | Long-form (2+ min), image-to-video #1 |
| 7 | Sora 2 Pro | 1,206 | Photorealism, long-form (35s), physics |

### Model Selection Guide

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Dialogue-heavy content | Seedance 1.5 Pro | Native lip-sync, multi-language |
| Anime/stylized | Kling + Niji 7 frames | Style control, consistency |
| Agency B-roll | Veo 3.1 | 4K, cinematic stability |
| VFX/experimental | Runway Gen-4.5 | A2D architecture, creative control |
| Long-form (2+ min) | Kling | Longest duration support |
| Open-source/local | LTX-2 or Wan 2.x | Self-hosted, no API costs |
| Start/stop frame precision | Wan FLF2V or Kling O1 | Dedicated FLF support |
| Photorealism | Sora 2 Pro | Best physics, natural light |

### Pricing Trends

Average cost per minute dropped 65% from 2024 to 2025. Expect continued pressure in 2026.

### 2026 Roadmap Expectations

- Audio features for Runway, Kling (Q1-Q2 2026)
- 2-minute clips from Runway Gen 5 (rumored)
- 30-second Seedance (Q2 2026), 60-second (late 2026)
- Character reference for Niji 7 (coming)

**Sources:** [InVideo Comparison](https://invideo.io/blog/kling-vs-sora-vs-veo-vs-runway/), [Pixazo 2026 Comparison](https://www.pixazo.ai/blog/ai-video-generation-models-comparison-t2v)

---

## Key Resources & Further Reading

### Official Documentation

- [Google Veo Prompt Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)
- [Runway Gen-4 Guide](https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide)
- [OpenAI Sora 2 Guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)
- [LTX-2 Prompting Guide](https://ltx.io/model/model-blog/prompting-guide-for-ltx-2)
- [Niji 7 Announcement](https://nijijourney.com/blog/niji-7)

### Community Guides

- [fal.ai Kling 2.6 Pro Guide](https://fal.ai/learn/devs/kling-2-6-pro-prompt-guide)
- [Atlabs Prompting Guides](https://www.atlabs.ai/blog)
- [Higgsfield Model Guides](https://higgsfield.ai/blog)
- [ImagineArt Prompt Guides](https://www.imagine.art/blogs)

### Tools & Platforms

- [Krea AI](https://www.krea.ai/) - Nano Banana, Nodes, multi-model workflow
- [fal.ai](https://fal.ai/) - API access to multiple models
- [Replicate](https://replicate.com/) - Open-source model hosting
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based local workflows
- [PixelDojo JSON Builder](https://pixeldojo.ai/ai-json-prompt-builder)

### GitHub Repositories

- [Wan 2.1](https://github.com/Wan-Video/Wan2.1)
- [Wan 2.2](https://github.com/Wan-Video/Wan2.2)
- [LTX-2](https://github.com/Lightricks/LTX-2)
- [Claude-Flow](https://github.com/ruvnet/claude-flow)

---

## Notes on PsyopAnime Workflow

Based on available information, the PsyopAnime collective appears to use a workflow combining:

1. **Midjourney** (likely with subscriptions) for initial image generation
2. **Photoshop skills** for refinement and compositing
3. **AI video generation tools** (pushing tech limits )
4. Satirical anime shorts focused on current events/commentary

Their approach emphasizes:
- High-quality initial frame generation
- Iterative refinement
- Pushing boundaries of what AI anime can achieve
- Community building around the creative process

They've expressed interest in building an "AI anime studio" requiring "5 badasses with midjourney subscriptions and photoshop skills."

---

*Guide compiled January 18, 2026. Models and capabilities evolve rapidly—verify current features before production use.*
