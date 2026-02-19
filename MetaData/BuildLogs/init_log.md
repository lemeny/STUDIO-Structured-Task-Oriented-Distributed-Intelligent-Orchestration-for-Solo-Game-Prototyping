# init_log

```yaml
version: 0.1.0
decisions:
  - id: D001
    decision: create_top_level_directories
    value:
      - Workflow
      - MetaData
  - id: D002
    decision: create_workflow_subdirectories
    value:
      - Workflow/Rules
      - Workflow/Roles
      - Workflow/Stages
  - id: D003
    decision: create_metadata_subdirectories
    value:
      - MetaData/BuildLogs
      - MetaData/RunLogs
      - MetaData/Metrics
      - MetaData/ModelInfo
  - id: D004
    decision: set_system_version
    value: 0.1.0
  - id: D005
    decision: define_workflow_configuration_file
    value: Workflow/workflow_config.yaml
  - id: D006
    decision: define_experiment_protocol_file
    value: MetaData/ExperimentProtocol.md
  - id: D007
    decision: ensure_empty_directories_are_tracked
    value: create_.gitkeep_files
```
