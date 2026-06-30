# COMPANY BRAIN

# Intelligence Architecture

## Version 1.0

### Status
Canonical Conceptual Model — Frozen

### Supersedes
Planning documents `Intelligence_Architecture_v1__reasoning_1`, `Intelligence_Architecture_v1__planning_1`, draft `Intelligence_Architecture_v1_draft`

### Depends On
- Architecture & Vision v2.2
- Ontology v1.2
- Memory Model v1.2
- Product Architecture v2.1

### Scope
Intelligence layer only. Does not define reasoning engines, models, prompts, retrieval, or infrastructure — those belong to Technical Architecture.

---

## Document Control

**Closes (long-standing open questions, tracked since Foundational Reasoning V4)**
- How the Brain reasons — generates recommendations, detects risk/opportunity/drift (Parts 6–10)
- How Consultant thinks, per mode (Part 11)
- How confidence is calculated conceptually (Part 13)
- How the Brain's reasoning improves from feedback without self-corrupting on noisy signals (Part 14)

**Fixed During Review Pass (draft → v1.0)**
- "Risk Signal" / "Operational Insight" did not match Ontology v1.2 Section 7's canonical Derived Intelligence Objects list. Renamed to **Operational Risk**; "Operational Insight" replaced with **Brain Score**. (Part 8, 15, 17, 18)
- Five of ten approved output types had no object definition or lifecycle. Added. (Part 15)
- Reasoning Pipeline branching was defined for Inquiry and Simulation modes only. Added Planning and Review mode branching. (Part 6)
- Confidence Model had no level→behavior mapping and no acknowledgment that output types behave differently at equal confidence. Added mapping and asymmetric handling rule. (Part 13)
- Adaptive Intelligence's "repeated validated feedback" was undefined, and the write-back path to memory was unstated. Added conceptual repetition rule and explicit write-path through Memory Model's Write Governance. (Part 14)
- Agent Readiness was named with no definition. Added. (Part 12)
- Drift Signal's evidence threshold was not connected to the Confidence Model. Cross-referenced. (Part 10)

**Fixed During Freeze Pass (this update)**
- Freshness & Decay (Part 15.1) did not state whether decay applies to objects already in terminal lifecycle states. Added explicit rule: decay applies only to objects in active/open states; terminal-state objects retain historical confidence, mirroring Memory Model v1.2's Archive Path.
- Recommendations sitting in the Presented state (awaiting human response) were not addressed by decay — a stale, unanswered recommendation could otherwise be presented indefinitely at its original confidence. Added.
- Part 19 ("Future Boundaries") deferred all re-evaluation trigger mechanics to Technical Architecture. Narrowed now that Review Trigger (Part 15) defines the mechanism conceptually — only exact timing/frequency of Time Window triggers remains deferred.

**Still Open (deferred on purpose)**
- Exact confidence scoring mechanics (weights, formula) — Technical Architecture
- Exact timing/frequency of Time Window review triggers — Technical Architecture
- Exact repetition count/window for Adaptive Learning validation — Technical Architecture
- Single home for trust/governance concerns spanning this and other documents — Trust & Governance Architecture v1 (not yet started)

This document is now frozen. No further Intelligence Architecture revisions are planned before Trust & Governance Architecture v1 begins. Any remaining open items are implementation questions for Technical Architecture or Trust & Governance Architecture.

---

# Purpose

Define how the Company Brain transforms memory into intelligence.

The Memory Model answers:
> How reality becomes memory.

The Intelligence Architecture answers:
> How memory becomes understanding, recommendations, predictions, risk awareness, opportunity awareness, and execution guidance.

---

# Core Question

Every previous architecture answers:

Reality → Knowledge Objects → Memory

This document answers:

Memory → Intelligence

---

# Scope Commitments

This document explicitly defines:
- Context Assembly
- Reasoning
- Recommendation Generation
- Risk Detection
- Opportunity Detection
- Drift Detection
- Consultant Reasoning (all four modes)
- Agent Intelligence Consumption
- Confidence Assessment
- Adaptive Intelligence
- Intelligence Object Lifecycle (all approved output types)
- Intelligence Object Ownership & Review
- Intelligence Object Freshness & Decay
- Intelligence Failure Handling

---

# Out Of Scope

