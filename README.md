# Company Brain Experience

An interactive learning system that makes the Company Brain architecture understood by anyone — executive, engineer, investor, or new team member.

## What This Is

The Company Brain is an organizational memory and intelligence system. It captures everything that happens inside an organization — meetings, decisions, commitments, conversations, actions — and turns that fragmented activity into something structured: it understands what happened, remembers it by type, reasons over what it knows, and delivers the right knowledge to the right person at the right moment. Most organizations run on memory that lives in people's heads and disappears the moment those people leave a meeting, a project, or the company. Company Brain exists to make that memory permanent, governed, and usable by both humans and AI.

The architecture itself is described across six canonical documents. This application makes reading those documents unnecessary as a starting point. Instead of working through documentation, you move through an interactive experience that builds the mental model progressively — starting from the problem the Brain solves, ending with a complete understanding of how every layer, memory type, and intelligence output fits together. The documents remain available as a reference for anyone who wants the precise source language, but they are never where the experience expects you to begin.

## Who This Is For

| Audience | What they get from this |
|---|---|
| Executive / Investor / Advisor | Business value, strategic differentiation, what makes this architecturally different from existing AI memory products |
| Product Manager / Designer | What the system does, how it affects users, the three ways people access it |
| Engineer / Technical Builder | Full architecture detail, layer boundaries, inputs/outputs, lifecycle, canonical source references |
| New Team Member | Progressive mental model built from zero — no prior knowledge assumed |
| General Explorer | Open navigation across all concepts, scenarios, comparisons, and the relationship graph |

## What's Inside

The guided learning arc — Problem, What Is It, Big Picture, How It Works — takes any audience from zero to a working mental model in under twelve minutes. It is the default path through the experience, but never a gate: every section is reachable directly, and the audience selected at the start adapts language throughout without forcing anyone through a fixed sequence.

The Concept Engine covers all 45 concepts that make up the architecture, from the seven pipeline layers down to the ten atomic primitives, five memory types, ten intelligence outputs, and six trust objects. Every concept gets a plain-language explanation that adapts to the chosen audience, a concrete real-world example, and a map of how it relates to everything else in the system.

The Reality Pipeline is an eight-step animated walkthrough of a single sales call, traced from the moment it happens through capture, understanding, memory formation, intelligence, and delivery — showing exactly how one ordinary event becomes a risk alert that reaches an account manager's inbox automatically.

Five Scenarios take real organizational situations — a missed commitment, a policy bypassed under deadline pressure, a new hire asking why an old decision was made, an AI agent drafting a proposal — and trace each one through the full architecture, layer by layer.

The Relationship Explorer is a navigable graph showing how every one of the 45 concepts connects to every other, filterable by architecture layer and by relationship type, with every node a doorway into its own concept card.

Eleven Concept Comparisons resolve the pairs people confuse most often — Memory versus Knowledge Objects, Drift Signal versus Policy Violation, Trust versus Confidence, and others — each as a side-by-side explainer naming the specific difference, not a restatement of two definitions.

The Document Layer keeps the six canonical architecture documents available as references, each with a summary and the concepts it defines, but deliberately never positioned as where the experience begins.

## The Architecture It Explains

Company Brain operates as seven pipeline layers: Capture and Understanding construct a structured model of organizational reality, Knowledge Objects give that model a canonical representation, Memory preserves it across five purpose-built stores, Intelligence reasons over it to generate ten types of output, Execution turns that reasoning into action, Exposure delivers it to the right human or AI actor, and Evolution feeds outcomes back in as organizational learning. A Trust system surrounds all seven layers rather than sitting inside the sequence — it governs who can write what, how disputes get resolved, and when autonomy must defer to a human. Three exposure modes determine how people and AI systems actually reach the Brain: Ambient Delivery surfaces context inside the tools people already use, Agent Access exposes the Brain as an MCP provider for AI tools, and Mission Control offers dedicated surfaces for investigation and governance.

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

## Running Locally

**Prerequisites**

- Python 3.10 or higher
- Git

**Steps**

```bash
git clone [repo-url]
cd company-brain-experience
python -m venv .c_brain_experience

# Windows
.c_brain_experience\Scripts\activate

# macOS / Linux
source .c_brain_experience/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Project Structure

```
company-brain-experience/
├── app.py            # entry point — session init, theme, routing only
├── core/             # theme, session state, routing, audience logic
├── components/       # reusable rendering components, no content
├── pages/            # page assembly only — imports components, passes content
├── content/          # every piece of human-readable text, as JSON
└── docs/             # the six canonical architecture documents, read-only
```

## Content Architecture

All human-readable content in this application lives in JSON files inside `content/`. Components receive content as parameters and render it; pages do nothing but load the right JSON and call the right components. No narrative content exists in any Python file. This separation exists because content like this changes constantly during a project like this one — concept explanations get sharper, examples get more specific, audience variants get rewritten — and none of that should ever require touching component or page code. Updating what the application says is a content change, never a code change.

## Source Documents

| Document | Version | What It Defines |
|---|---|---|
| Architecture & Vision | v2.2 | Seven pipeline layers, ten atomic primitives, Knowledge Object layer |
| Ontology | v1.2 | 60-object vocabulary, four ontology layers, 19 relationship types |
| Memory Model | v1.2 | Five memory stores, write governance, provenance, Commitment lifecycle |
| Intelligence Architecture | v1.0 | Reasoning pipeline, ten intelligence output types, confidence model |
| Trust & Governance | v1.0 | Authority model, six Trust Objects, delegation and challenge principles |
| Product Architecture | v2.1 | Three exposure modes, eight Mission Control surfaces, MCP provider |

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
