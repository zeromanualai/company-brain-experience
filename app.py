import streamlit as st

from components.layout import render_sidebar
from core.router import render_page
from core.session import init_session
from core.theme import inject_css

st.set_page_config(
    page_title="Company Brain Experience",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()
inject_css()
render_sidebar()
render_page(st.session_state["current_section"])
