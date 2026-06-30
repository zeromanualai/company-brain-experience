
# Company Brain Experience
## Final Build Plan v1.0
### Platform-First · Content-Second · Three Phases

---

# Project Name

> **Company Brain Experience**

Not "Interactive Understanding System."
Not "Architecture Atlas."
Not "Documentation Explorer."

When someone opens this, they should feel like they are
experiencing the Company Brain — not reading about it.
That starts with the name.

---

# What We Are Building

A single Streamlit application that progressively builds
the Company Brain mental model for any audience —
executive, engineer, new hire, investor, advisor —
starting from the problem it solves and ending
with complete architectural understanding.

It is the Company Brain's first act of self-demonstration.

---

# Technology Stack


Streamlit          — app framework, routing, layout
Plotly             — architecture diagrams, flow charts
SVG (inline)       — custom visuals rendered in st.markdown
JSON               — all content (never hardcode content into pages)
Markdown           — long-form text in content files
Google Fonts       — Space Grotesk, Inter, JetBrains Mono


**Why Streamlit:**
Content rewrites constantly during a project like this.
Streamlit lets you change a JSON file and see the result immediately.
Speed of iteration matters more than visual perfection at this stage.

**Why JSON for content:**
Content and UI are separate concerns.
If content lives inside Python files, every edit is a code change.
If content lives in JSON, a non-technical person can update it.
Later, content can be AI-generated from the canonical documents.

**No backend. No database. No external APIs.**
Everything runs from static files.

---

# Core Architecture Principle


Content Files (JSON + Markdown)
        ↓
Rendering Engines (Python components)
        ↓
Pages (assembly only — no logic, no content)


Pages never contain content.
Pages never contain business logic.
Pages only call components.

Components never contain content.
Components only know how to render a content shape.

Content files contain everything humans read.

---

# Folder Structure


company_brain_experience/
│
├── app.py                        ← entry point, routing only
│
├── core/
│   ├── theme.py                  ← colors, fonts, CSS injection
│   ├── session.py                ← session state management
│   ├── router.py                 ← page routing logic
│   └── audience.py               ← audience mode management
│
├── components/
│   ├── layout.py                 ← page shells, headers, breadcrumbs
│   ├── hero.py                   ← full-width intro sections
│   ├── pipeline_visual.py        ← the interactive architecture pipeline
│   ├── concept_card.py           ← universal concept card renderer
│   ├── scenario_player.py        ← step-by-step scenario walkthrough
│   ├── comparison_card.py        ← side-by-side concept comparisons
│   ├── flow_diagram.py           ← SVG/Plotly flow diagrams
│   ├── memory_store_card.py      ← memory type visual card
│   └── search_results.py         ← concept search results
│
├── pages/
│   ├── home.py                   ← audience selection + entry
│   ├── problem.py                ← The Problem
│   ├── what_is_cb.py             ← What Is Company Brain?
│   ├── big_picture.py            ← The Big Picture (interactive pipeline)
│   ├── reality_pipeline.py       ← The Reality Pipeline walkthrough
│   ├── concepts.py               ← dynamic concept page (data-driven)
│   ├── scenarios.py              ← scenario selector + player
│   ├── comparisons.py            ← concept comparison explorer
│   ├── relationships.py          ← relationship explorer
│   └── documents.py              ← document reference layer
│
├── content/
│   ├── concepts.json             ← all concept definitions
│   ├── scenarios.json            ← all step-by-step scenarios
│   ├── comparisons.json          ← concept comparison pairs
│   ├── relationships.json        ← concept relationship graph data
│   ├── audiences.json            ← per-audience language adaptations
│   └── documents.json            ← document metadata + summaries
│
└── assets/
    └── fonts/                    ← fallback fonts if Google Fonts unavailable


---

# Navigation Structure


🧠  Company Brain Experience

├── Home                  ← audience selection
├── The Problem           ← why this exists
├── What Is It?           ← mental model
├── Big Picture           ← full architecture visual
├── How It Works          ← Reality Pipeline walkthrough
├── ─────────────
├── Concepts              ← data-driven concept explorer
├── Scenarios             ← animated walkthroughs
├── Compare               ← concept comparisons
├── Relationships         ← concept graph
├── ─────────────
├── Documents             ← canonical reference layer
└── Search                ← concept search


