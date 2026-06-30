import streamlit as st

from components.breadcrumb import render_nav
from components.comparison_card import comparison_card
from components.layout import page_shell
from core.content import load_json


def render():
    page_shell("Compare", "The questions everyone gets confused by, answered side by side.")
    render_nav()

    comparisons = load_json("comparisons.json")
    ids = [c["id"] for c in comparisons]
    titles = [c["title"] for c in comparisons]

    current_id = st.session_state.get("comparison_id") or ids[0]
    if current_id not in ids:
        current_id = ids[0]
    default_index = ids.index(current_id)

    # Key includes current_id so the widget remounts and picks up index= correctly
    # when comparison_id changes from elsewhere (e.g. a breadcrumb/Back restore) —
    # Streamlit otherwise ignores `index=` on reruns once a widget key exists.
    selected_title = st.selectbox(
        "Choose a comparison",
        options=titles,
        index=default_index,
        label_visibility="collapsed",
        key=f"comparison_selectbox_{current_id}",
    )
    chosen_id = ids[titles.index(selected_title)]
    st.session_state["comparison_id"] = chosen_id

    comparison = next(c for c in comparisons if c["id"] == chosen_id)
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    comparison_card(comparison)
