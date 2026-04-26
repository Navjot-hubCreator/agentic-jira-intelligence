# Agentic Jira Intelligence System
AI-powered multi-agent system for Jira intelligence, risk assessment, and execution decisioning in FinTech environments.
> 
An AI-powered multi-agent system that analyzes Jira tickets to improve requirement clarity, estimate delivery effort, assess regulatory risk, and drive data-driven execution decisions.

## Key Value Proposition

This project simulates a real-world **AI-powered delivery organization**, where multiple specialized agents collaborate to transform unstructured Jira tickets into **structured, decision-ready insights**.

It demonstrates how AI can:
- Replace manual triage workflows
- Standardize effort estimation and prioritization
- Surface regulatory risks early in the lifecycle
- Enable leadership-level decision-making through structured outputs
---

## Overview

This project demonstrates how agent-based AI systems can enhance software delivery workflows by transforming unstructured Jira tickets into structured, decision-ready outputs.

The system uses multiple specialized agents to simulate roles typically performed by Business Analysts, Project Managers, Risk Analysts, and Delivery Leads.

## Real-World Relevance

This system is directly applicable to enterprise roles such as:

- AI Product Manager
- AI Delivery Lead
- Risk & Compliance Technology Analyst
- FinTech / RegTech Architect

It demonstrates the ability to:
- Design multi-agent AI systems
- Translate business workflows into AI pipelines
- Build decision intelligence dashboards
- Bridge engineering, risk, and product functions
---

## Problem Statement

In most organizations:

- Jira tickets are often incomplete or ambiguous
- Effort estimation is manual and inconsistent
- Regulatory and compliance risks are identified late
- Prioritization lacks structured decision logic

This results in delivery delays, increased risk exposure, and inefficient triage processes.

---

## Solution

The Agentic Jira Intelligence System introduces a multi-agent architecture that:

- Evaluates requirement clarity
- Estimates SDLC effort
- Assesses compliance risks (AML, GDPR, SEC)
- Scores priority based on business impact
- Produces a final execution decision

All outputs are presented through a structured dashboard designed for both engineers and leadership stakeholders.

---

## System Architecture


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
## Agent Responsibilities

### Business Analyst Agent
- Determines requirement clarity
- Identifies missing information
- Generates clarification questions

### Project Manager Agent
- Provides SDLC effort estimation
- Breaks down development lifecycle stages
- Outputs delivery timeline

### Risk Agent
- Evaluates regulatory risks across:
  - AML (Anti-Money Laundering)
  - GDPR (Data Privacy)
  - SEC (Financial Compliance)

### Effort Agent
- Classifies type of engineering work
- Provides reasoning for categorization

### Priority Agent
- Calculates priority score based on:
  - Regulatory impact
  - Urgency
  - Complexity

### Decision Engine
- Aggregates all agent outputs
- Determines:
  - Final priority score
  - Execution complexity
  - Recommended action

---

## Features

### Single Ticket Analysis
- Executive summary
- Requirement clarity assessment
- Effort estimation
- Risk classification
- Final execution recommendation

### Portfolio Analysis
- Multi-ticket prioritization
- Portfolio-level visibility
- Comparative decision support

### Decision Dashboard
- Structured metrics for leadership
- Clear separation of risk, effort, and priority
- Readable output for non-technical stakeholders

---

## Business Impact

This system demonstrates measurable improvements in delivery workflows:

- Reduces compliance risk through early-stage detection
- Improves triage speed by standardizing analysis
- Enhances requirement quality before development
- Enables consistent, data-driven prioritization
- Bridges communication between business, engineering, and risk teams

---

## Visual Insights

The dashboard includes:

- Priority vs Effort analysis
- Delivery timeline breakdown
- Risk classification overview

These visualizations support faster decision-making at both team and portfolio levels.

---

## Tech Stack

- Python
- Streamlit
- Pandas
- LangChain
- LLM (Ollama or OpenAI-compatible models)

---

## Installation and Setup

### 1. Clone the repository
git clone https://github.com/Navjot-hubCreator/agentic-jira-intelligence.git

cd agentic-jira-intelligence


### 2. Create virtual environment


python -m venv venv
source venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Run the application


streamlit run app.py


---

## Usage

1. Select analysis mode:
   - Single Ticket Analysis
   - Portfolio Analysis

2. Choose a Jira ticket

3. Run AI agents

4. Review:
   - Executive summary
   - Decision dashboard
   - Agent outputs

---

## Example Use Case

A banking organization implements this system to:

- Analyze AML-related development tickets
- Identify regulatory risks early
- Estimate effort more accurately
- Prioritize critical compliance work

Result:
- Improved regulatory readiness
- Reduced rework
- Faster delivery cycles

---
## Key Design Decisions

- Used a modular multi-agent architecture to mirror real enterprise workflows
- Prioritized structured outputs over free-form LLM responses for consistency
- Avoided RAG in the current version to ensure speed and stability
- Designed stateless agents for simplicity and scalability
- Focused UI on executive readability, not just technical output

These decisions ensure:
- Faster execution
- Easier debugging
- Better real-world adoption potential

---
## Future Enhancements

- Retrieval-Augmented Generation (RAG) for regulatory knowledge grounding
- Integration with Jira APIs for real-time ticket ingestion
- AI-driven backlog prioritization
- Voice-based requirement walkthrough for developers
- Advanced portfolio analytics

---

## Limitations

- Relies on prompt-based LLM outputs
- No persistent data storage
- Does not integrate with live Jira systems (yet)
- Risk scoring is heuristic-based

---

## Resume Impact

This project demonstrates:

- End-to-end AI system design
- Multi-agent orchestration
- Business + technical alignment
- Real-world FinTech / Risk use case

Positioning statement:

Built an AI-powered multi-agent system for Jira intelligence, enabling risk-aware prioritization and structured delivery decision-making

## Author

Navjot Perhar  
AI and Risk Systems | FinTech | Regulatory Technology

---