**Navigation rules:**
- Top five items are the guided learning path (in order)
- Bottom five items are the exploration layer (any order)
- A "Continue Learning" indicator shows where the user is in the arc
- Audience mode is always visible and always switchable
- No section is ever locked or unavailable

---

# Content File Schemas

Define these before building. Components are built to match these shapes.

## concepts.json

json
{
  "id": "memory",
  "plain_name": "Remembering",
  "technical_name": "Memory Layer",
  "one_sentence": "The Brain stores everything the organization knows, organized by what kind of knowledge it is.",
  "why_it_exists": "Organizations forget constantly. Without structured memory, every meeting ends and the knowledge disappears.",
  "what_it_does": "...",
  "real_example": "...",
  "audience_variants": {
    "executive": "...",
    "engineer": "...",
    "new_hire": "..."
  },
  "visual": "memory_stores",
  "relationships": {
    "created_by": ["knowledge_objects"],
    "feeds_into": ["intelligence"],
    "governed_by": ["trust"],
    "related": ["knowledge_objects", "ontology", "evolution"]
  },
  "technical_depth": "...",
  "source_doc": "Memory Model v1.2",
  "source_section": "§6"
}


## scenarios.json

json
{
  "id": "customer_meeting",
  "title": "The Customer Meeting",
  "subtitle": "How one sales call becomes memory, intelligence, and action",
  "steps": [
    {
      "step": 1,
      "layer": "Reality",
      "title": "The Meeting Happens",
      "narrative": "...",
      "technical_detail": "...",
      "concepts_touched": ["actor", "commitment", "communication"],
      "visual": "meeting_capture"
    }
  ]
}


## comparisons.json

json
{
  "id": "memory_vs_knowledge_objects",
  "title": "Memory vs Knowledge Objects",
  "question": "What's the difference between the Brain's filing format and what it actually stores?",
  "left": {
    "concept_id": "knowledge_objects",
    "role": "The filing card",
    "key_point": "Structured representation. Not stored permanently."
  },
  "right": {
    "concept_id": "memory",
    "role": "The filing system",
    "key_point": "Persistent, governed, provenance-tagged."
  },
  "the_key_difference": "..."
}


## audiences.json

json
{
  "executive": {
    "id": "executive",
    "label": "Executive / Investor / Advisor",
    "description": "I need to understand the business concept and strategic value.",
    "language_style": "business value and outcomes, no technical terms",
    "depth": "overview",
    "entry_section": "problem"
  }
}


---

# Concept Card Standard

Every concept rendered in the system follows this exact template.
This is the universal rendering contract between content and UI.


┌─────────────────────────────────────────────┐
│  Plain-language name          [technical]   │
│  ─────────────────────────────────────────  │
│  One sentence.                              │
│                                             │
│  WHY IT EXISTS                              │
│  What breaks if this doesn't exist.         │
│                                             │
│  WHAT IT DOES                               │
│  One paragraph, plain language.             │
│                                             │
│  REAL EXAMPLE                               │
│  Concrete, not abstract.                    │
│                                             │
│  [Visual if applicable]                     │
│                                             │
│  RELATIONSHIPS                              │
│  Created by:  ···                           │
│  Feeds into:  ···                           │
│  Governed by: ···                           │
│  Related:     ···                           │
│                                             │
│  [▼ Technical Detail]    [↗ Source Doc]    │
└─────────────────────────────────────────────┘


**Plain-language name** is always the primary heading.
**Technical name** appears small, secondary, grey.
**Technical Detail** is always collapsed by default.
**Source Doc** always links to the Document layer.

---

# Brand


Background:        #0D1117
Surface:           #161B22
Border:            #30363D
Primary Text:      #F0F6FC
Secondary Text:    #8B949E
Accent Orange:     #FF6B00  ← Company Brain brand
Capture:           #38BDF8  ← blue
Memory:            #818CF8  ← indigo
Intelligence:      #34D399  ← green
Trust:             #FBBF24  ← amber
Product:           #F472B6  ← pink
Evolution:         #A78BFA  ← violet

Fonts:
  Headings:        Space Grotesk
  Body:            Inter
  Code / IDs:      JetBrains Mono


