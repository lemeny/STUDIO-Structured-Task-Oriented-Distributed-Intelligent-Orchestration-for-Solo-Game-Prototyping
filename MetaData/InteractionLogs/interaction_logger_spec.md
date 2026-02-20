# Interaction Logger Spec

Version: 0.3.2

## Scope
Defines mandatory structure and process for logging STUDIO interactions.

## Required Log Path
- Directory: `MetaData/InteractionLogs/`
- Schema: `MetaData/InteractionLogs/logging_schema.json` (v0.1.1 schema remains authoritative)
- Log entries: JSON objects conforming to schema.

## Zero-Prompt Logging Behavior
Every interaction request in `BUILD`, `META`, or `RUN` mode is logged automatically by the logging daemon flow.
Users do not provide log file names, paths, or sequence numbers.

## Automatic Log Entry Generation
For every interaction:
1. Capture request and response payloads.
2. Populate all required schema fields.
3. Allocate a unique, monotonically increasing `log_index` and generate `interaction_id` unique within repository history.
4. Write one log file per interaction using naming convention:
   - `MetaData/InteractionLogs/<log_index>_<timestamp>_<interaction_id>.json`
5. Ensure `log_index` is the next available zero-padded 6-digit value (incremental, no duplicates).
6. Validate generated entry against `logging_schema.json` before persistence.

## Gap Detection and Backfill
- Detect gaps via the integrity checker sequence validation.
- Backfill any missing interaction records to restore contiguous `000001..N` ordering.
- Resume normal incremental logging at `N+1`.

## Integrity Validation Script
Run `python MetaData/InteractionLogs/check_integrity.py` to validate:
- required schema fields on log entries,
- indexed filename format and uniqueness,
- `log_index` to filename index consistency,
- contiguous incremental index sequence.

## Field Definitions
- `log_index`: Unique integer index for incremental log ordering.
- `interaction_id`: Unique string identifier.
- `mode`: One of `BUILD | META | RUN`.
- `timestamp`: ISO 8601 UTC date-time.
- `model_name`: Model family identifier.
- `model_version`: Model version string.
- `prompt_text`: Raw prompt text.
- `response_text`: Raw response text.
- `prompt_token_count`: Prompt token usage.
- `completion_token_count`: Completion token usage.
- `latency_ms`: End-to-end response latency.
- `workflow_version`: Workflow semver reference.
- `notes`: Supplemental annotations.


## Zero-Check Rule (Persistent Instinct)
- Strict one-to-one mapping is mandatory: `1 user interaction = 1 atomic log entry`.
- Logging executes as a standard background post-execution step for every interaction, without requiring explicit user reminders.
- New entries must always detect the latest `log_index` in `MetaData/InteractionLogs/` and increment by exactly `+1`.
- Fragmentation is disallowed for a single interaction; if fragmentation occurs, logs must be consolidated into one canonical entry.
