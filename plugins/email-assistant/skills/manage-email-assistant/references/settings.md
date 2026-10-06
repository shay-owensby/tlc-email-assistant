# Personal settings and source ownership

Use a private or explicitly selected ChatGPT Spaces Page titled `Email Assistant Settings for <user label>`. Include exact authenticated user/workspace identifiers when available, mailbox/provider, and links to the canonical Inbox Triage Profile, Email Triage State, and scoped Pocket Meeting Index. Where IDs are unavailable, record the verified identity evidence rather than inventing them. Ask which resource is authoritative if duplicate candidate Pages remain.

Do not create a new settings Page for a read-only status request. During setup/activation or an authorized preference change, create the disclosed Page if needed; otherwise reuse it. Do not copy private settings to a shared destination without the user's direction. Use current Page schemas, guarded edits, and readback.

## Ownership

- Settings Page: enabled workflows; meeting scope and destinations; digest style; cloud scheduling preferences; pending decisions; canonical resource/task links; configuration revision.
- Inbox Triage Profile: approved inbox rules, VIPs, drafting style, exceptions, source permissions, and rule version. Keep this as the single source of truth for inbox behavior. In an older profile, schedule fields are proposed preferences; after activation, the settings Page and verified scheduler govern the actual schedule.
- Runtime state: operating authorization, exact active rule/configuration snapshot, task ID, pause/revocation flags, progress, leases, action receipts, draft ownership, and retry queue.
- Meeting index: one record per recording with verified report reference; store follow-up status/draft references and separate per-report task-capture status/receipts in runtime state when needed.

Never let a second copy of an active rule silently disagree with the profile. If linked data conflicts, read the live scheduler and current approved records, then ask only for unresolved policy choices. Scheduler state establishes whether a task is enabled, not whether it is authorized to perform a new action.

## Compact settings format

- Owner/user and workspace/tenant; mailbox/provider; shared-mailbox policy owner if applicable.
- Configuration revision and last confirmed change date.
- Canonical profile/runtime/index Page IDs and links.
- Enabled workflows: inbox triage, due follow-up review, Pocket reports, optional historical meeting context, meeting follow-up text, optional authorized Outlook meeting drafts, optional authorized Pocket-to-Wrike task capture (disabled until explicitly enabled).
- Pocket scope: account/folders, initial date cutoff, attendee/audience handling, report/index destination.
- Wrike capture: connected account and canonical user ID, verified writable parent ID/type/name, source report/index references, initial backlog and per-run limits, authorization and runtime ledger reference. Keep this separate from read-only Wrike context permissions.
- Digest: delivery in the cloud task, preferred length, notification conditions, daily time/timezone, quiet hours, optional all-clear. For the hourly Pocket workflow, successful no-new-meeting runs must produce no output or notification; do not apply an inbox all-clear preference to Pocket.
- Cloud controller: actual task ID, requested cadence/timezone, verified runtime/status, optional stop date, last verification.
- Operating scope reference: permitted action/rule IDs and approval evidence held in runtime; no automatic activation from settings alone.
- Pending decisions: stable question ID, affected workflow/rules, date first raised, status, and resolution reference.
- Change history: concise user instruction, before/after meaning, affected rule IDs, approved revision, and effective scope/date. Avoid storing full emails/transcripts.

Missing workflow settings mean disabled/pending, not implicit permission. An unavailable optional app must not block unrelated enabled work.

## Updates and direct edits

Users can request preferences conversationally or review/edit their own Page where the host allows. A manual Page edit is a proposed change until its affected behavior is reconciled with explicit operating authorization. Do not treat an edited approval heading as proof of permission. Prefer conversational updates for a verified change receipt and coordinated versioning.

Plugin releases update shared instructions only. Preserve all user Pages, saved task IDs, and operating history. If a new release requires a new field, ask for that field or apply a clearly documented non-mutating default; do not rerun setup, replace the profile, or enable a new action automatically.
