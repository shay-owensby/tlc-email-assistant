---
name: manage-email-assistant
description: Coordinate the Email Assistant's daily inbox and Pocket meeting workflows, personalize saved rules, show status, and manage cloud activation or pause/resume. Use for ongoing assistant management and cross-workflow requests; use the bundled specialist skills for their individual jobs.
---

# Manage Email Assistant

Be the user's single point of contact for their Email Assistant. Coordinate the seven bundled specialist skills and keep personal configuration in ChatGPT Spaces. This skill supplies the orchestration instructions for a cloud scheduled task; installing it does not create an autonomous process or activate a schedule.

## Personalization model

The plugin supplies shared workflows. Each user owns their settings, inbox rules, context permissions, runtime state, and schedule. Do not edit installed SKILL.md files, plugin manifests, or another user's settings to implement a personal preference. Plugin upgrades must not overwrite these user-owned Pages or silently expand operating permission.

Resolve the authenticated user, workspace/tenant, mailbox, and provider from current connections and saved configuration. Read [references/settings.md](references/settings.md) for the durable settings contract. Use supplied canonical Page IDs first; otherwise search by the settings/profile title and exact account, then verify ownership and scope inside the Pages. An open Page or a matching title alone is not sufficient.

If setup is missing, use [setup-email](../setup-email/SKILL.md). Do not rerun full inbox discovery for a small rule change. If existing Pages can be reused, link them rather than making duplicates or copies of their active rules.

For shared mailboxes, separate personal display/digest preferences from mailbox-wide mutation policy. Establish the authorized policy owner and one operating controller for that shared mailbox. Do not start competing personalized mutation controllers for different users of the same inbox. If ownership or conflicting permissions are unresolved, stay in preview for that mailbox.

## Route the request

| User intent | Workflow |
| --- | --- |
| Set up the assistant or first inbox profile | Run setup-email; collect only additional meeting, digest, and cloud scheduling preferences needed for the requested workflows. |
| Add/change/remove a rule, VIP, source, style, or follow-up preference | Apply the focused change process in [references/rule-changes.md](references/rule-changes.md). |
| Review/maintain inbox, prepare replies, categorize, or archive | Run [email-triage](../email-triage/SKILL.md) under the active operating scope. |
| Summarize a meeting | Run [pocket-meeting-summary](../pocket-meeting-summary/SKILL.md), which handles the follow-up handoff unless excluded. |
| Run all Pocket stages hourly with silent empty checks | Follow [hourly Pocket workflow](references/pocket-hourly.md), using the bundled cloud-storage versions and separate stage receipts. |
| Add historical context to a saved report | Run [pocket-meeting-context](../pocket-meeting-context/SKILL.md). |
| Draft a follow-up from an existing meeting report | Run [pocket-meeting-follow-up](../pocket-meeting-follow-up/SKILL.md) with the existing report/handoff. |
| Add assigned work from saved Pocket summaries to Wrike | Run [pocket-summary-to-wrike](../pocket-summary-to-wrike/SKILL.md), which delegates capture to [wrike-tasks](../wrike-tasks/SKILL.md). Require the report scope and task-capture authorization. |
| Add another explicitly requested task to Wrike | Run [wrike-tasks](../wrike-tasks/SKILL.md). |
| Status, explain a decision, preview | Read current settings, profile, runtime receipts, and scheduler state. Do not mutate mail. |
| Start, pause, resume, or change schedule | Follow cloud controller management below. |

Apply specialist skills in the same run, reusing verified context. Do not create separate chats, agents, or schedules merely to route a task. A specialist invoked by the controller must not activate its own schedule.

Distinguish one-time directions from ongoing rules. “Draft this reply” is a one-time action; “Always draft replies from this sender” is a standing rule. Ask when intent is unclear. Changing a rule affects future matching work by default; historical reprocessing requires a separately identified scope.

## What users can customize

Support plain-language changes to sender/subject rules, VIPs, permitted draft/category/archive actions, exceptions, reply style, signature, allowed context sources, follow-up thresholds, meeting scope, report destination, digest detail, notifications, cadence, timezone, and quiet hours. Record exact scope rather than translating a narrow instruction into a broad domain rule.

A preference cannot add a missing connector capability or override the plugin's no-send boundary. Requests to send email, post to Teams, book meetings, or edit SharePoint content remain outside these workflows. Wrike is read-only context during email triage; only a separately authorized task-capture request or standing scope invokes pocket-summary-to-wrike or wrike-tasks for writes. Resolve the user and writable destination before activation. An upgrade must not enable capture for existing users. Do not promise additional actions by saving a free-text rule.

## Daily or recurring controller run

