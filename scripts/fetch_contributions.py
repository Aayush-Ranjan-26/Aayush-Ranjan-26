"""Fetch public GitHub contribution activity without using a personal token."""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


USERNAME = "Aayush-Ranjan-26"
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "contributions.json"


class ContributionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.days: dict[str, dict[str, int]] = {}
        self.cell_ids: dict[str, str] = {}
        self.tooltip_for: str | None = None
        self.tooltip_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        day = attributes.get("data-date")
        if day:
            label = attributes.get("aria-label", "")
            count_match = re.search(r"([\d,]+) contribution", label)
            count = int(count_match.group(1).replace(",", "")) if count_match else 0
            level = int(attributes.get("data-level") or 0)
            self.days[day] = {"count": count, "level": level}
            if cell_id := attributes.get("id"):
                self.cell_ids[cell_id] = day
            return

        if tag == "tool-tip" and (target := attributes.get("for")):
            self.tooltip_for = target
            self.tooltip_text = []

    def handle_data(self, data: str) -> None:
        if self.tooltip_for:
            self.tooltip_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "tool-tip" or not self.tooltip_for:
            return
        day = self.cell_ids.get(self.tooltip_for)
        label = " ".join(self.tooltip_text)
        count_match = re.search(r"([\d,]+) contribution", label)
        if day and count_match:
            self.days[day]["count"] = int(count_match.group(1).replace(",", ""))
        self.tooltip_for = None
        self.tooltip_text = []


def calculate_streaks(days: dict[str, dict[str, int]]) -> tuple[int, int]:
    ordered = sorted(days)
    current = longest = running = 0
    for day in ordered:
        if days[day]["count"] > 0:
            running += 1
            longest = max(longest, running)
        else:
            running = 0

    cursor = date.today()
    while cursor.isoformat() in days and days[cursor.isoformat()]["count"] > 0:
        current += 1
        cursor -= timedelta(days=1)
    return current, longest


def main() -> None:
    request = Request(
        f"https://github.com/users/{USERNAME}/contributions",
        headers={"User-Agent": "Aayush-Ranjan-26-profile-art"},
    )
    with urlopen(request, timeout=30) as response:
        markup = response.read().decode("utf-8")

    parser = ContributionParser()
    parser.feed(markup)
    if not parser.days:
        raise RuntimeError("GitHub contribution calendar could not be parsed.")

    current_streak, longest_streak = calculate_streaks(parser.days)
    payload = {
        "username": USERNAME,
        "generated_at": f"{date.today().isoformat()}T00:00:00Z",
        "days": parser.days,
        "stats": {
            "total": sum(day["count"] for day in parser.days.values()),
            "current_streak": current_streak,
            "longest_streak": longest_streak,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