Do NOT define:
- LLMs
- RAG
- Embeddings
- Vector Databases
- Prompt Engineering
- Fine-Tuning
- Agent Runtime
- Infrastructure

These belong to Technical Architecture.

---

# Part 1 — What Is Intelligence?

**Intelligence is the capability to transform memory into understanding and action.**

Memory preserves reality. Intelligence interprets reality.

---

# Part 2 — Relationship To Company Brain

Reality → Capture → Understanding → Knowledge Objects → Memory → **Intelligence** → Execution → Exposure → Evolution

---

# Part 3 — Intelligence Philosophy

### Intelligence Requires Memory
No intelligence without memory.

### Intelligence Is Contextual
Meaning depends on situation.

### Intelligence Is Probabilistic
Outputs represent confidence, not certainty.

### Intelligence Must Be Explainable
Every conclusion requires evidence.

### Intelligence Must Improve Through Feedback
Learning influences future reasoning.

### Intelligence Never Becomes Truth
Memory contains truth claims. Intelligence contains interpretations.

---

# Part 4 — Intelligence Inputs

Consumes:
- Factual Memory
- Interaction Memory
- Commitment Memory
- Action Memory
- Learning Memory

Additional Inputs:
- Current Actor
- Current Goal
- Current Query
- Current Constraints
- Current Environment

---

# Part 5 — Context Assembly

Purpose: transform distributed memory into a usable reasoning context.

## Context Assembly Inputs

### Relevance
How closely memory relates to the current task.

### Recency
How recently the memory changed.

### Goal Linkage
Relationship to active goals.

### Actor Proximity
Relationship to the actor involved.

### Commitment Linkage
Relationship to active commitments.

### Explicit References
Direct mentions or requests.

## Context Package

Output: a bounded set of memories assembled for reasoning.

Examples: Meeting Context · Project Context · Customer Context · Incident Context · Executive Context

---

# Part 6 — Reasoning Architecture

Purpose: transform Context into Intelligence.

## Reasoning Pipeline (Full / Default)

Context → Situation Understanding → Goal Evaluation → Constraint Evaluation → Commitment Evaluation → Risk Evaluation → Opportunity Evaluation → Recommendation Generation

## Pipeline Behavior By Consultant Mode

### Inquiry Mode
Situation → Context → Explanation
No Recommendation Generation required.

### Planning Mode
Full pipeline, sequential, no stages skipped.
Terminates at Recommendation Generation.

### Review Mode
Situation → Goal Evaluation (compare actual vs. intended) → Commitment Evaluation → Risk Evaluation → Progress & Risk Report
Opportunity Evaluation optional. Recommendation Generation only triggered if Risk Evaluation surfaces something actionable.

### Simulation Mode
Full pipeline, plus: Scenario Generation → Outcome Comparison
Recommendation Generation becomes "Recommended Scenario" rather than a single action.

## Failure Handling

If a stage lacks sufficient evidence:
- Mark uncertainty
- Lower confidence
- Request additional information
- Escalate to human if necessary

Reasoning never fabricates certainty.

---

# Part 7 — Recommendation Intelligence

Purpose: generate actionable guidance.

Inputs: Context · Goals · Rules · Commitments · Learning

Outputs: Recommendation · Reasoning · Confidence · Sources

Every recommendation must answer: *why this recommendation?*

---

# Part 8 — Risk Intelligence

Definition: a possible future condition that threatens goals, commitments, resources, or organizational health.

Sources: Open Commitments · Historical Failures · Policy Violations · Resource Constraints · Drift Signals

Output: **Operational Risk** *(named to match Ontology v1.2 Section 7 exactly — not "Risk Signal")*

---

# Part 9 — Opportunity Intelligence

Definition: a possible future condition that increases value, efficiency, alignment, or goal achievement.

Sources: Success Patterns · Customer Signals · Resource Availability · Relationship Signals · Learning Memory

Output: Opportunity Signal

*Per Ontology v1.2: Opportunity Signal is the pattern-detected hint. It becomes the Layer-4 ontology object Opportunity only once a human or agent commits resources to pursuing it.*

---

# Part 10 — Drift Intelligence

Purpose: detect divergence between intended reality and observed reality.

Inputs: Policy → SOP → Workflow

## Stages

### Drift Candidate
Single divergence observed.

### Drift Pattern
Repeated divergence detected.

