---
name: skill-writer
description: Use when the user asks to create, draft, write, update, improve, or design a Codex skill, skill folder, or SKILL.md file for a repeatable workflow or specialized task.
---

# Skill Writer

Use this skill to create concise, useful skills that teach Codex how to perform a repeatable task.

## Workflow

1. Understand the skill's purpose.
   - Identify the task the skill should help with.
   - Clarify the trigger phrases or situations where the skill should be used.
   - Decide whether the skill needs only `SKILL.md` or also scripts, references, or assets.

2. Choose the skill location.
   - For local project skills, use `.agents/skills/<skill-name>/SKILL.md`.
   - Use a lowercase, hyphenated folder name.
   - Keep the required file name exactly `SKILL.md`.

3. Write strong frontmatter.
   - Include `name` and `description`.
   - Make `name` match the folder name.
   - Make `description` explicit about when to use the skill, including common user phrasing.

4. Write the body.
   - Keep instructions concise and action-oriented.
   - Include only knowledge Codex needs for this task.
   - Prefer a short workflow over long explanations.
   - Add validation or final-response guidance when it matters.

5. Add resources only when useful.
   - Use `scripts/` for deterministic or frequently repeated code.
   - Use `references/` for detailed docs that should be loaded only when needed.
   - Use `assets/` for files that should be copied or used in outputs.
   - Do not add extra README, changelog, or setup docs unless explicitly requested.

6. Verify the skill.
   - Read the file back to catch formatting problems.
   - Confirm the frontmatter is valid YAML.
   - Confirm the instructions are specific enough to guide behavior but not bloated.

## SKILL.md Template

```markdown
---
name: skill-name
description: Use when the user asks to perform this specific repeatable task, including common trigger phrases and situations.
---

# Skill Title

One sentence describing what this skill helps Codex do.

## Workflow

1. First action.
2. Second action.
3. Verification or final response guidance.
```

## Quality Checklist

- The skill has a clear trigger in the description.
- The folder name, frontmatter name, and skill purpose match.
- The body is short enough to load quickly.
- The workflow tells Codex what to do, not just what the topic is.
- Optional files are added only when they directly support the skill.
