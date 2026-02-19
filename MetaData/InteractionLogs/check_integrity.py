#!/usr/bin/env python3
"""Validate STUDIO interaction log integrity without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "logging_schema.json"
INDEXED_LOG_RE = re.compile(r"^(?P<index>\d{6})_(?P<ts>\d{8}T\d{6}Z)_(?P<interaction>[a-zA-Z0-9._:-]+)\.json$")
ISO_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"{path}: invalid JSON ({exc})") from exc


def validate_required_and_basic_types(data: dict, required: list[str], path: Path) -> list[str]:
    errors: list[str] = []
    for key in required:
        if key not in data:
            errors.append(f"{path.name}: missing required field '{key}'")

    if "log_index" in data and (not isinstance(data["log_index"], int) or data["log_index"] < 1):
        errors.append(f"{path.name}: log_index must be integer >= 1")

    if "mode" in data and data["mode"] not in {"BUILD", "META", "RUN"}:
        errors.append(f"{path.name}: mode must be BUILD|META|RUN")

    if "timestamp" in data and (not isinstance(data["timestamp"], str) or not ISO_TS_RE.match(data["timestamp"])):
        errors.append(f"{path.name}: timestamp must match YYYY-MM-DDTHH:MM:SSZ")

    if "workflow_version" in data and (
        not isinstance(data["workflow_version"], str) or not SEMVER_RE.match(data["workflow_version"])
    ):
        errors.append(f"{path.name}: workflow_version must be semver")

    return errors


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    required: list[str] = schema.get("required", [])

    errors: list[str] = []
    indexed_entries: list[tuple[int, Path, dict]] = []

    for path in sorted(ROOT.glob("*.json")):
        data = load_json(path)

        # Skip schema itself from entry validation.
        if path.name == "logging_schema.json":
            continue

        errors.extend(validate_required_and_basic_types(data, required, path))

        match = INDEXED_LOG_RE.match(path.name)
        if not match:
            continue

        file_index = int(match.group("index"))
        indexed_entries.append((file_index, path, data))

        if "log_index" in data and data["log_index"] != file_index:
            errors.append(f"{path.name}: log_index ({data['log_index']}) does not match file index ({file_index})")

    indexes = [idx for idx, _, _ in indexed_entries]
    if len(indexes) != len(set(indexes)):
        errors.append("duplicate indexed log filename prefixes detected")

    if indexes:
        expected = list(range(1, max(indexes) + 1))
        if indexes != expected:
            errors.append(
                "indexed log files are not contiguous from 000001; missing indexes detected: "
                + ", ".join(f"{i:06d}" for i in sorted(set(expected) - set(indexes)))
            )

    if errors:
        print("Integrity check FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Integrity check PASSED ({len(indexed_entries)} indexed interaction logs validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
