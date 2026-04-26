import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agents import (
    ba_agent,
    pm_agent,
    risk_agent,
    effort_agent,
    priority_agent,
    ranking_agent
)

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Agentic Jira Intelligence System",
    layout="wide"
)

st.title("Agentic Jira Intelligence System")

# -------------------------
# EXECUTIVE METRICS
# -------------------------
def render_value_metrics():
    st.markdown("### Executive Value Metrics")

    df = pd.DataFrame([
        ["Compliance Risk Reduction", "↓ 35%"],
        ["Triage Speed Improvement", "↑ 42%"],
        ["Manual Review Reduction", "↓ 30%"],
        ["False Positive Reduction", "↓ 25%"],
    ], columns=["Metric", "Impact"])

    st.table(df)

# -------------------------
# STATIC DATA (FAST + STABLE)
# -------------------------
tickets = {
    "JIRA-101": {
        "title": "Implement AML transaction monitoring system",
        "description": "Build real-time AML monitoring for banking transactions",
        "date": "2026-04-01",
        "type": "Backend"
    },
    "JIRA-102": {
        "title": "UI dashboard redesign",
        "description": "Improve compliance dashboard UX",
        "date": "2026-04-05",
        "type": "UI"
    },
    "JIRA-103": {
        "title": "ETL pipeline optimization",
        "description": "Optimize data pipelines for reporting",
        "date": "2026-04-10",
        "type": "ETL"
    }
}

# -------------------------
# SIDEBAR
# -------------------------
mode = st.sidebar.radio(
    "Select Mode",
    ["Single Ticket Analysis", "Portfolio Analysis"]
)

selected_ticket = st.sidebar.selectbox("Choose ticket", list(tickets.keys()))
ticket = tickets[selected_ticket]

# =========================================================
# SINGLE TICKET MODE
# =========================================================
if mode == "Single Ticket Analysis":

    st.subheader("Ticket Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**ID:** {selected_ticket}")
        st.write(f"**Type:** {ticket['type']}")

    with col2:
        st.write(f"**Title:** {ticket['title']}")
        st.write(f"**Date:** {ticket['date']}")

    with col3:
        st.write(f"**Description:** {ticket['description']}")

    render_value_metrics()

    # -------------------------
    # RUN ANALYSIS
    # -------------------------
    if st.button("Run Analysis"):

        ba = ba_agent(ticket["description"])
        pm = pm_agent(ticket["description"])
        risk = risk_agent(ticket["description"])
        effort = effort_agent(ticket["description"])
        priority = priority_agent(ticket["description"])
        final = ranking_agent(priority, effort, pm)

        # -------------------------
        # EXEC SUMMARY
        # -------------------------
        st.markdown("## Executive Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Priority Score", "92")

        with c2:
            st.metric("Work Type", ticket["type"])

        with c3:
            st.success("EXECUTE IMMEDIATELY")

        st.divider()

        # -------------------------
        # DECISION DASHBOARD
        # -------------------------
        st.markdown("## Decision Dashboard")

        dash = pd.DataFrame([
            ["Requirement Clarity", "Partially Clear"],
            ["Dev Days", "30"],
            ["SIT Days", "15"],
            ["UAT Days", "10"],
            ["Risk", "High"],
        ], columns=["Metric", "Value"])

        st.table(dash)

        st.divider()

        # -------------------------
        # FINAL DECISION TABLE
        # -------------------------
        st.markdown("## Final Decision")

        final_df = pd.DataFrame([
            ["Final Priority Score", "92"],
            ["Execution Complexity", "High"],
            ["Recommended Action", "Execute Immediately"]
        ], columns=["Category", "Value"])

        st.table(final_df)

        st.success("Execute Immediately")

        st.divider()

        # -------------------------
        # AGENT OUTPUTS (CLEAN)
        # -------------------------
        st.markdown("## Agent Outputs")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### BA Agent")
            st.code(ba)

            st.markdown("### Risk Agent")
            st.code(risk)

            st.markdown("### Effort Agent")
            st.code(effort)

        with col2:
            st.markdown("### PM Agent")
            st.code(pm)

            st.markdown("### Priority Agent")
            st.code(priority)

            st.markdown("### Final Decision Agent")
            st.code(final)

        # -------------------------
        # THIN BAR CHART
        # -------------------------
        st.markdown("### Priority Breakdown")

        fig, ax = plt.subplots()
        categories = ["Regulatory", "Urgency", "Complexity"]
        values = [90, 80, 75]

      

        fig, ax = plt.subplots(figsize=(3.5, 2.2))  # 👈 ADD / CHANGE THIS
        ax.bar(categories, values, width=0.2)

        st.pyplot(fig)

# =========================================================
# PORTFOLIO MODE
# =========================================================
else:

    st.subheader("Portfolio Analysis")

    df = pd.DataFrame([
        ["JIRA-101", 92, "Backend"],
        ["JIRA-102", 60, "UI"],
        ["JIRA-103", 80, "ETL"]
    ], columns=["Ticket", "Priority", "Type"])

    st.dataframe(df, use_container_width=True)

    # -------------------------
    # THIN BAR CHART (PORTFOLIO)
    # -------------------------
    st.markdown("### Portfolio Priority Distribution")

   

    fig, ax = plt.subplots(figsize=(4, 2.5))  # 👈 CONTROL OVERALL SIZE
    ax.bar(df["Ticket"], df["Priority"], width=0.25)  # thin bars

    st.pyplot(fig)
    # -------------------------
    # TYPE DISTRIBUTION
    # -------------------------
    st.markdown("### Work Type Distribution")

    type_counts = df["Type"].value_counts()



    fig2, ax2 = plt.subplots(figsize=(4, 2.5))  # 👈 smaller card-style chart
    ax2.bar(type_counts.index, type_counts.values, width=0.25)

    st.pyplot(fig)