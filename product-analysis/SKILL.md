---
name: product-analysis
description: Reverse-engineer AI creation products from screenshots and browser-visible chats, controls, canvas assets, task states, and errors into evidence-graded user journeys, Agent contracts, one-Agent functional-equivalent prompts, or full product architecture. Use for observable product-behavior analysis; do not use to claim hidden chain-of-thought or unobserved backend implementation.
---

# 产品拆解 / Product Analysis

Turn observable product evidence into reusable product and Agent architecture artifacts without presenting inference as fact.

## Start Here

1. Identify the product, evidence location, requested stage, output format, and whether a target Agent is named.
2. Read [references/evidence-policy.md](references/evidence-policy.md) for every stage.
3. Inventory evidence with `rg --files` and inspect it chronologically. Do not treat filenames alone as proof.
4. Reuse prior-stage artifacts when available, but re-check their claims against the raw evidence before promoting them to facts.
5. Route to the smallest stage that satisfies the request:
   - User journey: read [references/stage-1-user-journey.md](references/stage-1-user-journey.md).
   - Agent contracts: read [references/stage-2-agent-contracts.md](references/stage-2-agent-contracts.md).
   - One-Agent functional-equivalent System Prompt: read [references/stage-3-agent-prompt.md](references/stage-3-agent-prompt.md).
   - Full product architecture: read [references/stage-4-product-architecture.md](references/stage-4-product-architecture.md).
6. If HTML is requested, also read [references/html-delivery.md](references/html-delivery.md).
7. If the request asks what models are used, how the visible Agent may be implemented, or which market models could reproduce it, also read [references/model-implementation-audit.md](references/model-implementation-audit.md).

## Four-Stage Workflow

The stages are composable but have different evidence boundaries:

1. **User journey** — describe what the user submits, sees, decides, changes, interrupts, and receives. Do not analyze Agent internals.
2. **Agent contracts** — identify only Agents actually visible in evidence, then model inputs, observable decisions, functional tools, outputs, context reads/writes, and handoffs. Do not write a full System Prompt.
3. **One-Agent prompt** — choose one explicit target Agent and translate its contract into a functional-equivalent prompt, state machine, traceability table, and tests. Do not claim official prompt recovery.
4. **Product architecture** — integrate user, Agent, tool, model, data, asset, state, billing, safety, and infrastructure views while separating current evidence, inference, recommendation, and unknowns.

When the user requests all stages, complete them in order and preserve stage gates. Do not silently skip a stage. Before claiming the set is complete, verify that every requested artifact exists.

## Non-Negotiable Invariants

- An Agent saying “completed” is evidence of a message, not evidence that assets, state, or quality are complete.
- A plan or public “thinking/planning complete” summary is not a confirmed tool call.
- Confirm execution only through a visible tool result, asset mutation, state mutation, or page result.
- Record conflicts between chat, task state, canvas, asset library, preview, and history; never choose one source without saying why.
- Use functional tool names when official names are absent and label them “functional name, not official tool name.”
- Never assume a candidate field, object, status, context domain, asset reference, or history record exists because a typical product would need it. Search for separate evidence of existence, value, producer write, consumer read, and downstream use; otherwise classify it as inference, recommendation, or unknown.
- Do not infer a fixed number of Agents, a hidden orchestrator, official schema, backend language, database, queue, cloud, model gateway, or vendor from product behavior alone.
- Do not reveal or seek cookies, tokens, passwords, auth headers, private credentials, or unnecessary personal data.
- Treat browser inspection as read-only unless the user separately authorizes a mutation. Do not generate, regenerate, publish, delete, purchase, recharge, or overwrite assets during evidence collection.
- Use only official product sources when external research is necessary to establish product facts. Third-party commentary may inspire questions, never confirm architecture.
- A product's owner, cloud ecosystem, UI label, or file/folder name is not proof of the Agent role, foundation model, image model, or model version. Record the visible identity first; treat vendor-stack affinity as inference and the exact model/version as unknown until a page or official mapping confirms it.

## Evidence Work Pattern

Maintain an evidence ledger with stable IDs. Each material claim should point to at least one of:

- Screenshot/page identifier and visible text
- Button, form option, Agent label, asset card, history entry, task status, model option, error, or billing display
- Official product page or documentation
- Reproducible read-only result

For every output, distinguish visible labels from the analyst’s semantic field names. Names such as `WorkflowState`, `AssetVersion`, or `CharacterContext` are analysis templates unless the product visibly exposes them.

Do not turn an analysis checklist into a list of product facts. For every candidate field, explicitly ask: Is it visible? Is its value visible? Is a write observable? Is a read or behavioral dependency observable? Is a downstream consumer observable? Record each answer independently.

## HTML Requirement

Whenever this skill creates or edits HTML, the main agent must load `ui-ux-pro-max`, announce why it is being used, and apply its accessibility, responsive, color, and interaction guidance. If that skill is unavailable, say so and use a self-contained accessible fallback rather than pretending it was applied.

After generating an HTML report, run:

```bash
python3 scripts/validate_html_report.py path/to/report.html
```

Also perform content checks specific to the selected stage; structural validation does not prove evidence quality.

## Completion Gate

Before delivery:

- Confirm requested sections are present and ordered.
- Confirm all local evidence links resolve.
- Confirm evidence labels are used consistently.
- Confirm conflicts and unknowns remain visible.
- Confirm no placeholder target, TODO, or scaffold text remains.
- Confirm the final artifact does not claim hidden reasoning or unobserved implementation.
- If multiple stage files were requested, list them in order and verify each exists.
- Reconcile the user's expected input/artifact count with the actual inventory and state any mismatch before claiming completeness.
- State the exact output location in the final response and link every created deliverable.
