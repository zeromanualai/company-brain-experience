Company Brain — Memory Model	v1.2

**COMPANY BRAIN**

Memory Model

Version 1.2

Canonical Conceptual Model

ZeroManual — Internal

June 2026

## Document Control

| **Field** | **Value** |
| --- | --- |
| Version | 1.2 |
| Status | Canonical Conceptual Model |
| Supersedes | Version 1.1 |
| Scope | Memory Model only. Does not define databases, storage engines, graphs, vectors, schemas, APIs, or infrastructure. Those belong to Technical Architecture. |

**Closes (long-standing open questions)**

- Memory Decay

- Conflict Resolution

- AI Write Governance

- Organizational Truth Handling

- Commitment Per-Subtype Lifecycle Restrictions

**Resolved In Product Architecture v2.0**

- Trust Cards

- Conflict Experience

- Drift Experience

**Still Open (deferred intentionally)**

- The exact mechanism that triggers a decay check (time-based vs. query-triggered) — deferred to Technical Architecture.

## Table of Contents

*Updates automatically in Microsoft Word. If it shows no entries, select it and press F9 to refresh.*

# 1. Purpose

This document defines how organizational reality becomes organizational memory.

The Ontology defines what exists. The Memory Model defines how what exists becomes remembered.

This document answers: how does the Company Brain transform organizational reality into persistent organizational memory?

This document is conceptual. It does not define:

- Databases

- Storage engines

- Graphs

- Vectors

- Schemas

- Infrastructure

Those belong to Technical Architecture.

# 2. Relationship to the Company Brain

The Company Brain architecture is:

**Reality → Understanding → Knowledge Objects → Memory → Intelligence → Execution → Exposure → Evolution**

The Memory Model defines the transition between Knowledge Objects and Memory, and the mechanisms through which Memory supports Intelligence, Execution, and Consumption.

The Memory Model is responsible for:

**Knowledge Objects → Memory → Consumption**

within the broader Company Brain architecture.

# 3. What Is Memory?

## Definition

**A memory is a persistent, structured representation of organizational reality through time.**

Memory is not storage. Memory is not a document. Memory is not a database record. Memory is organizational understanding that has been preserved.

## Core Principle

The Company Brain remembers reality. It does not remember everything. Memory is selective.

## Memory Formation Principle

Something becomes memory only when it satisfies at least one of the following:

- Changes organizational understanding

- Creates or modifies commitments

- Influences future decisions

- Changes organizational state

- Produces learning

- Affects goals, resources, rules, or relationships

Everything else may be captured. Not everything is remembered.

*This is the operational answer to the Architecture **&** Vision document**'**s Memory layer key question, “what should never be forgotten?” — anything matching one of the six conditions above.*

# 4. Knowledge Representation

## Definition

Knowledge Representation is the process by which organizational reality is transformed into canonical organizational knowledge before becoming memory.

The Understanding Layer produces structured organizational understanding.

That understanding is represented through Knowledge Objects.

Memory Formation then transforms those Knowledge Objects into persistent organizational memory.

## Conceptual Flow

**Reality → Capture → Understanding → Knowledge Objects → Memory Formation → Memory**

## Knowledge Objects

Knowledge Objects are canonical representations of organizational reality produced by the Understanding Layer.

Knowledge Objects are not memory.

Knowledge Objects are normalized organizational knowledge units from which memory is formed.

Knowledge Objects exist at two levels.

### Primitive Knowledge Objects

Primitive Knowledge Objects represent the irreducible organizational primitives defined by the Company Brain Architecture.

The Primitive Knowledge Object set is fixed and consists of:

- Actor Object

- Communication Object

- Commitment Object

- Action Object

- Resource Object

- Rule Object

- Goal Object

- Relationship Object

Primitive Knowledge Objects serve as the foundational representation layer for all higher-order organizational concepts.

### Composite Knowledge Objects

Composite Knowledge Objects represent higher-order organizational concepts.

They are constructed by combining Primitive Knowledge Objects according to the Company Brain Ontology.

Examples include:

- Person Object

- Team Object

- Project Object

- Department Object

- Policy Object

- Workflow Object

