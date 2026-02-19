# GDD Standard Specification

Creator_Role: System
Status: FROZEN
Source_Task_ID: BUILD-0.3.1-GDD-STANDARD-SPEC

## Purpose

Define the mandatory structure for all Designer_Agent Game Design Document (GDD) outputs so downstream Architect, Engineer, and QA roles can consume design artifacts consistently.

## Mandatory Output Structure for Designer_Agent GDD Tasks

Every Designer_Agent GDD output must include all of the following sections and required fields.

### Header (Required)
Include a top-level header block containing:
- Project Name
- Version
- Role
- Status

### 1) Experience & Pillars (Required)
Must define:
- The target "feel" of the game experience.
- Core design pillar keywords that anchor decision-making.

### 2) Game Loop (Required)
Must provide text-based visual flowcharts for:
- Micro loop (single session / moment-to-moment play).
- Macro loop (long-term progression and meta cycle).

### 3) Mechanics & Operations (Required)
Must detail:
- Grid logic behavior and constraints.
- Tetromino rules and manipulation boundaries.
- Resource constraints and operational limits.

### 4) Functional Decomposition (Required)
Must list implementation-oriented modules for Architect handoff, for example:
- Grid_Manager
- Animal_AI_System

Module naming can vary by project, but each module entry must include a one-line purpose statement.

### 5) Data Schemas (Required)
Must provide initial schema-level thinking for:
- Card types
- Animal stats
- Tile properties

Schema entries may be draft-level, but fields and intent must be explicit enough for architecture planning.

## Compliance Rule

A Designer_Agent output does not qualify as a complete GDD artifact unless all required sections above are present.
