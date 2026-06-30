import streamlit as st

from components.breadcrumb import render_nav
from components.concept_card import concept_card
from components.layout import page_shell
from core.content import load_json
from core.session import clear_nav, mark_concept_viewed, navigate_to, push_nav
from core.theme import COLORS

CATEGORY_LABELS = {
    "architecture_layer": "Architecture Layers",
    "atomic_primitive": "Atomic Primitives",
    "memory_type": "Memory Types",
    "intelligence_output": "Intelligence Outputs",
    "trust_object": "Trust Objects",
    "product_mode": "Product Modes",
    "ontology_concept": "Ontology Concepts",
}


def _render_browser(concepts):
    page_shell("Concepts", "Every concept in the architecture — pick one to go deeper.")
    render_nav()

    by_category = {}
    for c in concepts:
        by_category.setdefault(c["category"], []).append(c)

    for category, label in CATEGORY_LABELS.items():
        items = by_category.get(category, [])
        if not items:
            continue
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.78rem;font-weight:600;"
            f"text-transform:uppercase;letter-spacing:0.06em;margin:20px 0 8px 0;'>{label}</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(3)
        for i, c in enumerate(items):
            with cols[i % 3]:
                if st.button(c["plain_name"], key=f"browse_{c['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("concepts", concept_id=c["id"])
                    st.rerun()


def render():
    concepts = load_json("concepts.json")
    concept_id = st.session_state.get("concept_id")
    by_id = {c["id"]: c for c in concepts}

    if not concept_id or concept_id not in by_id:
        _render_browser(concepts)
        return

    concept = by_id[concept_id]
    mark_concept_viewed(concept_id)
    page_shell(concept["plain_name"], None)
    render_nav()

    if st.button("← All Concepts"):
        clear_nav()
        navigate_to("concepts", concept_id=None)
        st.rerun()

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    concept_card(concept)
