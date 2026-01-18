# Legal & Rights Primer for AI Video

*January 2026 Edition*

Navigating intellectual property, licensing, and regulatory compliance in AI video production.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Platform Terms of Service](#platform-terms-of-service)
3. [Commercial Use Matrix](#commercial-use-matrix)
4. [Copyright Status of AI Outputs](#copyright-status-of-ai-outputs)
5. [Training Data & Litigation](#training-data--litigation)
6. [Deepfake Regulations](#deepfake-regulations)
7. [Disclosure Requirements](#disclosure-requirements)
8. [Music & Audio Rights](#music--audio-rights)
9. [Voice Cloning Consent](#voice-cloning-consent)
10. [Risk Mitigation Framework](#risk-mitigation-framework)
11. [Insurance Considerations](#insurance-considerations)
12. [Compliance Checklists](#compliance-checklists)

---

## Executive Summary

### The January 2026 Legal Landscape

The legal framework for AI-generated video remains in flux, but several clear principles have emerged:

**What's Clear:**
- Purely AI-generated content likely cannot be copyrighted (US Copyright Office)
- Commercial use rights vary dramatically by platform
- Disclosure requirements are expanding globally (EU, California, China)
- Voice and likeness rights require explicit consent
- Music licensing remains unchanged (sync rights still required)

**What's Uncertain:**
- Fair use boundaries for AI training data
- Outcome of major pending lawsuits
- Federal preemption of state AI laws
- Long-term copyright treatment internationally

**Key Risks for Commercial Users:**
1. Using Veo 3.1 commercially (still Pre-GA, prohibited)
2. Generating content with protected IP (characters, logos)
3. Voice cloning without consent
4. Operating without proper disclosure in regulated jurisdictions
5. Insurance gaps for AI-specific liabilities

---

## Platform Terms of Service

### Veo 3.1 (Google)

**Status: PRE-GENERAL AVAILABILITY — COMMERCIAL USE PROHIBITED**

```
Current Terms (January 2026):
- Available via AI Ultra subscription ($249.99/month)
- Available via Vertex AI enterprise access
- Commercial use EXPLICITLY PROHIBITED under Pre-GA terms
- Non-exclusive, revocable license for generated content
- Google may use outputs for model improvement

Recommendation:
❌ Do NOT use for commercial projects
✓ Wait for General Availability announcement
✓ Contact Google for enterprise licensing timeline
```

### Sora 2 Pro (OpenAI)

**Status: COMMERCIAL USE PERMITTED (Paid Tiers)**

```
Terms Effective: January 1, 2026 (updated December 1, 2025)

Three-Tier Compliance Framework:
1. DISCLOSURE: Cannot represent AI content as human-created
2. IP PROTECTION: No protected characters or brand logos
3. PERSONALITY RIGHTS: Real person likeness requires consent

Commercial Tiers:
- Pro subscription: Full commercial rights
- Team subscription: Full commercial rights
- Enterprise: Full commercial rights + custom terms

IP Policy Update (October 3, 2025):
- Unauthorized IP use explicitly prohibited
- Opt-in copyright policy in effect
```

### Runway Gen-4.5

**Status: FULL COMMERCIAL USE PERMITTED**

```
Terms:
- Users retain ownership and all rights to outputs
- Commercial use allowed on ALL tiers (including free)
- No attribution required (though appreciated)

Data Usage:
- Standard tiers: Inputs/outputs may train Runway models
- Enterprise: Data NOT used for training, SOC 2 compliance

⚠️ RISK NOTE:
Runway facing class-action lawsuit alleging training on
YouTube videos and pirated films. Monitor case developments.
```

### Kling 2.6 (Kuaishou)

**Status: COMMERCIAL USE ON PAID TIERS**

```
Tier Breakdown:
- Free: Personal use ONLY, watermarked outputs
- Standard: Commercial permitted
- Pro: Commercial permitted
- Premier/Ultra: Commercial permitted + Private Mode

Data Considerations:
⚠️ Processing may occur on servers in China
⚠️ Critical for GDPR/data residency compliance
- Broad license granted for model improvement
- Private Mode only on higher tiers
```

### Pika

**Status: PRO TIER AND ABOVE ONLY**

```
Terms Updated: November 7, 2025

- Free: Personal use only, watermarked
- Standard: Personal use only (verify current terms)
- Pro ($35/month): Commercial permitted
- Above Pro: Commercial permitted

Note: Some conflicting information exists. Verify at pika.art
before production use.
```

### Luma Dream Machine

**Status: PLUS TIER AND ABOVE**

```
Tier Breakdown:
- Free/Lite: Personal use only, watermarked, content may train models
- Plus: Commercial permitted, limited rights granted
- Unlimited: Commercial permitted
- Enterprise: Full commercial + IP indemnification

Key Benefit:
✓ Luma provides IP indemnification to users (Enterprise)
✓ Luma cannot publicly display paid-plan generations
```

### LTX-2 (Lightricks)

**Status: STANDARD TIER AND ABOVE**

```
Terms Clarified: November 4, 2025

- Free/Lite: Personal use ONLY, business use violates terms
- Standard ($30/month): Commercial permitted
- Pro ($100/month): Commercial permitted

Open Source Model:
- Available for developers to customize/integrate
- Apache 2.0 compatible components

⚠️ Copyright Note:
LTX terms state users may have no ownership rights under
applicable law for AI-generated outputs (reflecting US position).
```

### Open Source Models

#### Wan 2.1/2.6 (Alibaba)

```
License: Apache 2.0 (FULLY PERMISSIVE)

✓ Commercial use: Unrestricted
✓ Modification: Permitted
✓ Distribution: Permitted
✓ Patent grant: Included
✓ No ownership claims on outputs

Downloads: 6.9M+ on Hugging Face

LOWEST LEGAL RISK for commercial use
```

#### HunyuanVideo (Tencent)

```
License: Tencent-Hunyuan-Community License

⚠️ TERRITORY RESTRICTIONS:
- EXCLUDES: EU, UK, South Korea
- 100M+ MAU entities need separate license
- Cannot use to improve other AI models

Commercial Use: Permitted within restrictions
Latest: HunyuanVideo-1.5 (November 2025), 8.3B params
```

---

## Commercial Use Matrix

### Quick Reference

| Platform | Free | Entry Paid | Full Commercial | Enterprise | Indemnity |
|----------|------|------------|-----------------|------------|-----------|
| Veo 3.1 | ❌ | ❌ | ❌ (Pre-GA) | Contact | ❌ |
| Sora 2 Pro | ❌ | ✓ | ✓ | ✓ | ❓ |
| Runway | ✓ | ✓ | ✓ | ✓ (no training) | ❌ |
| Kling 2.6 | ❌ | ✓ | ✓ | ✓ | ❌ |
| Pika | ❌ | ❌ | ✓ (Pro+) | ✓ | ❌ |
| Luma | ❌ | ❌ | ✓ (Plus+) | ✓ | ✓ (Ent) |
| LTX-2 | ❌ | ❌ | ✓ (Std+) | ✓ | ❌ |
| Seedance | ❓ | ✓ | ✓ | ❓ | ❌ |
| Wan (OSS) | ✓ | N/A | ✓ | N/A | N/A |
| Hunyuan | ✓* | N/A | ✓* | Custom | ❌ |

*Excludes EU, UK, South Korea; 100M+ MAU needs license

### Safest Options for Commercial Work

**Tier 1 (Lowest Risk):**
1. **Wan 2.6** — Apache 2.0, no restrictions
2. **Runway Enterprise** — No training on data, SOC 2
3. **Luma Enterprise** — IP indemnification included

**Tier 2 (Standard Risk):**
1. **Sora 2 Pro** — Clear compliance framework
2. **Kling Pro/Premier** — Well-documented terms
3. **LTX Standard/Pro** — Clear commercial rights

**Tier 3 (Elevated Risk):**
1. **Platforms in active litigation** — Monitor cases
2. **Veo 3.1** — Pre-GA status unclear
3. **HunyuanVideo in EU/UK** — Territory excluded

---

## Copyright Status of AI Outputs

### US Copyright Office Position (January 2025)

**Part 2 Report (January 29, 2025):**

```
Core Findings:

1. PURELY AI-GENERATED = NO COPYRIGHT
   Works created entirely by AI cannot receive copyright protection

2. HUMAN AUTHORSHIP REQUIRED
   Copyright only where humans determine "sufficient expressive elements"

3. PROMPTS ALONE INSUFFICIENT
   Prompts do not provide sufficient control for human authorship

4. CASE-BY-CASE ANALYSIS
   Whether human contributions constitute authorship = individual assessment

5. AI-ASSISTED WORKS
   Works where human creative expression remains evident MAY qualify
```

**Part 3 Report (May 2025) on Training:**

```
Training Data Fair Use Analysis:
- Cannot be prejudged; depends on specific circumstances
- AI developers using copyrighted works for models that generate
  "expressive content that competes with" originals likely EXCEED fair use
```

### Practical Implications

```
What This Means for Creators:

PROTECTED:
✓ Substantial human editing/arrangement of AI outputs
✓ AI as tool with human creative direction documented
✓ Composite works where human elements dominate

NOT PROTECTED:
✗ Raw AI outputs with minimal human input
✗ Prompt-only generation
✗ Automated batch generation

DOCUMENTATION REQUIREMENTS:
- Log all human creative decisions
- Record editing/modification processes
- Maintain version history showing human contribution
- Keep prompt iteration records (shows creative process)
```

### International Variations

| Jurisdiction | Position | Notes |
|--------------|----------|-------|
| USA | Human authorship required | Copyright Office guidance |
| EU | Similar human authorship standard | Under AI Act framework |
| UK | Pending clarification | Report due March 2026 |
| China | Emphasis on disclosure | Labeling > copyright grants |
| Japan | More permissive | May recognize AI contribution |

---

## Training Data & Litigation

### Major Pending Cases (January 2026)

**Getty Images v. Stability AI (UK)**
```
Status: Largely resolved November 2025
Outcome:
- Stability AI prevailed on copyright claims
- No "infringing copies" stored in model
- Getty WON on trademark (watermark in outputs)
Impact: Sets precedent that models ≠ copies
```

**Disney/Universal v. Midjourney (US)**
```
Filed: June 2025
Allegation: Training on copyrighted characters
Status: Active litigation
Risk: Downstream user exposure unclear
```

**Runway Class Action (US)**
```
Allegation: Training on YouTube videos, pirated films
Status: Active
Impact: Users of Runway outputs may face scrutiny
```

**Sony/Universal/Warner v. Suno**
```
Allegation: Music copyright infringement
Status: Active
Relevance: Affects AI music in video workflows
```

**OpenAI Multiple Suits**
```
Plaintiffs: Authors (Coates, Picoult), NY Times, others
Status: Ongoing
Settlement Activity: Anthropic settled $1.5B (late 2025)
```

### Training Data Disclosure

**Known Training Sources:**

| Model | Known/Alleged Sources | Documentation |
|-------|----------------------|---------------|
| Sora | Potentially Netflix, TikTok, Twitch | CTO uncertain on YouTube |
| Runway | Allegedly YouTube, pirated content | Under litigation |
| Stability | LAION-5B (scraped web) | Multiple lawsuits |
| Veo | Undisclosed | Google enterprise |
| Kling | Undisclosed | China-based |

### Opt-Out Status

```
Current Reality:
- EU AI Act mandates training data summaries (August 2025)
- GEMA v. OpenAI ordered source disclosure (Munich)
- Most platforms: NO retrospective opt-out for past training
- Going forward: Some platforms implementing exclusion

Best Practice:
- Assume your content may train future models
- Use robots.txt and AI-blocking headers
- Register with opt-out services where available
```

---

## Deepfake Regulations

### United States Federal Laws

**TAKE IT DOWN Act (Effective May 19, 2025)**
```
Scope: Non-consensual intimate imagery including AI deepfakes
Requirements:
- Platforms must remove within 48 hours of report
- Criminal penalties: Up to 3 years imprisonment
- Applies to AI-generated content
```

**DEFIANCE Act (Passed Senate January 2026)**
```
Scope: Federal civil right of action for deepfake victims
Remedies:
- Statutory damages: $150,000-$250,000
- Actual damages available
- Applies to intimate imagery
```

### State Laws

**California (18 Deepfake Laws)**
```
AI Transparency Act (AB853):
- Compliance extended to August 2, 2026
- Manifest + latent disclosure requirements

AB 621: Cause of action for minor deepfake pornography
SB 243 (Jan 1, 2026): AI chatbot disclosure
January 1, 2027: Full manifest/latent disclosure in effect

⚠️ AB 2655 struck down (August 2025) - Section 230 conflict
```

**Texas (Effective January 1, 2026)**
```
TRAIGA (HB 149):
- Prohibits AI for creating deepfakes
- Prohibits AI-generated CSAM
- Prohibits impersonating minors
```

**Federal Preemption Risk**
```
Executive Order (December 11, 2025):
- Proposes federal framework
- Would preempt inconsistent state laws
- Courts will determine enforceability
- Monitor for developments
```

### European Union AI Act

**Deepfake Requirements (Effective August 2, 2025)**
```
Classification: "Limited Risk" (transparency, not banned)

Article 50 Requirements:
1. Machine-readable marking and detectability
2. Disclosure when AI creates synthetic content
3. Applies to ALL deepfakes (not just harmful)

Penalties:
- Up to €35 million or 7% global revenue

Exceptions:
- Personal/non-professional use
- Proportionate treatment for artistic/satirical works

Territorial Scope:
- Applies to non-EU companies if content reaches EU users
```

**Code of Practice Timeline:**
- Draft: December 17, 2025
- Final: Expected June 2026

### China Labeling Requirements

**Effective September 1, 2025**
```
Dual Labeling Mandate:
1. VISIBLE: Watermarks, captions, labels
2. INVISIBLE: Metadata embedding

Applies To:
- Image, video, audio, text, VR
- All AI-generated content

Enforcement:
- CAC "Qinglang" actions
- Platform verification required
- Altering watermarks prohibited
```

---

## Disclosure Requirements

### Global Disclosure Matrix

| Jurisdiction | Requirement | Effective | Penalty |
|--------------|-------------|-----------|---------|
| EU | Machine-readable + visible | Aug 2, 2025 | €35M/7% revenue |
| California | Manifest + latent | Jan 1, 2027 | Civil penalties |
| New York | "Synthetic performers" in ads | June 2026 | Civil liability |
| China | Visible + metadata | Sep 1, 2025 | Platform sanctions |

### Platform-Specific Rules

**YouTube (Effective May 21, 2025)**
```
Disclosure Required For:
✓ Synthetic voices
✓ Digitally manipulated visuals depicting false actions
✓ Fabricated events

NOT Required For:
✗ Color correction
✗ Stylization
✗ AI-assisted enhancements
✗ Effects clearly unrealistic
```

**TikTok**
```
- Disclosure strongly encouraged
- "AI-generated" label option available
- Enforcement varies
```

**Meta (Facebook/Instagram)**
```
- "AI info" label for photorealistic content
- Detection systems active
- Creator disclosure encouraged
```

### Best Practice Disclosure Framework

```
Level 1: Internal Documentation
- Generation logs with timestamps
- Model/version used
- Prompt history
- Human modification records

Level 2: Metadata Embedding
- C2PA standard compliance
- Invisible watermarking
- EXIF data preservation

Level 3: Visible Disclosure
- "Created with AI" label
- Platform-specific tags
- Credits in description

Level 4: Legal Documentation
- Consent forms (for likenesses)
- License records
- Rights clearance chain
```

---

## Music & Audio Rights

### Generated Music Copyright

```
US Copyright Office Position:
- Purely AI-generated music: NOT copyrightable
- Human authorship required for protection
- Substantial editing/arrangement may qualify

Commercial Exploitation Options:
- Royalty-free licensing models
- Revenue-sharing platforms (Suno, Udio)
- Major label deals emerging (UMG-Udio partnership)
```

### Using Copyrighted Music with AI Video

```
UNCHANGED REQUIREMENTS:

Sync Rights (Composition):
- License from publisher/songwriter
- Covers the musical composition itself

Master Rights (Recording):
- License from label/recording owner
- Covers the specific recording

For AI Video:
- BOTH licenses still required
- No AI-specific exemptions
- Standard sync licensing applies
- Cover versions need mechanical + sync
```

### AI Music Platform Terms

| Platform | Commercial Use | Revenue Share | Training |
|----------|---------------|---------------|----------|
| Suno | Paid tiers | None | Uses for training |
| Udio | Paid tiers | None | UMG partnership |
| AIVA | Paid tiers | None | Classical focus |
| Mubert | Paid tiers | Yes (some) | Royalty pool |

---

## Voice Cloning Consent

### State Laws Requiring Consent

**Tennessee ELVIS Act**
```
- Property rights in name, image, likeness, AND voice
- Applies to AI-generated replicas
- Post-mortem rights for 40 years
```

**New York Digital Replicas Law (Effective January 1, 2025)**
```
Requirements:
- Informed consent required
- Applies to simulations indistinguishable from real voice
- Civil remedies for unauthorized use
```

**California**
```
- Similar protections enacted
- Extends to digital replicas
- Both living and deceased individuals
```

### Proposed Federal Protection

**NO AI FRAUD Act (Pending)**
```
Would create:
- Federal protections for voice/likeness
- Uniform consent requirements
- Criminal penalties for violations
```

### Voice Cloning Best Practices

```
ALWAYS:
✓ Obtain written consent before cloning
✓ Specify permitted uses in agreement
✓ Maintain consent documentation
✓ Limit scope to agreed purposes

NEVER:
✗ Clone without explicit permission
✗ Clone deceased individuals without estate consent
✗ Use cloned voice for deceptive purposes
✗ Exceed scope of consent agreement

CONSENT CHECKLIST:
[ ] Written consent form signed
[ ] Permitted uses specified
[ ] Duration of license defined
[ ] Territory limitations noted
[ ] Revocation terms clear
[ ] Compensation agreed (if any)
[ ] Attribution requirements stated
```

---

## Risk Mitigation Framework

### Documentation Requirements

```
Generation Records:
├── Prompts used (full text)
├── Model/version identifier
├── Timestamp of generation
├── Settings/parameters
├── Output file hashes
└── Modification history

Human Contribution Evidence:
├── Creative brief/direction
├── Edit decision list (EDL)
├── Before/after comparisons
├── Iteration history
└── Final human approval record

License Chain:
├── Platform terms version
├── Input material licenses
├── Music/audio clearances
├── Talent releases (if applicable)
└── Client usage agreement
```

### Model Selection for Commercial Safety

**Lowest Risk Stack:**
```
Video: Wan 2.6 (Apache 2.0, no restrictions)
Lip Sync: MuseTalk (open source)
Voice: Coqui TTS (open source)
Upscaling: Topaz (perpetual license)

Total License Risk: Minimal
Litigation Exposure: None known
Data Residency: Controllable (local)
```

**Standard Commercial Stack:**
```
Video: Runway Enterprise OR Luma Enterprise
Voice: ElevenLabs (clear commercial terms)
Music: Licensed library OR AI-generated (paid tier)

Benefits:
- Enterprise terms available
- Some indemnification (Luma)
- SOC 2 compliance (Runway)
```

**Elevated Risk (Avoid for High-Profile):**
```
- Platforms in active litigation
- Pre-GA products (Veo 3.1)
- Territory-restricted models in excluded regions
- Unlicensed voice cloning
```

---

## Insurance Considerations

### Market Developments (2025-2026)

**Exclusion Trend:**
```
Verisk/ISO Exclusions (Effective January 1, 2026):
- Standardized endorsements for carriers
- Allow exclusion of generative AI losses
- Check your current policies NOW
```

**New AI-Specific Products:**
```
Available Coverage:
- Armilla AI (Lloyd's underwritten): AI-specific liability
- Testudo: Technology errors coverage
- Coalition: Deepfake incident coverage (December 2025)
- Google Partnership: Beazley/Chubb for AI risks
```

### Insurance Audit Checklist

```
Review Current Policies:
[ ] Check for AI exclusion endorsements
[ ] Verify E&O coverage for AI outputs
[ ] Confirm D&O coverage for AI decisions
[ ] Review cyber policy for deepfake incidents
[ ] Assess media liability coverage

Consider Additional Coverage:
[ ] AI-specific liability endorsement
[ ] Content creator E&O
[ ] Deepfake incident response
[ ] Regulatory defense coverage
[ ] IP indemnification gap coverage
```

---

## Compliance Checklists

### Pre-Production Checklist

```
Platform Verification:
[ ] Confirmed commercial rights for intended platform
[ ] Reviewed current ToS version and date
[ ] Documented tier/subscription level
[ ] Verified data residency compliance (GDPR, etc.)

Content Rights:
[ ] Licensed all input materials
[ ] Obtained likeness releases if using real people
[ ] Cleared music/audio rights
[ ] Verified no protected IP in outputs
[ ] Voice cloning consent obtained (if applicable)

Documentation Setup:
[ ] Generation logging system active
[ ] Version control for outputs
[ ] Human contribution tracking ready
[ ] Consent forms filed
```

### Production Checklist

```
Per-Asset Documentation:
[ ] Prompt recorded
[ ] Model/version logged
[ ] Timestamp captured
[ ] Human edits documented
[ ] Final approval recorded

Quality/Compliance Review:
[ ] No unintended protected IP
[ ] No uncleared likenesses
[ ] No problematic content flags
[ ] Disclosure requirements met
[ ] Watermarking applied (if required)
```

### Delivery Checklist

```
Disclosure Requirements:
[ ] Jurisdiction-appropriate disclosure applied
[ ] Platform disclosure toggles set
[ ] Metadata embedded (C2PA if applicable)
[ ] Client informed of AI involvement

Documentation Archive:
[ ] All generation logs preserved
[ ] License chain documented
[ ] Consent forms filed
[ ] Version history saved
[ ] Client delivery confirmed
```

### Annual Review Checklist

```
Legal Landscape:
[ ] Review platform ToS updates
[ ] Monitor relevant litigation
[ ] Check new legislation/regulations
[ ] Update compliance procedures

Insurance:
[ ] Audit policies for AI exclusions
[ ] Review coverage adequacy
[ ] Consider new AI-specific products
[ ] Update risk assessment

Operational:
[ ] Train team on compliance updates
[ ] Update documentation procedures
[ ] Review and archive old projects
[ ] Test incident response procedures
```

---

## Key Contacts & Resources

### Legal Resources

- **US Copyright Office AI**: copyright.gov/ai/
- **EU AI Act Portal**: artificialintelligenceact.eu
- **California AG AI Guidance**: oag.ca.gov (search AI)
- **UK IPO AI Resources**: gov.uk/government/organisations/intellectual-property-office

### Industry Organizations

- **RIAA** (music licensing): riaa.com
- **C2PA** (content authenticity): c2pa.org
- **Partnership on AI**: partnershiponai.org

### Emergency Contacts

For deepfake/harassment incidents:
- **NCMEC CyberTipline**: missingkids.org/gethelpnow/cybertipline
- **StopNCII.org**: Image abuse removal
- **Platform trust & safety teams**: Report through official channels

---

*Legal & Rights Primer v1.0 — January 18, 2026*

**DISCLAIMER**: This guide provides general information only and does not constitute legal advice. Laws and platform terms change frequently. Consult qualified legal counsel for specific situations. Verify all platform terms directly before commercial use.
