# Text Adventure Story Expansion - Project Notes

## Project Overview
**Story:** "Love in the City of Dreams" - A romantic interactive drama about relationship challenges
**Format:** JSON-based branching narrative (story.json)
**Target:** 35-40 minute gameplay experience with multiple endings

## Original State
- 17 scenes, ~9,500 words
- 15 choice points
- 8-12 minutes gameplay
- **Problem:** Too short, rushed pacing

## Completed Expansion (All 7 Batches)
Successfully expanded to meet 35-40 minute target:
- **60+ scenes, ~23,000-25,000 words**
- **55+ choice points** (40+ single-choice prompts for pacing)
- **35-42 minutes estimated gameplay** ✓

## Story Structure

### Two Main Arcs
1. **New York Arc** - Alex's ex Jordan at work, corporate pressure
2. **Paris Arc** - Alex's childhood friend Riley as supervisor, old feelings

### Key Design Principles Applied

#### 1. Single-Choice Prompts for Pacing
- Used extensively (40+ added)
- Examples: "Continue...", "Two weeks later...", "The weekend begins..."
- Purpose: Build tension, allow absorption, create breathing room
- **Critical insight:** Single choices aren't fake choices - they're engagement prompts that maintain user interaction while building narrative momentum

#### 2. Gradual Progression
- **Before crisis:** Settlement scenes showing life adjustment (2-3 scenes)
- **Crisis build-up:** Multiple small incidents before major confrontation
- **After crisis:** Extended resolution showing growth/deterioration over time
- **Endings:** Detailed epilogues with time jumps

#### 3. Branching That Matters
Early choices create distinct paths:
- **NY Arc:** Career focus vs Support Alex vs Balance → Different dynamics with Jordan
- **Paris Arc:** Independent vs Dependent vs Expat → Different relationship with Riley
- **Crisis handling:** Confront vs Patient talk vs Take space → Different outcomes

## Scene Expansion Formula

### Crisis Scenes (split into 3-4 scenes)
1. **Setup** - Single choice to enter moment
2. **Peak moment** - The confrontation/discovery
3. **Immediate aftermath** - Single choice for processing
4. **Resolution/consequences** - Meaningful choice about next step

### Example: "patient-talk" expansion
- Original: 1 scene, direct to resolution
- Expanded: 4 scenes
  - patient-talk: Decision to wait (single choice)
  - patient-talk-conversation: The actual talk (single choice)
  - patient-talk-resolution: Working through it (single choice)
  - patient-talk-new-normal: New boundaries established (single choice)
  - patient-talk-ending: Proposal scene (final choice)

### Tragedy Paths (show deterioration)
Use time markers with single choices:
- "Two weeks later..." → show first small crack
- "Another month passes..." → show escalation
- "Three months later..." → show breaking point
- Each time jump is a single-choice prompt that maintains engagement

### Growth Paths (show healing)
Similar time-based structure:
- "The first therapy session..." (single choice)
- "Three months later..." (single choice)
- "One year later..." (single choice)
- Shows realistic healing timelines, not instant fixes

## Technical Structure (JSON)

```json
{
  "scene-name": {
    "title": "Scene Title",
    "story": [
      "Paragraph 1",
      "Paragraph 2",
      "Paragraph 3"
    ],
    "options": [
      {
        "text": "Choice text OR single-choice pacing prompt",
        "arc": "next-scene-name"
      }
    ]
  }
}
```

## Content Added by Batch

### Batch 1: NY Early Settlement (~2,600 words)
- new-york-settling, new-york-month-one
- new-york-career-focus, new-york-support-alex, new-york-balanced
- new-york-jordan-intro
- new-york-befriend-jordan, new-york-distance-jordan, new-york-early-talk

### Batch 2: Paris Early Settlement (~2,500 words)
- paris-settling, paris-month-one
- paris-independent, paris-dependent, paris-expat
- paris-riley-intro

### Batch 3: NY Crisis Expansion (~2,000 words)
- confrontation-moment
- honest-jealousy-resolution, honest-jealousy-ending
- patient-talk-conversation, patient-talk-resolution, patient-talk-new-normal, patient-talk-ending
- space-day-two, space-explanation

### Batch 4: Paris Crisis Expansion (~2,100 words)
- boundaries-weekend, boundaries-return, boundaries-decision
- silent-suffering-return, silent-suffering-discovery, silent-suffering-confrontation
- surprise-visit-arrival, surprise-visit-disaster

### Batch 5: Reconciliation Paths (~2,000 words)
- reconciliation-therapy-one, reconciliation-progress, reconciliation-milestone, reconciliation-wedding
- trust-built-seasons, trust-built-proposal

### Batch 6: Tragedy Paths (~1,500 words)
- play-cool-deterioration-one, play-cool-deterioration-two, play-cool-confrontation
- double-down-aftermath, double-down-breakup, double-down-aftermath-year

### Batch 7: Endings
- No changes needed - already well-developed

## Writing Style Notes

### Tone
- Present tense, second person ("You do this...")
- Direct, emotional, literary
- Internal monologue woven in naturally
- Specific sensory details (smells, sights, feelings)

### Pacing Techniques
- Short paragraphs for tension: "They're actually working."
- Longer paragraphs for reflection/buildup
- Dialogue without tags when clear from context
- Strategic line breaks for impact

### Emotional Beats
- Show don't tell: "Something flickers in their eyes" not "They looked disappointed"
- Physical manifestations: "Your hands shake", "stomach drops"
- Comparative thoughts: "Like you're strangers who once knew each other's names"

## Key Learnings for Future Expansions

1. **Single choices are crucial** - Not fake, they're pacing tools that maintain engagement
2. **Time jumps need prompts** - "Three months later..." as a choice, not just in text
3. **Crisis scenes need 3-4 beats** - Setup, peak, aftermath, resolution
4. **Show the work** - Therapy, growth, deterioration all take time
5. **Early choices should matter** - Create distinct variations, not just cosmetic differences
6. **Don't rush to endings** - Multiple scenes showing life after the crisis
7. **Balance paths** - Tragedy needs as much detail as romance

## Final Stats
- **Original:** 17 scenes, 9.5k words, 15 prompts, 8-12 min
- **Expanded:** 60+ scenes, 23-25k words, 55+ prompts, 35-42 min
- **Target achieved:** 35-40 minutes ✓

## Files Modified
- `/Users/jules/Projects/games/text_adventure/story.json` - Main story file with all expansions

---

*Project completed successfully. Story now has appropriate depth, pacing, and interactivity for target gameplay duration.*
