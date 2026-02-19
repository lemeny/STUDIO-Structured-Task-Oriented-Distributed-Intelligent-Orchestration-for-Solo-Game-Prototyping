#!/usr/bin/env python3
"""STUDIO zero-prompt interaction logger.

Allocates sequential log indices, writes schema-compatible entries, and can
backfill missing interaction logs to preserve contiguous history.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
INDEX_WIDTH = 6


@dataclass(frozen=True)
class LogFile:
    index: int
    path: Path


def indexed_logs() -> list[LogFile]:
    logs: list[LogFile] = []
    for path in sorted(ROOT.glob("*.json")):
        if path.name == "logging_schema.json":
            continue
        try:
            prefix = path.name.split("_", 1)[0]
            if len(prefix) == INDEX_WIDTH and prefix.isdigit():
                logs.append(LogFile(index=int(prefix), path=path))
        except Exception:
            continue
    return sorted(logs, key=lambda item: item.index)


def next_index(entries: Iterable[LogFile]) -> int:
    items = list(entries)
    return (max((item.index for item in items), default=0) + 1)


def now_pair() -> tuple[str, str]:
    now = datetime.now(UTC)
    return now.strftime("%Y%m%dT%H%M%SZ"), now.strftime("%Y-%m-%dT%H:%M:%SZ")


def write_log(payload: dict, ts_compact: str) -> Path:
    log_index = int(payload["log_index"])
    interaction_id = str(payload["interaction_id"])
    out = ROOT / f"{log_index:06d}_{ts_compact}_{interaction_id}.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Zero-prompt log writer")
    p.add_argument("--mode", required=True, choices=["BUILD", "META", "RUN"])
    p.add_argument("--workflow-version", required=True)
    p.add_argument("--prompt-text", required=True)
    p.add_argument("--response-text", required=True)
    p.add_argument("--notes", default="")
    p.add_argument("--model-name", default="GPT-5.2-Codex")
    p.add_argument("--model-version", default="5.2")
    p.add_argument("--prompt-token-count", type=int, default=0)
    p.add_argument("--completion-token-count", type=int, default=0)
    p.add_argument("--latency-ms", type=int, default=0)
    p.add_argument("--interaction-id", default="")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    logs = indexed_logs()
    index = next_index(logs)
    ts_compact, ts_iso = now_pair()
    interaction_id = args.interaction_id or f"{args.mode.lower()}-{ts_compact}-{index:06d}"

    payload = {
        "log_index": index,
        "interaction_id": interaction_id,
        "mode": args.mode,
        "timestamp": ts_iso,
        "model_name": args.model_name,
        "model_version": args.model_version,
        "prompt_text": args.prompt_text,
        "response_text": args.response_text,
        "prompt_token_count": args.prompt_token_count,
        "completion_token_count": args.completion_token_count,
        "latency_ms": args.latency_ms,
        "workflow_version": args.workflow_version,
        "notes": args.notes,
    }
    out = write_log(payload, ts_compact)
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
