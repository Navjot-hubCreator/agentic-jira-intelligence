from llm import get_llm

llm = get_llm()

BASE_RULES = """
You are an expert AI assistant for banking, risk, and regulatory systems.

STRICT RULES:
- Do NOT repeat ticket details
- Be structured
- Follow output format EXACTLY
- No extra text before or after
"""


# -------------------------
# BA AGENT
# -------------------------
def ba_agent(ticket):
    prompt = f"""
{BASE_RULES}

OUTPUT FORMAT:

Requirement Status: <Clear / Partially Clear / Unclear>

Missing Info:
- bullet points

Clarification Questions:
- bullet points

Ticket:
{ticket}
"""
    return llm.invoke(prompt)


# -------------------------
# PM AGENT (STRICT FORMAT)
# -------------------------
def pm_agent(ticket):
    prompt = f"""
{BASE_RULES}

OUTPUT FORMAT:

Dev Days: <number>
SIT Days: <number>
UAT Days: <number>
Go Live Estimate: <YYYY-MM-DD>

SDLC Breakdown:

Requirements Analysis:
Days: <number>
Reason: <short>

Design & Architecture:
Days: <number>
Reason: <short>

Development:
Days: <number>
Reason: <short>

SIT:
Days: <number>
Reason: <short>

UAT:
Days: <number>
Reason: <short>

Go Live Prep:
Days: <number>
Reason: <short>

Ticket:
{ticket}
"""
    return llm.invoke(prompt)


# -------------------------
# RISK AGENT
# -------------------------
def risk_agent(ticket):
    prompt = f"""
{BASE_RULES}

OUTPUT FORMAT:

AML Risk: <High / Medium / Low>
GDPR Risk: <High / Medium / Low>
SEC Risk: <High / Medium / Low>

Ticket:
{ticket}
"""
    return llm.invoke(prompt)


# -------------------------
# EFFORT AGENT
# -------------------------
def effort_agent(ticket):
    prompt = f"""
{BASE_RULES}

Choose ONLY ONE:

Backend / UI / ETL / Integration / DevOps

OUTPUT FORMAT:

Category: <one>
Reason: <1 line>

Ticket:
{ticket}
"""
    return llm.invoke(prompt)


# -------------------------
# PRIORITY AGENT
# -------------------------
def priority_agent(ticket):
    prompt = f"""
{BASE_RULES}

OUTPUT FORMAT:

Score: <0-100>
Regulatory Impact: <0-100>
Urgency: <0-100>
Complexity: <0-100>

Ticket:
{ticket}
"""
    return llm.invoke(prompt)


# -------------------------
# FINAL DECISION
# -------------------------
def ranking_agent(priority, effort, pm):
    prompt = f"""
{BASE_RULES}

OUTPUT FORMAT:

Final Priority Score: <0-100>
Execution Complexity: <Low / Medium / High>
Recommended Action: <Execute Immediately / Schedule / Defer>

Reason: <short>

INPUTS:
{priority}
{effort}
{pm}
"""
    return llm.invoke(prompt)