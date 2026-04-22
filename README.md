# Agentic Jira Intelligence System

An AI-powered multi-agent system that analyzes Jira tickets to improve requirement clarity, estimate delivery effort, assess regulatory risk, and drive data-driven execution decisions.

---

## Overview

This project demonstrates how agent-based AI systems can enhance software delivery workflows by transforming unstructured Jira tickets into structured, decision-ready outputs.

The system uses multiple specialized agents to simulate roles typically performed by Business Analysts, Project Managers, Risk Analysts, and Delivery Leads.

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



Jira Ticket Input
|
v
Business Analyst Agent (Requirement Clarity)
|
v
Project Manager Agent (Effort Estimation)
|
v
Risk Agent (AML / GDPR / SEC Risk Assessment)
|
v
Priority Agent (Business Impact Scoring)
|
v
Decision Engine (Execution Recommendation)
|
v
Streamlit Dashboard (Visualization Layer)


---

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

## Author

Navjot Perhar  
AI and Risk Systems | FinTech | Regulatory Technology

---

## License

This project is for demonstration and educational purposes.
