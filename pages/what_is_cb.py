import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from core.audience import adapt_text
from core.content import load_json
from core.session import navigate_to
from core.theme import COLORS


def render():
    page_shell("What Is Company Brain?", "One clear mental model — before any architecture.")
    render_nav()

    data = load_json("what_is_cb.json")

    st.markdown(
        f"""
        <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
            border-radius:10px;padding:24px;text-align:center;'>
            <p style='font-size:1.25rem;font-weight:600;color:{COLORS["text"]};'>
                {data["one_sentence"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style='max-width:700px;margin:0 auto;text-align:center;'>
            <p style='font-size:1.1rem;font-weight:600;color:{COLORS["orange"]};'>
                {data["mental_model_title"]}
            </p>
            <p style='font-size:1rem;color:{COLORS["text_sec"]};line-height:1.7;'>
                {data["mental_model_paragraph"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # Simple flow visual: information flowing in -> understood -> stored -> used
    flow_steps = [
        ("👁️", "Watches"),
        ("🧩", "Understands"),
        ("🗄️", "Remembers"),
        ("🤔", "Reasons"),
        ("📬", "Delivers"),
    ]
    cols = st.columns(len(flow_steps))
    for col, (icon, label) in zip(cols, flow_steps):
        with col:
            st.markdown(
                f"""
                <div style='text-align:center;background:{COLORS["surface_raised"]};
                    border:1px solid {COLORS["border"]};border-radius:8px;padding:14px 4px;'>
                    <div style='font-size:1.5rem;'>{icon}</div>
                    <div style='font-size:0.85rem;color:{COLORS["text_sec"]};margin-top:4px;'>{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    variant = adapt_text(None, data.get("audience_variants"))
    if variant:
        st.markdown(
            f"""
            <div style='text-align:center;color:{COLORS["text_mut"]};font-size:0.9rem;
                font-style:italic;'>{variant}</div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        if st.button("Continue → The Big Picture", use_container_width=True, type="primary"):
            navigate_to("big_picture")
            st.rerun()
