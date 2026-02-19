# Workflow State Policy

This policy defines valid state transitions for workflow artifacts.

## States

- **DRAFT**: Work is actively being authored or revised.
- **FROZEN**: Work is approved for execution and should not change without formal reopening.
- **DEPRECATED**: Work is retired and should not be used for new decisions.

## Allowed Transitions

- `DRAFT -> FROZEN`
  - Trigger: review complete and approval granted.
- `FROZEN -> DRAFT`
  - Trigger: change request or defect requires reopening.
- `FROZEN -> DEPRECATED`
  - Trigger: superseded by a newer approved artifact.
- `DRAFT -> DEPRECATED`
  - Trigger: work abandoned before approval.

## Restricted Transitions

- `DEPRECATED -> DRAFT` is not allowed.
- `DEPRECATED -> FROZEN` is not allowed.

Deprecated artifacts must be replaced by creating new draft artifacts.
