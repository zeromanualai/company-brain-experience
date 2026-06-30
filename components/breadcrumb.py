import streamlit as st

from core.session import SECTION_LABELS, compute_current_label, navigate_to, pop_nav, restore_nav
from core.theme import COLORS


def _build_segments():
    """Flattens [Home, ...history entries..., current page] into a list of
    {"text", "history_index"} segments. history_index is None for non-clickable
    segments (Home is handled separately; the current page is always terminal)."""
    history = st.session_state.get("nav_history", [])
    segments = []
    last_section = None

    for idx, entry in enumerate(history):
        section = entry.get("section")
        section_text = SECTION_LABELS.get(section, section or "")
        if section != last_section:
            segments.append({"text": section_text, "history_index": idx})
            last_section = section
        label = entry.get("label") or ""
        # Skip a label segment that just repeats the section header we already
        # emitted (e.g. landing on the bare "Concepts" browser with no concept
        # selected — its label and section name are both "Concepts").
        if label != section_text:
            for part in [p.strip() for p in label.split(" — ") if p.strip()]:
                segments.append({"text": part, "history_index": idx})

    current_section = st.session_state.get("current_section")
    current_section_text = SECTION_LABELS.get(current_section, current_section or "")
    if current_section != last_section:
        segments.append({"text": current_section_text, "history_index": None})

    current_label = compute_current_label()
    if current_label != current_section_text:
        for part in [p.strip() for p in current_label.split(" — ") if p.strip()]:
            segments.append({"text": part, "history_index": None})

    return segments


def render_back_button():
    history = st.session_state.get("nav_history", [])
    if not history:
        return
    if st.button("← Back", key=f"{st.session_state.get('current_section', 'unknown')}_nav_back"):
        pop_nav()
        st.rerun()


def render_breadcrumb():
    history = st.session_state.get("nav_history", [])
    calling_page = st.session_state.get("current_section", "unknown")

    if not history:
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.85rem;"
            f"font-family:JetBrains Mono,monospace;margin-bottom:12px;'>Home</div>",
            unsafe_allow_html=True,
        )
        return

    segments = _build_segments()

    truncated = len(segments) > 5
    display = ([{"text": "...", "history_index": None, "ellipsis": True}] + segments[-3:]) if truncated else segments

    # Equal-width, container-filling segments (same pattern as concept chips
    # elsewhere in the app) — proportional widths based on text length leave
    # visible dead space in each column since Streamlit allocates the full
    # row width per the ratio, regardless of how short the label is.
    cols = st.columns(len(display) + 1)

    with cols[0]:
        if st.button("Home", key=f"{calling_page}_breadcrumb_home", use_container_width=True):
            navigate_to("home")
            st.rerun()

    for i, seg in enumerate(display):
        with cols[i + 1]:
            prefix = "› "
            text = prefix + seg["text"]
            if seg.get("ellipsis") or seg["history_index"] is None:
                st.markdown(
                    f"<div style='color:{COLORS['text_mut']};font-size:0.85rem;"
                    f"font-family:JetBrains Mono,monospace;white-space:nowrap;overflow:hidden;"
                    f"text-overflow:ellipsis;border:1px solid transparent;border-radius:6px;"
                    f"padding:8px 4px;display:flex;align-items:center;height:38px;"
                    f"box-sizing:border-box;'>{text}</div>",
                    unsafe_allow_html=True,
                )
            else:
                if st.button(text, key=f"{calling_page}_breadcrumb_{i}_{seg['history_index']}", use_container_width=True):
                    restore_nav(seg["history_index"])
                    st.rerun()


def render_nav():
    """Call at the top of every page except home: renders the Back button and
    breadcrumb trail, in that order, beneath the page title."""
    render_back_button()
    render_breadcrumb()
