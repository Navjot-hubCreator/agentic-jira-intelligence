
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

---

## 7. Governance Design Principle

> AI structures decisions — it does NOT own decisions.

### Allowed:
- classification
- estimation
- risk detection
- prioritisation suggestion

### Not Allowed:
- final execution authority
- delivery commitment
- autonomous decision enforcement

---

## 8. Evaluation & Governance Control Layer (CORE SYSTEM SAFETY COMPONENT)

The system includes a dedicated **Evaluation & Governance Control Layer** that validates all agent outputs before they are consumed for decision-making.

This layer ensures the system is not just multi-agent, but **auditable, testable, and production-governed**.

---

### 8.1 Evaluation Layer Architecture
            ┌──────────────────────────────┐
            │ Evaluation & Governance Layer │
            └──────────────┬───────────────┘
                           │
    ┌──────────────────────┼──────────────────────┐
    ▼                      ▼                      ▼
    Consistency Checker Risk Completeness Validator Decision Drift Detector


---

### 8.2 Evaluation Responsibilities

#### 1. Consistency Checker
- detects contradictions across agent outputs
- flags conflicting reasoning chains
- prevents silent logic overwrites

---

#### 2. Risk Completeness Validator
- ensures AML / GDPR / SEC signals are not missed
- validates risk coverage completeness
- detects underweighted compliance risks

---

#### 3. Decision Drift Detector
- tracks consistency across similar Jira inputs
- detects instability in prioritisation logic
- identifies systemic model drift

---

### 8.3 Why This Layer is Critical

Without this layer:
- system may appear correct but be internally inconsistent
- hidden reasoning errors propagate downstream
- prioritisation decisions become unstable over time

With this layer:
- system becomes **auditable**
- system becomes **testable**
- system becomes **governance-grade**

---

## 9. Critical Production Insight

> In multi-agent systems, failure does NOT originate in one agent — it emerges from aggregation.

Key risk pattern:
- small upstream errors → amplify downstream
- prioritisation layer can over-trust weak signals
- system may appear logically consistent but be systematically biased

---

## 10. Mitigation Controls

- disagreement preservation (no forced override)
- confidence scoring per agent
- escalation triggers for low-confidence outputs
- human-in-loop override for high-risk tickets

---

## 11. Risk Classification

- automation bias in decision-making
- hidden estimation propagation errors
- prioritisation distortion risk
- regulatory misclassification risk
- lack of accountability clarity

---

## 12. Governance Framework Alignment

- NIST AI RMF (Govern / Map / Measure / Manage)
- SR 11-7 model risk principles
- EU AI Act high-risk decision support logic
- ISO 42001 AI management concepts

---

## 13. AI Lifecycle Governance

### Inception
- defined as decision support system
- human accountability explicitly assigned

### Design
- decomposed enterprise roles into agents
- structured workflow pipeline defined

### Build
- structured output constraints applied
- isolated agent reasoning chains

### Aggregation Layer
- weighted fusion logic
- conflict detection system
- uncertainty propagation flags

---

## 14. Evaluation & Stress Testing

### Scenarios Tested
- ambiguous Jira tickets
- conflicting stakeholder requirements
- incomplete specifications
- adversarial input manipulation
- compliance-heavy tickets

---

## 15. Explainability Layer

Each output includes:
- agent reasoning trace
- confidence score per agent
- risk classification rationale
- decision breakdown
- aggregation logic summary

---

## 16. Monitoring Framework

- decision drift tracking
- agent consistency monitoring
- risk detection recall measurement
- periodic recalibration of scoring logic

---

## 17. Human Accountability Model

Final accountability remains with:

> Engineering / Delivery Leadership

AI provides structured intelligence only.

---

## 18. Business Impact

- faster Jira triage
- improved requirement clarity
- earlier compliance detection
- consistent prioritisation logic
- improved portfolio visibility

---

## 19. Future Enhancements

- RAG-based regulatory grounding
- Jira API live integration
- adaptive prioritisation learning
- portfolio intelligence layer

---

## 20. Tech Stack

- Python
- Streamlit
- Pandas
- LangChain
- LLM APIs (OpenAI / Ollama)

---

## 21. Resume Positioning

This project demonstrates:

- multi-agent AI system design
- governed decision intelligence architecture
- FinTech risk-aware AI workflows
- production-grade AI governance thinking
- enterprise system design capability

---

## 22. Author

Navjot Perhar  
AI Systems | FinTech | Risk & Governance AI    