import streamlit as st

from core.audience import get_audience, load_audiences, set_audience
from core.content import load_json
from core.router import NAV
from core.session import clear_nav, navigate_to
from core.theme import COLORS


def render_sidebar():
    with st.sidebar:
        current = st.session_state.get("current_section", "home")

        for item in NAV:
            if item.get("divider"):
                st.markdown("---")
                continue

            if item.get("is_title"):
                st.markdown(
                    f"<div style='font-family:Space Grotesk,sans-serif;"
                    f"font-size:1.05rem;font-weight:700;color:{COLORS['text']};"
                    f"padding:4px 0 12px 0;'>{item['label']}</div>",
                    unsafe_allow_html=True,
                )
                continue

            is_active = current == item["id"]
            label = item["label"]
            if st.button(
                label,
                key=f"nav_{item['id']}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                # Top-level sidebar nav is a fresh jump, not a drill-in — it
                # clears any in-progress chip/search/comparison trail rather
                # than pushing onto it.
                clear_nav()
                if item["id"] == "concepts":
                    navigate_to(item["id"], concept_id=None)
                else:
                    navigate_to(item["id"])
                st.rerun()

        st.markdown("---")
        _render_progress_indicator()
        _render_audience_selector()


def _render_progress_indicator():
    total = len(load_json("concepts.json"))
    viewed = len(st.session_state.get("concepts_viewed", []))
    pct = int(100 * viewed / total) if total else 0
    st.markdown(
        f"""
        <div style='margin-bottom:14px;'>
            <div style='display:flex;justify-content:space-between;color:{COLORS["text_mut"]};
                font-size:0.75rem;margin-bottom:4px;'>
                <span>EXPLORED</span><span>{viewed} / {total}</span>
            </div>
            <div style='background:{COLORS["border"]};border-radius:4px;height:5px;width:100%;'>
                <div style='background:{COLORS["orange"]};border-radius:4px;height:5px;width:{pct}%;'></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_audience_selector():
    st.markdown(
        f"<div style='font-size:0.75rem;color:{COLORS['text_sec']};"
        f"text-transform:uppercase;letter-spacing:0.05em;margin-bottom:6px;'>"
        f"Audience</div>",
        unsafe_allow_html=True,
    )
    audiences = load_audiences()
    current_audience = get_audience()
    labels = [a["icon"] + "  " + a["label"] for a in audiences]
    ids = [a["id"] for a in audiences]

    default_index = ids.index(current_audience) if current_audience in ids else 0
    # Key includes current_audience so the widget remounts (picking up the new
    # index) whenever audience changes from elsewhere, e.g. the home page cards —
    # Streamlit otherwise ignores `index=` on reruns once a widget key exists.
    choice = st.selectbox(
        "audience_select",
        options=range(len(audiences)),
        format_func=lambda i: labels[i],
        index=default_index,
        label_visibility="collapsed",
        key=f"audience_selectbox_{current_audience or 'none'}",
    )
    chosen_id = ids[choice]
    if chosen_id != current_audience:
        set_audience(chosen_id)
        st.rerun()


def page_shell(title, subtitle=None):
    """Renders a consistent page header. Call at the top of every page."""
    st.markdown(
        f"<h1 style='margin-bottom:0;'>{title}</h1>",
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            f"<p style='color:{COLORS['text_sec']};font-size:1.05rem;"
            f"margin-top:4px;'>{subtitle}</p>",
            unsafe_allow_html=True,
        )
    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)


def section_label(text):
    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.75rem;"
        f"font-weight:600;text-transform:uppercase;letter-spacing:0.08em;"
        f"margin:18px 0 6px 0;'>{text}</div>",
        unsafe_allow_html=True,
    )
