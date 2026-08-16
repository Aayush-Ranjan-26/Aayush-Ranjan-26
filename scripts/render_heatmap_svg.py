"""Render public contribution data as a self-animating SVG heatmap."""

from __future__ import annotations

import json
from datetime import date, datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUTPUT = ROOT / "assets" / "contribution-heatmap.svg"
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#7ee787"]


def escaped(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    days: dict[str, dict[str, int]] = payload["days"]
    end = date.today()
    start = end - timedelta(days=364)
    start -= timedelta(days=(start.weekday() + 1) % 7)

    cell_size, gap = 11, 3
    left, top = 150, 82
    cells: list[str] = []
    months: list[str] = []
    prior_month = -1

    for week in range(53):
        week_start = start + timedelta(days=week * 7)
        if week_start.month != prior_month:
            months.append(
                f'<text x="{left + week * (cell_size + gap)}" y="64" class="month">{week_start.strftime("%b")}</text>'
            )
            prior_month = week_start.month

        for weekday in range(7):
            day = week_start + timedelta(days=weekday)
            info = days.get(day.isoformat(), {"count": 0, "level": 0})
            x = left + week * (cell_size + gap)
            y = top + weekday * (cell_size + gap)
            delay = round((week + weekday * 0.23) * 0.025, 3)
            label = f'{day.isoformat()}: {info["count"]} contributions'
            cells.append(
                f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="3" '
                f'fill="{PALETTE[min(info["level"], len(PALETTE) - 1)]}" aria-label="{escaped(label)}" '
                f'opacity="0" transform="translate(0,-6)"><animate attributeName="opacity" from="0" to="1" '
                f'begin="{delay}s" dur="0.28s" fill="freeze"/><animateTransform attributeName="transform" '
                f'type="translate" from="0 -6" to="0 0" begin="{delay}s" dur="0.28s" fill="freeze"/></rect>'
            )

    stats = payload["stats"]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="250" viewBox="0 0 1000 250" role="img" aria-labelledby="title desc">
  <title id="title">{escaped(payload["username"])} GitHub contribution activity</title>
  <desc id="desc">Animated 53-week contribution heatmap generated from public GitHub activity.</desc>
  <style>
    .label {{ fill: #8b949e; font: 14px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    .month {{ fill: #8b949e; font: 12px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    .title {{ fill: #c9d1d9; font: 700 20px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    .stat {{ fill: #7ee787; font: 700 16px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
  </style>
  <rect width="1000" height="250" rx="18" fill="#0d1117"/>
  <rect x="1" y="1" width="998" height="248" rx="17" fill="none" stroke="#30363d"/>
  <text x="42" y="45" class="title">$ ./contributions.sh --last-year</text>
  <text x="42" y="89" class="label">Sun</text><text x="42" y="131" class="label">Tue</text><text x="42" y="173" class="label">Thu</text><text x="42" y="215" class="label">Sat</text>
  {''.join(months)}
  {''.join(cells)}
  <text x="42" y="238" class="stat">{stats["total"]} contributions</text>
  <text x="310" y="238" class="label">current streak: {stats["current_streak"]} days</text>
  <text x="640" y="238" class="label">longest streak: {stats["longest_streak"]} days</text>
</svg>
'''
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()

