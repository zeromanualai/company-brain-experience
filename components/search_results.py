import streamlit as st

from core.content import load_json
from core.session import navigate_to, push_nav
from core.theme import COLORS


def _matches(text, query):
    return text and query.lower() in str(text).lower()


def search_concepts(query):
    hits = []
    for c in load_json("concepts.json"):
        haystack = " ".join(
            [
                c["plain_name"],
                c["technical_name"],
                c["one_sentence"],
                c["why_it_exists"],
                c["what_it_does"],
                c.get("technical_depth", ""),
            ]
        )
        if _matches(haystack, query):
            hits.append(c)
    return hits


def search_scenarios(query):
    hits = []
    for s in load_json("scenarios.json"):
        haystack = " ".join([s["title"], s["subtitle"], s["description"]])
        for step in s["steps"]:
            haystack += " " + step["title"] + " " + step["narrative"] + " " + " ".join(step.get("concepts_touched", []))
        if _matches(haystack, query):
            hits.append(s)
    return hits


def search_comparisons(query):
    hits = []
    for c in load_json("comparisons.json"):
        haystack = " ".join([c["title"], c["question"], c["the_key_difference"]])
        for side in c["sides"]:
            haystack += " " + side["plain_name"] + " " + side["technical_name"]
        if _matches(haystack, query):
            hits.append(c)
    return hits


def search_documents(query):
    hits = []
    for d in load_json("documents.json"):
        haystack = " ".join([d["title"], d["one_sentence"]] + d.get("key_concepts", []) + d.get("what_it_defines", []))
        if _matches(haystack, query):
            hits.append(d)
    return hits


def _group_header(label, count):
    st.markdown(
        f"<div style='color:{COLORS['orange']};font-size:0.78rem;font-weight:600;"
        f"text-transform:uppercase;letter-spacing:0.06em;margin:18px 0 8px 0;'>{label} ({count})</div>",
        unsafe_allow_html=True,
    )


def search_results(query):
    if not query or len(query.strip()) < 2:
        st.markdown(
            f"<p style='color:{COLORS['text_mut']};'>Type at least 2 characters to search "
            f"concepts, scenarios, comparisons, and source documents.</p>",
            unsafe_allow_html=True,
        )
        return

    concepts = search_concepts(query)
    scenarios = search_scenarios(query)
    comparisons = search_comparisons(query)
    documents = search_documents(query)
    total = len(concepts) + len(scenarios) + len(comparisons) + len(documents)

    if total == 0:
        st.markdown(
            f"<p style='color:{COLORS['text_mut']};'>No results for '<b>{query}</b>'. "
            f"Try a different term, or browse Concepts directly.</p>",
            unsafe_allow_html=True,
        )
        return

    st.markdown(
        f"<p style='color:{COLORS['text_sec']};font-size:0.9rem;'>{total} result(s) for '<b>{query}</b>'</p>",
        unsafe_allow_html=True,
    )

    if concepts:
        _group_header("Concepts", len(concepts))
        cols = st.columns(3)
        for i, c in enumerate(concepts):
            with cols[i % 3]:
                if st.button(c["plain_name"], key=f"search_concept_{c['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("concepts", concept_id=c["id"])
                    st.rerun()

    if scenarios:
        _group_header("Scenarios", len(scenarios))
        cols = st.columns(min(3, len(scenarios)))
        for i, s in enumerate(scenarios):
            with cols[i % len(cols)]:
                if st.button(s["title"], key=f"search_scenario_{s['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("scenarios", scenario_id=s["id"], scenario_step=0)
                    st.rerun()

    if comparisons:
        _group_header("Comparisons", len(comparisons))
        cols = st.columns(min(3, len(comparisons)))
        for i, c in enumerate(comparisons):
            with cols[i % len(cols)]:
                if st.button(c["title"], key=f"search_comparison_{c['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("comparisons", comparison_id=c["id"])
                    st.rerun()

    if documents:
        _group_header("Source Documents", len(documents))
        cols = st.columns(min(3, len(documents)))
        for i, d in enumerate(documents):
            with cols[i % len(cols)]:
                if st.button(d["title"], key=f"search_document_{d['id']}", use_container_width=True):
                    push_nav()
                    navigate_to("documents")
                    st.rerun()
