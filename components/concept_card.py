import streamlit as st

from core.audience import adapt_text
from core.content import load_json
from core.session import navigate_to, push_nav
from core.theme import COLORS, LAYER_COLORS


def _concepts_by_id():
    return {c["id"]: c for c in load_json("concepts.json")}


def _relationship_chip(concept_id, by_id, key_prefix, row_label):
    target = by_id.get(concept_id)
    label = concept_id.replace("_", " ")
    # Key must be unique per row AND per concept: the same target concept_id can
    # legitimately appear in more than one relationship row on the same card
    # (e.g. both "feeds_into" and "related") and must not collide.
    safe_row = row_label.lower().replace(" ", "_")
    key = f"{key_prefix}_{safe_row}_{concept_id}"
    if target is None:
        st.markdown(
            f"<span style='display:inline-block;border:1px dashed {COLORS['border']};"
            f"color:{COLORS['text_mut']};border-radius:14px;padding:4px 12px;"
            f"font-size:0.8rem;margin:3px 4px 3px 0;'>{label} · coming soon</span>",
            unsafe_allow_html=True,
        )
        return
    if st.button(target["plain_name"], key=key):
        push_nav()
        navigate_to("concepts", concept_id=concept_id)
        st.rerun()


def _relationship_row(label, concept_ids, by_id, key_prefix):
    if not concept_ids:
        return
    cols = st.columns(len(concept_ids) + 1)
    with cols[0]:
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.8rem;padding-top:6px;'>{label}</div>",
            unsafe_allow_html=True,
        )
    for col, concept_id in zip(cols[1:], concept_ids):
        with col:
            _relationship_chip(concept_id, by_id, key_prefix, row_label=label)


def _find_scenario_appearances(concept_id):
    """Returns [(scenario, first_step_number)] for every scenario that touches
    this concept, anywhere in concepts_covered or any step's concepts_touched."""
    hits = []
    for scenario in load_json("scenarios.json"):
        if concept_id in scenario.get("concepts_covered", []):
            first_step = next(
                (s["step"] for s in scenario["steps"] if concept_id in s.get("concepts_touched", [])),
                1,
            )
            hits.append((scenario, first_step))
    return hits


def _find_comparison_appearances(concept_id):
    """Returns every comparison where one of the sides points at this concept."""
    hits = []
    for comparison in load_json("comparisons.json"):
        if any(side.get("concept_id") == concept_id for side in comparison["sides"]):
            hits.append(comparison)
    return hits


def _where_this_appears(concept_id, key_prefix):
    scenario_hits = _find_scenario_appearances(concept_id)
    comparison_hits = _find_comparison_appearances(concept_id)

    if not scenario_hits and not comparison_hits:
        return

    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:20px 0 8px 0;'>Where This Appears</div>",
        unsafe_allow_html=True,
    )

    if scenario_hits:
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.8rem;margin-bottom:4px;'>Scenarios</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(min(3, len(scenario_hits)))
        for i, (scenario, step) in enumerate(scenario_hits):
            with cols[i % len(cols)]:
                if st.button(scenario["title"], key=f"{key_prefix}_appears_scn_{scenario['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("scenarios", scenario_id=scenario["id"], scenario_step=step - 1)
                    st.rerun()

    if comparison_hits:
        st.markdown(
            f"<div style='color:{COLORS['text_mut']};font-size:0.8rem;margin:10px 0 4px 0;'>Comparisons</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(min(3, len(comparison_hits)))
        for i, comparison in enumerate(comparison_hits):
            with cols[i % len(cols)]:
                if st.button(comparison["title"], key=f"{key_prefix}_appears_cmp_{comparison['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("comparisons", comparison_id=comparison["id"])
                    st.rerun()


def concept_card(concept, audience=None, expanded=False):
    """Renders a single concept following the universal Concept Card Standard."""
    by_id = _concepts_by_id()
    layer_color = LAYER_COLORS.get(concept.get("layer"), COLORS["orange"])

    one_sentence = adapt_text(concept["one_sentence"], concept.get("one_sentence_variants"), audience)
    why_it_exists = adapt_text(concept["why_it_exists"], concept.get("why_it_exists_variants"), audience)
    what_it_does = adapt_text(concept["what_it_does"], concept.get("what_it_does_variants"), audience)

    st.markdown(
        f"""
        <div style='display:flex;align-items:center;gap:10px;margin-bottom:2px;'>
            <span style='display:inline-block;width:10px;height:10px;border-radius:50%;
                background:{layer_color};'></span>
            <span style='font-family:Space Grotesk,sans-serif;font-size:1.5rem;font-weight:700;
                color:{COLORS["text"]};'>{concept["plain_name"]}</span>
        </div>
        <div style='color:{COLORS["text_mut"]};font-family:JetBrains Mono,monospace;font-size:0.82rem;
            margin-left:20px;margin-bottom:10px;'>{concept["technical_name"]}</div>
        <hr style='margin:6px 0 14px 0;'>
        <p style='font-size:1rem;color:{COLORS["text_sec"]};'>{one_sentence}</p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:16px 0 4px 0;'>Why It Exists</div>"
        f"<p style='color:{COLORS['text']};font-size:0.95rem;'>{why_it_exists}</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:16px 0 4px 0;'>What It Does</div>"
        f"<p style='color:{COLORS['text']};font-size:0.95rem;'>{what_it_does}</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:16px 0 4px 0;'>Real Example</div>"
        f"<p style='color:{COLORS['text_sec']};font-size:0.92rem;font-style:italic;'>{concept['real_example']}</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:20px 0 8px 0;'>Relationships</div>",
        unsafe_allow_html=True,
    )
    rels = concept.get("relationships", {})
    calling_page = st.session_state.get("current_section", "unknown")
    key_prefix = f"{calling_page}_rel_{concept['id']}"
    _relationship_row("Created by", rels.get("created_by"), by_id, key_prefix)
    _relationship_row("Feeds into", rels.get("feeds_into"), by_id, key_prefix)
    _relationship_row("Governed by", rels.get("governed_by"), by_id, key_prefix)
    _relationship_row("Related", rels.get("related"), by_id, key_prefix)

    _where_this_appears(concept["id"], key_prefix)

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    with st.expander("▼ Technical Detail", expanded=expanded):
        st.markdown(concept.get("technical_depth", ""))

    st.markdown(
        f"<div style='color:{COLORS['text_mut']};font-size:0.82rem;margin-top:8px;'>"
        f"↗ Source: {concept.get('source_doc', '')}, {concept.get('source_section', '')}</div>",
        unsafe_allow_html=True,
    )
