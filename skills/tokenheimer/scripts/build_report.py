#!/usr/bin/env python3
"""Build Tokenheimer's portable HTML/CSV outputs from normalized report JSON.

Standard-library only. It intentionally rejects cost/spend fields because monetary
cost is not part of the Tokenheimer data contract.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "assets" / "report-template.html"
START = "/* TOKENHEIMER_DATA_START */"
END = "/* TOKENHEIMER_DATA_END */"

FORBIDDEN_KEYS = {"cost", "cost_usd", "price", "spend", "spend_usd"}
CSV_FIELDS = [
    "id", "date", "start", "end", "harness", "model",
    "active_minutes", "elapsed_minutes", "tokens", "input_tokens",
    "output_tokens", "reasoning_tokens", "cached_tokens",
    "input_tokens_per_second", "output_tokens_per_second",
    "tool_calls", "tools", "skills", "summary", "files", "commits", "tags",
]


def walk_keys(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key
            yield from walk_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk_keys(child, f"{path}[{i}]")


def validate(data: dict) -> None:
    if not isinstance(data, dict):
        raise ValueError("report.json must contain a JSON object")
    for required in ("meta", "headline", "time", "usage", "development", "quality", "artifacts"):
        if required not in data:
            raise ValueError(f"missing required top-level key: {required}")
    if data.get("meta", {}).get("mode") not in {"quick", "full"}:
        raise ValueError("meta.mode must be 'quick' or 'full'")
    for path, key in walk_keys(data):
        if key.lower() in FORBIDDEN_KEYS:
            raise ValueError(f"monetary cost is outside the Tokenheimer contract: {path}.{key}")
    headline = data.get("headline", {})
    for required in ("active_time_hours", "sessions", "tokens_total", "models_observed"):
        if required not in headline:
            raise ValueError(f"headline.{required} is required")
    if data.get("meta", {}).get("mode") == "full" and "sessions" not in data:
        raise ValueError("full mode requires sessions[]")


def js_json(data: dict) -> str:
    # Prevent embedded JSON from accidentally terminating a script element.
    return json.dumps(data, ensure_ascii=False, indent=2).replace("<", "\\u003c")


def render_html(data: dict, template: Path) -> str:
    text = template.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise ValueError("template is missing Tokenheimer data markers")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    block = f"{START}\nconst REPORT_DATA = {js_json(data)};\n{END}"
    return pattern.sub(block, text, count=1)


def flatten(value):
    if isinstance(value, list):
        return " | ".join(str(x) for x in value)
    return "" if value is None else value


def write_sessions_csv(data: dict, path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in data.get("sessions", []) or []:
            writer.writerow({key: flatten(row.get(key)) for key in CSV_FIELDS})


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Tokenheimer HTML and session CSV from report.json")
    parser.add_argument("--data", required=True, type=Path, help="normalized report JSON")
    parser.add_argument("--out", required=True, type=Path, help="output directory")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="override report template")
    args = parser.parse_args()

    data = json.loads(args.data.read_text(encoding="utf-8"))
    validate(data)
    args.out.mkdir(parents=True, exist_ok=True)

    report_json = args.out / "report.json"
    if args.data.resolve() != report_json.resolve():
        shutil.copy2(args.data, report_json)

    (args.out / "report.html").write_text(render_html(data, args.template), encoding="utf-8")
    write_sessions_csv(data, args.out / "sessions.csv")

    print(f"[OK] {args.out / 'report.html'}")
    print(f"[OK] {report_json}")
    print(f"[OK] {args.out / 'sessions.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