### Drift Signal
Evidence threshold exceeded — requires confidence ≥ Medium per the Confidence Model (Part 13). Below Medium, stays a Drift Pattern under observation.

### Drift Severity
Low · Medium · High · Critical

Output: Drift Signal

---

# Part 11 — Consultant Intelligence

The Consultant is an intelligence consumer. See Part 6 for per-mode pipeline behavior.

## Inquiry Mode — "What do we know?" → Evidence-based explanation
## Planning Mode — "What should we do?" → Recommendations
## Review Mode — "Are we on track?" → Progress and risk analysis
## Simulation Mode — "What happens if?" → Scenario comparisons

---

# Part 12 — Agent Intelligence

Purpose: convert intelligence into execution plans.

Capabilities: Goal Interpretation · Task Decomposition · Context Consumption · Action Planning · Escalation · Human Handoff

## Agent Readiness

Assessment of whether an Agent has sufficient context, permissions, and confidence to execute a given action autonomously, versus requiring human handoff.

Driven by the same Confidence Model as all other Intelligence Objects (Part 13) — an Agent below the confidence threshold for a given action escalates rather than acts.

---

# Part 13 — Confidence Model

Purpose: assess certainty. Not mathematical — conceptual.

## Confidence Inputs

### Evidence Strength
Supporting memory volume and quality.

### Source Quality
Authority and trustworthiness.

### Agreement
Consistency across memories.

### Freshness
Recency of evidence. See Part 15.1 — freshness is not static; it decays as supporting evidence ages.

### Completeness
Coverage of required information.

## Confidence Levels

Very Low · Low · Medium · High · Very High

## Confidence → Behavior Mapping

| Level | Default Behavior |
|---|---|
| Very High / High | Present output normally |
| Medium | Present output, flag confidence level explicitly |
| Low | Request clarification or additional information before presenting |
| Very Low | Withhold output, escalate to human |

## Asymmetric Handling By Output Type

The mapping above is the default for Recommendation and Agent action. It is deliberately **not** applied uniformly:

- **Operational Risk and Drift Signal at Low/Very Low confidence are not withheld** — they are tracked at reduced confidence and surfaced with a clear "unconfirmed" flag. Under-reporting a possible risk is more costly than a false positive.
- **Recommendation and Agent execution at Low/Very Low confidence are withheld** by default — acting on a low-confidence suggestion is more costly than delaying it. This includes confidence that decays below threshold while a Recommendation sits unanswered in Presented state (Part 15.1) — it is re-flagged as stale rather than left presented at its original confidence.

---

# Part 14 — Adaptive Intelligence

Purpose: improve reasoning over time.

## Learning Inputs

Approved Recommendations · Rejected Recommendations · Modified Recommendations · Ignored Recommendations · Agent Successes · Agent Failures

## Learning Rule

Observation ≠ Learning
Single Feedback ≠ Learning
Repeated Validated Feedback = Learning

**Repeated**, conceptually: the same pattern recurring across multiple independent instances (different commitments, different actors, different time windows) — not the same instance re-observed multiple times. Exact count/window is a Technical Architecture decision.

**Validated**, conceptually: feedback that survives a second independent occurrence pointing the same direction, not a single human override.

## Adaptive Boundary

The Brain may improve reasoning.
The Brain may not silently rewrite organizational memory.

**Write Path:** validated learning does not write directly to memory. It is proposed as a Learning Memory candidate and passes through Memory Model v1.2's standard Write Governance (Section 9) — AI-proposed writes require automatic, delegated, or human approval depending on type. Intelligence proposes; Memory governs the write. This is the same boundary Memory Model v1.2 already establishes for all AI-originated memory — Intelligence Architecture does not introduce a second path around it.

---

# Part 15 — Intelligence Object Model

Every intelligence output becomes an Intelligence Object.

## Types

### Recommendation
Represents a suggested action.
Lifecycle: Draft → Presented → Accepted / Rejected / Modified
Owner: typically the actor or team the recommendation is directed at.

### Operational Risk
Represents a detected future threat.
Lifecycle: Detected → Validated → Tracked → Resolved
Owner example: Migration Team Lead.

### Opportunity Signal
Represents potential future value.
Lifecycle: Detected → Validated → Pursued / Dismissed
Owner: typically the team or role positioned to act on it (e.g. Account Owner, Growth Team).

