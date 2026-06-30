NAV = [
    {"id": "home", "label": "🧠  Company Brain Experience", "is_title": True},
    {"id": "problem", "label": "The Problem"},
    {"id": "what_is_cb", "label": "What Is It?"},
    {"id": "big_picture", "label": "The Big Picture"},
    {"id": "reality_pipeline", "label": "How It Works"},
    {"divider": True},
    {"id": "concepts", "label": "Concepts"},
    {"id": "scenarios", "label": "Scenarios"},
    {"id": "comparisons", "label": "Compare"},
    {"id": "relationships", "label": "Relationships"},
    {"divider": True},
    {"id": "documents", "label": "Source Documents"},
    {"id": "search", "label": "Search"},
]

# Phase 1 only implements these. Anything else falls back to a placeholder.
IMPLEMENTED_PAGES = {
    "home",
    "problem",
    "what_is_cb",
    "big_picture",
    "reality_pipeline",
    "documents",
    "concepts",
    "scenarios",
    "comparisons",
    "relationships",
    "search",
}


def render_page(section_id):
    """Dynamically import and render the page module for section_id."""
    import importlib

    import streamlit as st

    if section_id not in IMPLEMENTED_PAGES:
        st.info(f"'{section_id}' is not yet built. Coming in a later phase.")
        return

    module = importlib.import_module(f"views.{section_id}")
    module.render()
