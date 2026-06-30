import streamlit as st

from core.content import load_json
from core.session import navigate_to, push_nav
from core.theme import COLORS


def _side(col, side, key_prefix):
    by_id = {c["id"]: c for c in load_json("concepts.json")}
    concept_id = side.get("concept_id")
    target = by_id.get(concept_id)

    with col:
        st.markdown(
            f"""
            <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
                border-radius:10px;padding:18px;min-height:380px;'>
                <div style='font-weight:700;font-size:1.1rem;'>{side["plain_name"]}</div>
                <div style='color:{COLORS["text_mut"]};font-family:JetBrains Mono,monospace;
                    font-size:0.78rem;margin-bottom:10px;'>{side["technical_name"]}</div>
                <div style='color:{COLORS["orange"]};font-size:0.72rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.05em;margin-top:10px;'>Role In System</div>
                <p style='font-size:0.88rem;color:{COLORS["text_sec"]};'>{side["role_in_system"]}</p>
                <div style='color:{COLORS["orange"]};font-size:0.72rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.05em;margin-top:10px;'>Key Property</div>
                <p style='font-size:0.88rem;color:{COLORS["text_sec"]};'>{side["key_property"]}</p>
                <div style='color:{COLORS["orange"]};font-size:0.72rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.05em;margin-top:10px;'>What It Is Not</div>
                <p style='font-size:0.88rem;color:{COLORS["text_sec"]};'>{side["what_it_is_not"]}</p>
                <div style='color:{COLORS["orange"]};font-size:0.72rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.05em;margin-top:10px;'>Analogy</div>
                <p style='font-size:0.88rem;color:{COLORS["text_sec"]};font-style:italic;'>{side["analogy"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if target is not None:
            if st.button(f"Open {side['plain_name']} →", key=f"{key_prefix}_{concept_id}", use_container_width=True):
                push_nav()
                navigate_to("concepts", concept_id=concept_id)
                st.rerun()
        else:
            st.button(
                "Coming soon",
                key=f"{key_prefix}_{concept_id}_disabled",
                use_container_width=True,
                disabled=True,
            )


def comparison_card(comparison):
    st.session_state["comparison_id"] = comparison["id"]
    st.markdown(
        f"<h3 style='margin-bottom:2px;'>{comparison['title']}</h3>"
        f"<p style='color:{COLORS['text_sec']};font-size:0.95rem;'>{comparison['question']}</p>",
        unsafe_allow_html=True,
    )

    calling_page = st.session_state.get("current_section", "unknown")
    sides = comparison["sides"]
    cols = st.columns(len(sides))
    for i, (col, side) in enumerate(zip(cols, sides)):
        _side(col, side, key_prefix=f"{calling_page}_cmp_{comparison['id']}_{i}")

    st.markdown(
        f"""
        <div style='background:{COLORS["surface_raised"]};border:1px solid {COLORS["border"]};
            border-radius:10px;padding:16px 20px;margin-top:16px;'>
            <div style='color:{COLORS["orange"]};font-size:0.78rem;font-weight:600;
                text-transform:uppercase;letter-spacing:0.06em;margin-bottom:6px;'>The Key Difference</div>
            <p style='color:{COLORS["text"]};font-size:0.95rem;'>{comparison['the_key_difference']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
