# agents.py

# FAST, DETERMINISTIC AGENTS (NO LLM, NO DEPENDENCIES)

# -------------------------
# BA AGENT
# -------------------------
def ba_agent(ticket):
    return """Requirement Status: Partially Clear

Missing Info:
1. Data sources unclear
2. Threshold rules not defined
3. Monitoring frequency not specified

Clarification Questions:
1. What AML thresholds apply?
2. Which jurisdictions are covered?
"""


# -------------------------
# PM AGENT
# -------------------------
def pm_agent(ticket):
    return """Dev Days: 30
SIT Days: 15
UAT Days: 10
Go Live Estimate: 2026-06-01

SDLC Breakdown:

Requirements Analysis:
Days: 5
Reason: Scope clarity

Design & Architecture:
Days: 5
Reason: System design

Development:
Days: 20
Reason: Core backend build

SIT:
Days: 15
Reason: Integration testing

UAT:
Days: 10
Reason: Business validation
"""


# -------------------------
# RISK AGENT
# -------------------------
def risk_agent(ticket):
    return """AML Risk: High
GDPR Risk: Medium
SEC Risk: Low
"""


# -------------------------
# EFFORT AGENT
# -------------------------
def effort_agent(ticket):
    return """Category: Backend
Reason: Core transaction monitoring system
"""


# -------------------------
# PRIORITY AGENT
# -------------------------
def priority_agent(ticket):
    return """Score: 85
Regulatory Impact: 90
Urgency: 80
Complexity: 75
"""


# -------------------------
# FINAL DECISION
# -------------------------
def ranking_agent(priority, effort, pm):
    return """Final Priority Score: 92
Execution Complexity: High
Recommended Action: Execute Immediately

Reason:
1. High regulatory impact
2. Critical compliance dependency
"""