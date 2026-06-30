Company Brain — Ontology	v1.2

**COMPANY BRAIN**

Ontology

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
| Scope | Ontology only. Memory Model and Product Architecture remain separate documents. |

**Changes in This Revision**

- Added Relationship To Knowledge Representation, clarifying that Ontology defines concepts while Knowledge Objects define their representation (Section 2).

- Updated the Ontology Bridge to include Knowledge Objects between Ontology and Memory (Section 1).

- Added Ontology And Knowledge Objects, introducing Composite Knowledge Objects and their relationship to the Primitive Knowledge Objects defined in Architecture & Vision v2.2 (Section 3).

- Added Open Knowledge Compatibility and Representation Independence statements (Section 2).

- Added Ontology Boundary, clarifying what Ontology is explicitly not responsible for (Section 8).

- Reclassified object-level Knowledge Objects (Person Object, Team Object, Policy Object, etc.) as **Composite Knowledge Objects**, resolving a granularity mismatch against the primitive-level Knowledge Objects defined in Architecture & Vision v2.2 and Memory Model v1.2 (Section 3).

- Fixed a cross-document inconsistency in Decision's composition — removed Context from Decision's "Built From" list (Layer 4), aligning with Architecture & Vision v2.2's four-component definition and with Ontology's own Context Model (Section 4), which defines Context as emergent, not structural.

- Added an explicit Ownership Boundary between Primitive Knowledge Objects (owned by Architecture & Vision) and Composite Knowledge Objects (owned by Ontology) (Section 3).

- Updated the One-Sentence Summary to reflect Ontology's role as the foundation from which Knowledge Objects, Memory, Intelligence, Products, and Technology are derived.

**Resolved In Memory Model v1.2**

- Per-Subtype Commitment Lifecycle Restrictions — see Memory Model v1.2, Section 5.3.

**Still Open (deferred to Memory Model v1.2 / Technical Architecture)**

- Relationship coverage for objects not yet exercised by a real use case.

- Storage and versioning schema for ontology objects — explicitly out of scope for this conceptual document.

## Table of Contents

*Updates automatically in Microsoft Word. If it shows no entries, select it and press F9 to refresh.*

# 1. Purpose

This document defines the ontology of the Company Brain.

The purpose of the ontology is to answer a single question:

**What exists inside the world that the Company Brain understands?**

The ontology serves as the bridge between:

**Atomic Primitives → Ontology → Knowledge Objects → Memory → Intelligence → Products → Technology**

Knowledge Objects are the canonical representations derived from Ontology.

Ontology defines the concepts.

Knowledge Objects define their representation.

The ontology is not a database model.

It is not a technical schema.

It is not a representation format.

It is a conceptual model of organizational reality.

# 2. Ontology Philosophy

The Company Brain does not model documents, software, databases, or dashboards as primary concepts.

Those are representations.

Instead, the Company Brain models:

- Organizational reality

- Organizational coordination

- Organizational memory

The ontology therefore represents:

- What exists

- How things relate

- How organizations coordinate

- How organizations change through time

## Relationship To Knowledge Representation

The Ontology defines what exists inside organizational reality.

Knowledge Representation defines how ontology objects are represented, exchanged, interpreted, and consumed throughout the Company Brain.

The Ontology remains the source of conceptual truth.

Knowledge Objects are representations derived from Ontology.

The Ontology does not define representation formats.

The Ontology defines the concepts those formats represent.

### Open Knowledge Compatibility

The Company Brain may represent ontology objects through Canonical Knowledge Objects compatible with Open Knowledge Format (OKF).

OKF compatibility affects representation and exchange.

It does not alter the ontology itself.

The ontology remains independent of any specific representation format.

### Representation Independence

Organizational reality exists independently of how it is represented.

The Ontology remains valid regardless of:

- Databases

- APIs

- Knowledge Formats

- Knowledge Objects

- Storage Technologies

- Product Interfaces

Representations may evolve.

Ontology remains the conceptual foundation.

# 3. Ontology Layers

The ontology consists of four layers.

**Atomic Primitives → Core Objects → Organizational Structures → Operational Constructs**

## Ontology And Knowledge Objects

The Ontology defines organizational concepts.

Knowledge Objects are canonical representations of those concepts.