### Drift Signal
Represents divergence between intended and observed reality.
Lifecycle: Detected → Confirmed → Investigated → Resolved
Owner example: Operations Team.

### Knowledge Gap
Represents missing organizational understanding.
Lifecycle: Detected → Investigated → Resolved
Owner example: Domain Expert Group.

### Prediction
Represents a forecast of a future state.
Lifecycle: Generated → Tracked → Confirmed / Falsified
Owner: typically the goal or initiative owner the prediction concerns.

### Policy Violation
Represents an observed breach of a defined Policy or Rule.
Lifecycle: Detected → Validated → Escalated → Resolved
Owner: typically the Policy owner or relevant Role.

### Process Bottleneck
Represents a recurring constraint slowing execution.
Lifecycle: Detected → Validated → Addressed / Accepted
Review Trigger example: Workflow Execution Change.

### Agent Readiness
Represents an assessment of an Agent's fitness to act autonomously on a given action class.
Lifecycle: Assessed → Certified / Not Ready → Re-Assessed (triggered by new evidence, not time alone)
Owner: typically the Agent's supervising Team or Role.

### Brain Score
An aggregate health metric, not a discrete event-driven object — computed by rolling up confidence, drift severity, and unresolved risk across a scope (team, project, organization).
Lifecycle: Calculated → Published → Recalculated (on material change to inputs)
Review Trigger example: Material Change In Inputs.

## Shared Properties

Every Intelligence Object contains:

```text
Sources
Confidence
Timestamp
Related Actors
Related Goals
Related Commitments
Reasoning Trace
Status
Owner
Review Trigger
```

### Owner

The actor accountable for responding to the Intelligence Object. Purpose: ensure every actionable intelligence output has a responsible party.

Owner may be: Person · Team · Role · Agent — depending on object type.

### Review Trigger

The condition that requires re-evaluation of an Intelligence Object. Purpose: prevent intelligence objects from remaining indefinitely active without reassessment.

Review triggers may include: New Evidence · Goal Change · Commitment Change · Policy Change · Time Window · Manual Review Request.

---

# Part 15.1 — Intelligence Object Freshness & Decay

Purpose: define how Intelligence Objects evolve when supporting evidence becomes less relevant over time.

This mirrors Memory Model v1.2's distinction:

```text
Decay ≠ Archive
```

## Intelligence Freshness

Intelligence objects are generated from evidence available at a specific moment. As organizational reality changes:
- evidence may become stale
- assumptions may become invalid
- confidence may decrease

even when the intelligence object itself remains unresolved.

## Confidence Decay

Confidence may decrease when:
- supporting evidence ages
- contradictory evidence appears
- goals change
- commitments change
- organizational context changes

Example:

```text
Operational Risk
January: High Confidence
March:   Medium Confidence
June:    Low Confidence

Status: Still Open — the risk has not been resolved, only confidence has changed.
```

## Decay Scope — Active States Only

**Decay applies only to Intelligence Objects in active/open lifecycle states** (e.g. Detected, Validated, Tracked, Presented, Investigated, Escalated, Assessed). Once an object reaches a terminal state — Resolved, Accepted / Rejected / Modified, Pursued / Dismissed, Confirmed / Falsified, Addressed / Accepted, Certified — it stops decaying and retains its confidence as a historical record, mirroring Memory Model v1.2's Archive Path: archived records remain historically true and are not silently altered.

This includes Recommendations sitting unanswered in Presented state: an unresolved Recommendation is an active state and is subject to decay. If confidence decays past the Low/Very Low threshold (Part 13) while still Presented, it is re-flagged as stale rather than left presented at its original confidence — it does not, however, become Withdrawn automatically; that remains a status change subject to Review Trigger, not decay alone (see below).

## Decay Does Not Equal Resolution

```text
Confidence Decay ≠ Resolution
Resolution ≠ Confidence Decay
```

An unresolved intelligence object may become less certain. A resolved intelligence object retains its historical confidence. These are separate concepts.

## Intelligence Freshness Principle

The Company Brain continuously re-evaluates intelligence as reality changes. Intelligence is not permanent — it remains valid only while supported by evidence.

## Relationship To Confidence Model

Confidence decay influences the Confidence Model (Part 13). As confidence decreases:
- recommendations may require additional review, or be re-flagged as stale if unanswered
- agents may escalate rather than act
- drift signals may fall below confirmation thresholds
- operational risks may remain tracked but be marked as less certain (per the asymmetric handling rule, Part 13 — they are not withdrawn)

