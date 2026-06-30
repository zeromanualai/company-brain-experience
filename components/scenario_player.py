import streamlit as st

from components.scenario_visuals import get_visual
from core.session import navigate_to, push_nav
from core.theme import COLORS


def _step_dots(steps, current_index):
    dots_html = ""
    for i in range(len(steps)):
        color = COLORS["orange"] if i == current_index else COLORS["border"]
        size = "10px" if i == current_index else "8px"
        dots_html += (
            f"<span style='display:inline-block;width:{size};height:{size};"
            f"border-radius:50%;background:{color};margin:0 4px;'></span>"
        )
    st.markdown(f"<div style='text-align:center;margin-bottom:14px;'>{dots_html}</div>", unsafe_allow_html=True)


def _concept_chips(concepts_touched, key_prefix):
    if not concepts_touched:
        return
    st.markdown(
        f"<div style='color:{COLORS['text_mut']};font-size:0.78rem;text-transform:uppercase;"
        f"letter-spacing:0.06em;margin:14px 0 6px 0;'>Concepts touched</div>",
        unsafe_allow_html=True,
    )
    cols = st.columns(len(concepts_touched))
    for i, (col, concept_id) in enumerate(zip(cols, concepts_touched)):
        with col:
            label = concept_id.replace("_", " ")
            # Position index guards against the (unexpected) case of the same
            # concept_id appearing twice in one step's concepts_touched list.
            if st.button(label, key=f"{key_prefix}_{i}_{concept_id}", use_container_width=True):
                push_nav()
                navigate_to("concepts", concept_id=concept_id)
                st.rerun()


def scenario_player(scenario):
    steps = scenario["steps"]
    current_index = st.session_state.get("scenario_step", 0)
    current_index = max(0, min(current_index, len(steps) - 1))
    step = steps[current_index]

    _step_dots(steps, current_index)

    layer_color = step.get("layer_color", COLORS["orange"])
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <span style='background:{layer_color}22;color:{layer_color};border:1px solid {layer_color};
                border-radius:20px;padding:4px 14px;font-size:0.8rem;font-weight:600;'>
                {step["layer"]}
            </span>
        </div>
        <h2 style='text-align:center;margin-top:14px;'>Step {step["step"]}: {step["title"]}</h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style='max-width:760px;margin:0 auto;background:{COLORS["surface"]};
            border:1px solid {COLORS["border"]};border-radius:10px;padding:20px 24px;'>
            <p style='font-size:1.02rem;color:{COLORS["text"]};line-height:1.7;'>{step["narrative"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    visual = get_visual(scenario["id"], step["step"])
    if visual:
        st.markdown(
            f"<div style='margin:18px 0;'>{visual}</div>",
            unsafe_allow_html=True,
        )

    calling_page = st.session_state.get("current_section", "unknown")
    _concept_chips(step.get("concepts_touched"), key_prefix=f"{calling_page}_scn_{scenario['id']}_{current_index}")

    with st.expander("▼ Technical Detail"):
        st.markdown(step.get("technical_detail", ""))

    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

    col_prev, col_mid, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("← Previous", disabled=current_index == 0, use_container_width=True):
            st.session_state["scenario_step"] = current_index - 1
            st.rerun()
    with col_mid:
        st.markdown(
            f"<div style='text-align:center;color:{COLORS['text_mut']};padding-top:6px;'>"
            f"Step {current_index + 1} of {len(steps)}</div>",
            unsafe_allow_html=True,
        )
    with col_next:
        if st.button("Next →", disabled=current_index == len(steps) - 1, use_container_width=True, type="primary"):
            st.session_state["scenario_step"] = current_index + 1
            st.rerun()
