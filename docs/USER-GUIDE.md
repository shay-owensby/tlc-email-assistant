# Install Email Assistant from GitHub

For individual ChatGPT Pro users · Release 0.3.2

Email Assistant learns how you handle email, saves your approved rules in ChatGPT Spaces, and uses them to prepare reply drafts, categorize messages, and archive approved matches. It can also summarize Pocket AI meetings and draft follow-ups. It never sends email.

## Install once

1. Open [tlc-email-assistant](https://github.com/shay-owensby/tlc-email-assistant). It is public: no collaborator invitation or GitHub sign-in is required to read it.
2. Use a supported Codex/desktop marketplace interface. These commands run in a terminal with Codex CLI installed, not in ChatGPT's web composer. If `codex` is unavailable, ask the deployment owner to help set up the supported client. This public source requires no private GitHub token. Sign in to Codex with your own ChatGPT account when prompted.
3. Run:

```sh
codex plugin marketplace add shay-owensby/tlc-email-assistant --ref main
codex plugin add email-assistant@unchained-email-assistant
codex plugin list --marketplace unchained-email-assistant --json
```

The first command follows the `main` release branch. Confirm the installed Email Assistant version matches the release they provided, then start a fresh chat. If it does not appear, restart the desktop app and inspect marketplace errors with your support contact.

## Personalize

Connect your own Outlook account and Spaces capabilities. Connect Pocket AI for meeting workflows and optional sources only when needed. Ask:

> Help me set up my daily email assistant. Check my connections first.

Answer the questions, review the proposed rules, and approve the private save destination. Setup leaves your mailbox unchanged. Then ask:

> Preview triage using my approved rules without changing mail.

Correct the preview and authorize a small live pilot on specific messages. Review saved replies in Outlook Drafts; meeting follow-ups appear in the task unless you authorize saving them in Outlook too. You review and send messages yourself.

## Cloud scheduling

Your deployment owner must first verify that this GitHub-installed plugin and its references are available in your ChatGPT Work cloud environment. A local installation alone is not enough. If unavailable, leave scheduling pending and contact the deployment owner. Do not use a local scheduled task as a substitute.

After that check passes, provide your preferred days, time, timezone, permitted actions, and notifications. Confirm a scheduled cloud run succeeds with your computer disconnected. Installing the plugin does not activate a schedule.

## Get updates

When the owner announces a new release, run:

```sh
codex plugin marketplace upgrade unchained-email-assistant
codex plugin list --marketplace unchained-email-assistant --json
```

Confirm the installed version matches the announced release, then start a fresh chat. If the installed version is unchanged, use the supported plugin update/install controls with your support contact; do not assume the refresh completed the update. A successful cloud pilot should also check the subsequent scheduled run's version where available. Your personal rules remain in Spaces.

## Everyday requests

- “Never archive invoices.”
- “Keep my replies short and use this signature.”
- “Show my pending questions and drafts.”
- “Why did you archive this message?”
- “Undo the archive action on this message.”
- “Pause automatic archiving, but keep preparing drafts.”
- “Pause my email assistant.”

Check the confirmation that your rule was saved and when it takes effect. One-time requests do not automatically become permanent rules. A quiet assistant does not prove a successful run; check status or Scheduled.
