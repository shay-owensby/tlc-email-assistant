# Hourly Pocket meeting workflow

Use this reference when the user requests hourly Pocket reports, historical context, attendee follow-ups, and assigned-task capture. Run the bundled `pocket-meeting-summary`, `pocket-meeting-context`, `pocket-meeting-follow-up`, and `pocket-summary-to-wrike` skills in one cloud task. The bundled copies store reports in Spaces; upstream Productivity copies that require local files cannot replace them in a cloud-only schedule.

## Establish once

Resolve the connected Pocket account and recording/folder scope, private or explicitly chosen report/index/runtime Pages, current Wrike user and writable parent, timezone, and initial recording scope. Record a baseline of existing recording IDs when the user wants future meetings only; do not process historical meetings without permission. Establish the provider's supported change discovery or a paginated reconciliation window that can find late uploads and delayed transcripts, not just recordings dated since the last hourly run. Disclose any coverage limit before activation.

Record permission to save reports/context, return attendee follow-up text, and capture only clear user assignments through Wrike Tasks. Do not infer permission to send email or save mailbox drafts. Persist exact account/source/destination references, baseline, authorization, stage receipts, and quiet-run preference in the private runtime Page. Each user has their own configuration. Installation is not activation.

Inspect existing cloud schedules before creating one. Reuse a task already covering this Pocket scope. A user-requested separate Pocket task may coexist with the inbox-only task: explicitly exclude meeting processing from the inbox task and avoid overlapping Pocket controllers. If an existing combined manager already handles these meetings, update its meeting cadence or perform a user-authorized handoff with verified pause rather than duplicating it. Share serialization for shared runtime resources. Do not activate a local heartbeat or cron fallback.

Use an interval of **60 minutes**, cloud execution, and the user's timezone. Keep the user's chosen model/effort. Verify the saved task, runtime, and next run; a configured schedule is not a verified executed workflow. Test a representative cloud run and a no-new-meeting run before claiming unattended readiness.

## Each run

1. Load live settings, runtime, baseline and pause flags. Verify identities and take/reuse the authorized run lease. Retrieve the complete requested discovery scope with pagination; compare stable recording IDs and stage receipts. Keep a continuation on truncation. Failed or incomplete retrieval is not a successful no-new-meeting check.
2. For every eligible unprocessed recording, retrieve the full transcript once and run `pocket-meeting-summary`. Explicitly defer its automatic email follow-up and Wrike handoff to the following controller stages; deferral applies only to this run and does not cancel authorization. Save/read back the report and index. A verified report with an index failure can still feed independent downstream stages.
3. Run `pocket-meeting-context` with that report and index. It compares only relevant earlier reports and verifies the context section/index. No relevant history is a normal skip. A failed context edit does not require regenerating the report or block unrelated supported actions.
4. Run `pocket-meeting-follow-up` once from the verified report/evidence, including verified context when appropriate to attendees. Keep the result as review-only text. Save the draft text/reference in the private report/runtime destination for retrieval across new chats; no Outlook draft or email send is authorized by this workflow. Reuse an existing stage result on retry.
5. Run `pocket-summary-to-wrike` with the verified report and approved destination; it applies `wrike-tasks` to clear assignments/accepted commitments, checks existing work, and reads back saved tasks. Keep ambiguous items pending. Do not use speculative context commentary as a new assignment.
6. Persist separate report, index, context, follow-up, and Wrike statuses and task/draft references. Resume only unfinished stages, including recordings awaiting a complete transcript. Reconcile unknown writes before retry. Advance coverage only after discovery is complete or gaps/continuations are durably retained. Do not count a summarized recording as fully processed before the remaining stages are resolved.

## Quiet output

On a successful complete check with **no new eligible meeting**, return no user-facing text, notification, empty report, acknowledgment, or “no new meetings” message. Specialists return internal receipts to this controller instead of publishing their own summaries. Pending stages may resume silently; preserve results for the next relevant review. Do not send an all-clear digest.

When a new meeting is processed, return one concise result with the verified report link, attendee follow-up draft, and verified Wrike task links plus material unresolved items. Avoid duplicate notifications on replay. An unavailable connector, incomplete discovery, or required decision is a failure/blocked check, not evidence of no new meetings; surface that issue once and suppress unchanged repeats. If the scheduler cannot suppress routine empty-run notifications, disclose that limitation rather than promising complete silence or muting all meaningful meeting results.