---

# Phase 1
# Platform + Core Story
## "Someone with no background understands Company Brain in 10 minutes."

**This is the investor meeting, the advisor briefing, the first-day onboarding.**
Build nothing you don't need for that goal.

---

## What Gets Built

### Core Framework (no content yet — just infrastructure)


theme.py          → CSS injection, brand colors, fonts
session.py        → audience mode, current section, progress
router.py         → section routing from sidebar
audience.py       → audience selection state and language switching
layout.py         → page shell, header, sidebar, breadcrumb


All content is stubbed with placeholder text.
Goal: can navigate between empty pages with correct styling.

### Home Page

Audience selector. Five choices.
Each choice sets `session.audience` and routes to The Problem.
Can be changed at any time via sidebar.
No progress is lost when audience changes.

### The Problem (Section 1)

Four visual story cards, one per problem:
- The Meeting Problem
- The Commitment Problem
- The Context Problem
- The Repetition Problem

Each card: bold headline → one-sentence description → short narrative → visual icon.
Closes with: "This is organizational amnesia. Company Brain is the cure."

Audience adaptation:
- Executive: business cost framing ("This costs organizations...")
- Engineer: systems framing ("These are information architecture failures...")
- New hire: relatable framing ("You've probably experienced this...")

### What Is Company Brain? (Section 2)

One visual. One mental model paragraph. One sentence.
Audience-adaptive text beneath the visual.
"Continue" leads to Big Picture.

### The Big Picture (Section 3)

The full interactive architecture pipeline as an SVG/Plotly visual.
Every layer is clickable.
Clicking a layer opens a tooltip with one-sentence description.
"Explore this layer" links to its Concept card.
Trust shown as a surrounding boundary, not a layer in the sequence.

Three audience-adaptive captions beneath the visual.

### The Reality Pipeline (Section 4)

Eight-step animated walkthrough. This is the centrepiece.
One step visible at a time.
Previous / Next navigation.
Each step: layer name → plain narrative → example detail.
Technical detail expandable on each step.
Concepts mentioned in each step are highlighted and link to Concept cards.

Steps:
1. The Meeting Happens
2. Capture
3. Understanding (ten primitives extracted)
4. Knowledge Objects formed
5. Memory formation (which store, why)
6. Intelligence reasoning (what the Brain detects)
7. Exposure (Brain delivers to Maria in Gmail)
8. Evolution (learning logged)

### Document Reference Layer (Section 16)

Six document cards. Each card:
- Document name + version
- One-paragraph summary
- Key concepts it defines (linked)
- "Open document" expander showing the full text

Documents are references, not entry points.
Never appears first in navigation.

---

## What Does NOT Get Built in Phase 1


✗ Concept Explorer (full version)
✗ Relationship graph
✗ Concept comparisons
✗ Scenario selector
✗ Concept search
✗ All architecture layer deep-dives (Memory, Intelligence, etc.)
✗ Audience views beyond the three adaptive captions


---

## Phase 1 Exit Criteria

Before moving to Phase 2, every item must be true:


✓ A person who has never heard of Company Brain
  can navigate the full arc (Problem → What Is It → Big Picture → Pipeline)
  in under 12 minutes without confusion.

✓ The Reality Pipeline walkthrough is complete
  with all 8 steps, correct narrative, and working step navigation.

✓ Audience switching works on every page
  and visibly changes at least one piece of text per page.

✓ All six documents are accessible in the reference layer.

✓ The visual pipeline in Big Picture has all seven layers
  and Trust surrounding them, with working click-to-tooltip.

✓ Zero hardcoded content inside any page or component file.
  All content lives in JSON or Markdown files.

✓ CSS and fonts load correctly.
  All brand colors match spec.


---

# Phase 2
# Concept Engine + Architecture Depth
## "Anyone on the team understands every layer and every concept."

**This is team onboarding, advisor deep dives, and technical review.**
Build everything a new engineer or non-technical PM needs
to understand the architecture boundaries without reading the documents.

---

## What Gets Built

### Concept Engine

The most important technical decision in the entire build.

All concepts live in `concepts.json`.
The `concept_card.py` component renders any concept from that schema.
The `concepts.py` page dynamically routes to any concept by ID.

