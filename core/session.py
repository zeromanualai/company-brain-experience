import streamlit as st

DEFAULTS = {
    "audience": None,
    "current_section": "home",
    "prev_section": None,
    "concept_id": None,
    "scenario_id": "customer_meeting",
    "scenario_step": 0,
    "comparison_id": None,
    "search_query": "",
    "concepts_viewed": [],
    "nav_history": [],
    "_prev_search_query": "",
}

MAX_NAV_DEPTH = 10

SECTION_LABELS = {
    "home": "Home",
    "problem": "The Problem",
    "what_is_cb": "What Is It?",
    "big_picture": "The Big Picture",
    "reality_pipeline": "How It Works",
    "concepts": "Concepts",
    "scenarios": "Scenarios",
    "comparisons": "Compare",
    "relationships": "Relationships",
    "documents": "Source Documents",
    "search": "Search",
}

# Fields that make up a full navigable state snapshot.
_SNAPSHOT_FIELDS = [
    "current_section",
    "concept_id",
    "scenario_id",
    "scenario_step",
    "comparison_id",
    "search_query",
]


def init_session():
    for key, value in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # Audience persists across reloads via the URL query param (?audience=...),
    # since session_state itself does not survive a hard page refresh.
    if not st.session_state.get("audience"):
        audience_param = st.query_params.get("audience")
        if audience_param:
            st.session_state["audience"] = audience_param


def navigate_to(section_id, **kwargs):
    st.session_state["prev_section"] = st.session_state.get("current_section")
    st.session_state["current_section"] = section_id
    for key, value in kwargs.items():
        st.session_state[key] = value
    if section_id == "home":
        clear_nav()


def mark_concept_viewed(concept_id):
    """Tracks distinct concepts viewed, with the list ordered by recency — the
    last element is always the most recently viewed concept, used to power the
    home page's 'Continue where you left off' card."""
    viewed = st.session_state["concepts_viewed"]
    if concept_id in viewed:
        viewed.remove(concept_id)
    viewed.append(concept_id)


def _snapshot(label):
    snap = {field: st.session_state.get(field) for field in _SNAPSHOT_FIELDS}
    snap["section"] = snap.pop("current_section")
    snap["label"] = label
    return snap


def _identity(snap):
    """The subset of a snapshot that defines 'the same place' for dedup purposes."""
    return (
        snap["section"],
        snap["concept_id"],
        snap["scenario_id"],
        snap["scenario_step"],
        snap["comparison_id"],
        snap["search_query"],
    )


def compute_current_label():
    """Builds a human label for wherever the user currently is, used both as the
    default push_nav() label and as the non-clickable final breadcrumb segment."""
    from core.content import load_json

    section = st.session_state.get("current_section")

    if section == "concepts":
        concept_id = st.session_state.get("concept_id")
        if concept_id:
            match = next((c for c in load_json("concepts.json") if c["id"] == concept_id), None)
            if match:
                return match["plain_name"]
        return "Concepts"

    if section == "scenarios":
        scenario_id = st.session_state.get("scenario_id")
        match = next((s for s in load_json("scenarios.json") if s["id"] == scenario_id), None)
        step = st.session_state.get("scenario_step", 0)
        if match:
            return f"{match['title']} — Step {step + 1}"
        return "Scenarios"

    if section == "reality_pipeline":
        step = st.session_state.get("scenario_step", 0)
        return f"The Reality Pipeline — Step {step + 1}"

    if section == "comparisons":
        comparison_id = st.session_state.get("comparison_id")
        match = next((c for c in load_json("comparisons.json") if c["id"] == comparison_id), None)
        return match["title"] if match else "Compare"

    if section == "search":
        query = st.session_state.get("search_query", "")
        return f"Search: {query}" if query else "Search"

    return SECTION_LABELS.get(section, section or "Home")


def push_nav(label=None):
    """Snapshots the current state and pushes it onto the history stack, to be
    called BEFORE changing state for any 'drill-in' navigation (concept chips,
    search results, comparison opens, etc). Skips duplicate consecutive entries
    and caps the stack at MAX_NAV_DEPTH, dropping the oldest entry first."""
    if label is None:
        label = compute_current_label()

    snap = _snapshot(label)
    history = st.session_state.get("nav_history", [])

    if history and _identity(history[-1]) == _identity(snap):
        return

    history = history + [snap]
    if len(history) > MAX_NAV_DEPTH:
        history = history[-MAX_NAV_DEPTH:]
    st.session_state["nav_history"] = history


def pop_nav():
    """Pops the most recent history entry and fully restores state from it."""
    history = st.session_state.get("nav_history", [])
    if not history:
        return
    snap = history[-1]
    st.session_state["nav_history"] = history[:-1]
    _restore_snapshot(snap)


def restore_nav(index):
    """Restores state from a specific (non-terminal) history entry — used when a
    breadcrumb segment is clicked. Entries at and after `index` are dropped, since
    the user has just jumped back to that point in the trail."""
    history = st.session_state.get("nav_history", [])
    if index < 0 or index >= len(history):
        return
    snap = history[index]
    st.session_state["nav_history"] = history[:index]
    _restore_snapshot(snap)


def _restore_snapshot(snap):
    st.session_state["prev_section"] = st.session_state.get("current_section")
    st.session_state["current_section"] = snap["section"]
    st.session_state["concept_id"] = snap["concept_id"]
    st.session_state["scenario_id"] = snap["scenario_id"]
    st.session_state["scenario_step"] = snap["scenario_step"]
    st.session_state["comparison_id"] = snap["comparison_id"]
    st.session_state["search_query"] = snap["search_query"]


def clear_nav():
    st.session_state["nav_history"] = []


def reset_progress():
    """Clears explored-concepts tracking and the nav trail, returning to a
    fresh-session state without touching audience or other preferences."""
    st.session_state["concepts_viewed"] = []
    clear_nav()
    st.session_state["current_section"] = "home"
