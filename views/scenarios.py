import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from components.scenario_player import scenario_player
from core.content import load_json
from core.theme import COLORS


def render():
    page_shell("Scenarios", "Real situations, explained through the architecture.")
    render_nav()

    scenarios = load_json("scenarios.json")
    ids = [s["id"] for s in scenarios]

    current_id = st.session_state.get("scenario_id", ids[0])
    if current_id not in ids:
        current_id = ids[0]

    cols = st.columns(len(scenarios))
    for col, scenario in zip(cols, scenarios):
        with col:
            is_active = scenario["id"] == current_id
            if st.button(
                scenario["title"],
                key=f"scenario_select_{scenario['id']}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state["scenario_id"] = scenario["id"]
                st.session_state["scenario_step"] = 0
                st.rerun()

    scenario = next(s for s in scenarios if s["id"] == current_id)
    st.markdown(
        f"<p style='color:{COLORS['text_sec']};font-size:0.95rem;margin-top:14px;'>{scenario['description']}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    scenario_player(scenario)
