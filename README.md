
# Agentic Jira Intelligence System — Governed Multi-Agent AI Decision Platform

---

## 1. Executive Summary

The Agentic Jira Intelligence System is a **multi-agent AI decision intelligence platform** designed to transform unstructured Jira tickets into structured, execution-ready decisions for FinTech engineering and risk workflows.

The system simulates a real enterprise delivery environment where AI agents assist in:
- requirement clarification
- effort estimation
- regulatory risk detection
- prioritisation logic
- execution recommendation

However, this is explicitly designed as a:

> **Human-governed decision support system, not an autonomous execution engine**

All final decisions remain under human accountability.

---

## 2. Key Value Proposition

This project demonstrates how AI can move beyond task automation into **structured decision intelligence** by:

- Reducing ambiguity in Jira requirements
- Standardising effort estimation across teams
- Surfacing regulatory risks early in SDLC
- Improving prioritisation consistency
- Supporting leadership-level decision-making with structured outputs

---

## 3. Real-World Enterprise Relevance

This system is applicable to:

- AI Product Management
- Delivery Leadership (Engineering / PMO)
- Risk & Compliance Technology roles
- FinTech / RegTech transformation teams

It demonstrates:
- multi-agent system design
- enterprise workflow modelling
- structured AI decision pipelines
- governance-aware AI implementation

---

## 4. Problem Statement

In enterprise engineering environments:

- Jira tickets are often incomplete or ambiguous
- Estimation is inconsistent across teams
- Risk identification happens too late in SDLC
- Prioritisation is subjective and non-standardised

This leads to:
- delivery delays
- compliance exposure
- misaligned engineering effort
- poor portfolio visibility

---

## 5. Solution Overview

The system introduces a **multi-agent decision pipeline**:

- Requirement Clarity Agent → refines ambiguous tickets
- Effort Estimation Agent → provides structured SDLC estimates
- Risk Agent → evaluates AML / GDPR / SEC exposure
- Priority Agent → computes business impact scoring
- Decision Engine → aggregates outputs into execution recommendation

---

## 6. System Architecture



```
Jira Ticket Input
      │
      ▼
┌──────────────────────────────────────────────┐
│ Business Analyst Agent (Requirement Clarity) │
└──────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────┐
│ Project Manager Agent (Effort Estimation)    │
└──────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────┐
│ Risk Agent (AML / GDPR / SEC Risk Assessment)│
└──────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────┐
│ Priority Agent (Business Impact Scoring)     │
└──────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────┐
│ Decision Engine (Execution Recommendation)   │
└──────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────┐
│ Streamlit Dashboard (Visualization Layer)    │
└──────────────────────────────────────────────┘


                ┌──────────────────────┐
                │   Streamlit UI       │
                │ (Single / Portfolio) │
                └─────────┬────────────┘
                          │
                          ▼
                ┌──────────────────────┐
                │   Orchestrator       │
                │ (app.py controller)  │
                └─────────┬────────────┘
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼
┌────────────┐   ┌────────────┐   ┌────────────┐
│ BA Agent   │   │ PM Agent   │   │ Risk Agent │
└────┬───────┘   └────┬───────┘   └────┬───────┘
     │                │                │
     ▼                ▼                ▼
        ┌──────────────────────────────┐
        │ Knowledge Layer              │
        │ (Extensible for RAG)         │
        └──────────────┬───────────────┘
                       ▼
        ┌──────────────────────────────┐
        │ Decision Engine              │
        │ Priority + Effort            │
        └──────────────┬───────────────┘
                       ▼
        ┌──────────────────────────────┐
        │ Executive Dashboard          │
        │ Charts + Metrics             │
        └──────────────────────────────┘
```
## 6.1 Evaluation & Governance Layer (NEW — Production Enhancement)

To ensure this system is not just functional but **governed in a production-realistic manner**, an evaluation layer is introduced above all agent outputs.

This layer does NOT generate decisions — it evaluates the reliability of decisions produced by agents.

                    ┌──────────────────────────────┐
                    │ Evaluation & Governance Layer │
                    │ (Quality + Risk Validator)    │
                    └──────────────┬───────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
┌────────────────┐     ┌──────────────────┐     ┌────────────────────┐
│ Consistency     │     │ Risk Validator   │     │ Decision Drift     │
│ Checker         │     │ (AML/GDPR/SEC)   │     │ Detector           │
└────────────────┘     └──────────────────┘     └────────────────────┘

