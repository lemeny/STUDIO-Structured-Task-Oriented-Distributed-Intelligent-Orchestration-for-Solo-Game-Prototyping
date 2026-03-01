# Stage Gate Protocol

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.5.0-STAGE-GATE-PROTOCOL

## Purpose

Define mandatory governance gates between workflow stages so downstream work starts only after explicit upstream approval.

## Gate Model

Each stage owns a release gate at its output boundary.
A gate decision is one of:
- `PENDING`
- `APPROVED`
- `REJECTED`

Only `APPROVED` allows transition to the next stage.

## Gate Ownership

- Concept Gate Owner: `Designer_Agent`
- Design Gate Owner: `Designer_Agent`
- Architecture Gate Owner: `Architect_Agent`
- Implementation Gate Owner: `Engineer_Agent`
- Testing Gate Owner: `QA_Agent`

## Required Gate Record

Each approval must include a Gate Record with:
- `gate_id`: `GATE-<stage>-<YYYYMMDD>-<nn>`
- `stage`: Current stage name
- `gate_owner`: Role granting authority
- `decision`: `APPROVED`
- `approved_artifacts`: list of relative paths and versions/signatures
- `decision_note`: rationale and constraints for downstream roles
- `timestamp_utc`: ISO-8601 UTC timestamp

## Transition Rules

1. Concept -> Design requires approved Concept Gate.
2. Design -> Architecture requires approved Design Gate.
3. Architecture -> Implementation requires approved Architecture Gate.
4. Implementation -> Testing requires approved Implementation Gate.

If a gate is `PENDING` or `REJECTED`, the downstream stage must not start.

## Handoff Binding

- Designer-originated transitions must also satisfy `Workflow/Rules/designer_handoff_protocol.md`.
- Architecture-to-Implementation transitions must include an Architect Gate Signature as defined in `Workflow/Roles/Architect_Agent.md`.

## Audit Requirement

Gate decisions must be mirrored in `Workflow/task_board.md` handover notes with gate ID, artifact references, and decision timestamp.
