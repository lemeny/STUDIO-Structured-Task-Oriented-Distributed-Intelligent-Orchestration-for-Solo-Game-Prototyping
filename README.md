# STUDIO: Structured-Task-Oriented-Distributed-Intelligent-Orchestration-for-Solo-Game-Prototyping

一个整合 LLM 进行独立游戏开发的工作流实践。

## Version

- Previous: `v0.4.0`
- Current: `v0.5.0`
- Bump Type: `minor`

## Repository Structure

```text
.
├── Workflow/
│   ├── Rules/
│   ├── Roles/
│   ├── Stages/
│   ├── task_board.md
│   └── workflow_config.yaml
├── MetaData/
│   ├── BuildLogs/
│   ├── InteractionLogs/
│   ├── ExperimentProtocol.md
│   └── logging_policy.md
├── Projects/
│   └── <GameName>/...
└── README.md
```

## Workflow Directory

`Workflow/` 是 STUDIO 的执行层（execution layer），定义了任务如何从需求推进到设计、实现与测试：

- `Workflow/Rules/`：系统级规则与约束（状态策略、角色交接协议、统一 GDD 规范）。
- `Workflow/Roles/`：角色职责说明（Designer/Architect/Engineer/QA）。
- `Workflow/Stages/`：阶段性管线定义（当前为 `pipeline_v1.md`）。
- `Workflow/task_board.md`：跨角色任务看板与状态同步入口。
- `Workflow/workflow_config.yaml`：工作流主配置（系统版本、目录映射、状态和日志协议）。

## MetaData Directory (Research Layer)

`MetaData/` 是 STUDIO 的研究与可追溯层（research and traceability layer），负责记录系统演化证据：

- `MetaData/BuildLogs/`：每次 BUILD/META 结构性变更的变更日志。
- `MetaData/InteractionLogs/`：结构化交互日志与校验工具（含 schema、示例、完整性检查）。
- `MetaData/ExperimentProtocol.md`：可复现实验协议，记录流程初始化和研究过程。
- `MetaData/logging_policy.md`：日志记录强制策略（字段、顺序、校验要求）。

## Interaction Modes

STUDIO 使用三种交互模式来分离职责：

- `BUILD`：用于仓库结构、流程规则、配置和实现工件的建设与迭代。
- `META`：用于元层治理，包括日志策略、协议同步、版本与证据链维护。
- `RUN`：用于按既定流程执行任务，产出项目阶段性结果（设计/架构/实现/测试）。

## Versioning Notes

- 版本号遵循语义化版本（SemVer）。
- 本次更新为 `minor` 级别：从 `0.4.0` 升级到 `0.5.0`。
- 该版本用于同步 Stage Gate 治理升级后的 Workflow 结构与 MetaData 研究层定义。
