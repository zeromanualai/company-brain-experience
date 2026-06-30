COMPANY BRAIN — Architecture & Vision	v2.2

**COMPANY BRAIN**

Architecture & Vision

Version 2.2

Canonical Team Document

ZeroManual — Internal

June 2026

## Document Control

| **Field** | **Value** |
| --- | --- |
| Version | 2.2 |
| Status | Canonical Team Document |
| Supersedes | Version 2.1 |
| Scope | Architecture & Vision only. The companion Foundational Reasoning document is not affected by this revision. |

**Changes in This Revision**

- Added Canonical Knowledge Objects as the representation layer between Understanding and Memory (Sections 9 and 10).

- Added Primitive Knowledge Objects and Composite Knowledge Objects, establishing a two-tier organizational knowledge representation model (Section 9).

- Added Knowledge Representation Compatibility and Open Knowledge Format (OKF) alignment guidance (Section 9).

- Added the Exposure Layer, making delivery of memory and intelligence a first-class architectural responsibility (Sections 7 and 13).

- Expanded the Evolution Layer to learn from recommendation outcomes, delivery effectiveness, and human/AI interaction signals (Section 14).

- Added Principle 8 — Right Memory, Right Moment (Section 6).

- Expanded the Trust System to govern Canonical Knowledge Objects in addition to memory records (Section 15).

- Closed architectural open questions already resolved by Memory Model v1.1.

**Resolved In Memory Model v1.1**

- Memory Decay

- Conflict Resolution

- AI Write Governance

- Current vs Superseded Truth Model

See Memory Model v1.1 for authoritative definitions.

## Table of Contents

*Updates automatically in Microsoft Word. If it shows no entries, select it and press F9 to refresh.*

# 1. Introduction

## Purpose of This Document

This document defines the vision, architecture, and mental model of the Company Brain.

It is not a technical architecture document. It does not define:

- Databases

- APIs

- Infrastructure

- AI Models

- Programming Languages

- Frameworks

Instead, it defines:

- The problem we are solving

- What a Company Brain is

- How organizations actually function

- How Company Brain models organizational reality

- How Company Brain creates memory

- How Company Brain generates intelligence

- How Company Brain enables execution

- How Company Brain continuously learns

This document serves as the foundational reference for all future product, design, research, and engineering decisions.

# 2. The Problem

## Organizations Do Not Have Reliable Memory

Every company generates knowledge continuously. Knowledge is created through:

- Conversations

- Meetings

- Decisions

- Customer interactions

- Processes

- Emails

- Documents

- Chats

- Workflows

- Daily execution

Yet organizations do not possess a coherent memory system. Knowledge becomes fragmented across:

- People

- Documents

- Tools

- Systems

- Departments

Organizations continue functioning because humans compensate for these gaps. People remember:

- Who knows what

- Why decisions were made

- How exceptions are handled

- What happened previously

- Which process should be followed

AI systems cannot operate this way.

## Why Existing Systems Fail

### Search Systems

Search retrieves information. It does not understand:

- Context

- Intent

- Relationships

- Commitments

- Decisions

- Organizational history

### Knowledge Bases

Knowledge bases store information. They do not:

- Understand

- Reason

- Learn

- Detect gaps

- Preserve organizational memory

### Chatbots

Chatbots generate responses. They do not possess organizational understanding.

### Workflow Systems

Workflow systems execute predefined processes. They do not understand organizational reality.

## The Missing Layer

Between Raw Company Activity and Reliable Human & AI Execution, there is a missing layer. That layer is the Company Brain.

# 3. What Is A Company Brain?

## Definition

A Company Brain is a living organizational reality, memory, and intelligence system that continuously captures, understands, remembers, reasons over, and operationalizes how an organization functions.

It transforms fragmented organizational activity into structured organizational understanding.

The Company Brain becomes the shared source of truth for both humans and AI.

## What A Company Brain Is Not

- A document repository

- A knowledge base

- A wiki

- A search engine

- A chatbot

- A workflow tool

- An automation platform

These may interact with the Brain. They are not the Brain itself.

## What A Company Brain Is

- A model of organizational reality

- An organizational memory system

- An organizational intelligence system

- An organizational learning system

# 4. Organizational Reality

## Core Insight

Before a Company Brain can create memory, it must understand reality. The Brain cannot simply store documents. It must model how organizations actually function.

## Organizations Are Coordination Systems

Organizations are not fundamentally collections of:

