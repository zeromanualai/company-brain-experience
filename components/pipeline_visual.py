import streamlit as st

from core.session import navigate_to, push_nav
from core.theme import LAYER_COLORS, COLORS


def _layer_button(layer, key_prefix):
    color = LAYER_COLORS.get(layer["name"], COLORS["orange"])
    st.markdown(
        f"""
        <div style='border-left:4px solid {color};background:{COLORS["surface_raised"]};
            border-radius:6px;padding:10px 14px;margin-bottom:6px;'>
            <div style='font-weight:600;color:{COLORS["text"]};'>{layer["name"]}</div>
            <div style='font-size:0.82rem;color:{COLORS["text_sec"]};'>{layer["one_sentence"]}</div>
            <div style='font-size:0.75rem;color:{COLORS["text_mut"]};font-style:italic;margin-top:2px;'>
                {layer["key_question"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Explore this layer →", key=f"{key_prefix}_{layer['id']}", use_container_width=True):
        push_nav()
        navigate_to("concepts", concept_id=layer["id"])
        st.rerun()


def pipeline_visual(data, audience_caption=None):
    """Renders the interactive seven-layer architecture pipeline with a Trust boundary."""
    st.markdown(
        f"<div style='text-align:center;color:{COLORS['text_sec']};font-size:0.95rem;"
        f"margin-bottom:6px;'>Organizational Reality</div>"
        f"<div style='text-align:center;color:{COLORS['text_mut']};margin-bottom:10px;'>↓</div>",
        unsafe_allow_html=True,
    )

    trust = data["trust"]
    st.markdown(
        f"""
        <div style='border:2px solid {COLORS["trust"]};border-radius:14px;padding:18px 18px 6px 18px;'>
            <div style='text-align:center;color:{COLORS["trust"]};font-weight:700;
                letter-spacing:0.08em;font-size:0.8rem;text-transform:uppercase;margin-bottom:10px;'>
                {trust["name"]} — {trust["one_sentence"]}
            </div>
        """,
        unsafe_allow_html=True,
    )

    calling_page = st.session_state.get("current_section", "unknown")
    layers = data["layers"]
    for i, layer in enumerate(layers):
        _layer_button(layer, key_prefix=f"{calling_page}_pipeline")
        if i < len(layers) - 1:
            st.markdown(
                f"<div style='text-align:center;color:{COLORS['text_mut']};margin:2px 0;'>↓</div>",
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"<div style='text-align:center;color:{COLORS['text_mut']};margin:10px 0;'>↓</div>",
        unsafe_allow_html=True,
    )

    products = data["products"]
    cols = st.columns(len(products))
    for col, product in zip(cols, products):
        with col:
            if st.button(product["name"], key=f"{calling_page}_pipeline_product_{product['id']}", use_container_width=True):
                push_nav()
                navigate_to("concepts", concept_id=product["id"])
                st.rerun()

    if audience_caption:
        st.markdown(
            f"<div style='text-align:center;color:{COLORS['text_mut']};font-size:0.9rem;"
            f"font-style:italic;margin-top:14px;'>{audience_caption}</div>",
            unsafe_allow_html=True,
        )