- Meeting Object

- Initiative Object

Composite Knowledge Objects mirror Ontology Layers 2–4.

### Memory Formation Relationship

Memory Formation may consume:

- Primitive Knowledge Objects

- Composite Knowledge Objects

- Relationships between both

depending on the type of memory being formed.

### Knowledge Object Requirements

Both Primitive and Composite Knowledge Objects must be:

- Human-readable

- AI-readable

- Traceable

- Portable

- Versionable

- Governed

### Open Knowledge Compatibility

The Company Brain should maintain compatibility with Open Knowledge Format (OKF) whenever practical.

Knowledge Objects may be represented, exchanged, imported, exported, or synchronized through OKF-compatible formats where governance permits.

The Company Brain extends beyond OKF through:

- Memory Lifecycle Management

- Commitment Memory

- Learning Memory

- Organizational Intelligence

- Governance

- Evolution

# 5. Memory Creation & Formation Routing

## Formation Pipeline

**Reality → Capture → Understanding → Knowledge Objects → Memory Formation → Memory**

Memory Formation applies only to signals that already satisfy the Memory Formation Principle in Section 3 — Formation Routing decides which memory type(s) a qualifying signal writes to, not whether it qualifies in the first place.

### Memory Formation Clarification

Memory Formation consumes Knowledge Objects rather than raw documents, captured signals, or unstructured organizational activity.

The role of Memory Formation is to determine:

- What should be remembered

- Which memory type should store it

- How it should be linked

- How provenance should be preserved

## Formation Routing Rule

A single understood event may create records in multiple memory types simultaneously. Every resulting memory record:

- Shares a common source reference

- Preserves provenance

- Remains independently queryable

This prevents fragmentation while maintaining traceability.

## Worked Example — Meeting

A meeting occurs. The Understanding layer identifies Communication, Actors, Goals, and Context within it.

| **Memory Type** | **What The Meeting Produces** |
| --- | --- |
| Interaction Memory | Discussion, reasoning, negotiation, and context — recorded directly. |
| Commitment Memory | New commitments, assignments, and ownership changes — recorded in state Requested or Promised. |
| Action Memory | None yet. No execution has occurred. |

Later, when a commitment is fulfilled, Action Memory receives the execution, outcome, and state change — linked back to the originating commitment.

**Result: one meeting may generate 1 Interaction record and N Commitment records, with 0 Action records until execution actually occurs.**

# 6. Memory Types

The Company Brain contains five memory systems: Factual, Interaction, Commitment, Action, and Learning. Each serves a different purpose.

## 6.1 Factual Memory

| **Purpose** | Preserve stable organizational reality. |
| --- | --- |
| **Inputs** | Actors Resources Goals Policies SOPs Organizational Structures |
| **Stores** | People Teams Departments Roles Goals Policies SOPs Resources |
| **Typical Queries** | Who owns this? What teams exist? What policy governs this? What goals are active? Which role has authority? |
| **Lifecycle** | Observed → Recorded → Updated → Superseded → Archived. Not every record passes through every stage — a Factual record may remain Recorded or Updated indefinitely without ever being Superseded. |

## 6.2 Interaction Memory

| **Purpose** | Preserve organizational reasoning. |
| --- | --- |
| **Inputs** | Meetings Discussions Negotiations Approvals Communications |
| **Stores** | Discussion records Negotiation history Approval conversations Context |
| **Typical Queries** | Why was this discussed? What alternatives existed? Who objected? What reasoning was used? |
| **Lifecycle** | Observed → Interpreted → Recorded → Linked → Archived. As with Factual Memory, a record need not reach every stage to be valid. |

## 6.3 Commitment Memory

| **Purpose** | Preserve obligations between actors. |
| --- | --- |
| **Inputs** | Assignments, Requests, Responsibilities, Promises, and Decisions. *Decisions trigger new commitments but are themselves reconstructed, not stored — see Section 11.* |
| **Stores** | Commitments Tasks Expectations Ownership Responsibilities |
| **Typical Queries** | What is still open? Who owns this? What is overdue? What did Person X promise? What commitment came from this meeting? |
| **Lifecycle** | Requested → Promised → one of Fulfilled, Declined, Delegated, Cancelled, Renegotiated, or Breached. |
| **Special Property** | Commitment Memory is future-oriented. Most memory records describe reality. Commitments describe intended reality. |

