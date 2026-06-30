# Company Brain Experience

An interactive learning system that makes the Company Brain architecture understood by anyone — executive, engineer, investor, or new team member.

## What This Is

**What it is:** The **Company Brain** is an organizational memory and intelligence system. It captures everything that happens inside an organization — meetings, decisions, commitments, conversations, actions — and turns that fragmented activity into something structured: it understands what happened, remembers it by type, reasons over what it knows, and delivers the right knowledge to the right person at the right moment.

Most organizations run on memory that lives in people's heads and disappears the moment those people leave a meeting, a project, or the company. Company Brain exists to make that memory permanent, governed, and usable by both humans and AI.

**Why this app exists:** The architecture itself is described across six canonical documents. This application makes reading those documents unnecessary as a starting point.

Instead of working through documentation, you move through an interactive experience that builds the mental model progressively — starting from the problem the Brain solves, ending with a complete understanding of how every layer, memory type, and intelligence output fits together. The documents remain available as a reference for anyone who wants the precise source language, but they are never where the experience expects you to begin.

## View the App

The app is live. No setup required.

https://zm-company-brain-experience.streamlit.app/

## Who This Is For

| Audience | What they get from this |
|---|---|
| Executive / Investor / Advisor | Business value, strategic differentiation, what makes this architecturally different from existing AI memory products |
| Product Manager / Designer | What the system does, how it affects users, the three ways people access it |
| Engineer / Technical Builder | Full architecture detail, layer boundaries, inputs/outputs, lifecycle, canonical source references |
| New Team Member | Progressive mental model built from zero — no prior knowledge assumed |
| General Explorer | Open navigation across all concepts, scenarios, comparisons, and the relationship graph |

## What's Inside

**The Guided Learning Arc**
Problem → What Is It → Big Picture → How It Works takes any audience from zero to a working mental model in under twelve minutes. It's the default path through the experience, but never a gate — every section is reachable directly, and the audience selected at the start adapts language throughout without forcing anyone through a fixed sequence.

**The Concept Engine**
Covers all 45 concepts that make up the architecture, from the seven pipeline layers down to the ten atomic primitives, five memory types, ten intelligence outputs, and six trust objects. Every concept gets a plain-language explanation that adapts to the chosen audience, a concrete real-world example, and a map of how it relates to everything else in the system.

**The Reality Pipeline**
An eight-step animated walkthrough of a single sales call, traced from the moment it happens through capture, understanding, memory formation, intelligence, and delivery — showing exactly how one ordinary event becomes a risk alert that reaches an account manager's inbox automatically.

**Five Scenarios**
Real organizational situations — a missed commitment, a policy bypassed under deadline pressure, a new hire asking why an old decision was made, an AI agent drafting a proposal — each traced through the full architecture, layer by layer.

**The Relationship Explorer**
A navigable graph showing how every one of the 45 concepts connects to every other, filterable by architecture layer and by relationship type, with every node a doorway into its own concept card.

**Eleven Concept Comparisons**
Resolve the pairs people confuse most often — Memory versus Knowledge Objects, Drift Signal versus Policy Violation, Trust versus Confidence, and others — each as a side-by-side explainer naming the specific difference, not a restatement of two definitions.

**The Document Layer**
Keeps the six canonical architecture documents available as references, each with a summary and the concepts it defines, but deliberately never positioned as where the experience begins.

## The Architecture It Explains

**The seven-layer pipeline:** **Capture** and **Understanding** construct a structured model of organizational reality. **Knowledge Objects** give that model a canonical representation. **Memory** preserves it across five purpose-built stores. **Intelligence** reasons over it to generate ten types of output. **Execution** turns that reasoning into action. **Exposure** delivers it to the right human or AI actor. **Evolution** feeds outcomes back in as organizational learning.

**Trust & Governance** surrounds all seven layers rather than sitting inside the sequence — it governs who can write what, how disputes get resolved, and when autonomy must defer to a human.

**Three exposure modes** determine how people and AI systems actually reach the Brain: **Ambient Delivery** surfaces context inside the tools people already use, **Agent Access** exposes the Brain as an MCP provider for AI tools, and **Mission Control** offers dedicated surfaces for investigation and governance.