- Documents

- SOPs

- Databases

- Workflows

Those are representations. Organizations are systems of coordinated human activity. The Company Brain therefore models:

- Actors

- Communications

- Commitments

- Actions

- Resources

- Rules

- Goals

- States

- Time

- Relationships

These form the foundation of organizational reality. Section 5 defines each of these primitives in detail.

## How Reality Relates To The Pipeline

Organizational Reality is not a separate stage that runs alongside the layers in Section 7. It is the substrate those layers act on.

The Capture and Understanding layers construct a structured model of reality from raw activity. The Memory layer preserves that model through time. The Intelligence layer reasons over it. The Execution layer acts on it. The Exposure layer delivers it. The Evolution layer refines it. There is one pipeline. Organizational Reality is what the pipeline is made of; Section 7 describes how the pipeline operates on it.

# 5. Atomic Primitives of Organizational Reality

Earlier drafts treated Entity, Relationship, Event, Decision, and Context as the primitives. Research showed these were still composites. The deepest recurring primitives — the ones that do not decompose further — are the ten below.

| **Primitive** | **Definition** | **Examples** | **Key Question** |
| --- | --- | --- | --- |
| Actor | An entity capable of participating in organizational activity. | Employee, Team, Department, Customer, Vendor, AI Agent | Who? |
| Communication | An exchange of meaning between actors. | Meetings, Emails, Messages, Requests, Discussions | What was communicated? |
| Commitment | An obligation, responsibility, promise, expectation, or authorization. | Deliver a report, Approve a budget, Resolve an incident | Who owes what to whom? |
| Action | Work performed that changes organizational state. | Process refund, Deploy software, Approve request | What was done? |
| Resource | Something that can be used, consumed, managed, or affected. | Money, Products, Documents, Customer Accounts | What is being acted upon? |
| Rule | A constraint, policy, authority structure, or governing principle. | Approval thresholds, Security policies, Escalation paths, Spending limits | What is allowed? |
| Goal | A desired future state. | Increase retention, Launch by Q3, Reduce response time | Why are we doing this? |
| State | The current condition of something. | Open, In Progress, Resolved, Approved | What is the current situation? |
| Time | The temporal dimension of organizational activity. | Timestamp, Deadline, Duration, Recurrence | When? |
| Relationship | A meaningful connection between primitives. | Reports-to, Depends-on, Caused-by, Fulfills | How are things connected? |

**Higher-Order Concepts Built From These Primitives**

Everything else in the organization is a composite of the ten primitives above. For example:

| **Concept** | **Composition** |
| --- | --- |
| Decision | Communication + Goal + Rule + Commitment |
| Workflow | Actors + Actions + Rules + States + Commitments |
| Project | Actors + Goals + Resources + Commitments + Actions |

Decision and Workflow are not modeled as separate memory types. They are reconstructed on demand from the primitives that compose them — see the mapping in Section 10.

# **6. Core Principles**

| **#** | **Principle** | **Statement** |
| --- | --- | --- |
| 1 | Reality Before Representation | The Company Brain models organizational reality. Documents and systems are merely representations of that reality. |
| 2 | Memory Over Documents | Documents are sources. Memory is the asset. |
| 3 | Context Over Information | Information without context has limited value. The Brain must preserve why, who, when, and under what conditions — not only what. |
| 4 | Understanding Over Storage | Storage accumulates information. Understanding creates intelligence. |
| 5 | Trust Before Automation | Automation without trust creates risk. |
| 6 | Execution Creates Memory | Every action creates new organizational knowledge. |
| 7 | The Brain Must Learn | The Brain continuously evolves through outcomes and feedback. |
| 8 | Right Memory, Right Moment | The Company Brain is responsible for delivering the right memory, to the right actor, through the right channel, at the right moment. Memory has value only when it reaches the point of work. |

# **7. Company Brain Architecture**

The Company Brain consists of seven core layers:

**Capture → Understand → Memory → Intelligence → Execution → Exposure → Evolution**

These seven layers operationalize Organizational Reality end to end.

Capture and Understand construct it.

Memory preserves it.

Intelligence reasons over it.

Execution acts on it.

Exposure delivers it.

Evolution refines it and feeds the result back into Memory.

**Quick Reference**

