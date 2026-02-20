# Universal GDD Specification

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.3.1-UNIVERSAL-GDD-SPEC

## Purpose

Define the mandatory Game Design Document (GDD) skeleton for any project so design outputs are implementation-ready across Architect, Engineer, and QA workflows.

## Mandatory Structure

All design-stage GDD artifacts must include each section below.

### Header (Required)
Include:
- Project Name
- Version
- Role
- Status

### 1) Identity: Vision & Core Pillars (Required)
Document:
- Experience vision and intended player fantasy.
- Core pillar keywords and non-negotiable design principles.

### 2) Loop Architecture: Micro/Macro Logic (Required)
Provide text-based flow diagrams for:
- Micro loop (moment-to-moment/session behavior).
- Macro loop (progression, unlocks, and long-term return cycle).

### 3) Interaction Schema: Input/Feedback Mechanics (Required)
Define:
- Input model (controls, commands, player intents).
- Feedback channels (visual, audio, UI, haptic, systemic responses).
- Interaction constraints, edge conditions, and fail states.

### 4) Functional Modules (Required)
Provide a categorized implementation module list for architecture handoff.
For each module include:
- Module name.
- Category (for example: Core Gameplay, AI, UI, Economy, Progression, Tools).
- One-line responsibility summary.

### 5) State Machine: Entity Transition Logic (Required)
Specify primary entities and their allowed state transitions:
- State definitions.
- Transition triggers/guards.
- Invalid transitions and expected handling behavior.

## Compliance Rule

A design artifact is not eligible for `FROZEN` status unless all mandatory sections above are present and internally consistent.