`concepts.json` is populated with these priority concepts:

**Architecture Concepts (7)**

Capture · Understanding · Knowledge Objects · Memory
Intelligence · Execution · Exposure · Evolution


**Primitive Concepts (10)**

Actor · Communication · Commitment · Action · Resource
Rule · Goal · State · Time · Relationship


**Memory Concepts (5)**

Factual Memory · Interaction Memory · Commitment Memory
Action Memory · Learning Memory


**Intelligence Concepts (10)**

Recommendation · Operational Risk · Opportunity Signal
Drift Signal · Knowledge Gap · Prediction · Policy Violation
Process Bottleneck · Agent Readiness · Brain Score


**Trust Concepts (6)**

Claim · Evidence · Challenge · Approval · Exception · Delegation


**Product Concepts (3)**

Ambient Delivery · Agent Access · Mission Control


**Ontology Concepts (4)**

Atomic Primitives · Core Objects · Organizational Structures
Composite Knowledge Objects


Total: ~45 concept cards, all rendered by the same component.

### Architecture Layer Pages

Eight pages, one per layer (plus Ontology):
- Each page uses the Concept Card template
- Each page has a dedicated visual
- Each page includes: one-sentence, why it exists, what it does, inputs, outputs, relationships

**Priority visuals to build for this phase:**

The Ten Primitives grid
The Four Ontology Layers diagram
The Five Memory Stores visual
The Intelligence Engine (memory in → 10 outputs out)
The Trust Object lifecycle diagram
The Three Exposure Modes visual
The Evolution Loop


### Scenario Engine (Two Priority Scenarios)

Two scenarios built using the `scenario_player.py` component:

**Scenario 1: The Customer Meeting**
(Defined in full in Master Plan v3 Section 4 — already the Reality Pipeline)
Extended version with more technical detail on each step.

**Scenario 2: The Missed Commitment**
A Q3 promise never fulfilled.
How the Brain detects it, generates Operational Risk,
creates a Recommendation, notifies the owner,
and closes the loop via Evolution.

Both scenarios stored in `scenarios.json`.
Scenario player is fully reusable — adding a new scenario
is a JSON edit, not a code change.

### Concept Comparisons (Five Priority Pairs)


Memory vs Knowledge Objects      ← most important
Decision vs Commitment           ← most confused
Drift Signal vs Policy Violation ← similar but different
Trust vs Confidence              ← often conflated
Factual Memory vs Interaction Memory ← common confusion


All stored in `comparisons.json`.
Rendered by `comparison_card.py`.

### Audience Views (Fully Implemented)

All four audience modes now fully switch language across:
- Every concept card's one-sentence description
- The "why it exists" framing
- The real example scenario context
- Navigation labels (optional)

Content per audience mode lives in `audiences.json`.

---

## What Does NOT Get Built in Phase 2


✗ Relationship graph (interactive D3/Plotly graph)
✗ Full concept search with multi-entity results
✗ All five scenarios (two is enough)
✗ All concept comparison pairs (five is enough)
✗ Progress / journey tracking gamification
✗ Animations beyond step-by-step scenario navigation


---

## Phase 2 Exit Criteria


✓ Every architecture layer has a dedicated concept page
  with a visual, plain-language explanation, and relationships.

✓ All ~45 concepts are accessible via the Concept Explorer.
  Every concept card follows the standard template.
  Zero concepts are hardcoded pages — all rendered from concepts.json.

✓ Both scenarios run start to finish
  with step navigation, related concepts highlighted per step,
  and technical detail expandable on every step.

✓ Five concept comparison pairs are live and correct.

✓ Audience switching changes language on concept cards.

✓ A new engineer given access to Phase 2
  can correctly describe every layer's inputs, outputs,
  and boundary with adjacent layers — without reading the docs.


---

# Phase 3
# Exploration + Polish
## "Anyone can navigate the entire architecture by concept, not by document."

**This is the complete experience.**
Build everything that makes the system feel alive and self-navigating.

---

## What Gets Built

### Relationship Explorer

Interactive concept graph.
Nodes are concepts. Edges are relationship types:
Creates · Feeds Into · Governed By · Depends On · Related To