Knowledge Objects do not introduce new organizational concepts.

They are representations of existing ontology concepts.

### Composite Knowledge Objects

Composite Knowledge Objects represent Core Objects, Organizational Structures, and Operational Constructs.

Each Composite Knowledge Object is built by combining Primitive Knowledge Objects (the eight atomic types defined in Architecture & Vision v2.2), the same way Ontology Layer 2–4 objects are built from Atomic Primitives.

| Ontology Concept | Composite Knowledge Object |
| --- | --- |
| Person | Person Object |
| Team | Team Object |
| Commitment | Commitment Object |
| Policy | Policy Object |
| Meeting | Meeting Object |

**Note:** Commitment Object appears in both tiers.

It exists as:

- A Primitive Knowledge Object representing the Commitment primitive.

- A Composite Knowledge Object representing the Commitment ontology object.

This is intentional.

Commitment is one of the few concepts that exists both as an atomic primitive and as a first-class ontology object.

### Ownership Boundary

Architecture & Vision defines the Primitive Knowledge Object layer.

Primitive Knowledge Objects correspond to the atomic primitives that form the foundation of organizational reality.

Ontology defines Composite Knowledge Objects.

Composite Knowledge Objects are derived from Core Objects, Organizational Structures, and Operational Constructs and may evolve as the Ontology evolves.

Memory Model defines how both Primitive and Composite Knowledge Objects become persistent organizational memory.

Product Architecture defines how memory derived from those objects is consumed by humans and AI systems.

## Layer 1 — Atomic Primitives

The irreducible building blocks of organizational reality.

These primitives are defined in the Architecture & Vision document and serve as the foundation for both Ontology and Primitive Knowledge Objects.

Everything else in this ontology is derived from them.

- Actor

- Communication

- Commitment

- Action

- Resource

- Rule

- Goal

- State

- Time

- Relationship

These primitives are defined in the Architecture & Vision document. Everything else in this ontology is derived from them.

## Layer 2 — Core Objects

Core Objects are the first-class entities that exist inside the Company Brain — the primary objects humans and AI reason about.

| **Object** | **Built From** | **Represents** | **Examples** |
| --- | --- | --- | --- |
| Person | Actor, Relationships, Commitments, Actions | An individual participant within organizational reality. | Employee, Manager, Founder, Contractor |
| Team | Actors, Relationships, Goals, Commitments | A coordinated group of actors. | Engineering, Operations, Customer Success |
| Role | Actor, Rule, Commitment, Relationship | A set of expected responsibilities and authority. | CTO, Product Manager, Support Lead |
| Customer | Actor, Goals, Commitments, Actions | An external actor receiving value from the organization. | Enterprise account, Trial user, Free-tier user |
| Vendor | Actor, Commitments, Resources | An external actor providing value to the organization. | Software supplier, Contractor agency, Payment processor |
| Agent | Actor, Rules, Goals, Actions | An AI participant operating within organizational reality. Agents are actors, not tools. | Support agent, Scheduling agent, Code review agent |

*Person and Team additionally carry standing key questions that the eventual Workspace views are built around — for Person: who is this, what do they own, what have they influenced; for Team: what is it responsible for, what goals does it own, how does it interact with other teams.*

## Layer 3 — Organizational Structures

These define how organizations are organized.

| **Object** | **Built From** | **Represents** | **Examples** |
| --- | --- | --- | --- |
| Department | Teams, Goals, Relationships | A major organizational function. | Engineering, Sales, Operations |
| Goal | Goal Primitive, Relationships, Time | A desired future state. | Increase retention, Launch product, Reduce support cost |
| Initiative | Goal, Commitments, Actions, Resources | A coordinated effort pursuing a goal. | Q3 retention push, Platform migration |
| Project | Actors, Goals, Resources, Actions, Commitments | A bounded execution effort. | Website redesign, API v2 launch |
| Organization | Teams, Departments, Goals, Rules, Relationships | The entire company. | ZeroManual |

## Layer 4 — Operational Constructs

These represent how work actually happens.

