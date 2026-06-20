---
description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`

**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create project structure per implementation plan
- [ ] T002 [P] Configure linting and formatting tools

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T003 Setup database schema and configuration
- [ ] T004 [P] Configure environment variable handling

**Checkpoint**: Foundation ready — user story work can begin

## Phase 3: User Story 1 - [Title] (Priority: P1)

**Goal**: [Brief description]

**Independent Test**: [How to verify]

### Implementation for User Story 1

- [ ] T005 [P] [US1] Implement feature in relevant module
- [ ] T006 [US1] Add tests in tests/

**Checkpoint**: User Story 1 independently functional

## Phase N: Polish & Cross-Cutting Concerns

- [ ] TXXX Documentation updates
- [ ] TXXX Run pytest and pre-commit

## Dependencies & Execution Order

- Setup → Foundational → User Stories → Polish
- Tests (if included) should fail before implementation
