# Evidence Policy

Read this reference for every reverse-analysis stage.

## Evidence Classes

Use the labels requested by the user. When no labels are specified, use:

- **Confirmed / Page fact** — directly visible in the page, official source, or reproducible read-only result.
- **Reasonable inference** — supported by multiple facts but not directly visible as implementation.
- **Recommended design** — a proposed mechanism that would make the system safer or more reliable.
- **Unknown / Unconfirmed** — current evidence is insufficient.

Stage 1 commonly uses `页面事实 / 合理推断 / 尚未确认`. Architecture work commonly uses `已确认 / 合理推断 / 建议设计 / 未知`. Do not collapse recommended design into inference.

## Evidence Strength

Prefer evidence in this order for claims about user-visible completion:

1. Actual playable/rendered/exported output and its metadata
2. Asset existence plus a successful validation/preview result
3. Tool or runtime result tied to a task and asset
4. Canvas or asset card state
5. Task state
6. Agent statement or chat summary

This is a reasoning aid, not permission to discard conflicts. When sources disagree, record every source and label the claim as a conflict.

## What Counts as Execution

Confirm an action only when at least one execution artifact is visible:

- Asset created or changed
- Task or workflow state changed
- Tool result or runtime event appeared
- Page result or validated preview appeared

Do not promote these to execution evidence:

- “I will…” plans
- Public “thinking complete” or “planning complete” summaries
- An Agent’s statement that a result meets requirements
- A button or entry point that was not used

## Field Existence and Use Gate

Never assume all fields in an analysis template exist. Treat these as five separate claims that require separate evidence:

1. **Existence** — a field, label, object, card, selector, or serialized value is visible.
2. **Value** — the current value is readable, not merely the field label.
3. **Write** — a producer or user action visibly creates or changes it.
4. **Read** — an Agent, tool, page, or rule visibly depends on it.
5. **Consumption** — a downstream step visibly receives, references, or changes behavior because of it.

One claim does not prove the others. For example, a balance shown in the header proves a visible balance value; it does not prove a specific Agent reads it. A downstream image resembling a style does not prove a `style_id` field exists.

For important candidate fields, use a field-evidence audit:

| Candidate field/object | Existence evidence | Visible value | Write evidence | Read evidence | Downstream consumer | Conclusion | Evidence ID |
|---|---|---|---|---|---|---|---|

Apply these conclusions:

- Visible evidence supports only the specific visible claim.
- Behavior that requires some mechanism may support a reasonable inference, but not an official field name or schema.
- A field that should exist for a robust design is a recommended design.
- No evidence means unknown, not confirmed absent.
- A visible empty state may confirm that the page currently shows no records; it does not prove the backend stores none.

## Chronological Inspection

1. Inventory all evidence files and visible browser states.
2. Establish chronology from message order, timestamps, stage transitions, and asset mutations. Filenames may assist but cannot be the sole basis.
3. Start from the earliest user input and inspect every confirmation, modification, retry, error, and handoff.
4. Inspect chat and non-chat surfaces together: buttons, forms, cards, canvas, task panel, history, asset library, model selector, preview/editor, errors, and billing displays.
5. Assign stable evidence IDs such as `E-001` or screenshot IDs such as `S01`.

## Conflict Protocol

For each conflict, record:

- Source A and exact visible state
- Source B and exact visible state
- Whether either source has stronger validation evidence
- What can and cannot be concluded
- What read-only evidence would resolve the conflict

Common conflicts include chat “completed” vs missing assets, task “idle” vs executing cards, canvas assets vs empty library, preview failure vs completion message, and history/version mismatch.

## Safe Collection Boundary

- Browser inspection is read-only by default.
- Do not send messages or trigger product mutations merely to obtain evidence.
- Do not view or output credentials, tokens, cookies, auth headers, or sensitive identity data.
- If evidence collection requires generation, payment, deletion, publication, or overwriting, stop and request explicit authorization.
- External facts must come from official product pages or official documentation unless the user explicitly asks for broader research.

## Claim Hygiene

- Quote only short, necessary page text.
- Separate visible labels from analyst-created semantic names.
- Do not infer hidden chain-of-thought, official prompts, official function names, database tables, infrastructure vendors, or orchestration protocols.
- If an upstream modification should invalidate downstream assets but no behavior is visible, label the invalidation rule as recommendation or unknown, not current fact.
