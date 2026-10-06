# Email Assistant

Ten reusable skills for inbox maintenance, Pocket AI meetings, requested connected-app actions and Wrike completion, designed for ChatGPT Work with cloud scheduling. This folder is the distributable source package and local marketplace. It is distributed through a public GitHub marketplace; it is not a public ChatGPT directory listing or an activated automation.

## Client delivery

Start with [the delivery guide](docs/START-HERE.md), then use the [deployment guide](docs/ADMIN-GUIDE.md) for GitHub distribution and updates and the [user guide](docs/USER-GUIDE.md) for individual setup. The package includes a blank tracker for 15 users. GitHub distribution is selected; per-user installation, updates, and cloud access still need a pilot.

## Included skills

| Skill | Purpose |
| --- | --- |
| manage-email-assistant | The main entry point for daily coordination, personal rule changes, status, and cloud pause/resume. |
| setup-email | Analyze email habits, clarify preferences, obtain approval, and save an Inbox Triage Profile in ChatGPT Spaces. Mailbox read-only. |
| email-triage | Use the approved profile and operating permission to save reply drafts, categorize messages, and archive matching mail. Never send. |
| pocket-meeting-summary | Read a complete Pocket AI transcript, save an executive report and meeting index in Spaces, and hand off to the follow-up skill unless excluded. |
| pocket-meeting-follow-up | Draft a concise attendee email using confirmed meeting facts and the user's style. Saves and verifies an unsent draft in the user’s connected Outlook mailbox under the authorized scope; returns a receipt, not the email body in chat. Never send. |
| pocket-meeting-context | Compare a saved report with relevant past meetings in Spaces and reconcile supported open-item changes. |
| pocket-summary-to-wrike | Read each saved Pocket report in scope and hand clear assignments/accepted commitments to wrike-tasks, preserving source evidence and capture progress. |
| wrike-tasks | Add authorized tasks to the verified user and destination, reuse existing work, and read back every creation or update. |
| requested-actions | Carry out direct requests to send email, unsubscribe, archive selected mail, change calendar events, post Teams messages, and create/edit SharePoint documents when supported. |
| sync-wrike-completion | Complete clear full-task matches from the user’s sent Outlook email and selected Teams conversations within an explicitly enabled scope. |

The summary, context, and follow-up Pocket skills were copied with their supporting resources from the installed Productivity plugin, version 0.1.3. Only the bundled copies were adapted for cloud storage and portable delivery; the installed Productivity plugin was not changed. The Wrike Tasks skill is bundled from the supplied standalone skill so client installations do not depend on the author’s local skill folder.

## Recommended client host

Use ChatGPT Work with verified cloud scheduled tasks. All required skills, connections, profiles, and runtime state must be available in the cloud. Local Codex tasks, local files, browser sessions on a laptop, and local schedulers are not fallback execution paths. Codex can be used to author and test the package.