1. Load current settings, profile, operating authorization, runtime records, and cloud task identity. Stop dependent writes if the user paused/revoked them, approval is unclear, or account/version/scope does not match. Settings/profile Pages are durable context, not blanket authority for new actions.
2. Use the serialization and recovery contract in [email-triage runtime](../email-triage/references/runtime.md). Establish one run ID; specialist execution shares that run's verified lease/ownership instead of trying to lock against itself. Manual runs use the same coordination mechanism.
3. Determine which workflows are enabled and due from saved cadence and last verified progress. Daily review is the default proposed experience, but do not invent its time or create a schedule before the user supplies/approves it. The controller can run more frequently for inbox checks while emitting a daily digest at the user's selected time.
4. Run email-triage on new/changed inbox items and due follow-ups, respecting backlog and per-run limits. A saved draft remains pending user review.
5. If meeting monitoring is authorized, discover new recordings in the approved Pocket account/folder/date scope. Page through that scope and compare recording IDs with the cloud meeting index. Process unhandled recordings through pocket-meeting-summary. Also resume pending index/follow-up stages from runtime state even when the report is already indexed; reuse that saved report rather than regenerating it. Reuse the summary skill's follow-up output; do not run the follow-up skill twice. When historical context is enabled, defer the summary’s automatic follow-up until pocket-meeting-context completes or is safely skipped, then produce the follow-up once. Track report/index/context/follow-up outcomes separately so a partial failure does not recreate a completed report.
6. Meeting follow-ups are saved as unsent drafts in the user’s connected Outlook mailbox under the authorized draft scope. The pocket-meeting-follow-up skill owns mailbox resolution, draft lookup/save/readback, human-edit preservation and unknown-outcome recovery; do not perform a second save in the controller. Keep a recording-to-draft reference and verification status in runtime. Return the saved draft link or subject, not the email body in chat. Missing mailbox access or authorization leaves only that stage pending; upgrades do not broaden an existing chat-only scope. Never send.
7. If Pocket task capture is independently authorized, run pocket-summary-to-wrike on every new/revised saved report in the approved report scope and pending capture retries, including reports already indexed or generated by the Productivity skill. Track capture separately so a completed summary or failed email follow-up cannot hide uncaptured assignments. Reuse an existing same-run capture receipt rather than invoking it twice. Report collection access must be available in the cloud; local report paths are not a scheduled fallback. This stage does not require new-recording summary monitoring to be enabled.
8. Persist each workflow's verified checkpoint and pending work. A failure in Pocket must not hide a successful inbox run; continue independent authorized work where safe. Do not advance past a retrieval gap or count partial work as complete.
9. Return one combined update according to the notification settings: urgent items, drafts ready for review, due follow-ups, new meeting reports, verified Wrike task links and pending assignments, verified category/archive counts, and decisions or failures needing attention. Link to usable sources without copying sensitive content. Avoid separate specialist notifications for the same outcome. Stay quiet on unchanged/non-actionable runs unless the user requested a daily all-clear.

If a scheduled run needs input, record the question in the pending-decisions section, notify once, and skip only the dependent action. Do not wait indefinitely, invent an answer, or repeatedly ask the same unchanged question. Process user answers through the focused change workflow on the next interactive turn.

## Readiness and recovery

For onboarding, activation, connection failures, upgrade verification, or offboarding, read [operations](references/operations.md). Keep a compact home section in the existing Settings Page and distinguish verified live operation from saved configuration.

## Cloud controller management

- Use the live host's supported cloud scheduling tools. Verify the actual runtime is cloud and the task can access the installed plugin and connected apps without a local computer. Never use local Codex heartbeats, local cron, local files, or a local browser session as a fallback. If only local scheduling is exposed, keep activation pending and explain the missing capability.
- Before activation, show the enabled workflows, mailbox/recording scopes, proposed outcomes, schedule/timezone, notifications, runtime storage, and any missing permissions. Reuse authorization already supplied for that concrete scope. Verify a representative live run and a scheduled cloud run before calling the service operational.
- Maintain one cloud controller per authorized mailbox/policy scope. An explicitly requested separate Pocket-only schedule follows [hourly Pocket workflow](references/pocket-hourly.md) and must not overlap meeting processing in an inbox/combined controller. Resolve existing task IDs from runtime/settings and the live scheduler. For a user-approved consolidation, preserve old task history, pause superseded workers, and verify they are inactive before enabling the replacement. If migration fails, report which controller is active or paused; do not leave two active workers.
- The saved task prompt references this skill, exact user/account identity, canonical settings/profile/runtime/index Page IDs, authorized workflows and limits, and cloud-only execution. Read current Pages each run rather than embedding a stale rule copy as the authority. Store returned task IDs and verify settings after scheduling changes.
- Honor “pause” or a revoked action immediately within available controls. Disable the relevant cloud task or action, persist the restriction, and verify status; do not require approval to stop. In-flight work may have already committed, so reconcile its last receipts and report any inability to stop it. Resume only after explicit user direction and a check that the former approved scope is still valid; resume is not permission to broaden scope.

## Status and rule explanations

Report the verified enabled/paused state, cloud task identity and next run when available, last successful run, pending failures/questions, and current profile version. Separate a saved configuration from a verified operational workflow. For “why did you archive this?”, cite the exact rule/version and recorded message action, not a reconstructed guess.

For unsupported new workflows, identify the missing capability or specialist workflow instead of modifying the shared plugin on behalf of one end user. Normal preferences remain user-owned data and survive plugin updates. Finish interactive changes with a short receipt stating what changed, where it was saved, when it takes effect, and any portion still awaiting approval or verification.