| **Layer** | **Purpose** | **Key Question** |
| --- | --- | --- |
| 1. Capture | Observe and capture organizational reality. | What is happening? |
| 2. Understand | Transform activity into organizational understanding. | What does this mean? |
| 3. Memory | Preserve organizational understanding through time. | What should never be forgotten? |
| 4. Intelligence | Transform memory into organizational intelligence. | What should we understand? |
| 5. Execution | Transform intelligence into action. | What should happen next? |
| 6. Exposure | Deliver memory, intelligence, and actions to the right human or AI actor. | Who needs to know this? |
| 7. Evolution | Create organizational learning loops. | What changed because of what we did? |

*Sections 8 through 14 define each layer in full.*

# 8. Layer 1 — Capture Layer

| **Purpose** | Observe and capture organizational reality. |
| --- | --- |
| **Responsibilities** | Collect organizational signals Preserve source information Record activity |
| **Inputs** | People Meetings Emails Chats Systems Documents Workflows Events |
| **Key Question** | What is happening? |
| **Outputs** | Raw activity Raw events Raw communications Raw organizational signals |

# 9. Layer 2 — Understanding Layer

| **Purpose** | Transform activity into organizational understanding. |
| --- | --- |
| **Responsibilities** | Identify the atomic primitives present in every signal: Actors, Communications, Commitments, Actions, Resources, Rules, Goals, States, Relationships. Transform captured activity into structured organizational understanding. Produce Canonical Knowledge Objects representing organizational reality. |
| **Inputs** | Captured organizational activity. |
| **Key Question** | What does this mean? |
| **Outputs** | Structured organizational reality represented as Canonical Knowledge Objects. |

## Knowledge Objects

Knowledge Objects are canonical representations of organizational reality produced by the Understanding Layer.

They are derived from the Company Brain Ontology and provide a standardized representation that can be consumed by Memory, Intelligence, Products, and external systems.

Knowledge Objects are:

- Human-readable

- AI-readable

- Traceable

- Versionable

- Portable

Knowledge Objects are not memory.

They are the representation layer from which memory is formed.

### Primitive Knowledge Objects

These are the eight canonical, irreducible Knowledge Object types, one per atomic primitive (Section 5).

This is a closed set.

- Actor Object

- Communication Object

- Commitment Object

- Action Object

- Resource Object

- Rule Object

- Goal Object

- Relationship Object

### Composite Knowledge Objects

Composite Knowledge Objects represent Core Objects, Organizational Structures, and Operational Constructs (Ontology Layers 2–4).

Each Composite Knowledge Object is built by combining Primitive Knowledge Objects, mirroring how Ontology composes higher-order objects from atomic primitives.

Composite Knowledge Objects are defined and owned by the Ontology document.

Architecture & Vision defines only the Primitive layer.

### Ownership Boundary

Architecture & Vision defines only the Primitive Knowledge Object layer.

Primitive Knowledge Objects are the canonical representation of the atomic primitives that form the foundation of organizational reality.

Composite Knowledge Objects are defined, structured, and governed by the Ontology.

Architecture intentionally does not define Composite Knowledge Objects.

Their structure, relationships, inheritance rules, and composition logic are owned by the Ontology and may evolve independently of the Architecture document.

### Knowledge Representation Compatibility

The Company Brain maintains compatibility with emerging open knowledge standards such as Open Knowledge Format (OKF) whenever practical.

Knowledge Objects serve as the Company's canonical representation layer and may be exchanged through OKF-compatible formats where governance permits.

# 10. Layer 3 — Memory Layer

| **Purpose** | Preserve organizational understanding through time. This is the actual memory system of the Company Brain. |
| --- | --- |
| **Responsibilities** | Maintain five distinct, purpose-built memory stores Attach provenance, time, and state to every record Preserve relationships and links across memory types Track the lifecycle of every open commitment Serve relevant memory to the Intelligence layer on demand |
| **Inputs** | Canonical Knowledge Objects. |
| **Key Question** | What should never be forgotten? |
| **Outputs** | Persistent organizational memory. |

## Memory Formation

The Memory Layer operates on Canonical Knowledge Objects produced by the Understanding Layer.

Memory Formation transforms Knowledge Objects into persistent organizational memory through routing, lifecycle management, provenance tracking, and relationship preservation.

Knowledge Objects are representations of reality.

Memory is the preserved understanding of reality through time.

## Memory Architecture

The Brain consists of five memory systems.