Built with Plotly (network graph) or inline SVG.
Clicking a node opens the Concept card in a side panel.
Filtering by relationship type.
Filtering by architecture layer.

Data lives entirely in `relationships.json`.
No hardcoded graph logic.

### Full Concept Search

Searching any term returns:
- Matching concept cards
- Scenarios that involve this concept
- Comparison pairs that feature it
- Related concepts
- Source document references

Search index built at app load from `concepts.json` + `scenarios.json`.
Results grouped by type (Concept / Scenario / Comparison / Source).
Every result is a link into the Concept Explorer.

### Remaining Three Scenarios

**Scenario 3: The Policy That Wasn't Followed**
Team bypasses approval. Drift Signal → Policy Violation → Challenge → Exception.

**Scenario 4: The New Team Member**
New engineer asks "why did we choose this architecture?"
Interaction Memory surfaces the original decision context.

**Scenario 5: The AI Agent Building a Proposal**
Claude asks the Brain via MCP.
Brain provides governed, provenance-tagged context.
Agent builds an informed proposal instead of a generic one.

### Remaining Concept Comparisons

Complete all comparison pairs from Master Plan v3 Section 13:

Knowledge vs Memory
Recommendation vs Prediction
Challenge vs Conflict
Authority vs Ownership
Learning vs Memory
Policy vs SOP vs Workflow


### Visual Library

A browsable collection of all 17 priority visuals from Master Plan v3.
Each visual has a title, one-sentence description, and links to related concepts.
Built entirely from the `flow_diagram.py` component.

### Polish Pass


Transition smoothness between sections
Loading states on component render
Mobile responsiveness (readable on tablet minimum)
Audience mode persistence across sessions (localStorage or URL param)
Progress indicator ("You've explored 8 of 45 concepts")
Keyboard navigation between scenario steps
Print/share view for concept cards


---

## Phase 3 Exit Criteria


✓ Relationship Explorer renders all concepts as nodes
  with correct edges and clickable navigation to concept cards.

✓ Search returns relevant results for every concept name,
  every memory type, every intelligence output,
  and every atomic primitive.

✓ All five scenarios run correctly end to end.

✓ All concept comparison pairs are live.

✓ Visual Library shows all 17 priority visuals.

✓ The full experience (all three phases) works on a 1280px screen
  without horizontal scrolling or broken layouts.

✓ The system passes the Success Definition from Master Plan v3:
  A non-technical person can explain Company Brain after 10 minutes.
  An engineer understands all layer boundaries without reading docs.
  Any concept can be found, understood, and related to the whole.


---

# Anti-Patterns (Enforced Throughout All Phases)

Treat these as rules, not suggestions.


✗ Content hardcoded into any page or component file
✗ Technical terminology introduced before plain-language explanation
✗ A concept page with no "why it exists" section
✗ A concept with no related concepts linked
✗ Navigation that says "Section 1", "Section 2"
✗ The document layer as a primary navigation item
✗ Any page that feels like a documentation section
✗ A visual with no plain-language caption
✗ Audience switching that changes nothing visible
✗ A scenario step with no concept links


---

# Content-First Rule

For every page built, content is written before the UI is finalized.

Order of operations:

1. Write the content for a section in plain text
2. Validate it against the Master Plan v3 principles
3. Structure it into the JSON schema
4. Build the component to render that schema
5. Wire the component into the page


Never do step 4 before step 3.
Never do step 5 before step 4.

This prevents building UI that doesn't fit the content
and prevents writing content that doesn't fit the system.

---

# Summary

| Phase | Name | Delivers | Exit Criteria |
|---|---|---|---|
| **1** | Platform + Core Story | Investor/advisor demo, full pipeline walkthrough, document reference | Non-technical person understands CB in 12 min |
| **2** | Concept Engine + Depth | All 45 concepts, all 7 layers, 2 scenarios, 5 comparisons | New engineer understands all layer boundaries without docs |
| **3** | Exploration + Polish | Relationship graph, full search, 5 scenarios, visual library, polish | Complete experience, every concept navigable by concept not document |

Three phases. Three clear deliverables. Three human-readable exit criteria.

---

# Success Definition

Unchanged from Master Plan v3.

The system succeeds when people stop saying
> "I should read those documents"

and start saying
> "I already understand it."
