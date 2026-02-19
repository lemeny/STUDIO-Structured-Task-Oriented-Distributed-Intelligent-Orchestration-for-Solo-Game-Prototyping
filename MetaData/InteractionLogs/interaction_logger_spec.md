# Interaction Logger Spec

Version: 0.1.0

## Scope
Defines mandatory structure and process for logging STUDIO interactions.

## Required Log Path
- Directory: `MetaData/InteractionLogs/`
- Schema: `MetaData/InteractionLogs/logging_schema.json`
- Log entries: JSON objects conforming to schema.

## Mandatory Interaction Header
Every future interaction request must include:
1. Explicit `MODE` (`BUILD`, `META`, or `RUN`)
2. Version reference (`workflow_version` in semver format)

If either field is missing, interaction is invalid for logging-compliant workflow execution.

## Automatic Log Entry Generation
For every interaction:
1. Capture request and response payloads.
2. Populate all required schema fields.
3. Generate `interaction_id` unique within repository history.
4. Write one log file per interaction using naming convention:
   - `MetaData/InteractionLogs/<timestamp>_<interaction_id>.json`
5. Validate generated entry against `logging_schema.json` before persistence.

## Field Definitions
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
