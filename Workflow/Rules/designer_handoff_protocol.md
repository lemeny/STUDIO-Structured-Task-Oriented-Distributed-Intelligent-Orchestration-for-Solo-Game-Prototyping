# Designer Handoff Protocol

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.5.0-HANDOFF-GATE-PROTOCOL

## Purpose

Guarantee every Designer-originated document update is transferred to downstream roles in a consistent, machine-readable, and auditable structure.

## Scope

Applies to all files under:
- `Projects/*/Design_Docs/`
- `Projects/*/Design_Specs/`

and any design-stage artifact produced under `Designer_Agent` identity.

## Mandatory Handoff Unit

Each Designer update intended for downstream work must include a **Handoff Packet** with the following fields.

### Required Fields
- `handoff_id`: Unique ID (format: `DH-<project>-<YYYYMMDD>-<nn>`)
- `from_role`: Must be `Designer_Agent`
- `to_role`: One of `Architect_Agent | Engineer_Agent | QA_Agent`
- `source_artifact`: Relative file path (for example: `Projects/Savanna_Pulse/Design_Docs/GDD_v1.md`)
- `source_version`: Designer artifact version string
- `change_scope`: Bounded section references (for example: `§2 Micro Loop`, `§3 Feedback Channels`)
- `handover_tag`: `FROZEN_PARTIAL` or `FROZEN`
- `dependencies`: Explicit assumptions or required upstream/downstream inputs
- `acceptance_contract`: Testable statements the receiver can implement/verify
- `open_risks`: Known risks and unresolved decisions
- `requested_by`: Optional task/request identifier
- `timestamp_utc`: ISO-8601 UTC timestamp

## Handoff Packet Template

```yaml
handoff_id: DH-<project>-<YYYYMMDD>-<nn>
from_role: Designer_Agent
to_role: <Architect_Agent|Engineer_Agent|QA_Agent>
source_artifact: <relative/path/to/design/artifact>
source_version: <x.y.z>
change_scope:
  - <section ref 1>
  - <section ref 2>
handover_tag: <FROZEN_PARTIAL|FROZEN>
dependencies:
  - <dependency 1>
acceptance_contract:
  - <verifiable expectation 1>
open_risks:
  - <risk 1>
requested_by: <task id or prompt id>
timestamp_utc: <YYYY-MM-DDTHH:MM:SSZ>
```

## Placement Rules

For every design update, include the packet in one of these locations:
1. At the end of the updated design artifact under `## Handoff Packet`, or
2. In a sibling file named `Handoff_<handoff_id>.md` in the same design directory.

## Task Board Synchronization Rules

When a packet is created:
1. Record the handover in `Workflow/task_board.md` using the existing handover note fields.
2. Ensure the note references `handoff_id`, `source_artifact`, and `change_scope`.
3. Keep task status aligned with artifact state (`DRAFT` + `FROZEN_PARTIAL` handovers are allowed).

## Receiver Consumption Contract

- Architect consumes `change_scope + acceptance_contract + dependencies` as architecture input boundaries.
- Engineer consumes behavior guarantees and invalid-state handling from accepted architecture outputs.
- QA consumes acceptance_contract statements directly as test intent seeds.

## Compliance Gate

A Designer update is considered handoff-ready only when:
1. Handoff Packet exists with all required fields.
2. Task board note exists and references the packet.
3. Referenced section names/paths resolve to existing artifact content.


## Architect-to-Developer Transition (Formal Gate Handoff)

For Architecture -> Implementation, the handoff is valid only when all of the following are present:
1. An Architect-originated handoff packet with bounded build scope.
2. A valid `architect_gate_signature` from `Architect_Agent`.
3. A task board handover note linking packet and gate signature.

### Architect Handoff Packet (Required Fields)
- `handoff_id`: Unique ID (format: `AH-<project>-<YYYYMMDD>-<nn>`)
- `from_role`: Must be `Architect_Agent`
- `to_role`: Must be `Engineer_Agent`
- `source_artifact`: Relative architecture artifact path
- `source_version`: Architecture artifact version string
- `implementation_scope`: Bounded modules/interfaces approved for build
- `architect_gate_id`: Must match `architect_gate_signature.gate_id`
- `constraints_for_engineering`: Non-negotiable implementation constraints
- `acceptance_contract`: Verifiable statements implementation must satisfy
- `open_risks`: Known risks and unresolved integration concerns
- `timestamp_utc`: ISO-8601 UTC timestamp

### Architect-to-Developer Handoff Template

```yaml
handoff_id: AH-<project>-<YYYYMMDD>-<nn>
from_role: Architect_Agent
to_role: Engineer_Agent
source_artifact: <relative/path/to/architecture/artifact>
source_version: <x.y.z>
implementation_scope:
  - <module/interface 1>
architect_gate_id: GATE-Architecture-<YYYYMMDD>-<nn>
constraints_for_engineering:
  - <constraint 1>
acceptance_contract:
  - <verifiable expectation 1>
open_risks:
  - <risk 1>
timestamp_utc: <YYYY-MM-DDTHH:MM:SSZ>
```

## Downstream Start Rule (Hard Block)

No downstream stage can begin unless its immediate upstream gate status is **APPROVED** and recorded.

Specifically:
- Architecture work must not begin until Design Gate is approved.
- Implementation work must not begin until Architecture Gate is approved.
- Testing work must not begin until Implementation Gate is approved.

Any execution that starts without gate approval is non-compliant and must be halted and reopened through task board governance.