| **Memory Type** | **Purpose** | **Stores** | **Key Question** |
| --- | --- | --- | --- |
| Factual Memory | Preserve what exists. | Actors, Resources, Structures, Policies, Goals, Processes | What do we know? |
| Interaction Memory | Preserve organizational reasoning. | Discussions, Decisions, Tradeoffs, Context | Why do we know it? |
| Commitment Memory | Preserve commitments and obligations. | Promises, Responsibilities, Ownership, Expectations | Who owes what to whom? |
| Action Memory | Preserve execution history. | Actions, Outcomes, Exceptions, Escalations | What actually happened? |
| Learning Memory | Preserve organizational learning. | Lessons, Patterns, Successes, Failures, Improvements | What have we learned? |

## Commitment Lifecycle

Commitment Memory does not store promises as static facts. Every commitment carries a state, so the Brain can always answer whether an obligation is open, at risk, or resolved.

| **State** | **Definition** | **Typical Trigger** |
| --- | --- | --- |
| Requested | An actor has asked for a commitment; not yet binding. | A request is raised in a Communication. |
| Promised | The responsible actor has accepted the obligation. Binding, with a condition of satisfaction and, where relevant, a due date. | The responsible actor accepts the request. |
| Delegated | The obligation has been transferred to another actor. The original commitment closes; a new one opens. | The responsible actor hands the work to someone else. |
| Fulfilled | The condition of satisfaction has been met and accepted by the requester. | Work is completed and accepted. |
| Declined | The request was not accepted. No obligation is created. | The requested actor refuses the request. |
| Cancelled | A previously active commitment is withdrawn by agreement before fulfillment. | Requester or responsible actor withdraws it. |
| Renegotiated | Scope, deliverable, or due date is changed by agreement. The original commitment closes; a new version opens, linked to it. | Terms change mid-flight. |
| Breached | The due date passed, or the condition was rejected, without fulfillment, cancellation, delegation, or renegotiation. | Deadline passes with no resolution. |

*Flow: Requested → Promised → one of Fulfilled, Declined, Cancelled, Delegated, Renegotiated, or Breached. Delegated and Renegotiated always link forward to a new commitment record rather than mutating the original — the history of the change is part of the memory.*

## Primitive-to-Memory Mapping

Every atomic primitive from Section 5 has an explicit home in the memory architecture. Actor, Resource, Rule, and Goal are facts about what exists, so they live in Factual Memory. State, Time, and Relationship are not separate stores — they are attributes carried by every record in every memory type.

| **Primitive** | **Primary Memory Home** | **How It Is Used Elsewhere** |
| --- | --- | --- |
| Actor | Factual Memory | Referenced as a participant by every Interaction, Commitment, and Action record. |
| Resource | Factual Memory | Referenced by Action (what was acted on) and Commitment (what was promised). |
| Rule | Factual Memory | Referenced by Commitment (terms and authority) and Intelligence (compliance checks). |
| Goal | Factual Memory | Referenced by Interaction (why a decision was made) and Intelligence (progress evaluation). |
| Communication | Interaction Memory | The source of new Commitments and the basis for reconstructing Decisions. |
| Commitment | Commitment Memory | Created by Communication; discharged, breached, or delegated through Action. |
| Action | Action Memory | Updates Resource state; fulfills or breaches open Commitments. |
| State | Attached to every record, in every memory type | Not a separate store. Every Commitment, Action, and fact carries its current condition. |
| Time | Attached to every record, in every memory type | Not a separate store. Every record is timestamped and time-qualified. |
| Relationship | Expressed as links across all memory types | Not a separate store. The connective structure that lets memory be traversed as a graph. |

# 11. Layer 4 — Intelligence Layer

| **Purpose** | Transform memory into organizational intelligence. |
| --- | --- |
| **Responsibilities** | Reason over memory Detect patterns Identify risks Detect gaps Generate recommendations Support decisions Detect drift between how work is designed to happen (Rules) and how it actually happens (Action Memory) — the ostensive-versus-performative gap |
| **Inputs** | All memory systems. |
| **Key Question** | What should we understand? |
| **Outputs** | Insights Recommendations Opportunities Warnings Plans Drift signals between policy and practice |

# 12. Layer 5 — Execution Layer

| **Purpose** | Transform intelligence into action. |
| --- | --- |
| **Responsibilities** | Execute work Coordinate activity Complete commitments Operate the organization |
| **Inputs** | Intelligence and recommendations. |
| **Key Question** | What should happen next? |
| **Outputs** | Actions and outcomes. |

## Participants

