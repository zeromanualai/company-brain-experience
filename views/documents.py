from pathlib import Path

import streamlit as st

from components.breadcrumb import render_nav
from components.layout import page_shell
from core.audience import adapt_text, get_audience
from core.content import load_json
from core.theme import COLORS

_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"


def render():
    page_shell(
        "Source Documents",
        "The canonical architecture documents — a reference, not a prerequisite.",
    )
    render_nav()

    intro_variant = adapt_text(None, load_json("page_intros.json").get("documents"))
    if get_audience() and intro_variant:
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.88rem;"
            f"font-style:italic;margin-bottom:16px;'>{intro_variant}</div>",
            unsafe_allow_html=True,
        )

    documents = load_json("documents.json")

    for doc in documents:
        st.markdown(
            f"""
            <div style='background:{COLORS["surface"]};border:1px solid {COLORS["border"]};
                border-radius:10px;padding:18px 22px;margin-bottom:14px;'>
                <div style='display:flex;justify-content:space-between;align-items:baseline;'>
                    <span style='font-weight:700;font-size:1.05rem;'>{doc["title"]}</span>
                    <span style='color:{COLORS["text_mut"]};font-family:JetBrains Mono,monospace;
                        font-size:0.8rem;'>{doc["version"]}</span>
                </div>
                <div style='color:{COLORS["text_mut"]};font-size:0.78rem;margin-top:2px;'>{doc["status"]}</div>
                <p style='color:{COLORS["text_sec"]};font-size:0.92rem;margin-top:10px;'>{doc["one_sentence"]}</p>
                <p style='color:{COLORS["text_mut"]};font-size:0.85rem;font-style:italic;margin-top:8px;'>
                    Read this if: {doc["read_this_if"]}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander(f"What {doc['title']} defines"):
            for item in doc["what_it_defines"]:
                st.markdown(f"- {item}")

            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            file_path = _DOCS_DIR / doc["filename"]
            if file_path.exists():
                with st.expander("↗ Open full document text"):
                    st.markdown(file_path.read_text(encoding="utf-8"))
