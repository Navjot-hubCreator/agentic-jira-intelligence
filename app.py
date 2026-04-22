import streamlit as st
import pandas as pd
import plotly.express as px
import re

from agents import (
    ba_agent,
    pm_agent,
    risk_agent,
    effort_agent,
    priority_agent,
    ranking_agent,
)

from data import jira_data

st.set_page_config(layout="wide")
st.title("Agentic Jira Intelligence System")

mode = st.radio(
    "Select Mode",
    ["Single Ticket Analysis", "Portfolio Analysis"]
)

# -------------------------
# HELPERS
# -------------------------
def extract_number(pattern, text, default=0):
    match = re.search(pattern, text)
    return int(match.group(1)) if match else default


def extract_text(pattern, text, default="N/A"):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else default


# -------------------------
# SINGLE TICKET
# -------------------------
if mode == "Single Ticket Analysis":

    ticket_id = st.selectbox("Choose ticket", [t["id"] for t in jira_data])
    ticket = next(t for t in jira_data if t["id"] == ticket_id)

    st.subheader("Ticket Details")
    st.markdown(f"""
    **Title:** {ticket['title']}  
    **Description:** {ticket['description']}  
    **Type:** {ticket['type']}  
    **Date:** {ticket['date']}
    """)

    ticket_text = f"""
    Title: {ticket['title']}
    Description: {ticket['description']}
    Type: {ticket['type']}
    Date: {ticket['date']}
    """

    if st.button("Run Analysis"):

        ba = ba_agent(ticket_text)
        pm = pm_agent(ticket_text)
        risk = risk_agent(ticket_text)
        effort = effort_agent(ticket_text)
        priority = priority_agent(ticket_text)
        ranking = ranking_agent(priority, effort, pm)

        # -------------------------
        # EXTRACT
        # -------------------------
        dev_days = extract_number(r"Dev Days[: ]+(\d+)", pm)
        sit_days = extract_number(r"SIT Days[: ]+(\d+)", pm)
        uat_days = extract_number(r"UAT Days[: ]+(\d+)", pm)

        priority_score = extract_number(r"Score[: ]+(\d+)", priority)
        if priority_score == 0:
            priority_score = extract_number(r"FINAL SCORE[: ]+(\d+)", priority)

        aml_risk = extract_text(r"AML Risk[: ]+(\w+)", risk)
        gdpr_risk = extract_text(r"GDPR Risk[: ]+(\w+)", risk)
        sec_risk = extract_text(r"SEC Risk[: ]+(\w+)", risk)

        decision = extract_text(r"Recommended Action[: ]+(.+)", ranking)
        complexity = extract_text(r"Execution Complexity[: ]+(.+)", ranking)

        clarity = extract_text(r"Requirement Status[: ]+(.+)", ba)

        # -------------------------
        # EXECUTIVE SUMMARY
        # -------------------------
        st.subheader("Executive Summary")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Priority Score", f"{priority_score}/100")
        c2.metric("Work Type", ticket["type"].capitalize())
        c3.metric("Risk", aml_risk)
        c4.metric("Decision", decision)

        # -------------------------
        # FINAL DECISION (CLEAN)
        # -------------------------
        st.subheader("Final Decision")

        st.markdown(f"""
**Priority Score:** {priority_score}  
**Execution Complexity:** {complexity}  
""")

        st.success(f"Recommended Action: {decision}")

        # -------------------------
        # DASHBOARD
        # -------------------------
        st.subheader("Decision Dashboard")

        df_dashboard = pd.DataFrame({
            "Metric": ["Requirement Clarity", "Dev Days", "SIT Days", "UAT Days", "Risk"],
            "Value": [clarity, dev_days, sit_days, uat_days, aml_risk]
        })

        st.table(df_dashboard)

        # -------------------------
        # VISUALS
        # -------------------------
        st.subheader("Visual Insights")

        col1, col2, col3 = st.columns(3)

        fig1 = px.scatter(
            x=[dev_days],
            y=[priority_score],
            labels={"x": "Dev Effort (Days)", "y": "Priority"},
            title="Priority vs Effort"
        )
        fig1.update_layout(height=250)
        col1.plotly_chart(fig1, use_container_width=True)

        fig2 = px.bar(
            x=["Dev", "SIT", "UAT"],
            y=[dev_days, sit_days, uat_days],
            title="Timeline"
        )
        fig2.update_layout(height=250)
        col2.plotly_chart(fig2, use_container_width=True)

        fig3 = px.bar(
            x=["AML", "GDPR", "SEC"],
            y=[
                {"Low":1,"Medium":2,"High":3}.get(aml_risk,1),
                {"Low":1,"Medium":2,"High":3}.get(gdpr_risk,1),
                {"Low":1,"Medium":2,"High":3}.get(sec_risk,1),
            ],
            title="Risk Overview"
        )
        fig3.update_layout(height=250)
        col3.plotly_chart(fig3, use_container_width=True)

        # -------------------------
        # AGENTS
        # -------------------------
        with st.expander("View Full Agent Outputs"):

            st.markdown("### BA Agent")

            df_ba = pd.DataFrame({
                "Requirement Status": [clarity],
                "Missing Info": [
                    "1. Real-time definition\n2. Transaction scope\n3. False positives\n4. Integration"
                ],
                "Questions": [
                    "1. Volume?\n2. Regulations?"
                ]
            })
            st.table(df_ba)

            # PM
            st.markdown("### PM Agent")
            c1, c2, c3 = st.columns(3)
            c1.metric("Dev Days", dev_days)
            c2.metric("SIT Days", sit_days)
            c3.metric("UAT Days", uat_days)

            # RISK (CLEAN ROWS)
            st.markdown("### Risk Agent")
            st.markdown(f"""
- AML Risk: {aml_risk}  
- GDPR Risk: {gdpr_risk}  
- SEC Risk: {sec_risk}
""")

            # EFFORT
            st.markdown("### Effort Agent")
            category = extract_text(r"Category[: ]+(.+)", effort)
            reason = extract_text(r"Reason[: ]+(.+)", effort)

            st.markdown(f"""
- Category: {category}  
- Reason: {reason}
""")

            # PRIORITY
            st.markdown("### Priority Agent")
            reg = extract_number(r"Regulatory Impact[: ]+(\d+)", priority)
            urg = extract_number(r"Urgency[: ]+(\d+)", priority)
            comp = extract_number(r"Complexity[: ]+(\d+)", priority)

            st.markdown(f"""
- Score: {priority_score}  
- Regulatory Impact: {reg}  
- Urgency: {urg}  
- Complexity: {comp}
""")

            # FINAL
            st.markdown("### Final Decision")
            st.markdown(f"""
- Priority Score: {priority_score}  
- Execution Complexity: {complexity}  
""")
            st.success(f"Recommended Action: {decision}")


# -------------------------
# PORTFOLIO
# -------------------------
else:

    st.subheader("Portfolio Analysis")

    results = []

    for t in jira_data:
        text = f"{t['title']} {t['description']}"
        p = priority_agent(text)
        score = extract_number(r"Score[: ]+(\d+)", p)

        results.append({
            "Ticket": t["id"],
            "Priority": score,
            "Type": t["type"]
        })

    df = pd.DataFrame(results)

    # CLEAN TABLE (HEADERS + COMPACT)
    st.table(df)

    # BETTER CHART
    fig = px.bar(
        df,
        x="Ticket",
        y="Priority",
        color="Type",
        title="Portfolio Priority Distribution"
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)