| **Humans** | **AI** |
| --- | --- |
| Employees Managers Operators Executives | Assistants Agents Workflows Automations |

# **13. Layer 6 — Exposure Layer**

| **Purpose** | Deliver memory, intelligence, and actions to humans and AI systems through appropriate channels. |
| --- | --- |
| **Responsibilities** | Ambient Delivery, Agent Access, Mission Control Delivery, Reality Feed Distribution, Context Injection, Notification Routing, Multi-channel Memory Exposure |
| **Inputs** | Memory, Intelligence, Execution |
| **Key Question** | Who needs to know this? Where should it appear? When should it appear? How should it be delivered? |
| **Outputs** | Slack Suggestions, Email Context, Calendar Briefs, CRM Context, Browser Extension Context, MCP Responses, Reality Feed Items, Mission Control Views |

# **14. Layer 7 — Evolution Layer**

| **Purpose** | Create organizational learning loops. Ensure the Brain continuously improves. |
| --- | --- |
| **Responsibilities** | Evaluate outcomes, Capture lessons, Update memory, Improve future reasoning, Detect drift, Analyze feedback, Evaluate recommendations, Evaluate agent performance, Evaluate exposure effectiveness, Generate policy update candidates, Compare designed rules and processes against executed Action patterns and route confirmed divergence into Learning Memory as candidate process improvements |
| **Inputs** | Actions, outcomes, feedback signals, recommendation outcomes, exposure outcomes |
| **Key Question** | What changed because of what we did? |
| **Outputs** | Updated organizational memory, updated organizational understanding, updated learning signals, policy improvement candidates |

The Evolution Layer learns not only from organizational outcomes, but also from how humans and AI systems interact with delivered memory, recommendations, and actions.

Examples include:

- Accepted Suggestions

- Rejected Suggestions

- Ignored Suggestions

- Agent Approval Rates

- Agent Rejection Rates

- Exposure Effectiveness

These become learning signals used to improve future reasoning and delivery.

# 15. Supporting Systems

Supporting systems operate across all layers. They are not the Brain itself. They enable safe interaction with the Brain.

## **Trust System**

| **Purpose** | Ensure organizational understanding remains trustworthy. |
| --- | --- |
| **Responsibilities** | Source traceability, Ownership Verification, Audit history, Confidence assessment, Governance, Provenance & versioning, Knowledge Representation Governance |
| **Key Question** | Can we trust this? |

### Knowledge Representation Governance

Ensure Canonical Knowledge Objects remain:

- Consistent

- Traceable

- Versioned

- Portable

- Governed

across all Company Brain components.

## Consultant System

| **Purpose** | Help humans and AI understand and improve the organization. |
| --- | --- |
| **Responsibilities** | Recommendations Guidance Reviews Planning support Continuous improvement |
| **Key Question** | What should we do next? |

## Workspace System

| **Purpose** | Provide interfaces for interacting with the Brain. |
| --- | --- |
| **Responsibilities** | Search Views Dashboards Knowledge Studio Automation Studio Reporting |
| **Key Question** | How do we interact with the Brain? |

# **16. Organizational Learning Loop**

| **Traditional Systems** | **Company Brain** |
| --- | --- |
| Store → Retrieve | Observe Reality → Understand Reality → Create Knowledge Objects → Create Memory → Generate Intelligence → Execute → Expose → Learn → Update Reality Model |

The Brain continuously improves its understanding of the organization.

# **17. Relationship to Products**

The Company Brain is the foundation. Products are built on top.

**Company Brain → Intelligence → Exposure → Applications → Interfaces**

The Brain remains the source of truth.

Products do not replace the Brain.

They expose and operationalize it.

Everything else is an interaction layer.

# **18. Long-Term Vision**

**Today:**

Organizations operate through fragmented knowledge.

**Tomorrow:**

Organizations operate through a Company Brain.

The Company Brain becomes the living model of organizational reality.

- It remembers.

- It understands.

- It reasons.

- It coordinates.

- It delivers.

- It learns.

Humans and AI operate from the same shared understanding. The organization becomes capable of preserving and compounding its intelligence over time.

# One-Sentence Summary

| **The Company Brain is a living organizational reality, knowledge, memory, intelligence, exposure, and learning system that models how an organization functions, preserves what it learns, reasons over what it knows, delivers the right understanding at the right moment, and enables both humans and AI to operate from a shared understanding of reality.** |
| --- |

ZeroManual — Internal   ·   Page  of