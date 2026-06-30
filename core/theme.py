import streamlit as st

COLORS = {
    "bg": "#0D1117",
    "surface": "#161B22",
    "surface_raised": "#1C2128",
    "border": "#30363D",
    "text": "#F0F6FC",
    "text_sec": "#8B949E",
    "text_mut": "#484F58",
    "orange": "#FF6B00",
    "capture": "#38BDF8",
    "understand": "#60A5FA",
    "memory": "#818CF8",
    "intelligence": "#34D399",
    "trust": "#FBBF24",
    "execution": "#FB923C",
    "exposure": "#F472B6",
    "evolution": "#A78BFA",
}

LAYER_COLORS = {
    "Capture": "#38BDF8",
    "Understanding": "#60A5FA",
    "Knowledge Objects": "#818CF8",
    "Memory": "#818CF8",
    "Intelligence": "#34D399",
    "Execution": "#FB923C",
    "Exposure": "#F472B6",
    "Evolution": "#A78BFA",
    "Trust": "#FBBF24",
}


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

        #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{
            visibility: hidden;
            height: 0;
        }}

        /* The rule above hides the whole header bar, which is also where
        Streamlit renders the "reopen sidebar" arrow once the sidebar has been
        collapsed ([data-testid="stExpandSidebarButton"], nested inside the
        header). `visibility` (unlike `display`) lets a descendant override an
        ancestor's hidden value without restoring the ancestor's own layout —
        so the header itself stays height:0 and invisible, but this one button
        renders and stays clickable. */
        [data-testid="stExpandSidebarButton"] {{
            visibility: visible !important;
            pointer-events: auto !important;
        }}

        .stApp {{
            background-color: {COLORS["bg"]};
        }}

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            color: {COLORS["text"]};
        }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Space Grotesk', sans-serif !important;
            color: {COLORS["text"]} !important;
        }}

        code, .mono {{
            font-family: 'JetBrains Mono', monospace !important;
        }}

        section[data-testid="stSidebar"] {{
            background-color: {COLORS["surface"]};
            border-right: 1px solid {COLORS["border"]};
        }}

        .stButton > button {{
            background-color: transparent;
            border: 1px solid {COLORS["border"]};
            color: {COLORS["text"]};
            border-radius: 6px;
            transition: all 0.15s ease;
            word-break: normal;
            overflow-wrap: break-word;
            hyphens: none;
        }}

        .stButton > button:hover {{
            border-color: {COLORS["orange"]};
            color: {COLORS["orange"]};
        }}

        .stButton > button[kind="primary"] {{
            background-color: {COLORS["orange"]};
            border-color: {COLORS["orange"]};
            color: #0D1117;
        }}

        [data-testid="stExpander"] {{
            background-color: {COLORS["surface"]};
            border: 1px solid {COLORS["border"]};
            border-radius: 8px;
        }}

        .stTabs [data-baseweb="tab-list"] {{
            background-color: transparent;
            gap: 8px;
        }}

        .stTabs [data-baseweb="tab"] {{
            background-color: transparent;
            color: {COLORS["text_sec"]};
        }}

        .stTabs [aria-selected="true"] {{
            color: {COLORS["orange"]} !important;
            border-bottom-color: {COLORS["orange"]} !important;
        }}

        input, textarea {{
            background-color: {COLORS["bg"]} !important;
            border: 1px solid {COLORS["border"]} !important;
            color: {COLORS["text"]} !important;
        }}

        input:focus, textarea:focus {{
            border-color: {COLORS["orange"]} !important;
            box-shadow: 0 0 0 1px {COLORS["orange"]} !important;
        }}

        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        ::-webkit-scrollbar-track {{
            background: {COLORS["bg"]};
        }}
        ::-webkit-scrollbar-thumb {{
            background: {COLORS["border"]};
            border-radius: 5px;
        }}

        a, a:visited {{
            color: {COLORS["orange"]};
        }}

        hr {{
            border-color: {COLORS["border"]};
        }}

        [data-testid="stMainBlockContainer"] {{
            animation: cb-fade-in 0.25s ease-out;
        }}
        @keyframes cb-fade-in {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @media (max-width: 768px) {{
            [data-testid="stMainBlockContainer"] {{
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }}
            h1 {{ font-size: 1.7rem !important; }}
            h2 {{ font-size: 1.3rem !important; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