Cloud tasks can use connected tools and installed skills, subject to account and workspace access. Confirm a real cloud run before promising unattended operation. [Scheduled task documentation](https://learn.chatgpt.com/docs/automations)

## Connections

These are separately installed/authorized integrations, not bundled credentials or automatically installed dependencies.

| Capability | Required for | Setup check |
| --- | --- | --- |
| Outlook Email | Inbox setup and triage; saved meeting follow-up drafts | Confirm the correct mailbox, reads, reply draft creation/readback, categories, folder resolution, and reversible archive actions. For direct requests, also verify send semantics and supported unsubscribe methods. |
| ChatGPT Spaces / Pages | All durable profiles, runtime state, meeting reports and index | Confirm read, search, create, guarded edit, and readback in the selected private/client destination. |
| Pocket AI | Meeting summaries and follow-ups sourced from recordings | Confirm full transcript retrieval and recording identity under the client's account. |
| Outlook Calendar | Availability/context and directly requested event changes | Verify allowed calendars, timezone, availability, supported writes, organizer rights and invitation behavior. |
| Teams | Context, directly requested posts, and selected completion evidence | Verify selected channels/chats, authorship, message/reply retrieval, and post/readback capabilities when requested. |
| Wrike | Inbox context, authorized task capture and completion checks | Verify user, destinations, task details/activity, workflow statuses, writes and readback. Capture and completion need separate authorization; triage context stays read-only. |
| SharePoint | Document context and directly requested creation/edits | Verify exact sites/libraries/files, audience, supported file types, content writes and version-safe readback. |
| Write Like Me | Optional style assistance for meeting follow-ups | If unavailable, the existing skill uses supplied examples/preferences and a concise fallback. |

Do not assume installed apps in the author's account are available to the client. Microsoft tenant policy or the ChatGPT workspace may require administrator involvement. Read access does not establish write capability or unattended approval. A user-managed connection and a team service account are different identities; do not substitute one for the other.

The package deliberately has no .app.json or custom MCP server. It uses independently connected integrations; app IDs from another account are not portable credentials.

## Distribute to the client

Use a GitHub marketplace for the client's approximately 15 individual ChatGPT Pro accounts. The source repository is public, so users need no collaborator invitation or private GitHub credentials. Follow [the owner guide](docs/ADMIN-GUIDE.md) and [user installation/update instructions](docs/USER-GUIDE.md). Repository: [shay-owensby/tlc-email-assistant](https://github.com/shay-owensby/tlc-email-assistant), branch `main`.

This route needs no custom MCP server or shared ChatGPT workspace. Its documented installation path is local Codex/desktop. Verify access to the plugin and every reference from a cloud scheduled run with the computer disconnected before claiming the cloud-only requirement is met. If unavailable, keep activation pending; local scheduling is not a fallback.

## Client onboarding

1. After the individual-account delivery route passes its pilot, install Email Assistant from that verified source and connect Outlook Email, Pocket AI, and Spaces capabilities. Connect optional sources only when relevant.
2. Start ChatGPT Work in the cloud. Select Email Assistant and ask: “Help me set up my daily email assistant.” The manager routes initial setup, records personal settings in Spaces, and asks you to approve the profile and save destination.
3. Ask: “Preview inbox triage using my approved profile. Do not change mail.” Review proposed replies, categories, archive rules, and missing context.
4. Authorize a bounded live pilot. Confirm saved drafts, preserved categories/read state, and reversible archiving on agreed messages. Run it again to check for duplicates.
5. Specify cloud schedule, timezone, initial backlog, limits, notifications, and optional stop date. Authorize the operating scope and runtime-state storage. Confirm one manager-controlled cloud task per mailbox policy scope. It coordinates enabled inbox and meeting workflows; do not create competing specialist schedules.
6. Verify at least one scheduled cloud run without local dependencies and review the first few outcomes. Configure pause/revocation and recovery before wider rollout.
7. To capture assigned meeting work, ask: “Use $pocket-summary-to-wrike to read all Pocket meeting reports in this collection and add clearly assigned tasks to my Wrike task list.” Supply the report/index and confirm the destination when no default exists. For future reports, explicitly enable capture in the manager’s existing cloud controller; installing the update does not enable it.
8. For meetings, ask: “Summarize this Pocket AI meeting in Spaces and draft the attendee follow-up.” Meeting skills run on demand unless included in the manager’s authorized cloud schedule.

Where a host uses a plugin-qualified skill name, select the installed skill from its menu rather than assuming a standalone local `$skill-name` is available.

## Before client rollout

Use release 0.7.0 in `dist/`; older ZIPs are retained as historical artifacts. See [PILOT.md](PILOT.md). Structural validation is complete only when reported in `dist/VALIDATION.md`; live Microsoft/Pocket/Spaces behavior and cloud scheduling remain unverified until tested in the client's environment. Packaging does not activate schedules or write to mailboxes.

## Personalize without editing the plugin

Each user keeps an Email Assistant Settings Page, an approved Inbox Triage Profile, and runtime state in Spaces. The manager reads those records on every run. Users can say:

- “Never archive invoices.”
- “Keep my reply drafts short and use this signature.”
- “Summarize only Pocket recordings in this folder.”
- “Pause automatic archiving, but keep preparing drafts.”
- “Show me what you did today and why.”

Clear user instructions authorize their exact requested changes. The manager asks only for missing scope or additional permission, records the change, and reports when it takes effect. One-time requests do not become permanent rules. Direct edits to a settings Page are reconciled with operating authorization before they change automatic behavior.

The shared plugin defines supported workflows; personal Pages define each user’s preferences. Upgrading the plugin preserves those Pages. Wrike task capture uses its bundled specialist workflow with separate authorization. Sending, unsubscribe, calendar changes, Teams posts and SharePoint changes require a direct user request for each action or specified batch, and supported live connector operations. They cannot be enabled as standing automatic rules. Clear-evidence Wrike completion may run after separate activation for sent Outlook email and selected Teams conversations, normally at the inbox controller cadence. A personal rule cannot add missing connector capabilities. For shared mailboxes, establish one authorized mailbox-wide policy instead of conflicting per-user mutation controllers.

## Rebuild the release

From this source folder, run `python3 scripts/build_release.py`. It validates package paths, manifests and references, builds versioned plugin/marketplace ZIPs, rereads their contents, and writes checksums and the structural validation report to `dist/`. It does not install, publish, connect accounts, or activate schedules. Run the skill-creator validator separately for changed skills before release.
