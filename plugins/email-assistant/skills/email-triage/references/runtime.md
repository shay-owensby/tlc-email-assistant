# Runtime state and recovery

Use this contract for mutating runs and recurring activation. The approved inbox profile contains inbox preferences; the runtime record contains operating authorization and execution history. Keep them separate so routine logging cannot change approved rules. Other workflows reuse coordination and recovery with their own authorized action/source/task scope. They do not require an Inbox Triage Profile unless they also execute profile-based inbox triage; mark inapplicable profile fields accordingly rather than inventing a profile or blocking independent work.

## Capability checks

Inspect the current tool schemas rather than assuming provider parity. Require only operations needed for the authorized action. Inbox triage may need account identification, paginated inbox/thread and sent-mail reads, draft discovery/creation/readback, label/category inventory and changes, archive destination/movement, and durable state reads/writes. A specified-message archive does not require drafting or categorization tools; a Wrike completion run requires its source/task/status tools, not mailbox mutation tools. Only require draft update support if updating a verified assistant draft is needed. Recurring writes always require durable state and safe coordination.

If a capability is missing, continue independent supported work within scope and report the affected action as unavailable. Do not simulate a mailbox draft in a Page and call it delivered, treat a category as a folder move, or call a send operation to make a reply draft. Never guess an API's side effects or bypass tool approval requirements. An interactive approval requirement can make that action unsuitable for unattended execution; report it rather than assuming the schedule will bypass it.

## State record

Use an existing authorized runtime store, or create the disclosed ChatGPT Spaces state Page after activation authorization. Read its current content before writing; use observed hashes/sequences and inspect all receipts. Keep its audience no broader than the authorized profile destination. If a known private destination is unavailable, do not silently fall back to a shared location.

Keep these fields:

- Account/provider, profile Page ID, approved profile version and exact active rule snapshot or digest.
- Operating authorization evidence/date, allowed actions and rule IDs, excluded actions, initial backlog scope, per-run limits, and expiry if any.
- Scheduler ID/status, cadence/timezone, notification policy, context source references, runtime state Page ID/link, linked personal settings Page, verified owner/workspace identity, configuration revision, and pause/revoked-action flags.
- Last fully covered retrieval cursor/interval, any pagination continuation, overlap policy, retry queue, and tracked follow-up due dates.
- Current run ID, lease owner/expiry or verified scheduler serialization guarantee, start/end times, coverage and outcome summary.
- Action ledger entries: account, stable message/thread identity, current provider ID, inbound revision/fingerprint, rule ID/version, action/destination, idempotency key, before-state, planned/confirmed/failed/unknown status, tool receipt, verification time, and resulting draft/message ID.
- Assistant draft ownership: draft ID and last verified content fingerprint; enough metadata to detect a human edit without storing full body text.

Keep the ledger minimal, without full bodies or attachments. Summarize old run summaries if necessary, but preserve the identifiers needed to avoid duplicates, unresolved outcomes, and outstanding follow-ups. Storage limits are not permission to discard unresolved action history.

## Prevent overlap and duplicate actions

Use a single recurring controller per authorized mailbox scope. Manual runs must share the same state and coordination mechanism. Before mutations, use a documented serialization guarantee or acquire a short-lived lease with a conflict-guarded write to the shared state; reread to verify ownership. A successful unguarded write is not a lock. If neither serialization nor a reliable guarded lease is available, do not enable unattended mutations.

An active unexpired lease held by another run means skip this run. Renew a lease before it expires; if it cannot be renewed, stop writes. Recover an expired lease only after rereading the ledger and reconciling unfinished operations. Release only your own lease. A lease prevents overlapping agents; it does not prevent the human user from changing their mailbox, so recheck message state before writes.

Specialist work invoked by the orchestrator in the same run reuses that run's verified lease and owner ID; it must not acquire a competing lease or release its caller's lease. Direct/manual runs still coordinate with the controller. Check current pause/revocation and configuration revision at action boundaries; version mismatch leaves dependent writes blocked until the approved profile and operating scope are reconciled.

Derive each action key from mailbox identity, stable message/thread identity, inbound revision, rule ID/version, and action/destination. A timestamp alone is not a deduplication key. A new inbound message can reopen a previously processed thread. A profile revision may justify reevaluation, but it must not cause a duplicate draft for an already-handled inbound message. Draft lookup and actual mailbox state take precedence over a missing or stale ledger entry.

Persist planned actions before executing them, then record each result and verify it. For multi-step work, verify the prerequisite before attempting the next action. If state persistence fails, stop starting new writes; recover outstanding actions from the mailbox before resuming.

## Checkpoints and follow-up

A provider change cursor is preferred when available. Otherwise rescan an overlap window using received/modified times supported by that provider, then deduplicate against mailbox state and the ledger. An inbox containing read mail still needs coverage. If modified-time search is unavailable, use a bounded inbox reconciliation to catch changed threads and explicitly track due follow-ups.

On first activation, process only the agreed backlog. If a page limit or run budget interrupts retrieval, record the continuation and processed interval rather than moving the checkpoint to the current time. Advance the coverage checkpoint only after all items in the interval have been evaluated and each planned action is verified or durably recorded for retry. Never move it past an unresolved retrieval gap.

Recheck due follow-ups against latest inbound, sent mail, and drafts before acting. A sent reply, a new response, or user cancellation can close or reset the obligation. A saved draft cannot. Use approved thresholds; record business-day assumptions and do not invent a holiday calendar.

## Failure recovery

- Definite rejection with no commit: keep the action pending, correct only a supported cause, and retry within the connector's guidance and current run limits.
- Timeout or unknown commit: read the mailbox and draft list before any retry. If the action is already present, verify and record it; if the outcome remains uncertain, keep it unknown and request attention. Do not blindly repeat a draft creation or folder move.
- Partial batch success: retain verified successes and retry only the rejected/unfinished items. Keep counts separate.
- Authorization/account mismatch, changed execution scope, or an inaccessible/unapproved profile when that workflow requires one: stop dependent writes and surface the issue. For non-profile workflows, check their own explicit operating scope. Other unrelated mailbox accounts are not substitutes.
- User changes during execution: preserve the user's current state. Do not overwrite a human draft or automatically reverse a manual unarchive/category change. Record it for clarification when the ongoing rule needs adjustment.

When the user requests reversal, use the recorded before-state and current mailbox state to restore only assistant changes within that request, preserving subsequent human changes. Do not perform a broad automatic rollback after a partial failure; reconcile first.
