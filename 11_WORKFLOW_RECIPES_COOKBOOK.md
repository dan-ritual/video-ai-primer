# Workflow Recipes Cookbook

*January 2026 Edition*

Production-tested workflows for common video AI scenarios.

---

## Table of Contents

1. [Recipe Format Guide](#recipe-format-guide)
2. [Talking Head & Avatar Recipes](#talking-head--avatar-recipes)
3. [Cinematic & Narrative Recipes](#cinematic--narrative-recipes)
4. [Product & Commercial Recipes](#product--commercial-recipes)
5. [Social Media Recipes](#social-media-recipes)
6. [Music Video Recipes](#music-video-recipes)
7. [Character Consistency Recipes](#character-consistency-recipes)
8. [Batch Production Recipes](#batch-production-recipes)
9. [Post-Production Recipes](#post-production-recipes)
10. [Troubleshooting Recipes](#troubleshooting-recipes)

---

## Recipe Format Guide

Each recipe follows this structure:

```
RECIPE: [Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: When to use this workflow
TIME: Estimated time to complete
COST: Estimated cost per output
QUALITY: Expected quality level
TOOLS: Required tools/platforms
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• [Input requirements]

STEPS:
1. [First step]
2. [Second step]
...

TIPS:
• [Pro tips and optimizations]

VARIATIONS:
• [Alternative approaches]
```

---

## Talking Head & Avatar Recipes

### Recipe 1: Quick Spokesperson Video

```
RECIPE: Quick Spokesperson Video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Marketing video with AI presenter
TIME: 15-30 minutes
COST: $0.50-5 per minute of output
QUALITY: Professional
TOOLS: HeyGen or Synthesia, Script editor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Written script (200 words = ~1 minute)
• Brand guidelines (optional)
• Logo/graphics for overlay (optional)

STEPS:
1. Write/refine script for spoken delivery
   - Use short sentences
   - Add natural pauses with ellipses
   - Include pronunciation guides for unusual words

2. Select avatar in HeyGen/Synthesia
   - Match to target audience demographics
   - Consider cultural appropriateness
   - Test with short phrase first

3. Choose background/setting
   - Studio (professional), Office (corporate), Custom (branded)
   - Ensure good contrast with avatar

4. Generate video
   - HeyGen: Studio Creator → Paste script → Generate
   - Synthesia: New video → Select avatar → Add script

5. Add overlays in post
   - Logo watermark
   - Lower thirds
   - Call-to-action graphics

6. Export and deliver

TIPS:
• Break long scripts into multiple clips for better lip sync
• Use premium avatars for important content
• Preview audio before full generation
• Keep backgrounds simple for professional look

VARIATIONS:
• Multi-language: Use HeyGen dubbing for 175+ languages
• Custom avatar: Upload presenter photo (consent required)
• Screen recording: Combine with software demo footage
```

### Recipe 2: Custom Avatar from Photo

```
RECIPE: Custom Avatar from Photo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Personal/brand avatar for ongoing use
TIME: 30-60 minutes (one-time setup)
COST: $5-20 for avatar creation
QUALITY: High (depends on source photo)
TOOLS: Hedra Character-3, High-quality photo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• High-res frontal photo (1024x1024 minimum)
• Neutral expression, good lighting
• Plain background preferred
• Audio samples (optional, for voice matching)

STEPS:
1. Prepare source photo
   - Crop to square, face centered
   - Remove background if busy
   - Ensure even lighting on face
   - Resolution: minimum 1024x1024

2. Upload to Hedra
   - Select "Create Avatar" / "Custom"
   - Upload prepared photo
   - Set style: "professional" or "expressive"

3. Test avatar with sample audio
   - Upload 10s test audio
   - Evaluate lip sync quality
   - Check expression range

4. Refine if needed
   - Adjust emotion_range parameter
   - Try different source photos
   - Test multiple expressions

5. Save avatar for reuse
   - Note avatar_id for API use
   - Document settings for consistency

TIPS:
• Photos with slight smile work better than neutral
• Avoid harsh shadows on face
• Eye contact with camera is crucial
• Keep hair away from face for cleaner tracking

VARIATIONS:
• Stylized avatar: Apply artistic filter to photo first
• Multiple expressions: Create separate avatars for different moods
• API automation: Store avatar_id for batch generation
```

### Recipe 3: Lip Sync Correction Pipeline

```
RECIPE: Lip Sync Correction Pipeline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Fix lip sync on existing video
TIME: 5-15 minutes per clip
COST: $0.05-0.10 per minute
QUALITY: Very Good to Excellent
TOOLS: MuseTalk (free) or Sync Labs (paid)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Source video with face visible
• Correct audio track (WAV/MP3)
• GPU with 8GB+ VRAM (for MuseTalk)

STEPS:
1. Prepare inputs
   - Extract original audio if replacing: ffmpeg -i video.mp4 -vn audio.wav
   - Ensure new audio matches video duration
   - Check audio quality (clean, no background noise)

2. For MuseTalk (free, local):
   ```bash
   python inference.py \
     --video_path source.mp4 \
     --audio_path new_audio.wav \
     --output_path synced.mp4 \
     --enhance_face True
   ```

3. For Sync Labs (cloud, paid):
   - Upload video and audio
   - Select accuracy level: "ultra" for best results
   - Set expression_preserve: 0.7-0.8
   - Process and download

4. Quality check
   - Watch at normal speed
   - Check consonants: B, M, P (lips close)
   - Check vowels: A, O (mouth opens)
   - Verify no face distortion

5. Fix problem areas (if needed)
   - Re-run problem sections
   - Use manual keyframing (Sync Labs Pro)
   - Consider cutting around unfixable frames

TIPS:
• Clean audio = better lip sync
• Frontal face shots work best
• Avoid rapid head movements
• 30fps minimum for smooth results

VARIATIONS:
• Batch processing: Script MuseTalk for multiple files
• Multi-face: Process each face separately, composite
• Expression enhancement: Add emotion hints during sync
```

---

## Cinematic & Narrative Recipes

### Recipe 4: Multi-Shot Narrative Sequence

```
RECIPE: Multi-Shot Narrative Sequence
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Short film scene, commercial narrative
TIME: 2-4 hours
COST: $10-50 depending on model choices
QUALITY: Professional
TOOLS: Runway/Kling + ComfyUI + NLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Shot list with descriptions
• Character reference images
• Style reference images
• Audio script or scratch track

STEPS:
1. Plan the sequence
   - Write shot descriptions (see Prompt Library)
   - Determine duration per shot
   - Plan transitions
   - Map to audio if available

2. Create consistency anchors
   - Generate character sheet (Recipe 10)
   - Extract face embeddings
   - Document style tokens
   - Set seed family (base_seed = random, subsequent = base+1, base+2...)

3. Generate hero shots first
   - Most important shots with premium model
   - Establish look and feel
   - These become reference for other shots

4. Generate supporting shots
   - Match hero shot style
   - Use same negative prompts
   - Reference hero shots for consistency

5. Review and regenerate failures
   - Check consistency: face, costume, style
   - Regenerate problem shots (same seed family)
   - Accept minor variations

6. Assemble in NLE (DaVinci/Premiere)
   - Import all clips
   - Rough cut to audio
   - Add transitions
   - Color grade for consistency

7. Final audio
   - Add dialogue/VO
   - Layer SFX
   - Add music bed
   - Mix and master

TIPS:
• Generate 2-3 versions of each shot for options
• Keep detailed notes on working prompts
• Color grading unifies inconsistent shots
• Consider upscaling hero shots only (cost savings)

VARIATIONS:
• Dialogue-first: Generate audio, then video to match
• Music-first: Map beats to cuts (Recipe 7)
• Documentary style: More flexibility on consistency
```

### Recipe 5: Product Hero Shot (360 Orbital)

```
RECIPE: Product Hero Shot (360 Orbital)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: E-commerce, product launch, advertising
TIME: 30-60 minutes
COST: $2-10 per product
QUALITY: Premium
TOOLS: Runway Gen-4.5 or Hailuo 02, Product photo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• High-quality product photo (white/clean background)
• Product dimensions/reference
• Brand color palette (optional)

STEPS:
1. Prepare product image
   - Remove background completely
   - Add subtle shadow if needed
   - Ensure product fills ~60% of frame
   - Resolution: 1920x1080 or higher

2. Craft orbital prompt
   ```json
   {
     "prompt": {
       "subject": "[Product name], [materials], [colors], floating in center",
       "action": "Rotating slowly 360 degrees, hovering",
       "scene": "Pure black/white gradient background, volumetric studio lighting",
       "style": "Premium product photography, Apple-style, no dust or scratches",
       "technical": {
         "camera_motion": ["slow orbital 360", "slight zoom at halfway"],
         "duration": 6
       }
     },
     "negative_prompt": "hands, human, dust, fingerprints, scratches, cluttered"
   }
   ```

3. Generate with Image-to-Video
   - Upload product image as starting frame
   - Apply prompt
   - Set motion_scale: 3-4 (subtle)

4. Review and iterate
   - Check: smooth rotation, consistent lighting
   - Watch for: clipping, distortion, unwanted elements
   - Regenerate with adjusted prompts if needed

5. Post-production
   - Seamless loop point editing (if needed)
   - Add subtle SFX (whoosh, ambient)
   - Export for web/social

TIPS:
• Lower motion_scale for stable products
• Use "floating" to avoid surface artifacts
• Generate multiple durations for different platforms
• Consider matching brand music/audio

VARIATIONS:
• Assembly reveal: Components fly together
• Exploded view: Parts separate to show internals
• Feature callout: Pause and highlight features
• Environment composite: Place in lifestyle setting
```

### Recipe 6: Scene Extension / Outpainting

```
RECIPE: Scene Extension / Outpainting
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Extend scene beyond original frame
TIME: 15-30 minutes
COST: $0.50-2 per extension
QUALITY: Good to Very Good
TOOLS: Runway Gen-4.5, Image editor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Source video or image
• Target aspect ratio/dimensions
• Description of extended areas

STEPS:
1. Extract key frame
   - Choose representative frame
   - Note all visible elements
   - Identify extension direction

2. Prepare canvas
   - Create larger canvas (e.g., 16:9 → 21:9)
   - Place original content
   - Mask extension areas

3. Generate extension
   - Upload masked frame to Runway
   - Prompt: "Continue the scene naturally..."
   - Include original scene description
   - Describe extended areas specifically

4. Blend if needed
   - Feather edges in post
   - Color match extended areas
   - Check lighting continuity

5. Generate video
   - Use extended image as I2V input
   - Match original video motion
   - Or create new complementary motion

TIPS:
• Extension works best for environments
• Avoid extending across people/faces
• Keep extension content simpler than original
• Multiple passes may be needed for quality

VARIATIONS:
• Vertical to horizontal: Portrait to landscape conversion
• Zoom out reveal: Progressively extend
• Background replacement: Keep subject, new environment
```

---

## Social Media Recipes

### Recipe 7: Trend-Reactive Content (Fast Turnaround)

```
RECIPE: Trend-Reactive Content (Fast Turnaround)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: React to trending topics quickly
TIME: 15-30 minutes
COST: $0.25-1 per video
QUALITY: Good (speed prioritized)
TOOLS: Pika or Kling (fast modes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Trend concept/idea
• Reference images (optional)
• Trending audio (if applicable)

STEPS:
1. Identify trend angle (5 min)
   - What's the hook?
   - How does brand/creator fit?
   - What visual will resonate?

2. Rapid prompt creation (5 min)
   - Keep it simple and clear
   - Focus on recognizable elements
   - Include trending keywords if relevant

3. Generate first draft (2-5 min)
   - Use Pika for fastest turnaround
   - Or Kling fast mode
   - Accept "good enough" quality

4. Quick iteration if needed (5-10 min)
   - Refine prompt based on output
   - 2-3 attempts maximum
   - Move on if not working

5. Minimal post-production (5 min)
   - Add trending audio
   - Simple text overlay
   - Platform-specific export

6. Post immediately
   - Trend timing is everything
   - Perfect is enemy of published
   - Monitor engagement

TIPS:
• Templates speed up repeated trend formats
• Pre-save common prompts
• Batch generate while reviewing
• Have backup concepts ready

VARIATIONS:
• Meme format: Template + AI variation
• Duet/React: Generate, then record reaction
• Series: Multiple angles on same trend
```

### Recipe 8: Character Swap Viral Video

```
RECIPE: Character Swap Viral Video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Swap character in existing video
TIME: 30-60 minutes
COST: $1-5 per video
QUALITY: Good to Very Good
TOOLS: Kling V2V or ComfyUI + IP-Adapter
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Source video (clear subject, good quality)
• Target character reference images (3-5)
• Style reference (optional)

STEPS:
1. Prepare source video
   - Trim to key moment (2-5 seconds ideal)
   - Ensure face clearly visible
   - Good lighting helps

2. Prepare character reference
   - Multiple angles if available
   - Consistent style across references
   - Clear face visibility

3. Generate with Kling Video-to-Video
   - Upload source video
   - Upload character reference
   - Set strength: 0.6-0.8
   - Prompt: "Same action and movement, but [character description]"

4. Or use ComfyUI pipeline
   ```
   [Source Video] → [Frame Extract]
        ↓
   [Character Ref] → [IP-Adapter FaceID]
        ↓
   [Wan/Kling V2V] → [Frame Sequence]
        ↓
   [Video Encode] → [Output]
   ```

5. Review and refine
   - Check: face consistency, motion preserved
   - Watch for: artifacts, identity bleed
   - Regenerate problem sections

6. Add audio
   - Keep original audio if relevant
   - Or add trending sound
   - Voice swap if dialogue present

TIPS:
• Source videos with clear faces work best
• Side profiles are harder to swap
• Multiple references improve consistency
• Accept some frame variations

VARIATIONS:
• Self to anime: Swap yourself into anime style
• Celebrity style: (Ensure proper consent/disclosure)
• Fantasy character: Original IP character swap
```

### Recipe 9: Looping Background for Streams

```
RECIPE: Looping Background for Streams
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Animated backgrounds for live streams
TIME: 30-45 minutes
COST: $0.50-2 per loop
QUALITY: Good
TOOLS: Any video model + Video editor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Background concept description
• Target duration (2-10 seconds for loop)
• Stream theme/branding

STEPS:
1. Design loop-friendly scene
   - Avoid elements that can't loop (linear action)
   - Good choices: flowing water, clouds, particles, flames
   - Subtle movement preferred

2. Generate base video
   - Prompt for continuous motion
   - Include "seamless, continuous, endless"
   - Generate longer than needed (trim later)

3. Find loop point
   - Import to video editor
   - Locate similar start/end frames
   - Trim to clean loop point

4. Create seamless loop
   - Add cross-dissolve at loop point (0.5-1s)
   - Or use video looping tools
   - Test by playing on repeat

5. Export for streaming
   - Match stream resolution (1080p typical)
   - High bitrate for quality
   - MP4 or MOV format

TIPS:
• Slower motion = easier looping
• Abstract/particle content loops best
• Test with chroma key if needed
• Create multiple loops for variety

VARIATIONS:
• Green screen version: For overlay compositions
• Seasonal variants: Same scene, different times/seasons
• Reactive: Animated elements that respond to stream events
```

---

## Music Video Recipes

### Recipe 10: Beat-Synced Dance Video

```
RECIPE: Beat-Synced Dance Video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Music video with synchronized choreography
TIME: 2-4 hours
COST: $10-30 per minute of music
QUALITY: Professional
TOOLS: Seedance 1.5 Pro, librosa, NLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Final audio track (WAV/MP3)
• Dancer description
• Location/environment concept
• Shot list mapped to music sections

STEPS:
1. Analyze audio
   ```python
   import librosa
   import json

   y, sr = librosa.load("track.mp3")
   tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
   beat_times = librosa.frames_to_time(beats, sr=sr)

   # Export for reference
   markers = {"tempo": tempo, "beats": beat_times.tolist()}
   json.dump(markers, open("beat_markers.json", "w"))
   ```

2. Plan shots to music structure
   ```
   0:00-0:15  INTRO     → Establishing shot, dancer enters
   0:15-0:45  VERSE 1   → Medium shots, controlled movement
   0:45-1:15  CHORUS    → Wide shots, full energy
   1:15-1:30  BREAKDOWN → Close-ups, dramatic pause
   ...
   ```

3. Generate with Seedance
   - Upload audio track
   - Set dancer description
   - Set environment
   - Enable beat sync
   - Generate per section

4. Review sync quality
   - Major actions should hit downbeats
   - Energy should match music dynamics
   - Regenerate sections that miss beats

5. Assemble and polish
   - Import all sections to NLE
   - Fine-tune sync with slip editing
   - Add transitions on phrase boundaries
   - Color grade for consistency

6. Final mix
   - Replace scratch audio with final master
   - Add SFX where needed
   - Export multiple formats

TIPS:
• Seedance understands BPM automatically
• Describe energy levels in prompts
• Breaking into sections = better control
• Accept some variation, fix in edit

VARIATIONS:
• Performance video: Stage/concert setting
• Narrative MV: Story intercut with performance
• Lyric focus: Text overlays synced to lyrics
```

### Recipe 11: Audio-Reactive Visuals

```
RECIPE: Audio-Reactive Visuals
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Visualizer, ambient content, VJ material
TIME: 1-2 hours
COST: $5-15 per minute
QUALITY: Good to Very Good
TOOLS: Veo 3.1 or LTX-2, Audio analysis tools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Audio track
• Visual style concept
• Color palette (optional)

STEPS:
1. Analyze audio characteristics
   - Identify tempo, key moments
   - Map energy curve
   - Note frequency characteristics

2. Create visual prompts
   - Abstract: "Flowing light particles, pulsing"
   - Geometric: "Rotating sacred geometry, expanding"
   - Nature: "Aurora borealis waves, breathing"
   - Include audio-reactive language

3. Generate with native audio model
   - Veo 3.1: Include audio in prompt
   - LTX-2: Enable audio conditioning
   - Describe sync behavior

4. For manual sync approach
   - Generate base visuals
   - In After Effects / DaVinci:
     - Use audio waveform to drive effects
     - Scale, glow, color on beats
     - Camera moves on phrases

5. Iterate and refine
   - Watch with audio multiple times
   - Adjust timing/effects
   - Create seamless loops if needed

TIPS:
• Abstract content is most forgiving
• Energy mapping > precise beat sync
• Multiple layers add depth
• Consider frequency-specific reactions (bass = big moves)

VARIATIONS:
• Album visualizer: Full album, consistent style
• Live VJ set: Multiple loops to mix live
• Podcast visualizer: Subtle, conversation-appropriate
```

---

## Character Consistency Recipes

### Recipe 12: Character Sheet Creation

```
RECIPE: Character Sheet Creation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Foundation for multi-shot character consistency
TIME: 30-60 minutes
COST: $1-5 for generation
QUALITY: High (foundation quality)
TOOLS: MidJourney/FLUX + Image editor
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Character concept description
• Style reference (optional)
• Target video model (for compatibility)

STEPS:
1. Define character details
   ```
   Name: [Character name]
   Age: [Apparent age]
   Gender: [Gender presentation]
   Build: [Body type]
   Hair: [Color, style, length]
   Eyes: [Color, shape]
   Skin: [Tone, features]
   Distinguishing: [Unique features]
   Costume: [Default outfit]
   Expression: [Typical mood/expression]
   ```

2. Generate turnaround sheet
   MidJourney prompt:
   ```
   character turnaround sheet, [detailed description],
   front view, side view, back view, three-quarter view,
   character design, white background, full body,
   consistent design, [style] --ar 16:9 --v 6
   ```

3. Generate expression sheet
   ```
   character expression sheet, [character description],
   neutral, happy, sad, angry, surprised, thoughtful,
   portrait grid, white background, consistent style
   --ar 16:9 --v 6
   ```

4. Separate and organize views
   - Crop individual views
   - Name consistently:
     - char_front.png
     - char_side_left.png
     - char_side_right.png
     - char_back.png
     - char_3q_left.png
     - char_3q_right.png

5. Extract face reference
   - High-res front face crop
   - Used for FaceID/InstantID
   - Multiple expressions if needed

6. Document in reference bank
   ```
   character_name/
   ├── identity/
   │   ├── front_face.png
   │   └── expressions/
   ├── body/
   │   ├── turnaround.png
   │   └── individual/
   ├── style/
   │   └── reference.png
   └── character_spec.json
   ```

TIPS:
• Generate multiple versions, choose best
• Higher resolution = better consistency
• Keep costume simple for easier matching
• Document everything for reproducibility

VARIATIONS:
• Anime character: Use Niji mode or FLUX anime
• 3D model approach: Create in software, render views
• Photo-based: Multiple photos of real person (with consent)
```

### Recipe 13: Multi-Shot with IP-Adapter

```
RECIPE: Multi-Shot with IP-Adapter
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Consistent character across multiple shots
TIME: 1-2 hours for sequence
COST: $2-10 (depends on model choice)
QUALITY: High consistency
TOOLS: ComfyUI + IP-Adapter + Wan/LTX-2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Character sheet (Recipe 12)
• Shot list with descriptions
• ComfyUI with Kijai video nodes
• IP-Adapter models downloaded

STEPS:
1. Set up ComfyUI workflow
   ```
   [Load Character Reference]
        ↓
   [CLIP Vision Encoder]
        ↓
   [IP-Adapter FaceID Plus V2]
        ↓
   [Load Video Model (Wan/LTX-2)]
        ↓
   [Apply IP-Adapter to Model]
        ↓
   [Text Prompt] + [Negative Prompt]
        ↓
   [Video Sampler]
        ↓
   [Video Decode] → [Save Video]
   ```

2. Configure IP-Adapter settings
   ```
   weight: 0.7  (balance identity vs creativity)
   weight_type: "ease in-out"
   noise: 0.0  (for strong identity)
   ```

3. Establish seed family
   ```
   shot_1_seed = 42000
   shot_2_seed = 42001
   shot_3_seed = 42002
   # Increment by 1 for each shot
   ```

4. Generate shots sequentially
   - Shot 1: Establish baseline
   - Review quality
   - Adjust settings if needed
   - Continue with remaining shots

5. Review consistency
   - Side-by-side comparison
   - Check: face, costume, style
   - Regenerate inconsistent shots

6. Post-process
   - Minor color correction
   - Assemble sequence
   - Add audio

TIPS:
• Face reference is most important
• Lower IP-Adapter weight for more varied poses
• Higher weight for strict face matching
• Same negative prompts across all shots

VARIATIONS:
• Dual character: Two IP-Adapters, one per character
• Style + Character: IP-Adapter + Style LoRA
• Dynamic clothing: Change costume description per shot
```

---

## Batch Production Recipes

### Recipe 14: Automated Batch Generation

```
RECIPE: Automated Batch Generation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Generate many videos from prompt list
TIME: Setup: 30 min, then hands-off
COST: Depends on volume and model
QUALITY: Consistent with single generation
TOOLS: Python + fal.ai/Replicate API
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Prompt list (CSV or JSON)
• API credentials
• Output directory
• Optional: GPU for local models

STEPS:
1. Prepare prompt file
   ```json
   {
     "batches": [
       {
         "id": "product_001",
         "prompt": "Sleek wireless earbuds rotating...",
         "model": "kling",
         "duration": 5,
         "style": "premium"
       },
       {
         "id": "product_002",
         "prompt": "Smart watch face glowing...",
         "model": "kling",
         "duration": 5,
         "style": "premium"
       }
     ]
   }
   ```

2. Create batch processor
   ```python
   import fal_client
   import asyncio
   import json
   from pathlib import Path

   async def process_batch(batch_file, output_dir):
       with open(batch_file) as f:
           data = json.load(f)

       output_dir = Path(output_dir)
       output_dir.mkdir(exist_ok=True)

       tasks = []
       for item in data["batches"]:
           task = generate_video(item, output_dir)
           tasks.append(task)

       # Process with concurrency limit
       semaphore = asyncio.Semaphore(5)

       async def limited_task(task):
           async with semaphore:
               return await task

       results = await asyncio.gather(
           *[limited_task(t) for t in tasks]
       )

       # Save results log
       with open(output_dir / "results.json", "w") as f:
           json.dump(results, f, indent=2)

   async def generate_video(item, output_dir):
       try:
           result = await fal_client.submit(
               "fal-ai/kling-video/v1/standard/text-to-video",
               arguments={
                   "prompt": item["prompt"],
                   "duration": item["duration"]
               }
           )
           # Download result
           # ... save to output_dir / f"{item['id']}.mp4"
           return {"id": item["id"], "status": "success"}
       except Exception as e:
           return {"id": item["id"], "status": "error", "error": str(e)}
   ```

3. Run batch
   ```bash
   python batch_processor.py prompts.json ./output/
   ```

4. Review results
   - Check results.json for failures
   - Visually review outputs
   - Regenerate failures with adjusted prompts

5. Organize outputs
   - Move successful to final folder
   - Log failures for retry
   - Archive prompts for reproducibility

TIPS:
• Start with small batch to test
• Implement retry logic for failures
• Monitor API costs in real-time
• Consider off-peak hours for speed

VARIATIONS:
• Multi-model batch: Route to different models by prompt type
• Quality tiers: Draft → Review → Premium regeneration
• Scheduled batches: Run overnight with cron/scheduler
```

---

## Post-Production Recipes

### Recipe 15: AI Upscaling Pipeline

```
RECIPE: AI Upscaling Pipeline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Enhance AI video resolution/quality
TIME: 5-30 minutes depending on length
COST: $0.01-0.10 per frame (cloud) or free (local)
QUALITY: Significant improvement
TOOLS: Topaz Video AI or ESRGAN/RealESRGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• AI-generated video (720p or lower)
• GPU for processing
• Upscaling software

STEPS:
1. Analyze source video
   - Current resolution
   - Frame rate
   - Artifact types present

2. Choose upscaling approach

   For Topaz Video AI (best quality, paid):
   - Import video
   - Select AI model: "Proteus" for general, "Iris" for faces
   - Set output: 1080p or 4K
   - Enable: Deinterlace, Stabilize, Grain reduction
   - Process

   For RealESRGAN (free, local):
   ```bash
   # Extract frames
   ffmpeg -i input.mp4 -qscale:v 1 frames/%05d.png

   # Upscale frames
   realesrgan-ncnn-vulkan -i frames -o upscaled -n realesrgan-x4plus

   # Reassemble video
   ffmpeg -framerate 24 -i upscaled/%05d.png -c:v libx264 -pix_fmt yuv420p output.mp4
   ```

3. Preserve original audio
   ```bash
   # Extract audio from original
   ffmpeg -i input.mp4 -vn -acodec copy audio.aac

   # Combine with upscaled video
   ffmpeg -i upscaled.mp4 -i audio.aac -c:v copy -c:a aac final.mp4
   ```

4. Quality check
   - Compare side-by-side
   - Check for upscaling artifacts
   - Verify no frame drops

TIPS:
• AI video sometimes upscales better than real footage
• Face-specific models for talking head content
• 2x upscale is usually sufficient and faster
• Consider upscaling only final edit (cost savings)

VARIATIONS:
• Frame interpolation: 24→60fps with RIFE
• Denoising: Reduce AI generation artifacts
• Color enhancement: Combined with grading
```

### Recipe 16: Audio Sweetening for AI Video

```
RECIPE: Audio Sweetening for AI Video
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Add professional audio to silent AI video
TIME: 30-60 minutes
COST: $0.50-5 depending on sources
QUALITY: Professional audio
TOOLS: DAW, ElevenLabs, AudioLDM2, Freesound
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• AI-generated video (silent or with scratch audio)
• DAW (Logic, Ableton, Audacity)
• SFX libraries or generation tools
• Music (licensed or generated)

STEPS:
1. Analyze video for audio needs
   - List all visible actions
   - Identify environment (indoor/outdoor)
   - Note emotional tone
   - Plan music placement

2. Create audio layer map
   ```
   Layer 1: Room Tone / Ambience
   └─ Constant, very low level

   Layer 2: Environmental
   └─ Background sounds, birds, traffic, etc.

   Layer 3: SFX / Foley
   └─ Action-synced sounds

   Layer 4: Dialogue / VO
   └─ If applicable

   Layer 5: Music
   └─ Under or featured
   ```

3. Generate/source audio elements

   Ambient/Environmental:
   - Freesound.org for free sounds
   - Generate with AudioLDM2
   - Or purchase from library

   SFX:
   - ElevenLabs sound effects generation
   - Foley libraries
   - Record custom if needed

   Music:
   - AI generation (Suno, Udio)
   - Stock music (Artlist, Epidemic)
   - Original commission

4. Sync audio to video
   - Import video to DAW
   - Place each layer
   - Sync SFX to action (frame accurate)
   - Adjust timing as needed

5. Mix and master
   - Balance levels (dialogue priority)
   - Add EQ for clarity
   - Compress for consistency
   - Apply limiting for delivery

6. Export
   - Match video frame rate
   - Sample rate: 48kHz for video
   - Bit depth: 24-bit minimum

TIPS:
• Room tone makes everything cohesive
• Subtle SFX > obvious SFX
• Leave headroom for platform compression
• Preview on multiple speakers

VARIATIONS:
• Dialogue-first: Generate from script, add rest
• Music video: Music drives everything
• Ambient: Environmental audio only
```

---

## Troubleshooting Recipes

### Recipe 17: Fixing Hand/Face Artifacts

```
RECIPE: Fixing Hand/Face Artifacts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Repair common AI generation defects
TIME: 15-30 minutes per issue
COST: $0.50-2 for regeneration
QUALITY: Improved from original
TOOLS: Original model + Video editor + Rotoscoping
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Video with artifacts
• Original prompt
• Reference for correct appearance

STEPS:
1. Identify artifact type and location
   - Extra fingers
   - Merged fingers
   - Distorted face
   - Wrong hand position
   - Timing (which frames)

2. Try prompt refinement first
   Enhanced negative prompts:
   ```
   deformed hands, extra fingers, missing fingers, fused fingers,
   mutated hands, bad anatomy, wrong proportions, extra limbs,
   malformed hands, poorly drawn hands, poorly drawn face,
   mutation, deformed, ugly, blurry, bad anatomy, bad proportions,
   extra limbs, cloned face, disfigured, gross proportions
   ```

3. Regenerate problem sections
   - Extract good frames before/after
   - Regenerate only problem segment
   - Use I2V with good frame as start
   - Match lighting and motion

4. Inpainting approach
   - Export problem frames
   - Mask artifact areas
   - Use image inpainting
   - Reinsert corrected frames

5. Editing workaround
   - Cut away from problem shots
   - Insert B-roll during artifacts
   - Use motion blur to hide
   - Crop to exclude problem areas

6. Face swap correction
   - Extract face from good frame
   - Apply to problem frames using FaceFusion
   - Blend edges

TIPS:
• Prevention > Repair (use strong negatives)
• Hands hidden > Hands deformed
• Quick cuts hide many sins
• Color grading can hide minor issues

VARIATIONS:
• AI-assisted repair: Use newer model to fix older output
• Manual rotoscoping: For critical shots worth the time
• Composite approach: Good parts from multiple takes
```

### Recipe 18: Recovering Failed Generations

```
RECIPE: Recovering Failed Generations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USE CASE: Salvage partial or glitched outputs
TIME: 10-30 minutes
COST: Usually free (leveraging existing output)
QUALITY: Variable
TOOLS: Video editor, ffmpeg, Image tools
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENTS:
• Failed or partially successful video
• Original prompt
• Patience

STEPS:
1. Analyze failure type

   Partial success (some frames good):
   - Extract usable frames
   - Build from good content
   - Regenerate missing sections

   Glitched output (artifacts throughout):
   - Check if any frames usable
   - Try different model
   - Simplify prompt

   Timeout/incomplete:
   - Check if partial file exists
   - Try to recover partial
   - Regenerate with simpler prompt

2. Extract usable content
   ```bash
   # Extract all frames
   ffmpeg -i failed.mp4 -qscale:v 1 frames/%05d.png

   # Check which frames are good
   # Copy good frames to separate folder
   ```

3. Build from salvage
   - Use good frames as I2V start
   - Regenerate to extend good content
   - Match style with original

4. Alternative model approach
   - Same prompt, different model
   - Sometimes compatibility issues
   - Try simpler version first

5. Prompt debugging
   - Identify what caused failure
   - Remove complex elements
   - Try piece by piece
   - Build back up gradually

TIPS:
• Save all outputs (even failures)
• Log what didn't work
• Simpler prompts = higher success
• Platform issues happen (try again later)

VARIATIONS:
• Multi-model composite: Best frames from each model
• Time-lapse recovery: Stitch good frames as time-lapse
• Style transfer: Apply to any recovered frames
```

---

*Workflow Recipes Cookbook v1.0 — January 18, 2026*
*Recipes tested on: ComfyUI, Runway, Kling, Pika, Veo 3.1, Wan 2.6, LTX-2, HeyGen, Hedra*
