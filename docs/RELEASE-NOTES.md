# Release notes

## 0.7.0 — October 6, 2026

- Adds requested-actions for direct email sends, unsubscribe, selected-message archiving, calendar changes, Teams posts and SharePoint document changes, subject to live connector support. Each external action requires a direct user request; scheduled inbox and meeting runs stay draft-only.
- Adds sync-wrike-completion for clear full-task completion evidence in the user’s sent Outlook email and selected Teams conversations. Supports separate activation in the existing inbox controller, verified workflow status, partial-work review, source coverage, manual-reopening protection and readback.
- Keeps user accounts, selected sources, task scopes and standing permissions separate from shared plugin defaults. No existing schedule gains new actions through upgrade.
- Packages ten skills and adds behavioral pilot cases. Actual Microsoft write capabilities, client installation and end-to-end scheduled execution remain pending live verification.

## 0.6.0 — October 6, 2026

- Saves authorized Pocket attendee follow-ups as unsent drafts in the user’s connected Outlook mailbox, returning draft links/receipts instead of email bodies in chat.
- Verifies sender, recipients, draft status and content; preserves human edits, reuses existing drafts, and reconciles unknown saves before retry.
- Updates the hourly schedule prompt to authorize mailbox draft saves while preserving silence on successful no-new-meeting checks.
- Keeps missing access/recipient details pending and never sends email. Existing chat-only scopes are not widened by installing the update. Live mailbox delivery remains pending client pilot verification.

## 0.5.0 — October 6, 2026

- Adds a Spaces-based pocket-meeting-context skill adapted from Productivity and an hourly cloud workflow with separate summary, context, follow-up and Wrike stages.
- Renames the unreleased capture skill to pocket-summary-to-wrike to match the client prompt.
- Successful no-new-meeting runs return no user-facing output; failed checks are surfaced once rather than reported as empty successes.
- Adds client schedule instructions and an activation preflight; no personal schedule is activated by these documentation changes.

## 0.4.0 — October 6, 2026

- Adds pocket-summary-to-wrike for reading each saved Pocket report in the requested scope and capturing only clear assignments or accepted commitments to the connected user.
- Bundles wrike-tasks for identity/destination resolution, duplicate checks, task creation/reuse, and readback.
- Adds authorized manager and summary handoffs with per-report capture progress, revision handling, and unknown-outcome recovery. Existing users remain disabled for capture until they authorize it.
- Retains cloud-only recurring execution and supports explicitly supplied upstream Markdown reports for interactive capture.
- Packages seven skills; live Wrike and scheduled capture remain pending client pilot verification. No tasks or schedules are created by this release build.

## 0.3.2 — October 6, 2026

- Selects the public `shay-owensby/tlc-email-assistant` GitHub marketplace for the 15 individual Pro accounts; no collaborator invitations needed.
- Adds installation and targeted marketplace refresh commands with installed-version verification.
- Keeps personal rules in Spaces and cloud scheduling pending until the individual-account pilot passes.
- Publishes source through GitHub; no MCP service, invitations, or schedules created. Skill behavior unchanged.

## 0.3.1 — October 6, 2026

- Corrects the deployment assumption: all 15 users have individual ChatGPT Pro accounts.
- Supersedes 0.3.0 workspace-administrator instructions; no installation channel is claimed ready.
- Distinguishes direct hosted MCP, public plugin publication, and local GitHub installation.
- Clarifies that private repository installs need per-user read access and that a remote MCP connection on the web differs from workspace-import MCP restrictions.
- Skill behavior unchanged. Hosted service development/public submission and live individual-account tests remain pending.

## 0.3.0 — October 6, 2026

- Client delivery with separate administrator and end-user instructions.
- Private GitHub marketplace installation and controlled release updates for approximately 15 users.
- Manager readiness/recovery reference and a compact home section in the existing Settings Page.
- Expanded pilot cases and a blank rollout tracker.
- Five existing workflows retained; no sending, new app mutations, or automatic activation added.

Validation covers skill structure, manifests, local references, portable packaging, and archive readback. Client installation and live cloud behavior remain pending. No customer configuration, credentials, or mailbox contents are bundled.

## 0.2.0

Added manage-email-assistant, focused personal rule changes in Spaces, and one cloud controller per mailbox policy scope.

## 0.1.0

Initial setup-email, email-triage, pocket-meeting-summary, and pocket-meeting-follow-up bundle.
