import streamlit as st

from core.audience import adapt_text, get_audience, load_audiences, set_audience
from core.content import load_json
from core.session import clear_nav, navigate_to, reset_progress
from core.theme import COLORS


def render():
    intro_variant = adapt_text(None, load_json("page_intros.json").get("home"))
    if get_audience() and intro_variant:
        st.markdown(
            f"<div style='text-align:center;color:{COLORS['orange']};font-size:0.85rem;"
            f"font-style:italic;padding-top:8px;'>{intro_variant}</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style='text-align:center; padding: 40px 0 12px 0;'>
            <div style='font-size:3rem;'>🧠</div>
            <h1 style='font-size:2.4rem;margin-top:8px;'>Company Brain Experience</h1>
            <p style='color:{COLORS["text_sec"]};font-size:1.15rem;max-width:680px;
                margin:12px auto 0 auto;'>
                Your organization forgets constantly. Company Brain is the cure.
                This is a guided experience that builds the full mental model —
                starting from the problem, ending with complete understanding.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='text-align:center;color:{COLORS['text']};font-size:1.1rem;"
        f"font-weight:600;margin-bottom:18px;'>Who are you?</div>",
        unsafe_allow_html=True,
    )

    audiences = load_audiences()
    cols = st.columns(len(audiences))
    for col, audience in zip(cols, audiences):
        with col:
            st.markdown(
                f"""
                <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
                    border-radius:10px;padding:18px 14px;min-height:160px;text-align:center;'>
                    <div style='font-size:1.8rem;'>{audience["icon"]}</div>
                    <div style='font-weight:600;margin-top:8px;font-size:0.95rem;'>{audience["label"]}</div>
                    <div style='color:{COLORS["text_sec"]};font-size:0.82rem;margin-top:6px;'>{audience["description"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Choose", key=f"audience_choose_{audience['id']}", use_container_width=True):
                set_audience(audience["id"])
                clear_nav()
                navigate_to(audience.get("entry_section", "problem"))
                st.rerun()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<p style='text-align:center;color:{COLORS['text_mut']};font-size:0.85rem;'>"
        f"This is not a gate. You can change your audience at any time from the sidebar.</p>",
        unsafe_allow_html=True,
    )

    _render_continue_card()


def _render_continue_card():
    viewed = st.session_state.get("concepts_viewed", [])
    if not viewed:
        return

    concepts = load_json("concepts.json")
    by_id = {c["id"]: c for c in concepts}
    last_id = viewed[-1]
    last_concept = by_id.get(last_id)
    if not last_concept:
        return

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(
            f"""
            <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
                border-radius:10px;padding:18px 22px;text-align:center;'>
                <div style='color:{COLORS["orange"]};font-size:0.78rem;font-weight:600;
                    text-transform:uppercase;letter-spacing:0.06em;'>Continue Exploring</div>
                <p style='color:{COLORS["text_sec"]};font-size:0.9rem;margin-top:6px;'>
                    You've visited {len(viewed)} concept{"s" if len(viewed) != 1 else ""}.
                    Last viewed: <b style='color:{COLORS["text"]};'>{last_concept["plain_name"]}</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"Continue → {last_concept['plain_name']}", key="home_continue", use_container_width=True, type="primary"):
            clear_nav()
            navigate_to("concepts", concept_id=last_id)
            st.rerun()

        st.markdown(
            "<style>"
            "div[data-testid='stElementContainer']:has(.cb-reset-progress-anchor)"
            " + div[data-testid='stElementContainer'] button {"
            f"  background: transparent !important;"
            f"  border: none !important;"
            f"  color: {COLORS['text_sec']} !important;"
            f"  font-size: 0.78rem !important;"
            f"  padding: 4px 2px !important;"
            f"  box-shadow: none !important;"
            "}"
            "div[data-testid='stElementContainer']:has(.cb-reset-progress-anchor)"
            " + div[data-testid='stElementContainer'] button:hover {"
            f"  color: {COLORS['text']} !important;"
            "  text-decoration: underline;"
            "}"
            "</style>"
            "<div class='cb-reset-progress-anchor'></div>",
            unsafe_allow_html=True,
        )
        if st.button("↺ Reset progress", key="home_reset_progress"):
            reset_progress()
            if hasattr(st, "toast"):
                st.toast("Progress reset.")
            else:
                st.success("Progress reset.")
            st.rerun()
