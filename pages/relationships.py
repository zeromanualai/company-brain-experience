import streamlit as st

from components.breadcrumb import render_nav
from components.flow_diagram import EDGE_TYPE_LABELS, node_jump_list, relationship_graph
from components.layout import page_shell
from core.content import load_json
from core.theme import COLORS


def render():
    page_shell("Relationships", "Why everything is connected — explore the concept graph.")
    render_nav()

    data = load_json("relationships.json")
    all_layers = sorted({n["layer"] for n in data["nodes"]})
    all_types = list(EDGE_TYPE_LABELS.keys())

    col1, col2 = st.columns(2)
    with col1:
        layer_filter = st.multiselect(
            "Filter by architecture layer",
            options=all_layers,
            default=[],
            placeholder="All layers",
        )
    with col2:
        type_filter = st.multiselect(
            "Filter by relationship type",
            options=all_types,
            format_func=lambda t: EDGE_TYPE_LABELS.get(t, t),
            default=[],
            placeholder="All relationship types",
        )

    st.markdown(
        f"<div style='color:{COLORS['text_mut']};font-size:0.82rem;margin-top:4px;'>"
        f"{len(data['nodes'])} concepts, {len(data['edges'])} relationships total. "
        f"Dashed/disabled nodes are referenced but not yet built as concept cards.</div>",
        unsafe_allow_html=True,
    )

    with st.spinner("Rendering relationship graph..."):
        visible_nodes, visible_edges = relationship_graph(
            data,
            layer_filter=layer_filter or None,
            type_filter=type_filter or None,
        )

    node_jump_list(visible_nodes, key_prefix="relgraph")