```
Organizational Reality
        ↓
┌─────────────── Trust & Governance ───────────────┐
│                                                    │
│  Capture → Understanding → Knowledge Objects       │
│                    ↓                               │
│                 Memory                             │
│                    ↓                               │
│              Intelligence                          │
│                    ↓                               │
│     Execution → Exposure → Evolution               │
│                                                    │
└────────────────────────────────────────────────────┘
        ↓
  Ambient Delivery · Agent Access · Mission Control
```

## Project Structure

```
company-brain-experience/
├── app.py            # entry point — session init, theme, routing only
├── core/             # theme, session state, routing, audience logic
├── components/       # reusable rendering components, no content
├── views/            # page assembly only — imports components, passes content
├── content/          # every piece of human-readable text, as JSON
└── docs/             # the six canonical architecture documents, read-only
```

## Content Architecture

**How content and code are separated:** All human-readable content in this application lives in JSON files inside `content/`. Components receive content as parameters and render it; pages do nothing but load the right JSON and call the right components. No narrative content exists in any Python file.

**Why it's structured this way:** Content like this changes constantly during a project like this one — concept explanations get sharper, examples get more specific, audience variants get rewritten — and none of that should ever require touching component or page code. Updating what the application says is a content change, never a code change.

## Source Documents

| Document | Version | What It Defines | View |
|---|---|---|---|
| Architecture & Vision | v2.2 | Seven pipeline layers, ten atomic primitives, Knowledge Object layer | [View on Drive](https://drive.google.com/drive/folders/1-pPJfR8DasFVG5U8jzRwR28Pz88bN6NX?usp=drive_link) · [View in App](https://zm-company-brain-experience.streamlit.app/) |
| Ontology | v1.2 | 60-object vocabulary, four ontology layers, 19 relationship types | [View on Drive](https://drive.google.com/drive/folders/1sURWv9cWpSU0KWb1yhrYngtsug8AZmiA?usp=sharing) · [View in App](https://zm-company-brain-experience.streamlit.app/) |
| Memory Model | v1.2 | Five memory stores, write governance, provenance, Commitment lifecycle | [View on Drive](https://drive.google.com/drive/folders/1fAE3XSBCGSiB6X2rqd-50ZsFA7b6OlUX?usp=sharing) · [View in App](https://zm-company-brain-experience.streamlit.app/) |
| Intelligence Architecture | v1.0 | Reasoning pipeline, ten intelligence output types, confidence model | [View on Drive](https://drive.google.com/drive/folders/1bLPz-svKoxX8Y73rSMLuvgqrJpdly5yi?usp=sharing) · [View in App](https://zm-company-brain-experience.streamlit.app/) |
| Trust & Governance | v1.0 | Authority model, six Trust Objects, delegation and challenge principles | [View on Drive](https://drive.google.com/drive/folders/1X1phtyCoL0v9bsCY4GNrqM6vNkIM33W2?usp=sharing) · [View in App](https://zm-company-brain-experience.streamlit.app/) |
| Product Architecture | v2.1 | Three exposure modes, eight Mission Control surfaces, MCP provider | [View on Drive](https://drive.google.com/drive/folders/1ITAiLaPX9r_KZJmxHNdGB_LZ0MdxHPsq?usp=sharing) · [View in App](https://zm-company-brain-experience.streamlit.app/) |

"View on Drive" links to the canonical source folder. "View in App" opens the live app's Documents page, where the full text of every document is already available — there is no per-document deep link, so all six point to the same Documents section.

## Design Principles

**Problem First, Architecture Second**
Never introduce architecture before the problem it solves.

**One Sentence First**
Every concept must be explainable in one sentence before any further explanation is offered.

**"So What?" Before "What"**
Before explaining what something is, answer why anyone should care.

**Mental Models Before Terminology**
Teach the concept before introducing the name.

**Relationships Over Definitions**
People understand systems through connections, not isolated definitions.

**Progressive Disclosure**
Four depths available for every concept — one sentence, one paragraph, full explainer, canonical document reference — and the user always chooses the depth, never the system.

**Audience-Adaptive Experience**
The same architecture means different things to different people. The system adapts to who is asking, not to what is documented.

**Visual First**
Architecture is spatial. Spatial things should be explored spatially. Every major concept has a visual, and everything is clickable.

**The Brain Demonstrates Itself**
This system behaves the way the Brain behaves: surfacing the right explanation at the right moment, connecting concepts relationally, answering "why" before "what."

---

Built for ZeroManual · Company Brain Architecture v2.2
