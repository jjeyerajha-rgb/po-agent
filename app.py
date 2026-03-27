import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st

from agents import (
    StoryWriterAgent,
    BacklogManagerAgent,
    AcceptanceCriteriaAgent,
    SprintPlannerAgent,
    ReleaseNotesAgent,
    StakeholderCommsAgent,
    MeetingPrepAgent,
)
from utils.export import to_markdown, get_download_filename

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="PO Agent - Product Owner Assistant",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------------------
st.markdown(
    """
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white;
    }
    .main-header h1 { color: white; margin: 0; }
    .main-header p  { color: rgba(255,255,255,.85); margin: .5rem 0 0; }

    .feature-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: box-shadow .2s;
    }
    .feature-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,.1); }

    .stTextArea textarea { border-radius: 8px; }
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        padding: .5rem 2rem;
    }

    .result-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-top: 1rem;
    }

    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
    }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🎯 PO Agent")
    st.caption("Your AI Product Owner Assistant")
    st.divider()

    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key. It stays in your session only.",
    )
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.session_state.api_key_set = True

    model = st.selectbox(
        "Model",
        ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"],
        help="Choose the LLM model to use",
    )
    os.environ["OPENAI_MODEL"] = model

    st.divider()
    st.markdown("### Capabilities")

    PAGES = {
        "🏠 Dashboard": "dashboard",
        "📝 Story Writer": "story_writer",
        "📋 Backlog Prioritizer": "backlog_manager",
        "✅ Acceptance Criteria": "acceptance_criteria",
        "🏃 Sprint Planner": "sprint_planner",
        "📦 Release Notes": "release_notes",
        "💬 Stakeholder Comms": "stakeholder_comms",
        "📅 Meeting Prep": "meeting_prep",
        "🕘 History": "history",
    }
    selected = st.radio("Navigate", list(PAGES.keys()), label_visibility="collapsed")
    page = PAGES[selected]

    st.divider()
    st.caption("Built with Streamlit + OpenAI")


# ---------------------------------------------------------------------------
# Helper to run an agent and store results
# ---------------------------------------------------------------------------
def run_agent(agent_cls, label: str, **kwargs: str) -> str | None:
    if not st.session_state.api_key_set and not os.getenv("OPENAI_API_KEY"):
        st.error("Please enter your OpenAI API key in the sidebar to continue.")
        return None
    agent = agent_cls()
    with st.spinner(f"{agent.icon} {agent.name} is working..."):
        try:
            result = agent.run(**kwargs)
        except Exception as exc:
            st.error(f"Error: {exc}")
            return None
    st.session_state.history.append(
        {"agent": agent.name, "label": label, "result": result}
    )
    return result


def show_result(result: str, title: str) -> None:
    st.markdown("---")
    st.subheader("Result")
    st.markdown(result)

    md = to_markdown(title, result)
    fname = get_download_filename(title.lower().replace(" ", "_"))
    st.download_button(
        "Download as Markdown",
        data=md,
        file_name=fname,
        mime="text/markdown",
    )


# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------

# ---- Dashboard -----------------------------------------------------------
if page == "dashboard":
    st.markdown(
        """
    <div class="main-header">
        <h1>🎯 Product Owner Agent</h1>
        <p>Your AI-powered assistant for day-to-day Product Owner tasks.
        Focus on strategy and decisions — let the agent handle the rest.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    features = [
        (
            "📝",
            "User Story Writer",
            "Generate INVEST-compliant user stories with acceptance criteria, story points, and dependencies.",
        ),
        (
            "📋",
            "Backlog Prioritizer",
            "Prioritize items using MoSCoW, WSJF, RICE, or Value-vs-Effort frameworks.",
        ),
        (
            "✅",
            "Acceptance Criteria",
            "Create comprehensive Given/When/Then scenarios covering happy paths, edge cases, and errors.",
        ),
        (
            "🏃",
            "Sprint Planner",
            "Plan sprints with balanced goals, capacity planning, and risk identification.",
        ),
        (
            "📦",
            "Release Notes",
            "Generate audience-tailored release notes and changelogs.",
        ),
        (
            "💬",
            "Stakeholder Comms",
            "Draft status updates, executive summaries, and tailored communications.",
        ),
        (
            "📅",
            "Meeting Prep",
            "Prepare agendas, talking points, and materials for any ceremony or meeting.",
        ),
        (
            "🔄",
            "Session History",
            "All generated outputs are saved in your session for easy reference.",
        ),
        (
            "⬇️",
            "Export & Download",
            "Download any result as a Markdown file for sharing or archiving.",
        ),
    ]
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 3]:
            st.markdown(
                f"""<div class="feature-card">
                <h3>{icon} {title}</h3>
                <p>{desc}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    st.info(
        "👈 Select a capability from the sidebar to get started. "
        "Make sure to enter your OpenAI API key first!"
    )

# ---- Story Writer --------------------------------------------------------
elif page == "story_writer":
    st.header("📝 User Story Writer")
    st.caption(
        "Generate well-structured user stories following INVEST principles"
    )

    with st.form("story_form"):
        context = st.text_area(
            "Product / Feature Context",
            placeholder="e.g. E-commerce platform, mobile banking app, SaaS dashboard...",
            height=80,
        )
        requirements = st.text_area(
            "Requirements / Idea *",
            placeholder="Describe what you want to build or the problem you want to solve...",
            height=150,
        )
        col1, col2 = st.columns(2)
        with col1:
            personas = st.text_input(
                "Target Persona(s)",
                placeholder="e.g. Online shopper, Admin user, API consumer",
            )
        with col2:
            notes = st.text_input(
                "Additional Notes",
                placeholder="e.g. Must integrate with Stripe, needs i18n support",
            )
        submitted = st.form_submit_button("Generate User Stories", type="primary")

    if submitted and requirements:
        result = run_agent(
            StoryWriterAgent,
            f"Stories: {requirements[:50]}",
            context=context,
            requirements=requirements,
            personas=personas,
            notes=notes,
        )
        if result:
            show_result(result, "User Stories")

# ---- Backlog Prioritizer -------------------------------------------------
elif page == "backlog_manager":
    st.header("📋 Backlog Prioritizer")
    st.caption("Prioritize backlog items using proven frameworks")

    with st.form("backlog_form"):
        items = st.text_area(
            "Backlog Items *",
            placeholder="List your backlog items (one per line or as a structured list)...",
            height=200,
        )
        col1, col2 = st.columns(2)
        with col1:
            framework = st.selectbox(
                "Prioritization Framework",
                ["RICE", "MoSCoW", "WSJF", "Value vs. Effort"],
            )
            business_context = st.text_area(
                "Business Context",
                placeholder="Key business goals, upcoming deadlines, market context...",
                height=100,
            )
        with col2:
            capacity = st.text_input(
                "Sprint Capacity (story points)",
                placeholder="e.g. 40 story points",
            )
        submitted = st.form_submit_button("Prioritize Backlog", type="primary")

    if submitted and items:
        result = run_agent(
            BacklogManagerAgent,
            f"Backlog: {framework}",
            items=items,
            framework=framework,
            business_context=business_context,
            capacity=capacity,
        )
        if result:
            show_result(result, "Backlog Prioritization")

# ---- Acceptance Criteria --------------------------------------------------
elif page == "acceptance_criteria":
    st.header("✅ Acceptance Criteria Generator")
    st.caption("Generate comprehensive Given/When/Then acceptance criteria")

    with st.form("ac_form"):
        story = st.text_area(
            "User Story / Feature Description *",
            placeholder="Paste or describe the user story you need acceptance criteria for...",
            height=150,
        )
        context = st.text_area(
            "Feature Context",
            placeholder="Additional context about the feature, system, or domain...",
            height=80,
        )
        col1, col2 = st.columns(2)
        with col1:
            nfr = st.text_input(
                "Non-functional Requirements",
                placeholder="e.g. Page load < 2s, WCAG 2.1 AA compliant",
            )
        with col2:
            edge_cases = st.text_input(
                "Specific Edge Cases",
                placeholder="e.g. Empty cart, expired session, concurrent edits",
            )
        submitted = st.form_submit_button(
            "Generate Acceptance Criteria", type="primary"
        )

    if submitted and story:
        result = run_agent(
            AcceptanceCriteriaAgent,
            f"AC: {story[:50]}",
            story=story,
            context=context,
            nfr=nfr,
            edge_cases=edge_cases,
        )
        if result:
            show_result(result, "Acceptance Criteria")

# ---- Sprint Planner -------------------------------------------------------
elif page == "sprint_planner":
    st.header("🏃 Sprint Planner")
    st.caption("Plan your next sprint with goal setting and capacity planning")

    with st.form("sprint_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            duration = st.selectbox("Sprint Duration", ["2 weeks", "1 week", "3 weeks"])
        with col2:
            capacity = st.text_input(
                "Team Capacity (points)", placeholder="e.g. 40"
            )
        with col3:
            velocity = st.text_input(
                "Average Velocity", placeholder="e.g. 35"
            )

        goals = st.text_area(
            "Product Goals / Objectives",
            placeholder="What are the key goals for this sprint?",
            height=80,
        )
        backlog_items = st.text_area(
            "Available Backlog Items *",
            placeholder="List prioritized backlog items with estimates...",
            height=200,
        )
        col1, col2 = st.columns(2)
        with col1:
            carryover = st.text_area(
                "Carry-over Items",
                placeholder="Incomplete items from the previous sprint...",
                height=80,
            )
        with col2:
            risks = st.text_area(
                "Known Risks / Blockers",
                placeholder="Team absences, external dependencies, etc.",
                height=80,
            )
        submitted = st.form_submit_button("Plan Sprint", type="primary")

    if submitted and backlog_items:
        result = run_agent(
            SprintPlannerAgent,
            "Sprint Plan",
            duration=duration,
            capacity=capacity,
            velocity=velocity,
            goals=goals,
            backlog_items=backlog_items,
            carryover=carryover,
            risks=risks,
        )
        if result:
            show_result(result, "Sprint Plan")

# ---- Release Notes --------------------------------------------------------
elif page == "release_notes":
    st.header("📦 Release Notes Generator")
    st.caption("Generate professional release notes for any audience")

    with st.form("release_form"):
        col1, col2 = st.columns(2)
        with col1:
            version = st.text_input("Version", placeholder="e.g. v2.4.0")
            release_date = st.text_input("Release Date", placeholder="e.g. 2026-04-01")
        with col2:
            audience = st.selectbox(
                "Target Audience",
                ["End Users", "Stakeholders / Executives", "Developers / Technical"],
            )

        items = st.text_area(
            "Completed Items *",
            placeholder="List features, bug fixes, improvements delivered in this release...",
            height=200,
        )
        col1, col2 = st.columns(2)
        with col1:
            known_issues = st.text_area(
                "Known Issues",
                placeholder="Any known issues or limitations...",
                height=80,
            )
        with col2:
            context = st.text_area(
                "Additional Context",
                placeholder="Migration notes, breaking changes, etc.",
                height=80,
            )
        submitted = st.form_submit_button("Generate Release Notes", type="primary")

    if submitted and items:
        result = run_agent(
            ReleaseNotesAgent,
            f"Release {version}",
            version=version,
            release_date=release_date,
            audience=audience,
            items=items,
            known_issues=known_issues,
            context=context,
        )
        if result:
            show_result(result, "Release Notes")

# ---- Stakeholder Communications -------------------------------------------
elif page == "stakeholder_comms":
    st.header("💬 Stakeholder Communications")
    st.caption("Draft tailored communications for any audience")

    with st.form("comms_form"):
        col1, col2 = st.columns(2)
        with col1:
            comm_type = st.selectbox(
                "Communication Type",
                [
                    "Status Update",
                    "Executive Summary",
                    "Sprint Review Summary",
                    "Roadmap Update",
                    "Risk Escalation",
                    "Feature Announcement",
                    "Project Kickoff",
                    "Post-mortem Summary",
                ],
            )
            audience = st.text_input(
                "Target Audience",
                placeholder="e.g. C-suite, Engineering leads, Customer success team",
            )
        with col2:
            tone = st.selectbox(
                "Tone",
                ["Professional", "Formal", "Casual", "Urgent", "Celebratory"],
            )

        message = st.text_area(
            "Key Message / Content *",
            placeholder="What do you need to communicate? Include key points, metrics, decisions...",
            height=150,
        )
        context = st.text_area(
            "Project Context",
            placeholder="Background info the audience needs...",
            height=80,
        )
        data = st.text_area(
            "Supporting Data / Metrics",
            placeholder="KPIs, velocity, burndown data, customer feedback...",
            height=80,
        )
        submitted = st.form_submit_button("Draft Communication", type="primary")

    if submitted and message:
        result = run_agent(
            StakeholderCommsAgent,
            f"{comm_type}: {message[:40]}",
            comm_type=comm_type,
            audience=audience,
            message=message,
            context=context,
            data=data,
            tone=tone,
        )
        if result:
            show_result(result, comm_type)

# ---- Meeting Prep ---------------------------------------------------------
elif page == "meeting_prep":
    st.header("📅 Meeting Prep Assistant")
    st.caption("Prepare comprehensive materials for any meeting or ceremony")

    with st.form("meeting_form"):
        col1, col2 = st.columns(2)
        with col1:
            meeting_type = st.selectbox(
                "Meeting Type",
                [
                    "Sprint Planning",
                    "Sprint Review / Demo",
                    "Retrospective",
                    "Backlog Refinement / Grooming",
                    "Stakeholder Meeting",
                    "Product Strategy Session",
                    "Kick-off Meeting",
                    "One-on-One",
                    "Other",
                ],
            )
            duration = st.selectbox(
                "Duration",
                ["30 minutes", "60 minutes", "90 minutes", "2 hours", "Half day"],
            )
        with col2:
            attendees = st.text_input(
                "Attendees / Roles",
                placeholder="e.g. Dev team, Scrum Master, Stakeholders",
            )

        objectives = st.text_area(
            "Meeting Objectives *",
            placeholder="What do you want to accomplish in this meeting?",
            height=100,
        )
        context = st.text_area(
            "Context / Background",
            placeholder="Sprint progress, recent changes, relevant metrics...",
            height=100,
        )
        action_items = st.text_area(
            "Previous Action Items",
            placeholder="Outstanding items from previous meetings...",
            height=80,
        )
        submitted = st.form_submit_button("Prepare Meeting Materials", type="primary")

    if submitted and objectives:
        result = run_agent(
            MeetingPrepAgent,
            f"{meeting_type} Prep",
            meeting_type=meeting_type,
            attendees=attendees,
            duration=duration,
            objectives=objectives,
            context=context,
            action_items=action_items,
        )
        if result:
            show_result(result, f"{meeting_type} Preparation")

# ---- History --------------------------------------------------------------
elif page == "history":
    st.header("🕘 Session History")
    st.caption("All generated outputs from this session")

    if not st.session_state.history:
        st.info("No outputs generated yet. Try one of the capabilities from the sidebar!")
    else:
        for i, entry in enumerate(reversed(st.session_state.history)):
            with st.expander(
                f"{entry['agent']} — {entry['label']}", expanded=(i == 0)
            ):
                st.markdown(entry["result"])
                md = to_markdown(entry["label"], entry["result"])
                fname = get_download_filename(entry["label"].lower().replace(" ", "_"))
                st.download_button(
                    "Download",
                    data=md,
                    file_name=fname,
                    mime="text/markdown",
                    key=f"dl_{i}",
                )

        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