| **Object** | **Built From** | **Represents** | **Examples** |
| --- | --- | --- | --- |
| Commitment | Commitment Primitive, Actor, Time, State | An obligation between actors. | Assignment, Responsibility, Approval obligation, Customer promise |
| Task | Commitment, Action, Goal | A discrete unit of work. | Write report, Fix bug, Approve invoice |
| Workflow | Actors, Actions, Rules, States, Commitments | A repeatable pattern of organizational execution. Not a memory type — a derived construct. | Refund process, Onboarding sequence, Incident response |
| SOP | Rules, Actions, Goals | The intended way work should occur. | Refund SOP, Onboarding SOP |
| Policy | Rules, Goals, Authority | A governing organizational constraint. | Spending limit policy, Data retention policy |
| Decision | Communication, Goal, Rule, Commitment | A commitment to a future course of action. Not atomic — reconstructed from multiple primitives. | Pricing change, Hiring decision, Vendor selection |
| Meeting | Actors, Communications, Time | A coordination event. | Standup, Planning session, Customer call |
| Incident | Actions, Resources, Commitments, States | An unexpected operational disruption. | Outage, Data breach, Missed deadline |
| Opportunity | Goal, Resource, Commitment | Potential future value. | Upsell, Partnership, Expansion deal |

*Context is emergent (Section 4), surfaced when reasoning over a Decision — not a structural component of it. This aligns Decision's composition with Architecture & Vision v2.2.*

## Commitment Lifecycle

The Commitment object follows the same eight-state lifecycle defined in the Architecture & Vision document:

*Requested → Promised → one of Fulfilled, Declined, Delegated, Cancelled, Renegotiated, or Breached.*

### Lifecycle Inheritance

Any ontology object that lists Commitment among its Built From components inherits this eight-state lifecycle by default. This applies to Task, and to the Assignment, Approval Obligation, and Customer Promise examples listed above.

An object only departs from the default lifecycle once a future revision defines a narrower one explicitly. Per-subtype restrictions are defined in Memory Model v1.2, Section 5.3.

### Disambiguating Policy, SOP, and Workflow

Policy, SOP, and Workflow all draw heavily on Rule and Goal, which can make them look interchangeable. They are not — each answers a different question.

| **Object** | **Nature** | **Answers** |
| --- | --- | --- |
| Policy | The constraint. Defines what is allowed, required, or prohibited, and who has authority to grant exceptions. Changes rarely. | What is allowed? |
| SOP | The design. The prescribed sequence of steps for satisfying a Policy or achieving a Goal in a recurring situation. Written before execution. | How is this supposed to happen? |
| Workflow | The observation. The pattern reconstructed from Action Memory showing how work actually happened across many executions. Exists only after execution. | How does this actually happen? |

SOP and Workflow are the same situation viewed from two sides: SOP is the designed, ostensive version; Workflow is the executed, performative version. This is exactly the distinction the Architecture & Vision document's Intelligence layer is built to detect — it compares SOP against Workflow to surface drift between policy and practice. Policy sits one level above both, constraining what any SOP or Workflow is allowed to specify.

# 4. Context Model

Context is not treated as a primitive. Context is an emergent construct.

Context is generated from:

- Goals

- Rules

- Relationships

- History

- Actions

- Commitments

- Time

- Resources

For example, a decision's context may include previous decisions, active goals, existing commitments, resource constraints, and current organizational state.

*Context answers: why did this happen?*

# 5. Organizational Memory Mapping

Every ontology object maps into memory. This section gives two views: which objects each memory type stores, and — closing the gap left open in the previous draft — exactly where each individual object lives and where else it is referenced.

## By Memory Type

| **Memory Type** | **Stores** |
| --- | --- |
| Factual Memory | People, Teams, Departments, Roles, Goals, Policies, SOPs, Resources, Organization structure |
| Interaction Memory | Meetings, Discussions, Negotiations, Approvals |
| Commitment Memory | Responsibilities, Assignments, Promises, Obligations, Expectations, Tasks |
| Action Memory | Workflows (as executed), Incidents, Executions, Exceptions, Outcomes |
| Learning Memory | Lessons, Patterns, Failures, Successes, Process improvements, Policy improvements |

## By Object — Primary Home and Cross-References

