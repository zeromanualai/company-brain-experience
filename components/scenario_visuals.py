from core.theme import COLORS

_BG = COLORS["bg"]
_SURFACE = COLORS["surface_raised"]
_BORDER = COLORS["border"]
_TEXT = COLORS["text"]
_TEXT_SEC = COLORS["text_sec"]
_ORANGE = COLORS["orange"]


def _step1_meeting_happens():
    """Three people on a call, with a transcript appearing."""
    return f"""
    <svg viewBox="0 0 480 180" style="width:100%;max-width:480px;display:block;margin:0 auto;">
      <circle cx="80" cy="60" r="28" fill="{COLORS['capture']}22" stroke="{COLORS['capture']}" stroke-width="2"/>
      <text x="80" y="65" text-anchor="middle" fill="{_TEXT}" font-size="14" font-weight="600">M</text>
      <text x="80" y="105" text-anchor="middle" fill="{_TEXT_SEC}" font-size="11">Maria</text>

      <circle cx="240" cy="60" r="28" fill="{COLORS['capture']}22" stroke="{COLORS['capture']}" stroke-width="2"/>
      <text x="240" y="65" text-anchor="middle" fill="{_TEXT}" font-size="14" font-weight="600">S</text>
      <text x="240" y="105" text-anchor="middle" fill="{_TEXT_SEC}" font-size="11">Sarah</text>

      <circle cx="400" cy="60" r="28" fill="{COLORS['capture']}22" stroke="{COLORS['capture']}" stroke-width="2"/>
      <text x="400" y="65" text-anchor="middle" fill="{_TEXT}" font-size="14" font-weight="600">VP</text>
      <text x="400" y="105" text-anchor="middle" fill="{_TEXT_SEC}" font-size="11">Acme VP</text>

      <line x1="108" y1="60" x2="212" y2="60" stroke="{_BORDER}" stroke-width="1.5"/>
      <line x1="268" y1="60" x2="372" y2="60" stroke="{_BORDER}" stroke-width="1.5"/>

      <rect x="140" y="135" width="200" height="34" rx="6" fill="{_SURFACE}" stroke="{_BORDER}"/>
      <text x="240" y="156" text-anchor="middle" fill="{_TEXT_SEC}" font-size="11" font-family="monospace">
        transcript recording...
      </text>
    </svg>
    """


def _step3_building_blocks():
    """The meeting decomposing into atomic primitives."""
    blocks = [
        ("Actor", COLORS["capture"]),
        ("Communication", COLORS["understand"]),
        ("Commitment", COLORS["memory"]),
        ("Goal", COLORS["intelligence"]),
        ("Relationship", COLORS["evolution"]),
    ]
    widths = [max(60, len(label) * 7 + 16) for label, _ in blocks]
    gap = 12
    total_width = sum(widths) + gap * (len(widths) - 1)
    cursor = (480 - total_width) / 2

    block_svg = ""
    for (label, color), w in zip(blocks, widths):
        x_center = cursor + w / 2
        block_svg += f"""
        <line x1="240" y1="55" x2="{x_center}" y2="105" stroke="{_BORDER}" stroke-width="1.5"/>
        <rect x="{cursor}" y="105" width="{w}" height="32" rx="6" fill="{color}22" stroke="{color}" stroke-width="1.5"/>
        <text x="{x_center}" y="126" text-anchor="middle" fill="{_TEXT}" font-size="11" font-weight="600">{label}</text>
        """
        cursor += w + gap
    return f"""
    <svg viewBox="0 0 480 150" style="width:100%;max-width:480px;display:block;margin:0 auto;">
      <rect x="170" y="15" width="140" height="36" rx="6" fill="{_SURFACE}" stroke="{_ORANGE}" stroke-width="2"/>
      <text x="240" y="38" text-anchor="middle" fill="{_TEXT}" font-size="12" font-weight="700">The Meeting</text>
      {block_svg}
    </svg>
    """


def _step6_connecting_dots():
    """Memory stores converging into Operational Risk and Recommendation alerts."""
    stores = [
        ("Factual", 30),
        ("Interaction", 130),
        ("Commitment", 230),
        ("Action", 330),
        ("Learning", 430),
    ]
    store_svg = ""
    for label, x in stores:
        store_svg += f"""
        <rect x="{x-38}" y="10" width="76" height="30" rx="6" fill="{COLORS['memory']}22" stroke="{COLORS['memory']}" stroke-width="1.5"/>
        <text x="{x}" y="29" text-anchor="middle" fill="{_TEXT}" font-size="10" font-weight="600">{label}</text>
        <line x1="{x}" y1="40" x2="{170 if x < 240 else 330}" y2="95" stroke="{_BORDER}" stroke-width="1"/>
        """
    return f"""
    <svg viewBox="0 0 480 170" style="width:100%;max-width:480px;display:block;margin:0 auto;">
      {store_svg}
      <rect x="90" y="95" width="160" height="50" rx="8" fill="{COLORS['intelligence']}22" stroke="{COLORS['intelligence']}" stroke-width="2"/>
      <text x="170" y="116" text-anchor="middle" fill="{_TEXT}" font-size="11" font-weight="700">Operational Risk</text>
      <text x="170" y="132" text-anchor="middle" fill="{_TEXT_SEC}" font-size="9">Q3 renewal at risk</text>

      <rect x="270" y="95" width="170" height="50" rx="8" fill="{_ORANGE}22" stroke="{_ORANGE}" stroke-width="2"/>
      <text x="355" y="116" text-anchor="middle" fill="{_TEXT}" font-size="11" font-weight="700">Recommendation</text>
      <text x="355" y="132" text-anchor="middle" fill="{_TEXT_SEC}" font-size="9">Schedule check-in</text>
    </svg>
    """


_VISUALS = {
    ("customer_meeting", 1): _step1_meeting_happens,
    ("customer_meeting", 3): _step3_building_blocks,
    ("customer_meeting", 6): _step6_connecting_dots,
}


def get_visual(scenario_id, step_number):
    """Returns SVG markup for the highest-impact illustrated steps, or None.
    Only customer_meeting steps 1, 3, and 6 have an implemented visual — every
    other step relies on narrative and technical detail alone."""
    builder = _VISUALS.get((scenario_id, step_number))
    if not builder:
        return None
    # Strip leading whitespace from every line: st.markdown treats 4+ spaces of
    # indentation as a Markdown code block, which silently turns the SVG into
    # literal escaped text instead of rendering it.
    return "\n".join(line.strip() for line in builder().strip().splitlines())
