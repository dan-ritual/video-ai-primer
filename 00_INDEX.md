# Video AI Primer

*January 2026 Edition*

---

```
PRIMER SPECIFICATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Version:        1.0
Last Updated:   January 18, 2026
Total Guides:   21 documents
Total Size:     ~400KB of curated knowledge
```

---

## Quick Navigation

| # | Document | Purpose | Priority |
|---|----------|---------|----------|
| 00 | INDEX.md | This file - navigation & overview | — |
| 01 | [Comprehensive Guide](#01-comprehensive-guide) | Foundation & model overview | ★★★★★ |
| 02 | [Model Selection Tree](#02-model-selection-tree) | Decision framework by use case | ★★★★★ |
| 03 | [JSON Prompting Guide](#03-json-prompting-guide) | Structured prompt engineering | ★★★★★ |
| 04 | [Prompt Template Library](#04-prompt-template-library) | Copy-paste templates | ★★★★☆ |
| 05 | [Platform Harness Guide](#05-platform-harness-guide) | API & platform deep dives | ★★★★☆ |
| 06 | [ComfyUI Workflows](#06-comfyui-workflows) | Node-based automation | ★★★★☆ |
| 07 | [Image Models Overview](#07-image-models-overview) | Start frame generation | ★★★★★ |
| 08 | [Start/Stop Frame Deep Dive](#08-startstop-frame-deep-dive) | FLF workflows & anime | ★★★★★ |
| 09 | [Character Consistency](#09-character-consistency) | Multi-shot coherence | ★★★★☆ |
| 10 | [Audio-Video Sync](#10-audio-video-sync) | Sound integration | ★★★☆☆ |
| 11 | [Workflow Recipes](#11-workflow-recipes) | Production cookbook | ★★★★☆ |
| 12 | [Cost Optimization](#12-cost-optimization) | Budget & efficiency | ★★★☆☆ |
| 13 | [Claude Code Toolkit](#13-claude-code-toolkit) | Automation scripts | ★★★★☆ |
| 14 | [Agent Quality Evals](#14-agent-quality-evals) | Automated assessment | ★★★☆☆ |
| 15 | [Legal Rights Primer](#15-legal-rights-primer) | ToS & compliance | ★★★☆☆ |
| 16 | [Influencers Guide](#16-influencers-guide) | Who to follow | ★★★☆☆ |
| 17 | [Future-Proofing Roadmap](#17-future-proofing-roadmap) | 2026-2027 predictions | ★★★☆☆ |
| 18 | [Research Log](#18-research-log) | Source documentation | ★★☆☆☆ |
| 19 | [FFmpeg Pipeline](#19-ffmpeg-pipeline) | RIFE, Real-ESRGAN, CLI automation | ★★★★★ |
| 20 | [ComfyUI Ecosystem](#20-comfyui-ecosystem) | Workflows, resources, Claude Code integration | ★★★★★ |
| 99 | [AGENTS.md](#agents-optimization) | Agent retrieval guide | Meta |

---

## File Mapping

### Current Filenames → Sequence Numbers

```
RENAMING SCHEME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

00_INDEX.md                          ← (This File - New)
01_VIDEO_AI_COMPREHENSIVE_GUIDE.md   ← VIDEO_AI_COMPREHENSIVE_GUIDE_JAN2026.md
02_MODEL_SELECTION_DECISION_TREE.md  ← MODEL_SELECTION_DECISION_TREE.md
03_JSON_PROMPTING_GUIDE.md           ← JSON_PROMPTING_GUIDE.md
04_PROMPT_TEMPLATE_LIBRARY.md        ← PROMPT_TEMPLATE_LIBRARY.md
05_PLATFORM_HARNESS_GUIDE.md         ← PLATFORM_HARNESS_GUIDE.md
06_COMFYUI_NODE_WORKFLOWS_GUIDE.md   ← COMFYUI_NODE_WORKFLOWS_GUIDE.md
07_IMAGE_MODELS_STATE_OF_UNION.md    ← IMAGE_MODELS_STATE_OF_UNION.md
08_START_STOP_FRAME_DEEP_DIVE.md     ← START_STOP_FRAME_DEEP_DIVE.md
09_CHARACTER_CONSISTENCY_GUIDE.md    ← CHARACTER_CONSISTENCY_GUIDE.md
10_AUDIO_VIDEO_SYNC_GUIDE.md         ← AUDIO_VIDEO_SYNC_GUIDE.md
11_WORKFLOW_RECIPES_COOKBOOK.md      ← WORKFLOW_RECIPES_COOKBOOK.md
12_COST_OPTIMIZATION_GUIDE.md        ← COST_OPTIMIZATION_GUIDE.md
13_CLAUDE_CODE_VIDEO_TOOLKIT.md      ← CLAUDE_CODE_VIDEO_TOOLKIT.md
14_AGENT_QUALITY_EVALS_FRAMEWORK.md  ← AGENT_QUALITY_EVALS_FRAMEWORK.md
15_LEGAL_RIGHTS_PRIMER.md            ← LEGAL_RIGHTS_PRIMER.md
16_VIDEO_AI_INFLUENCERS_GUIDE.md     ← VIDEO_AI_INFLUENCERS_GUIDE.md
17_FUTURE_PROOFING_ROADMAP.md        ← FUTURE_PROOFING_ROADMAP.md
18_RESEARCH_LOG.md                   ← RESEARCH_LOG.md
19_FFMPEG_POSTPROCESSING_PIPELINE.md ← (New - Grok-Verified)
20_COMFYUI_ECOSYSTEM_POWERUSER_GUIDE.md ← (New)
99_AGENTS.md                         ← (To Be Created)

ARCHIVE:
XX_PROPOSED_PRIMER_TASKS.md          ← PROPOSED_PRIMER_TASKS.md (superseded)
```

---

## Section Breakdown

### Foundation (01-03)
*Start here if you're new to this primer*

#### 01 Comprehensive Guide
**File:** `01_VIDEO_AI_COMPREHENSIVE_GUIDE.md`
**Size:** ~31KB | **Read Time:** 25-30 min

The master overview covering:
- January 2026 model landscape
- Veo 3.1, Kling 2.6, Sora 2 Pro, Runway Gen-4.5
- Open source options (Wan 2.6, LTX-2, HunyuanVideo)
- Capability matrices and comparisons
- Getting started recommendations

---

#### 02 Model Selection Tree
**File:** `02_MODEL_SELECTION_DECISION_TREE.md`
**Size:** ~20KB | **Read Time:** 15-20 min

Decision framework for choosing the right model:
- By content type (realistic, anime, abstract)
- By use case (social media, commercial, film)
- By budget constraints
- By technical requirements
- Flowcharts and decision trees

---

#### 03 JSON Prompting Guide
**File:** `03_JSON_PROMPTING_GUIDE.md`
**Size:** ~17KB | **Read Time:** 15 min

Structured prompting methodology:
- JSON schema for video prompts
- Model-specific syntax
- Negative prompt engineering
- Advanced techniques

---

### Prompting & Templates (04)

#### 04 Prompt Template Library
**File:** `04_PROMPT_TEMPLATE_LIBRARY.md`
**Size:** ~25KB | **Read Time:** Reference doc

Copy-paste ready templates:
- 8 video models covered
- JSON schemas per model
- Negative prompt libraries
- Shot type templates

---

### Platforms & Tools (05-06)

#### 05 Platform Harness Guide
**File:** `05_PLATFORM_HARNESS_GUIDE.md`
**Size:** ~26KB | **Read Time:** 20 min

API and platform deep dives:
- fal.ai, Replicate, RunPod, Together.ai
- Cost comparisons
- API integration patterns
- Rate limits and optimization

---

#### 06 ComfyUI Workflows
**File:** `06_COMFYUI_NODE_WORKFLOWS_GUIDE.md`
**Size:** ~12KB | **Read Time:** 10-15 min

Node-based video generation:
- Essential nodes for video
- Workflow templates
- Custom node recommendations
- Optimization tips

---

### Image-to-Video Pipeline (07-08)
*Your specialty workflow area*

#### 07 Image Models Overview
**File:** `07_IMAGE_MODELS_STATE_OF_UNION.md`
**Size:** ~17KB | **Read Time:** 15 min

Start frame generation landscape:
- Nano Banana Pro (Gemini 3 Pro Image)
- Midjourney V7 and Niji 7
- FLUX.2 (Dev, Pro, Schnell)
- Ideogram 3.0
- Comparative analysis

---

#### 08 Start/Stop Frame Deep Dive
**File:** `08_START_STOP_FRAME_DEEP_DIVE.md`
**Size:** ~24KB | **Read Time:** 20 min

First-Last Frame (FLF) workflows:
- Wan 2.1/2.2 FLF2V pipelines
- Anime production with Niji 7
- Nano Banana Pro integration
- Character consistency in FLF
- Production recipes

---

### Production Techniques (09-11)

#### 09 Character Consistency
**File:** `09_CHARACTER_CONSISTENCY_GUIDE.md`
**Size:** ~21KB | **Read Time:** 15-20 min

Multi-shot coherence methods:
- IP-Adapter techniques
- LoRA training for characters
- --sref and --cref usage
- Cross-shot workflows

---

#### 10 Audio-Video Sync
**File:** `10_AUDIO_VIDEO_SYNC_GUIDE.md`
**Size:** ~23KB | **Read Time:** 15-20 min

Sound integration:
- Native audio models (Veo, Seedance)
- Lip sync (Hedra, HeyGen)
- Music synchronization
- Foley automation

---

#### 11 Workflow Recipes
**File:** `11_WORKFLOW_RECIPES_COOKBOOK.md`
**Size:** ~39KB | **Read Time:** 25-30 min (reference)

18 production recipes:
- Social media content
- Product videos
- Character animations
- Music videos
- Documentaries
- Step-by-step procedures

---

### Operations (12-14)

#### 12 Cost Optimization
**File:** `12_COST_OPTIMIZATION_GUIDE.md`
**Size:** ~17KB | **Read Time:** 15 min

Budget management:
- Per-model pricing
- Self-hosting economics
- Budget templates
- ROI calculations

---

#### 13 Claude Code Toolkit
**File:** `13_CLAUDE_CODE_VIDEO_TOOLKIT.md`
**Size:** ~43KB | **Read Time:** 30 min (reference)

Automation scripts:
- Python API wrappers
- Batch processing
- Quality checking
- Pipeline orchestration
- Claude Code integration

---

#### 14 Agent Quality Evals
**File:** `14_AGENT_QUALITY_EVALS_FRAMEWORK.md`
**Size:** ~34KB | **Read Time:** 25 min

Automated assessment:
- Visual quality metrics
- LLM-as-Judge frameworks
- Evaluation pipelines
- Quality gates

---

### Context (15-18)

#### 15 Legal Rights Primer
**File:** `15_LEGAL_RIGHTS_PRIMER.md`
**Size:** ~23KB | **Read Time:** 20 min

Compliance guidance:
- ToS analysis by platform
- Copyright considerations
- Deepfake regulations
- Commercial use rights

---

#### 16 Influencers Guide
**File:** `16_VIDEO_AI_INFLUENCERS_GUIDE.md`
**Size:** ~23KB | **Read Time:** 15 min

Social graph for practitioners:
- Must-follow accounts
- YouTube channels
- Communities & Discords
- PsyopAnime workflow analysis

---

#### 17 Future-Proofing Roadmap
**File:** `17_FUTURE_PROOFING_ROADMAP.md`
**Size:** ~17KB | **Read Time:** 15 min

Predictions through 2027:
- Technology trajectory
- Skills to develop
- Investment priorities
- Risk factors

---

#### 18 Research Log
**File:** `18_RESEARCH_LOG.md`
**Size:** ~17KB | **Read Time:** Reference

Source documentation:
- Research notes
- Citation tracking
- Update history

---

### Meta (99)

#### 99 AGENTS.md
**File:** `99_AGENTS.md`
**Size:** ~TBD | **Read Time:** N/A (agent consumption)

Agent retrieval optimization:
- Structured for Claude Code, OpenCode, Amp, Codex
- Semantic chunking
- Query optimization
- Cross-reference graph

---

## Reading Paths

### Path 1: New to This Primer
*~2 hours for core understanding*

```
START → 01 Comprehensive Guide
      → 02 Model Selection Tree
      → 07 Image Models Overview
      → 08 Start/Stop Frame Deep Dive
      → 11 Workflow Recipes (skim)
```

### Path 2: Start Frame Workflow Focus
*Your specialty - 1 hour deep dive*

```
START → 07 Image Models Overview
      → 08 Start/Stop Frame Deep Dive
      → 03 JSON Prompting Guide
      → 09 Character Consistency
```

### Path 3: Production Pipeline Setup
*Building end-to-end workflows*

```
START → 05 Platform Harness Guide
      → 06 ComfyUI Workflows
      → 13 Claude Code Toolkit
      → 11 Workflow Recipes
```

### Path 4: Staying Current
*Information velocity optimization*

```
START → 16 Influencers Guide
      → 17 Future-Proofing Roadmap
      → 18 Research Log
```

### Path 5: Agent Integration
*For automated retrieval*

```
START → 99 AGENTS.md
      → (Follow agent-specific instructions)
```

---

## Document Statistics

```
CORPUS OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Documents:     19 (+ this index)
Total Size:          ~415 KB
Word Count:          ~70,000 words (estimated)
Unique Topics:       50+
Code Snippets:       100+
Decision Trees:      15+
Workflow Recipes:    18+

COVERAGE BY AREA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model Knowledge:     ████████████████████ 100%
Prompting:           ████████████████████ 100%
Workflows:           ████████████████████ 100%
Image→Video:         ████████████████████ 100%
Audio:               ████████████░░░░░░░░  60%
Legal:               ████████████████░░░░  80%
Automation:          ████████████████████ 100%
Future Outlook:      ████████████████░░░░  80%

UPDATE FREQUENCY TARGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model Guides:        Monthly (rapid change)
Workflows:           Bi-weekly (techniques evolve)
Legal:               Quarterly (regulations change)
Future Roadmap:      Quarterly (predictions shift)
Index:               As needed
```

---

## Changelog

### v1.0 — January 18, 2026
- Initial release of complete primer
- 19 core documents
- Full coverage of January 2026 landscape
- Image model and FLF workflow integration
- Influencer social graph

### Planned Updates
- [ ] v1.1: Add Veo 3.1 GA-specific workflows
- [ ] v1.2: Integrate new open-source model releases
- [ ] v1.3: Expand audio synchronization section
- [ ] v1.4: Add more production case studies

---

## How to Use This Primer

### For Human Readers

1. **Start with your priority path** (see Reading Paths above)
2. **Bookmark this INDEX** for quick navigation
3. **Use Ctrl+F/Cmd+F** within documents for specific topics
4. **Follow the Influencers Guide** to stay updated
5. **Check Research Log** for source verification

### For AI Agents

1. **Ingest 99_AGENTS.md first** for retrieval instructions
2. **Use semantic search** across document corpus
3. **Respect document boundaries** for coherent responses
4. **Cross-reference using the index** for multi-document queries
5. **Check timestamps** in individual docs for freshness

---

## File Organization

### Directory Structure (Recommended)

```
/jan2026-video-gen/
├── 00_INDEX.md                         # This file
├── 01_VIDEO_AI_COMPREHENSIVE_GUIDE.md
├── 02_MODEL_SELECTION_DECISION_TREE.md
├── 03_JSON_PROMPTING_GUIDE.md
├── 04_PROMPT_TEMPLATE_LIBRARY.md
├── 05_PLATFORM_HARNESS_GUIDE.md
├── 06_COMFYUI_NODE_WORKFLOWS_GUIDE.md
├── 07_IMAGE_MODELS_STATE_OF_UNION.md
├── 08_START_STOP_FRAME_DEEP_DIVE.md
├── 09_CHARACTER_CONSISTENCY_GUIDE.md
├── 10_AUDIO_VIDEO_SYNC_GUIDE.md
├── 11_WORKFLOW_RECIPES_COOKBOOK.md
├── 12_COST_OPTIMIZATION_GUIDE.md
├── 13_CLAUDE_CODE_VIDEO_TOOLKIT.md
├── 14_AGENT_QUALITY_EVALS_FRAMEWORK.md
├── 15_LEGAL_RIGHTS_PRIMER.md
├── 16_VIDEO_AI_INFLUENCERS_GUIDE.md
├── 17_FUTURE_PROOFING_ROADMAP.md
├── 18_RESEARCH_LOG.md
├── 99_AGENTS.md
├── index.html                          # Web interface
└── /archive/
    └── XX_PROPOSED_PRIMER_TASKS.md     # Superseded
```

---

*Video AI Primer — Index v1.0*
*January 18, 2026*
