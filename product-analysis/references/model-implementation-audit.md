# Model and Implementation Audit

Read this reference when the user asks what model powers a visible AI feature, requests a system-prompt analysis tied to model behavior, or wants open/closed models for building a similar product.

## Separate Five Different Claims

Never collapse these into one “model” claim:

1. **Visible product or Agent identity** — the name shown in the UI.
2. **Foundation model** — the text/multimodal model that interprets and generates.
3. **Specialized media model** — image, video, audio, speech, or embedding model.
4. **Deterministic tool/service** — creates validated records, URLs, IDs, submissions, billing entries, or task states.
5. **System Prompt and workflow policy** — instructions and state gates that shape behavior.

A model may emit a structured action request; it should not be credited with creating a real URL, submitting a product, changing billing, or writing a verified business state unless a visible tool/service result supports that action.

## Vendor and Version Evidence Gate

- Company ownership or ecosystem affinity may justify a **reasonable inference** about likely model families; it never confirms an exact deployed model.
- A visible “AI-generated” label confirms AI involvement only at that surface. It does not identify the vendor, model family, version, or which parts were generated.
- A model selector, response metadata, official product-to-model mapping, or reproducible official result can confirm only the fields it actually exposes.
- If the version is not visible, write `unknown`; do not substitute the vendor’s current flagship version.
- Prompt analysis must remain functional-equivalent. Model behavior does not reveal the official hidden System Prompt.

Use a trace table:

| Capability | Visible evidence | Confirmed component | Likely implementation | Exact model/version | Confidence | Evidence |
|---|---|---|---|---|---|---|

## Capability Decomposition

For each visible feature, decide which layer should own it:

- Conversation, intent classification, explanation, and structured action proposal → conversational/multimodal LLM.
- Main-image generation or editing → image model plus asset storage and media validation.
- Clickable card/link construction → schema-constrained model output plus deterministic route/entity service.
- Product creation, audit submission, payment, permissions, and task state → deterministic business services with authorization and idempotency.
- Recommendations → rules/statistics/recommender and possibly an LLM explanation layer; do not assume the LLM calculated the recommendation.
- Safety, billing, and publishing constraints → service-enforced controls, not Prompt-only rules.

## Market Alternative Research

When the user wants to build a similar product:

1. Research current candidates using primary official model documentation or official repositories. Model versions change; record the research date.
2. Include both closed API and open-weight candidates when they are realistically relevant.
3. For each candidate record exact model/version or family, openness/license, suitable role, key benefit, constraints, deployment implications, and official source.
4. Compare task-level stacks rather than ranking one model for everything: conversational/tool-use model, image/media model, deterministic services, retrieval/knowledge, safety, and evaluation.
5. Selection criteria should include structured-output/tool-call success, Chinese/domain quality, image text rendering and reference consistency, latency, cost, data residency/privacy, deployment effort, license, safety controls, and version stability.
6. Label every candidate stack as **recommended design**, never as current-product evidence.

Prefer a small set of deployable reference stacks (for example, domestic managed API, international managed API, and private/open-weight) over an undifferentiated catalog. Require an evaluation set based on the observed workflow before choosing a production model.

## Delivery Checks Learned from Prior Reviews

- Inventory evidence chronologically and reconcile the expected number of inputs with the files actually accessible.
- Do not let folder names override what the screenshots visibly identify.
- Include a model transparency section when the report promises a full architecture or the user asks about model versions and benefits.
- If System Prompt analysis is requested, include a functional-equivalent prompt with evidence traceability and state clearly that it is not the official prompt.
- Preserve explicit visual direction across related reports, while keeping accessibility and responsive behavior.
- End with exact artifact paths and clickable links so the user can locate the deliverables immediately.
