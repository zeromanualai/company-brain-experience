import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from components.search_results import search_results
from core.session import clear_nav


def render():
    page_shell("Search", "Not keyword search — concept search. Every result is a doorway in.")
    render_nav()

    query = st.text_input(
        "Search",
        value=st.session_state.get("search_query", ""),
        placeholder="Try 'commitment', 'drift', 'trust'...",
        label_visibility="collapsed",
    )
    st.session_state["search_query"] = query

    # Deleting search text back to empty clears the nav trail — but only when the
    # user actually cleared it on this page, not just because search starts empty.
    prev_query = st.session_state.get("_prev_search_query", "")
    if prev_query and not query.strip():
        clear_nav()
    st.session_state["_prev_search_query"] = query

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    search_results(query)