| **Object** | **Primary Memory Home** | **Also Referenced In** |
| --- | --- | --- |
| Person | Factual Memory | Interaction (decisions made), Commitment (what they own), Action (what they did) |
| Team | Factual Memory | Commitment (goals and commitments owned), Interaction (team discussions) |
| Role | Factual Memory | Inherited through Person — no independent record |
| Customer | Factual Memory | Commitment (promises made to them), Action (interactions and outcomes) |
| Vendor | Factual Memory | Commitment (contracts and obligations), Action (deliveries) |
| Agent | Factual Memory | Action (what it executed), Commitment (what it owns) |
| Department | Factual Memory | — |
| Goal | Factual Memory | Interaction (why a decision was made), Intelligence (progress evaluation) |
| Initiative | Factual Memory | Commitment Memory and Action Memory (the commitments and actions inside it) |
| Project | Factual Memory | Commitment Memory and Action Memory |
| Organization | Factual Memory | — |
| Commitment | Commitment Memory | Action Memory (the action that fulfills or breaches it) |
| Task | Commitment Memory (inherits from Commitment) | Action Memory (the execution record once complete) |
| Workflow | Not stored — reconstructed on demand | Action Memory (executed steps), Commitment Memory (commitments fulfilled), Factual Memory (the SOP or Rule it follows) |
| SOP | Factual Memory | Intelligence (compared against Workflow to detect drift) |
| Policy | Factual Memory | Commitment Memory (terms referenced by commitments), Intelligence (compliance checks) |
| Decision | Not stored — reconstructed on demand | Interaction Memory (the discussion), Commitment Memory (the commitment created), Factual Memory (the Goal or Rule referenced) |
| Meeting | Interaction Memory | — |
| Incident | Action Memory | Commitment Memory (response obligations created) |
| Opportunity | Factual Memory | Commitment Memory (commitments made to pursue it), Action Memory (actions taken toward it) |

# 6. Relationship Model

No object exists in isolation. The Company Brain is fundamentally relational — without relationships, the Brain becomes storage; with relationships, the Brain becomes understanding.

| **From** | **Relationship** | **To** |
| --- | --- | --- |
| Person | belongs to | Team |
| Team | owns | Goal |
| Goal | drives | Initiative |
| Initiative | contains | Projects |
| Project | creates | Commitments |
| Commitment | fulfilled by | Actions |
| Action | changes | State |
| Decision | creates | Commitments |
| Policy | constrains | Actions |
| Incident | triggers | Actions |
| Learning | updates | Policy |
| Person | occupies | Role |
| Role | reports to | Role |
| Team | belongs to | Department |
| Department | belongs to | Organization |
| Customer | holds | Commitments (contracts, promises) |
| Vendor | provides | Resources |
| Agent | acts on behalf of | Person or Team |
| Agent | executes | Actions |

*This is a representative set, not an exhaustive schema. Relationships not yet modeled here will be added as Memory Model defines storage and traversal requirements.*

# 7. Derived Intelligence Objects

These are not stored directly. They emerge from reasoning, and belong to the Intelligence layer, not the Ontology layer:

- Knowledge Gap

- Operational Risk

- Agent Readiness

- Brain Score

- Recommendation

- Prediction

- Opportunity Signal

- Drift Signal

- Policy Violation

- Process Bottleneck

*Opportunity Signal is the Intelligence layer**'**s pattern-detected hint that potential value may exist — for example, a usage pattern suggesting a customer is ready for an upsell. It becomes an Opportunity, the Layer 4 ontology object, once a human or agent commits resources to formally pursuing it.*

# 8. What The Company Brain Ultimately Understands

The Company Brain does not understand documents.

It understands organizational reality:

**Who exists → What they are trying to achieve → What commitments exist → What actions occur → What rules govern behavior → How everything is connected → How reality changes through time**

Everything else is a representation of those concepts.

## Ontology Boundary

The Ontology is responsible for defining organizational reality.

The Ontology is not responsible for:

- Knowledge Representation Formats

- Memory Lifecycle

- Memory Formation

- Memory Retrieval

- Product Experiences

- User Interfaces

- Agent Protocols

- Storage Technology

Those concerns belong to other Company Brain documents.

# One-Sentence Summary

| **The Company Brain Ontology defines the objects, structures, and relationships that make up organizational reality, serving as the conceptual foundation from which Knowledge Objects, Memory, Intelligence, Products, and Technology are derived.** |
| --- |

ZeroManual — Internal   ·   Page  of