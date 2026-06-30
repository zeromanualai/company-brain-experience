import json
from pathlib import Path

import streamlit as st

_CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"


@st.cache_data
def load_json(filename):
    with open(_CONTENT_DIR / filename, encoding="utf-8") as f:
        return json.load(f)
