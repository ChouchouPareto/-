# Stage 3 — One-Agent Functional-Equivalent Prompt

Use this stage for one named Agent only. The goal is behavioral equivalence under similar inputs, tools, and context—not recovery of an official prompt.

## Target Gate

Require a concrete target Agent supported by Stage 2 evidence.

- If the request still contains a placeholder and multiple Agents are plausible, ask one concise question before producing the prompt.
- If the user explicitly orders immediate continuation without choosing, select the Agent with the strongest end-to-end evidence and state the assumption prominently.
- Do not mark Stage 3 complete until a target-specific artifact exists.

## Evidence Boundary

Collect every appearance of the target Agent and answer:

1. Problem solved
2. Takeover point
3. Trigger
4. Downstream recipient
5. In-scope work
6. Out-of-scope work
7. Modification re-trigger behavior
8. Mandatory stop conditions
9. Automatic continuation conditions
10. User-confirmation requirements

## Contracts

Build:

- Input contract using the same six source types as Stage 2, marking required vs optional
- Output contract covering user response, components, assets, context writes, and downstream task
- Tool contract with preconditions, confirmation, validation, retry evidence, idempotency risk, interruption, and state-write failure
- State machine covering observed or carefully designed equivalents of waiting, planning, confirmation, execution, validation, feedback, retry, failure, interruption, completion, and handoff
- Mermaid state diagram

## Rule Derivation

Translate evidence into rules labeled:

- Fact rule
- Inference rule
- Recommended rule
- Unknown

Cover identity, goal, boundary, input checks, context reads/writes, workflow, tool choice, tool preconditions, confirmation, validation, modification, rollback, failure, retry, interruption, handoff, completion, and output format.

## Functional-Equivalent System Prompt

Use this structure:

1. Agent name
2. Role
3. Core goal
4. Task boundary
5. Input contract
6. Global-context protocol
7. Workflow
8. Tool-call protocol
9. User-confirmation mechanism
10. Result validation
11. Modification and rollback
12. Exception handling
13. State machine
14. Downstream handoff
15. Completion conditions
16. Output format

If the user requires the original 15-section form, place the Agent name above section 1 and preserve their numbering.

Use semantic placeholder fields and angle-bracket tool names when official formats are unknown. Mark them as design placeholders.

Do not copy every candidate field from the Stage 2 checklist into the prompt. Include a read/write field only when evidence supports it or the field is explicitly labeled as an inference/recommended placeholder. A visible field does not prove the target Agent can read it; an inferred read does not grant write permission.

## Stability Requirements

- A tool success response is not sufficient; validate asset existence, references, content constraints, metadata, and cross-surface state.
- Paid or bulk execution, overwriting confirmed assets, and downstream handoff require structured confirmation records when applicable.
- Upstream changes should create new versions and invalidate dependent assets; label this as recommendation when behavior is not visible.
- Retry counts are unknown unless observed. If suggesting a default, label it as a recommendation and defer to platform policy.
- On interruption, state-write failure, insufficient balance, safety block, or state conflict, do not claim completion.

## Traceability and Tests

After the prompt, provide a rule-to-evidence table and at least six tests:

1. Complete normal input
2. Missing required input
3. Local modification
4. Tool failure
5. User interruption
6. Context/page state conflict

Add insufficient balance, safety block, duplicate request, or downstream failure when relevant. Each test should include input, initial state, expected decision, expected tools, expected state change, and prohibited behavior.

Stop after the chosen Agent. Do not continue into other Agents unless requested.