### Per-Subtype Lifecycle Restrictions

By default, every Commitment-derived object inherits the full eight-state Commitment lifecycle.

The table below records the only known exceptions.

Absence from this table means the default eight-state lifecycle applies unrestricted.

| Subtype | Restriction | Reason |
| --- | --- | --- |
| Customer Promise | No Delegated | An external obligation cannot be reassigned the way an internal task can. |
| Customer Promise | Renegotiated requires explicit customer-facing notice | Customer-facing promises cannot silently change terms. |
| Task | None — full 8 states | — |
| Assignment | None — full 8 states | — |
| Approval Obligation | None — full 8 states | — |

New subtypes inherit the full lifecycle unless explicitly added to this table.

## 6.4 Action Memory

| **Purpose** | Preserve what actually happened. |
| --- | --- |
| **Inputs** | Executions Workflow runs Incidents Exceptions State changes |
| **Stores** | Actions Outcomes Incident responses Workflow executions |
| **Typical Queries** | What happened? How was this resolved? What actions fulfilled this commitment? How does this process actually operate? |
| **Lifecycle** | Observed → Recorded → Linked → Used → Archived. Shown as possible stages, not a required sequence. |
| **Special Property** | Action Memory represents observed reality. Not intended reality. |

## 6.5 Learning Memory

| **Purpose** | Preserve organizational learning. |
| --- | --- |
| **Inputs** | Outcomes Patterns Failures Successes Drift Analysis |
| **Stores** | Lessons Heuristics Patterns Process Improvements Policy Improvements |
| **Typical Queries** | What did we learn? Has this happened before? What usually works? What mistakes should be avoided? |
| **Lifecycle** | Created → Validated → Used → Reinforced or Decayed → Archived. |
| **Special Property** | Learning Memory is the primary memory type subject to decay. Lessons lose relevance when organizational reality changes. |

# 7. Memory Lifecycle

All memory records move through lifecycle stages.

## Active Lifecycle

**Observed → Interpreted → Recorded → Linked → Used → Updated**

## Archive Path

**Updated → Superseded → Archived**

Archived records remain historically true. They are removed from the active working set. They are never silently deleted.

## Decay Path

Decay is different from archival. Decay affects relevance. Not existence.

For example, a lesson learned five years ago may still exist. Its confidence and applicability may decrease.

Decay primarily affects Learning Memory, and secondarily Interaction Memory when context becomes obsolete.

*Decay and archival are independent processes: a fully decayed Learning record is not automatically archived, and may later be explicitly reinforced if the conditions that produced it recur.*

# 8. Provenance

Every memory record carries:

- Who asserted it

- When

- From what source

- Under which rule version

- Confidence

- Challenge status

Purpose: memory must be explainable. Every memory must answer the question, why do we believe this?

# 9. Write Governance

Memory creation is governed. Not every actor may write every memory.

| **Writer** | **Permissions** |
| --- | --- |
| Human | May create Factual, Interaction, Commitment, and Learning memory, subject to authority. |
| AI | May propose memory updates. Writes may require automatic approval, delegated approval, or human approval, depending on memory type. |
| Automation | Restricted to predefined scopes. Must preserve provenance. |

**Core Principle: AI may contribute memory. AI does not become the source of truth.**

# 10. Conflict Resolution

Conflicting memories are expected. They are never silently overwritten.

- Rule 1 — Preserve both records.

- Rule 2 — Mark one as Current and the other as Superseded.

- Rule 3 — Maintain provenance for both.

## Tie-Break Rules

When confidence is equal:

- Higher authority source

- More recent evidence

- Explicit human review

## Highest-Risk Memory Type

Factual Memory — for example, two systems disagreeing about account ownership.

# 11. Memory Relationships

Memory gains value through relationships.

| **From** | **Relationship** | **To** |
| --- | --- | --- |
| Meeting | creates | Commitment |
| Commitment | fulfilled by | Action |
| Action | changes | State |
| Action | contributes to | Learning |
| Learning | updates | Policy or SOP |

