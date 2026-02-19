# STUDIO Logging Policy

Version: 0.1.1

## Objective
Enforce mandatory interaction logging for every model response in STUDIO.

## Mandatory Rules
1. No response may be produced without generating a corresponding `InteractionLog` entry.
2. Every log file must use a unique, monotonically increasing index (`log_index`).
3. Logs must be stored incrementally in `MetaData/InteractionLogs/`.

## Storage and Naming Convention
- Directory: `MetaData/InteractionLogs/`
- File name format: `<log_index>_<timestamp>_<interaction_id>.json`
- `log_index` format: zero-padded 6-digit integer (e.g., `000001`).
- `timestamp` format in file name: compact UTC (`YYYYMMDDTHHMMSSZ`).

## Index Allocation Procedure
1. Enumerate existing log files in `MetaData/InteractionLogs/` that match `^[0-9]{6}_.*\.json$`.
2. Parse the leading numeric prefix.
3. Next index = `max(existing_index) + 1`, or `1` if none exist.
4. Write exactly one new log entry for the interaction before final response delivery.

## Compliance Requirements
- Log JSON must validate against `MetaData/InteractionLogs/logging_schema.json`.
- `workflow_version` must be present and semver compliant.
- `mode` must be one of `BUILD`, `META`, or `RUN`.

## Operational Check
- Execute `python MetaData/InteractionLogs/check_integrity.py` before finalizing META changes that affect interaction logs.
