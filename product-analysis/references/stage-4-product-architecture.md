# Stage 4 — Full Product Architecture

Use this stage after reviewing raw evidence and available Stage 1–3 artifacts. Missing prior artifacts are evidence gaps, not permission to invent them.

## Classification

Use four distinct classes:

- Confirmed
- Reasonable inference
- Recommended design
- Unknown

Never confirm backend language, database, queue, object storage, CDN, cloud, model gateway, or vendor from frontend behavior alone.

## Fact Sources

Inventory user operations, chats, Agent labels, buttons/forms, canvas assets, history, model choices, tool/runtime results, errors, billing displays, official sources, and reproducible read-only observations.

## Core Product Domains

Inspect account/permission, entry/project management, script, style, character/consistency, scene, prop, storyboard, video, audio/voice, preview/editor, versions, asset library, sharing/publishing, billing, errors, and task state. An entry point does not prove the backend capability is complete.

## End-to-End Flow

Track one complete creation task through five parallel views:

1. User interaction
2. Agent control
3. Tool calls
4. Data/global context
5. Image/video/audio assets

For each step record trigger, processor, reads, decision, tools, result, state write, confirmation, next recipient, and failure branch.

## Nine Layers

Analyze without assuming confirmation:

1. User and channel
2. Interaction/workbench
3. Product application
4. Agent/workflow orchestration
5. Tools/services
6. Model access/routing
7. Global context/data
8. Knowledge/public assets
9. Infrastructure/governance

## Global Context

Do not use one undifferentiated context box. Consider semantic domains such as:

- UserContext
- ProjectConfig
- ScriptContext
- CharacterContext
- SceneContext
- PropContext
- StoryboardContext
- AssetContext
- WorkflowState
- BillingContext
- EvaluationContext

These are architecture templates until visible evidence confirms names or fields.

Do not assume every context domain or listed field exists. Before placing a current-state field in the architecture, audit its existence, value, producer write, consumer read, and downstream use. Include unsupported domains only as clearly classified inference or recommended design, with a design reason.

## Knowledge Architecture

Separate project data from reusable knowledge. Address:

- Professional and cinematic knowledge
- Model capability knowledge
- Style knowledge
- Prompt templates
- Safety/copyright and billing rules
- User-private assets vs platform-public assets
- Temporary project data
- Feedback/model-performance data

Explain how style becomes model-executable constraints, how character references are reused, where camera-language knowledge comes from, how model limits are known, why safety/billing should be tool-enforced, whether feedback persists, and how private/public assets are isolated.

## Technical Selection

For each area state required capability, possible technology category, recommended design, and why current implementation cannot be confirmed. Cover workbench, orchestration, state machine, async tasks, model gateway, tools, context storage, structured business data, media storage/CDN, versions, queue, confirmation/cancel, billing hold, safety, tracing, evaluation, knowledge retrieval, and tenant isolation.

When models are material to the request, read [model-implementation-audit.md](model-implementation-audit.md). Separate product ownership from model evidence, separate the conversational model from media models and deterministic services, and provide current alternatives only as dated recommended designs backed by official model sources.

## Entities and Diagrams

Consider User, Project, Conversation, Agent, AgentRun, Workflow, Task, ToolCall, Script, Character, Scene, Prop, Storyboard, Asset, AssetVersion, UserConfirmation, ModelInvocation, Error, BillingRecord, and Feedback as analysis templates.

Provide:

- Entity table
- Mermaid ER diagram
- Key relations
- Evidence-backed relations vs inferred relations
- Mermaid sequence diagram for a representative scenario, clearly labeling assumptions
- Layered product panorama

For the panorama, group each layer in its own `subgraph`. Label edges with call, read, write, event, confirmation, asset reference, or state update. Use solid lines for confirmed, dashed for inference, and dotted or a special color for recommendation. Include a legend and current validation failures.

## As-Is, To-Be, and Risk

Separate current architecture from recommended architecture. Evaluate:

- Single source of truth
- Result/length/style/dialogue-sync validation
- Asset dependency invalidation
- Retry idempotency
- Balance estimate and hold
- Agent completion gate
- End-to-end tracing
- Model feedback
- Local recomputation after edits

Prioritize risks including cross-surface state conflict, verbal completion before tool completion, asset/context write mismatch, stale downstream assets, duplicate charges, duration drift, style drift, safety error, cancellation propagation, private-asset leakage, stale knowledge, and stale model capability rules.

## Delivery Order

1. One-sentence executive summary
2. Evidence and gaps
3. Core domains
4. End-to-end flow table
5. Layered architecture
6. Agent/tool/context relationship
7. Global-context architecture
8. Knowledge/public-asset architecture
9. Model access/routing
10. Technical selection table
11. Entity table and ER diagram
12. Sequence diagram
13. Product panorama
14. As-Is
15. To-Be
16. Risks
17. Component-evidence traceability
18. Remaining unknowns

Do not include a component in the main panorama unless it has evidence or a clear design reason and classification.