Evaluation Responsibilities
1. Consistency Checker
Detects contradiction between agent outputs
Flags unstable or conflicting reasoning chains
2. Risk Validator
Validates whether risk classification is complete
Ensures regulatory signals are not missed or underweighted
3. Decision Drift Detector
Tracks whether similar Jira inputs produce inconsistent outputs over time
Identifies instability in prioritisation logic
Why this layer matters

Without this layer:

system appears correct but may be internally inconsistent
agent outputs can drift without detection
prioritisation errors remain hidden

With this layer:

system becomes auditable
system becomes testable
system becomes governance-aligned

This transforms the system from “multi-agent pipeline” → “governed decision intelligence system”


---

## 7. Governance Design Principle (Critical)

This system is built on a key principle:

> AI structures decisions — it does NOT own decisions.

### Allowed:
- estimation
- classification
- risk detection
- prioritisation suggestion

### Not allowed:
- final approval of work
- enforcement of delivery timelines
- autonomous execution decisions

---

## 8. Critical Governance Insight (Production Learning)

During system design and testing, a key risk pattern was identified:

### 🔴 Agent Amplification Risk

Small biases in early-stage agents (e.g. requirement interpretation or effort estimation) can:
- propagate downstream
- amplify through prioritisation logic
- produce confident but skewed execution recommendations

### Why this matters:
The system may appear consistent and logical, while still producing **systematically distorted decisions**.

---

## 9. Mitigation Controls Introduced

To address this, the system includes:

### 1. Explicit disagreement handling
- conflicting agent outputs are preserved, not hidden

### 2. Confidence scoring per agent
- each output includes uncertainty signal

### 3. Human escalation trigger
- low-confidence or high-disagreement cases require review

---

## 10. Risk Classification

Key risks include:
- automation bias in decision-making
- hidden propagation of estimation errors
- over-reliance on AI prioritisation
- lack of decision accountability clarity
- regulatory misclassification of work items

---

## 11. Governance Framework Alignment

- NIST AI RMF (Govern, Map, Measure, Manage)
- SR 11-7 aligned model risk thinking
- EU AI Act high-level decision support principles
- ISO 42001 AI management concepts

---

## 12. AI Lifecycle Governance

### Inception
- defined as decision support system
- established human accountability boundary

### Design
- decomposed enterprise roles into agents
- structured workflow pipeline design

### Build
- constrained prompt design
- structured output enforcement

### Aggregation Layer
- weighted decision fusion
- conflict detection logic
- uncertainty flagging system

---

## 13. Evaluation & Testing

### Independent Testing
- ambiguous Jira tickets
- conflicting stakeholder requirements
- incomplete specifications
- adversarial or manipulated inputs

### Stress Testing Scenarios
- requirement inflation
- contradictory priorities
- missing acceptance criteria
- compliance-sensitive tickets

---

## 14. Explainability

Each output includes:
- agent-level reasoning trace
- confidence scoring
- risk classification rationale
- decision breakdown
- aggregation logic summary

---

## 15. Control Framework

| Control Type | Implementation |
|--------------|----------------|
| Preventive | structured prompts, schema constraints |
| Detective | logging, disagreement detection |
| Corrective | human-in-loop override |

---

## 16. Monitoring

- decision drift tracking
- agent consistency monitoring
- risk detection evaluation
- periodic recalibration of scoring logic

---

## 17. Human Accountability Model

Final responsibility always remains with:

> Engineering Lead / Delivery Manager

AI provides structured intelligence only — not authority.

---

## 18. Business Impact

- improved requirement clarity
- faster triage and prioritisation
- early detection of regulatory risks
- consistent effort estimation
- improved delivery transparency

---

## 19. Future Enhancements

- RAG-based regulatory knowledge grounding
- Jira API integration for live ingestion
- advanced portfolio analytics
- adaptive prioritisation learning layer

---

## 20. Tech Stack

- Python
- Streamlit
- Pandas
- LangChain
- LLMs (OpenAI / Ollama compatible)

---

## 21. Resume Positioning

This project demonstrates:

- multi-agent AI system design
- governed decision intelligence architecture
- FinTech + regulatory workflow understanding
- structured AI engineering thinking
- production-oriented AI governance mindset

---

## 22. Author

Navjot Perhar  
AI Systems | FinTech | Risk & Governance AI