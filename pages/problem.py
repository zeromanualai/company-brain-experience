import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from core.audience import adapt_text
from core.content import load_json
from core.session import navigate_to
from core.theme import COLORS


def render():
    page_shell(
        "The Problem",
        "Before any architecture — what actually breaks inside an organization.",
    )
    render_nav()

    stories = load_json("problem_stories.json")

    cols = st.columns(2)
    for i, story in enumerate(stories):
        with cols[i % 2]:
            variant = adapt_text(story["narrative"], story.get("audience_variants"))
            st.markdown(
                f"""
                <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
                    border-radius:10px;padding:20px;margin-bottom:16px;min-height:240px;'>
                    <div style='font-size:1.6rem;'>{story["icon"]}</div>
                    <div style='font-weight:700;font-size:1.1rem;margin-top:6px;'>{story["title"]}</div>
                    <div style='color:{COLORS["orange"]};font-size:0.95rem;font-weight:600;margin-top:4px;'>
                        {story["headline"]}
                    </div>
                    <p style='color:{COLORS["text_sec"]};font-size:0.9rem;margin-top:10px;'>{variant}</p>
                    <p style='color:{COLORS["text_mut"]};font-size:0.82rem;font-style:italic;margin-top:8px;'>
                        {story["cost"]}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style='text-align:center;padding:28px 0;'>
            <p style='font-size:1.25rem;font-weight:600;color:{COLORS["text"]};'>
                This is organizational amnesia.
            </p>
            <p style='font-size:1.1rem;color:{COLORS["text_sec"]};'>
                Every organization has it. Company Brain is the cure.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        if st.button("Continue → What Is Company Brain?", use_container_width=True, type="primary"):
            navigate_to("what_is_cb")
            st.rerun()