*Important: Decision remains reconstructed and Action**'**s resulting state is not reified into a separate “State Change” object — Action Memory already carries the before/after state, which is what Pattern Detection reads. Neither Decision nor a standalone state-change record becomes a new ontology object.*

# 12. Memory Drift

## Definition

Drift occurs when intended reality differs from observed reality.

The comparison uses:

**Policy → SOP → Workflow**

| **Object** | **Source** |
| --- | --- |
| Policy | Factual Memory |
| SOP | Factual Memory |
| Workflow | Reconstructed from Action Memory |

## Drift Signal

A Drift Signal is generated when recurring execution patterns diverge from intended process design. Examples:

- Approvals skipped

- Unofficial steps added

- Repeated exception handling

- Alternative execution paths emerge

*Drift Signals belong to Intelligence. Not Memory.*

# 13. Organizational Learning

Learning occurs when reality updates understanding.

## Process

**Action Memory → Pattern Detection → Learning Formation → Learning Memory → Future Intelligence**

## Evolution Loop

**Policy → SOP → Execution → Action Memory → Learning Memory → Updated Policy**

## What Gets Written

Learning records may contain:

- Conditions

- Observed pattern

- Supporting evidence

- Confidence

- Recommendations

*Typical query: what have we learned from similar situations?*

# 14. Relationship to Intelligence

Memory is not intelligence.

Memory preserves understanding.

Intelligence reasons over memory.

**Reality → Knowledge Objects → Memory → Intelligence**

Without Memory, Intelligence has no continuity.

Without Intelligence, Memory has no operational value.

Memory also serves Consumption.

Intelligence is not the only consumer of memory.

Humans, agents, applications, and exposure systems all consume memory through contextual assembly and delivery.

# 15. Memory Consumption & Delivery

## Definition

Memory Consumption is the process by which stored organizational memory is assembled, contextualized, and delivered to a human or AI actor for use in work.

Memory is not valuable because it exists.

Memory becomes valuable when consumed.

## Context Assembly

Before delivery, memory is assembled into contextual packages.

Memory is rarely delivered as isolated records.

Examples include:

- Meeting Brief

- Executive Brief

- Customer Context

- Incident Context

- Proposal Context

- Project Context

### Inputs

A contextual package may combine:

- Factual Memory

- Interaction Memory

- Commitment Memory

- Action Memory

- Learning Memory

into a single response.

## Memory Delivery Routes

### Ambient Route

Examples:

- Slack Suggestions

- Gmail Context

- Outlook Context

- Calendar Briefs

- CRM Panels

- Browser Extension Context

### Agent Route

Examples:

- MCP Retrieval

- A2A Retrieval

- Context Injection

- Agent Memory Access

### Mission Control Route

Examples:

- Personal Reality

- Team Reality

- Organizational Memory

- Consultant

- Operational Intelligence

## Retrieval Principles

### Principle 1

Memory retrieval should be relevance-driven, not storage-driven.

### Principle 2

The same memory may appear through multiple delivery routes.

### Principle 3

Memory should be delivered at the moment of work whenever practical.

### Principle 4

Humans and AI systems consume memory through the same trust and provenance mechanisms.

## Feedback Signals

Every memory consumption event may generate feedback signals.

Examples:

- Accepted

- Rejected

- Modified

- Ignored

- Escalated

- Acted Upon

### Learning Relationship

**Memory Consumption → Feedback Signal → Evolution → Learning**

## Consumption Principle

Memory exists to improve work.

Memory should be evaluated not only by accuracy and completeness, but also by usefulness at the moment of work.

## Exposure Principle

The same memory may support:

- Human work

- AI work

- Decisions

- Coordination

- Execution

through different delivery mechanisms.

# One-Sentence Summary

| **The Company Brain Memory Model defines how organizational reality becomes canonical knowledge, how that knowledge becomes persistent memory, how memory is trusted, connected, evolved, assembled into context, delivered to humans and AI systems, and continuously improved through learning and feedback.** |
| --- |

ZeroManual — Internal   ·   Page  of