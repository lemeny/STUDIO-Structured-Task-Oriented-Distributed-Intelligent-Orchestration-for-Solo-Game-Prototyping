# General Workflow Rules (Master Protocol)

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.3.0-GENERAL-WORKFLOW

## Purpose

This master protocol defines how STUDIO supports asynchronous, multi-role collaboration while preserving artifact traceability and state integrity.

## 1) Handover Logic (Non-Blocking)

### 1.1 Core Principle
Roles must not wait for full-stage completion when a stable sub-component is ready. Any role may hand over a bounded output unit once it reaches **FROZEN_PARTIAL** status.

### 1.2 FROZEN_PARTIAL Definition
**FROZEN_PARTIAL** means a scoped sub-component is stable enough for downstream consumption, while the parent artifact can remain in DRAFT.

Examples:
- Designer freezes "Movement Logic" behavior notes for engineering.
- Architect freezes "Input API Contract" while broader system diagrams continue evolving.
- Engineer freezes "PlayerController module" while adjacent modules remain in progress.

### 1.3 Required Conditions Before Handover
A sub-component can be marked **FROZEN_PARTIAL** only when:
1. Scope boundaries are explicit.
2. Dependency assumptions are listed.
3. Known risks/open issues are recorded.
4. Ownership of downstream integration is assigned.

### 1.4 Allowed Consumption Behavior
Downstream roles may start implementation/testing immediately against FROZEN_PARTIAL units, but must:
- reference exact artifact path and section,
- track unresolved dependencies,
- reopen via change request if upstream modifies frozen scope.

## 2) Identity-Based Loading

### 2.1 Role Card Source
Role definitions are loaded from `Workflow/Roles/` only.

### 2.2 Stage-to-Role Mapping
At task execution, the system must load role cards by current stage:
- **Design stage** -> `Designer_Agent.md`
- **Architecture stage** -> `Architect_Agent.md`
- **Implementation stage** -> `Engineer_Agent.md`
- **Testing stage** -> `QA_Agent.md`

If a task spans multiple stages, load all relevant role cards in order of execution.

### 2.3 Identity Lock
Every artifact must be generated under an explicit active role identity. Cross-role edits are allowed only with traceable handover notes.

## 3) Standardized Artifact Headers

### 3.1 Mandatory Header Fields
Every newly generated workflow artifact must include the following metadata header near the top of the file:

- `Creator_Role`
- `Status` (`DRAFT`, `FROZEN`, or `DEPRECATED`)
- `Source_Task_ID`

### 3.2 Header Rules
- `Creator_Role` must match one role profile name in `Workflow/Roles/` (or `System` for framework-level docs).
- `Status` must follow state policy in `Workflow/Rules/state_policy.md`.
- `Source_Task_ID` must map to an entry in the task board.

## 4) Artifact State and Transition Alignment

- Artifact baseline lifecycle remains: `DRAFT -> FROZEN -> DEPRECATED`.
- `FROZEN_PARTIAL` is an operational handover tag for sub-components and does not replace top-level artifact state.
- Final release outputs must still reach full `FROZEN` at artifact level.

## 5) Operational Notes

1. Prefer narrow, frozen interfaces early to unlock parallel work.
2. Preserve backward references when frozen partials are superseded.
3. Record handover events in task board notes to keep role synchronization auditable.