## Relationship To Review Triggers

Confidence decay alone does not automatically close or change the status of an Intelligence Object. Review Triggers determine when re-evaluation occurs.

**Freshness affects confidence. Review affects status. These are separate mechanisms.**

---

# Part 16 — Worked Example

Commitment: "Launch migration by June 30"
↓
Commitment Memory detects: overdue dependency, missing owner
↓
Risk Intelligence: Operational Risk generated (confidence: High, Owner: Migration Team Lead, Review Trigger: New Commitment Status Change)
↓
Recommendation Intelligence: "Assign ownership and escalate dependency" (confidence: High)
↓
Consultant (Planning Mode): surfaces recommendation
↓
Manager: accepts recommendation
↓
Execution occurs
↓
Feedback Signal generated → Recommendation Object: Accepted (terminal state — confidence frozen, no further decay per Part 15.1)
↓
This is one instance, not yet a learning pattern (Learning Rule, Part 14) — Adaptive Intelligence logs the signal but does not yet alter future reasoning. A second, independently-occurring instance of the same accept pattern (different commitment, different team) would qualify.

---

# Part 17 — Intelligence Outputs

Cross-document alignment with Ontology v1.2, Section 7 (Derived Intelligence Objects).

**Approved Intelligence Outputs** *(matching Ontology v1.2 exactly — ten of ten)*:

- Recommendation
- Operational Risk
- Opportunity Signal
- Drift Signal
- Knowledge Gap
- Prediction
- Agent Readiness
- Brain Score
- Policy Violation
- Process Bottleneck

No new intelligence types may be introduced without updating Ontology.

---

# Part 18 — Relationship To Product Architecture

| Intelligence Object | Product Surface |
|---|---|
| Recommendation | Consultant |
| Operational Risk | Personal Reality |
| Opportunity Signal | Operational Intelligence |
| Drift Signal | Drift Experience |
| Knowledge Gap | Consultant |
| Prediction | Consultant (Simulation Mode) |
| Policy Violation | Drift Experience |
| Process Bottleneck | Operational Intelligence |
| Agent Readiness | Agent System |
| Brain Score | Ambient Delivery (Executive view) |
| Context Package | Ambient Delivery |

---

# Part 19 — Future Boundaries

Deferred to Technical Architecture:
- Reasoning Engines
- Model Selection
- Prompting
- Agent Runtime
- Retrieval Systems
- Vector Infrastructure
- Graph Infrastructure
- Execution Infrastructure
- Confidence scoring formula
- Exact timing/frequency of Time Window review triggers *(narrowed — the trigger mechanism itself is now defined in Part 15)*
- Adaptive Learning repetition threshold

Deferred to Trust & Governance Architecture v1 (not yet started):
- Single owner for Intelligence-layer trust/provenance surfacing, consistent with the same scattering Memory Model and Product Architecture already flagged

---

# Final Deliverable Goal

After reading this document, a team member should be able to answer:
- How does the Brain think?
- How does it generate recommendations?
- How does it detect risks?
- How does it detect opportunities?
- How does it detect drift?
- How does it improve over time?
- How do agents use intelligence?
- How does memory become action?
- Who is accountable for each piece of intelligence, and when does it get re-checked?
- Does an unresolved intelligence object stay trustworthy as time passes?

---

# One-Sentence Summary

The Intelligence Architecture defines how the Company Brain transforms memory into contextual understanding, recommendations, risk awareness, opportunity awareness, and drift detection — through a confidence model that behaves asymmetrically by output type, a freshness mechanism that decays confidence without silently resolving or erasing intelligence, explicit ownership and review triggers on every output, and a learning loop that writes back to memory only through Memory Model v1.2's existing governance — while preserving explainability, confidence, and trust.

---

# Freeze Statement

With Ownership, Review Triggers, Intelligence Freshness, and Confidence Decay now incorporated and reconciled against the rest of the document (decay scoped to active states only, review trigger scope narrowed in Part 19), Intelligence Architecture v1.0 is frozen.

No further Intelligence Architecture revisions are planned before:

```text
Trust & Governance Architecture v1
```

Remaining open items are implementation questions for Technical Architecture or Trust & Governance Architecture (see Document Control, "Still Open").