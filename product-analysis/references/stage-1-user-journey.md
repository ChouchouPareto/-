# Stage 1 — User Journey

Use this stage when the goal is to reconstruct the user’s experience from initial need to final output. Do not analyze hidden Agent calls, prompts, or backend architecture.

## Inspect

- Initial request, supplied script, style, reference materials, uploads, and form selections
- First product response and every requested confirmation
- What changes in chat, canvas, task state, and assets after each confirmation
- Continue, modify, alternative choice, interrupt, back, retry, preview, edit, download, and publish affordances
- Normal generation, user correction, generation failure, insufficient balance, interruption, and inconsistent state
- Buttons, options, Agent labels, role/scene/prop/storyboard cards, history, task state, model selector, preview/editor, error messages, and recovery actions

Do not infer that the user supplied a script, style, reference image, voice, or preference merely because a downstream result exists. Find the original visible submission or mark the source as unconfirmed.

## Evidence Table

Use these columns unless the user specifies another schema:

| Stage | User goal | User action | Page feedback | Decision required | Page/asset state change | Problem/friction | Evidence |
|---|---|---|---|---|---|---|---|

Evidence cells should name exact visible text, button labels, Agent names, assets, errors, and screenshot/page IDs.

## Journey Diagram

Use exactly three swimlanes when requested:

1. User
2. Product interface
3. System result

Every node should state the user goal/action, interface feedback, decision, next state, and failure recovery. Use diamonds for decisions and label branches explicitly, such as:

- satisfied / dissatisfied
- success / failure
- continue / interrupt
- sufficient balance / insufficient balance

Include normal, correction, and failure/interruption paths. Link every material node to evidence IDs.

## Experience Layer

Add, when requested:

- User emotion by stage
- Likely thoughts and concerns
- Observed pain points, clearly separated from editable analyst notes
- Product opportunities for a comparable product
- Three highest-value UX discussion questions

Do not claim a final video exists merely because an Agent or card says it is complete. Verify preview/playback/export evidence.

## Stop Gate

Stop after the journey deliverable. Do not continue into Agent contracts, prompt reconstruction, tool lists, or global architecture unless the user requests the next stage.
