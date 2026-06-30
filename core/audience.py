import json
from pathlib import Path

import streamlit as st

_CONTENT_PATH = Path(__file__).resolve().parent.parent / "content" / "audiences.json"


@st.cache_data
def load_audiences():
    with open(_CONTENT_PATH, encoding="utf-8") as f:
        return json.load(f)


def get_audience():
    return st.session_state.get("audience")


def set_audience(audience_id):
    st.session_state["audience"] = audience_id
    st.query_params["audience"] = audience_id


def get_audience_data(audience_id=None):
    audience_id = audience_id or get_audience()
    if not audience_id:
        return None
    for entry in load_audiences():
        if entry["id"] == audience_id:
            return entry
    return None


def adapt_text(field_value, audience_variants, audience_id=None):
    """Given a default field value and a dict of audience_id -> variant text,
    return the variant for the current/given audience, falling back to default."""
    audience_id = audience_id or get_audience()
    if audience_id and audience_variants and audience_id in audience_variants:
        return audience_variants[audience_id]
    return field_value
