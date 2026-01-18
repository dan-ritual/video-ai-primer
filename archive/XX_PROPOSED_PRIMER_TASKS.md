# Proposed Additional Primer Tasks

*Building out the Video AI Primer — January 2026*

Based on the research conducted, here are 10 additional tasks to expand the primer into a comprehensive resource.

---

## Task 1: Character Consistency Deep Dive

**Objective:** Create a definitive guide to maintaining character consistency across multi-shot video sequences.

**Scope:**
- IP-Adapter integration for ComfyUI
- LoRA training for custom characters (Kohya, SDXL Trainer)
- Character sheet creation workflows
- Reference image banking strategies
- Cross-model consistency techniques (same character in Kling vs Wan vs Veo)
- Face swap vs face generation comparison

**Deliverable:** `CHARACTER_CONSISTENCY_GUIDE.md`

**Why:** This is the #1 pain point for video creators. Justine Moore's viral character swap thread shows massive demand.

---

## Task 2: Audio-Video Synchronization Masterclass

**Objective:** Document every method for adding synchronized audio to AI video.

**Scope:**
- Native audio models (Veo 3.1, LTX-2, Seedance)
- Lip sync tools (Pika, Hedra, LivePortrait)
- Music sync with beat detection
- SFX generation (ElevenLabs, AudioLDM2)
- Foley automation workflows
- Dialogue dubbing and localization

**Deliverable:** `AUDIO_VIDEO_SYNC_GUIDE.md`

**Why:** Audio is the differentiator between amateur and professional AI video. Veo 3.1's native audio changes the game.

---

## Task 3: Claude Code Video Automation Toolkit

**Objective:** Build a complete Claude Code skill for video generation orchestration.

**Scope:**
- Custom slash commands (`/gen-video`, `/batch-render`, `/upscale`)
- ComfyUI API integration
- ffmpeg post-processing chains
- Project file organization
- Batch prompting from CSV/JSON
- Progress tracking and error handling
- Output organization and naming conventions

**Deliverable:** `claude-video-skill/` directory with SKILL.md and scripts

**Why:** Your workflow already uses Claude Code. A dedicated skill would accelerate production 10x.

---

## Task 4: Model Selection Decision Tree

**Objective:** Create an interactive decision framework for choosing the right video AI model.

**Scope:**
- Use case categorization (commercial, artistic, social, film)
- Budget constraints mapping
- Quality vs speed trade-offs
- Feature requirement matching
- API availability consideration
- Future-proofing assessment

**Deliverable:** `MODEL_DECISION_TREE.md` + interactive React artifact

**Why:** With 10+ viable models, decision paralysis is real. A structured framework saves hours of trial and error.

---

## Task 5: Prompt Engineering Template Library

**Objective:** Build a copy-paste ready library of proven prompts for each model.

**Scope:**
- 50+ tested prompts per model category
- Scene types: action, dialogue, landscape, product, abstract
- Camera movement templates
- Style modifier collections
- Negative prompt libraries
- A/B tested variations with results

**Deliverable:** `PROMPT_TEMPLATE_LIBRARY.md` + JSON export

**Why:** Good prompts are hard to write from scratch. A tested library provides reliable starting points.

---

## Task 6: Cost Optimization Guide

**Objective:** Document strategies for minimizing video AI generation costs.

**Scope:**
- Platform pricing deep comparison (per-second costs)
- Credit optimization strategies
- Batch processing efficiency
- When to use fast/turbo modes
- Self-hosting cost analysis (GPU rental vs cloud vs local)
- Free tier maximization
- Volume discount negotiations

**Deliverable:** `COST_OPTIMIZATION_GUIDE.md` + pricing calculator

**Why:** At scale, video AI costs explode. Smart optimization can reduce spend by 60-80%.

---

## Task 7: Quality Assessment Framework

**Objective:** Create objective criteria for evaluating AI video quality.

**Scope:**
- Temporal consistency metrics
- Motion naturalness scoring
- Artifact detection (hand issues, face warping)
- Resolution and detail preservation
- Physics plausibility
- Style adherence measurement
- A/B comparison methodology

**Deliverable:** `QUALITY_ASSESSMENT_FRAMEWORK.md` + scoring rubric

**Why:** "Good enough" is subjective. A framework enables consistent evaluation and improvement tracking.

---

## Task 8: Legal & Rights Primer

**Objective:** Document the intellectual property landscape for AI-generated video.

**Scope:**
- Model-by-model terms of service summary
- Commercial use permissions
- Copyright status of outputs
- Training data provenance concerns
- Deepfake regulations by jurisdiction
- Attribution requirements
- Music/audio licensing considerations

**Deliverable:** `LEGAL_RIGHTS_PRIMER.md`

**Why:** Commercial use without understanding rights is risky. Clear guidance prevents legal issues.

---

## Task 9: Workflow Recipes Cookbook

**Objective:** Document complete end-to-end workflows for common production scenarios.

**Scope:**
- Recipe 1: Product video from still image
- Recipe 2: Music video with dancer
- Recipe 3: Explainer video with avatar
- Recipe 4: Social media ad (vertical)
- Recipe 5: Film pre-visualization
- Recipe 6: Anime short scene
- Recipe 7: Documentary B-roll
- Recipe 8: Character introduction sequence

**Deliverable:** `WORKFLOW_RECIPES_COOKBOOK.md`

**Why:** Seeing complete workflows from start to finish teaches more than isolated techniques.

---

## Task 10: Future-Proofing Roadmap

**Objective:** Track announced features, beta programs, and predicted developments.

**Scope:**
- Model release calendars (known)
- Beta program access tracking
- Feature predictions based on papers
- Industry trend analysis
- Acquisition/merger impacts
- OSS vs proprietary trajectory
- Hardware requirement projections

**Deliverable:** `FUTURE_ROADMAP.md` (living document)

**Why:** Video AI evolves monthly. Staying ahead of changes prevents workflow obsolescence.

---

## Priority Ranking

Based on immediate utility:

| Priority | Task | Effort | Impact |
|----------|------|--------|--------|
| 1 | Character Consistency Deep Dive | High | Critical |
| 2 | Claude Code Video Automation Toolkit | High | Very High |
| 3 | Prompt Engineering Template Library | Medium | Very High |
| 4 | Audio-Video Synchronization | High | High |
| 5 | Workflow Recipes Cookbook | Medium | High |
| 6 | Cost Optimization Guide | Low | High |
| 7 | Model Selection Decision Tree | Medium | Medium |
| 8 | Quality Assessment Framework | Medium | Medium |
| 9 | Legal & Rights Primer | Low | Medium |
| 10 | Future-Proofing Roadmap | Low | Low |

---

## Suggested Next Session

**Recommended:** Start with Task 1 (Character Consistency) or Task 2 (Claude Code Toolkit) depending on immediate needs:

- **If you're producing multi-shot content now** → Task 1 (Character Consistency)
- **If you want to automate your workflow** → Task 3 (Claude Code Toolkit)
- **If you need quick wins** → Task 5 (Prompt Templates)

Let me know which task(s) you'd like to tackle next!

---

*Proposed January 18, 2026*
