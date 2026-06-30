import math

import plotly.graph_objects as go
import streamlit as st

from core.session import navigate_to, push_nav
from core.theme import COLORS, LAYER_COLORS

EDGE_TYPE_LABELS = {
    "creates": "Creates",
    "feeds_into": "Feeds Into",
    "governed_by": "Governed By",
    "related_to": "Related To",
}


def _layout(nodes):
    """Deterministic circular layout, grouped by category so related concepts cluster together."""
    ordered = sorted(nodes, key=lambda n: (n["category"], n["id"]))
    n = len(ordered)
    positions = {}
    for i, node in enumerate(ordered):
        angle = 2 * math.pi * i / n
        positions[node["id"]] = (math.cos(angle), math.sin(angle))
    return positions


def relationship_graph(data, layer_filter=None, type_filter=None):
    """Renders the concept relationship graph. Returns nothing — selection happens via the
    button list rendered beneath the chart, which is more reliable across Streamlit/Plotly
    versions than relying on Plotly click-selection events for primary navigation."""
    all_nodes = data["nodes"]
    all_edges = data["edges"]

    visible_nodes = [n for n in all_nodes if not layer_filter or n["layer"] in layer_filter]
    visible_ids = {n["id"] for n in visible_nodes}
    visible_edges = [
        e
        for e in all_edges
        if e["from"] in visible_ids
        and e["to"] in visible_ids
        and (not type_filter or e["type"] in type_filter)
    ]

    positions = _layout(visible_nodes)

    edge_x, edge_y = [], []
    for e in visible_edges:
        x0, y0 = positions[e["from"]]
        x1, y1 = positions[e["to"]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=1, color=COLORS["border"]),
        hoverinfo="none",
        showlegend=False,
    )

    node_x = [positions[n["id"]][0] for n in visible_nodes]
    node_y = [positions[n["id"]][1] for n in visible_nodes]
    node_color = [LAYER_COLORS.get(n["layer"], COLORS["orange"]) for n in visible_nodes]
    node_text = [n["label"] for n in visible_nodes]
    node_hover = [f"{n['label']} ({n['technical_name']})" for n in visible_nodes]

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        textfont=dict(size=9, color=COLORS["text_sec"]),
        hovertext=node_hover,
        hoverinfo="text",
        marker=dict(size=14, color=node_color, line=dict(width=1, color=COLORS["bg"])),
        showlegend=False,
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        paper_bgcolor=COLORS["bg"],
        plot_bgcolor=COLORS["bg"],
        margin=dict(l=10, r=10, t=10, b=10),
        height=560,
        xaxis=dict(visible=False, showgrid=False, zeroline=False),
        yaxis=dict(visible=False, showgrid=False, zeroline=False),
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    return visible_nodes, visible_edges


_LAYER_ORDER = [
    "Capture", "Understanding", "Knowledge Objects", "Memory", "Intelligence",
    "Execution", "Exposure", "Evolution", "Trust", "Product", "Ontology",
]


def _layer_sort_key(layer):
    try:
        return (0, _LAYER_ORDER.index(layer))
    except ValueError:
        return (1, layer or "")


def node_jump_list(visible_nodes, key_prefix):
    """A reliable, always-clickable list of the currently visible nodes, grouped
    by architecture layer (same grouping as the Concepts browser) with a small
    colored dot matching the layer's pipeline color, for faster scanning."""
    st.markdown(
        f"<div style='color:{COLORS['text_mut']};font-size:0.78rem;text-transform:uppercase;"
        f"letter-spacing:0.06em;margin:14px 0 8px 0;'>Click a node to open its concept card</div>",
        unsafe_allow_html=True,
    )

    by_layer = {}
    for node in visible_nodes:
        by_layer.setdefault(node.get("layer") or "Other", []).append(node)

    for layer in sorted(by_layer.keys(), key=_layer_sort_key):
        nodes_in_layer = sorted(by_layer[layer], key=lambda n: n["label"])
        color = LAYER_COLORS.get(layer, COLORS["orange"])
        st.markdown(
            f"<div style='display:flex;align-items:center;gap:6px;margin:10px 0 4px 0;'>"
            f"<span style='display:inline-block;width:9px;height:9px;border-radius:50%;"
            f"background:{color};'></span>"
            f"<span style='color:{COLORS['text_sec']};font-size:0.8rem;font-weight:600;'>{layer}</span>"
            f"</div>",
            unsafe_allow_html=True,
        )
        cols = st.columns(3)
        for i, node in enumerate(nodes_in_layer):
            with cols[i % 3]:
                disabled = node["category"] == "coming_soon"
                if st.button(
                    node["label"],
                    key=f"{key_prefix}_jump_{node['id']}",
                    use_container_width=True,
                    disabled=disabled,
                ):
                    push_nav()
                    navigate_to("concepts", concept_id=node["id"])
                    st.rerun()
