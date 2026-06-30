import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from components.scenario_player import scenario_player
from core.audience import adapt_text, get_audience
from core.content import load_json
from core.theme import COLORS


def render():
    page_shell(
        "The Reality Pipeline",
        "How one real event becomes memory, intelligence, and action — the centrepiece of the experience.",
    )
    render_nav()

    intro_variant = adapt_text(None, load_json("page_intros.json").get("reality_pipeline"))
    if get_audience() and intro_variant:
        st.markdown(
            f"<div style='text-align:center;color:{COLORS['text_mut']};font-size:0.88rem;"
            f"font-style:italic;margin-bottom:14px;'>{intro_variant}</div>",
            unsafe_allow_html=True,
        )

    scenarios = load_json("scenarios.json")
    scenario = next(s for s in scenarios if s["id"] == "customer_meeting")
    scenario_player(scenario)
