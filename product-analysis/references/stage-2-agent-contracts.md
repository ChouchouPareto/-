# Stage 2 — Agent Contracts

Use this stage to identify Agents actually visible in the observed scenario and describe their behavioral I/O contracts. Do not assume a standard Agent count and do not write a complete System Prompt.

## Agent Inventory

For each visible Agent label, record:

- First appearance and evidence ID
- Trigger and upstream stage
- Whom it appears to replace or succeed
- Downstream handoff
- Whether it visibly re-enters after modification or failure
- Expected roles that do not appear in this scenario

Distinguish an Agent identity from a chat container, project shell, task view, or orchestrator hypothesis.

## Six Input Sources

Inspect each Agent for:

1. User current input
2. User long-term information
3. Project global context
4. Upstream Agent output
5. Platform public assets, knowledge, and rules
6. Tool and runtime results

Do not mark balance, membership, assets, Face IDs, voices, history, permissions, or preferences as inputs merely because they could exist. Require visible evidence that they exist; require stronger evidence that the Agent reads them.

For every candidate global-context field, audit existence, visible value, write, read, and downstream consumption separately. Do not populate the field table from the checklist by default. If only a semantic need is evident, use a clearly marked analysis placeholder rather than a claimed product field.

## Observable Decisions

Summarize functional decisions, not hidden reasoning:

- Problem being solved
- Required-input completeness
- Next-step selection
- User confirmation gate
- Automatic continuation
- Mandatory stopping conditions
- Modification handling
- Tool failure handling
- Completion criteria
- Whether result quality was actually validated

Label every rule by evidence class.

## Tool Contract

When no official name is visible, use a functional name and append “functional name, not official tool name.” Separate:

- Planned or verbally described action
- Visible execution attempt
- Confirmed result
- Failed or conflicting result

Record input, precondition, visible result, failure/retry evidence, state write, and evidence ID.

## Five Output Types

Inspect:

1. User-facing response
2. Page interaction output
3. Text/image/video/audio asset output
4. Global-context write
5. Downstream task and handoff package

## I/O Contract Card

Use this ten-part format for every Agent:

1. Core goal
2. Trigger condition
3. Inputs by the six source types
4. Observable decisions
5. Tools
6. Outputs by the five types
7. Context read/write table: object, read/write, producer, consumer, timing, evidence class, evidence
8. Completion condition
9. Exceptions and retries
10. Unconfirmed questions

## Global Data Flow

After all cards, map producer-to-consumer relationships. Explicitly inspect:

- Multiple versions of the same data
- Chat/canvas/task/asset consistency
- Stable references from role/scene/prop to storyboard
- Downstream invalidation after upstream change
- Read-only or write-only fields
- Agent verbal completion without global-state update

## Recommended Delivery Order

1. Scope and evidence gaps
2. Agent inventory
3. I/O contract cards
4. Tool summary
5. Global-context field table
6. Producer-consumer table
7. Input-decision-tool-output-handoff flow with capability boundaries
8. Fact/inference/unknown list
9. Five highest-value validation questions

Stop before writing a full System Prompt.
