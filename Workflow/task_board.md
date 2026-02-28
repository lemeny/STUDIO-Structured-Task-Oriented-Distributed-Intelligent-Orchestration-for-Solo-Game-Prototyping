# STUDIO Task Board

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.4.0-TASKBOARD-SYNC

## Version
- Previous: `v0.3.0`
- Current: `v0.4.0`

## Role-Linked Task Synchronization

| Task ID | Stage | Role Owner | Output Path | Task Status |
|---|---|---|---|---|
| T-3001 | Design | Designer_Agent | `Projects/Demo_Game/Design_Specs/` | DRAFT |
| T-3002 | Architecture | Architect_Agent | `Projects/Demo_Game/Tech_Arch/` | DRAFT |
| T-3003 | Implementation | Engineer_Agent | `Projects/Demo_Game/Implementation/` | DRAFT |
| T-3004 | Testing | QA_Agent | `Projects/Demo_Game/QA_Results/` | DRAFT |
| T-3101 | Design | Designer_Agent | `Projects/Savanna_Pulse/Design_Docs/` | IN_PROGRESS |

## Status Link Rules
1. Each task must map to one role owner and one primary output directory.
2. Status changes must be reflected in both task row and artifact header.
3. Partial handovers use notes with `FROZEN_PARTIAL` tags before full task freeze.

## Handover Note Template
- `Handoff_ID`:
- `From`:
- `To`:
- `Artifact/Section`:
- `Handover Tag`: `FROZEN_PARTIAL`
- `Acceptance Contract`:
- `Dependency Notes`:
- `Open Risks`:
- `Timestamp`:
