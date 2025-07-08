# Guide to Writing in Narrative-Flavored Procedural PsuedoLang (NF-PPL)

## Overview

Narrative-Flavored Procedural PsuedoLang (NF-PPL) is a human-readable, structured method of expressing procedures, workflows, or architectural decompositions. It combines the clarity of formal structure with the familiarity of natural language. It is optimized for human execution and review—especially among interdisciplinary or distributed teams.

---

## 1. Core Philosophy

* **Speak plainly.** Favor complete sentences and subject-verb-object clarity.
* **Preserve structure.** Use indentation and bullets to reflect control flow.
* **Favor precision over cleverness.** Clear is better than concise; concise is better than cute.
* **Predictable formatting.** Every pattern should feel familiar and scannable.

---

## 2. Document Anatomy

* **Front Matter** (Optional): Short purpose and scope statement.
* **Global Invariants**: Rules like "Always run backup" or "Never edit the diagram".
* **Section Headings**: Use `=== SECTION TITLE ===` to indicate major phases.
* **Bulleted Action Blocks**: Where the actual steps live.
* **Footer Outputs**: What gets produced, shared, or confirmed.

---

## 3. Syntax Guidelines

### 3.1 Indentation & Nesting

* Use **2 spaces per level**.
* Avoid nesting deeper than **3 levels**. Split into sub-procedures if needed.

### 3.2 Bullets

* Use `-` for unordered steps.
* Use `1.`, `2.`, `3.` when sequence matters.
* Sub-steps: `a.`, `b.`, `c.`

### 3.3 Action Style

* Use **imperative voice**: “Verify the checksum”, “Roll back the deployment”.
* Each bullet = **one atomic action**.
* Use consistent verbs: e.g., always “Verify”, not "Ensure", "Check", etc.

---

## 4. Control Structures

### 4.1 Loops

Phrase loops narratively:

```text
For every **user** in *user_list*, send a welcome email.
```

Close with an optional cue:

```text
(End per-user loop)
```

### 4.2 Conditions

Use natural sentence structure:

```text
If the test fails, then stop the run and notify QA.
```

Include alternate paths:

```text
Otherwise, archive the result and continue.
```

### 4.3 Error Handling

```text
If anything fails:

  - Roll back the component.
  - Notify the on-call channel.
  - Stop here and report the failure.
```

### 4.4 Invariants

Use emphatic tone for guardrails:

```text
ALWAYS test locally before merging.
NEVER touch the production database directly.
```

---

## 5. Resource Binding

Bind artifacts or objects clearly:

```text
Assume the *production database* and call it `prod_db`.
Assume the *current diagram* and call it `draft_tree`.
```

Stick to `snake_case` or use **bold**/ *italics* to clarify aliases.

---

## 6. Outputs & Handoffs

* End each phase with what was produced:

```text
You should now have: *deployment_report.md*
```

* Explicitly state handoff:

```text
Share the test results in the *#qa-team* channel.
```

---

## 7. Commentary & Notes

* Use parentheses for inline context:

```text
(This usually takes about 3 minutes to complete)
```

* Use `#` only for editor-facing notes.

---

## 8. Anti-Patterns to Avoid

| Bad Pattern                 | Why It Hurts                      | Better Practice                        |
| --------------------------- | --------------------------------- | -------------------------------------- |
| Mixed verb use              | Confuses execution semantics      | Use one verb per concept               |
| Nested conditionals >2 deep | Hides logic                       | Extract into a named subprocedure      |
| Implicit outputs            | Downstream steps become ambiguous | State outputs and destinations clearly |
| Missing error branches      | Human stalls on failure           | Provide rollback, retry, or escalate   |

---

## 9. Examples

### Loop Example

```text
For every **CSV file** in *incoming_data_files*:

  - Verify the header matches the schema.
  - If the file is malformed, then move it to *quarantine_dir* and continue.
  - Load the file into the staging database.
(End per-file loop)
```

### Conditional Exit

```text
If the deployment takes longer than 20 minutes, then stop here and call the SRE lead.
```

### Output Declaration

```text
You should now have: *dashboard_export_2025Q2.json*
Share this file with the *analytics-review@* group before Tuesday.
```

---

## 10. Adoption Strategy

* **Pilot it** in one SOP or design procedure.
* **Use templates** for recurring structures (loops, validations, error handlers).
* **Review quarterly** for clarity creep or structure drift.

---

## 11. Appendix: Quick Sentence Starters

| Purpose      | Phrase                      |
| ------------ | --------------------------- |
| Start a loop | For every **X** in *Y*, ... |
| Branching    | If *condition*, then ...    |
| Invariant    | ALWAYS ...                  |
| Wait/Gate    | Wait until *event*          |
| Error Path   | If anything fails:          |
| Output Cue   | You should now have: ...    |
| Handoff      | Share this with ...         |

---

## Final Note

The power of NF-PPL comes from making procedure feel conversational without sacrificing rigour. It invites scrutiny, enables delegation, and accelerates onboarding. Use it to document processes that are **human-first, logic-aware, and execution-ready**.