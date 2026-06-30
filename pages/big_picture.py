from components.breadcrumb import render_nav
from components.layout import page_shell
from components.pipeline_visual import pipeline_visual
from core.audience import adapt_text
from core.content import load_json


def render():
    page_shell("The Big Picture", "One view of the entire system, before any detail.")
    render_nav()

    data = load_json("pipeline_layers.json")
    caption = adapt_text(None, data.get("audience_captions"))
    pipeline_visual(data, audience_caption=caption)
