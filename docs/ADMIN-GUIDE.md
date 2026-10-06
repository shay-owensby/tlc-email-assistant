# GitHub distribution and updates

Email Assistant 0.3.2 · Approximately 15 individual ChatGPT Pro users

GitHub is the selected distribution route. No custom MCP server is needed for this route. The public repository is [shay-owensby/tlc-email-assistant](https://github.com/shay-owensby/tlc-email-assistant), using branch `main`. The instructions below describe direct Codex/desktop marketplace installation; cloud scheduled access remains a separate pilot requirement.

## Prepare the repository

The owner selected public GitHub distribution. Keep the following marketplace layout at the repository root, including hidden folders:

```text
.agents/plugins/marketplace.json
plugins/email-assistant/plugin.json
plugins/email-assistant/.codex-plugin/plugin.json
plugins/email-assistant/skills/
docs/
scripts/build_release.py
README.md
PILOT.md
```

Keep credentials, mailbox content, saved personal rules, completed rollout trackers, and private pilot evidence out of GitHub. The included `.gitignore` excludes common local/private output paths but is not a substitute for reviewing staged files.

Users can retrieve this public repository without collaborator invitations or private repository authentication. Do not grant repository write access merely for installation. Their ChatGPT and connected-app sign-ins remain separate.

Release source: `shay-owensby/tlc-email-assistant`, branch `main`, version 0.3.2. The deployment owner should provide the client support contact separately. Publish only tested changes to `main`. Users follow that branch when they refresh their marketplace.

## Pilot installation

Use [USER-GUIDE.md](USER-GUIDE.md) with two users first. Verify local installation and an update using separate accounts. Then test whether the installed plugin, all bundled references, connections, and private Spaces Pages are accessible in each user's ChatGPT Work cloud run with their computer disconnected.

A successful local install is not evidence that web/cloud tasks can load a GitHub marketplace plugin. If cloud access is unavailable, record that limitation and leave recurring activation pending. Do not replace the required cloud schedule with a local task or silently build a different hosting solution. Resolve the cloud delivery gap before onboarding the other thirteen for unattended use.

## Publish updates

1. Edit the plugin source, increment the version in both manifests, and add release notes. Keep personal settings in Spaces.
2. Run skill validators for changed skills and `python3 scripts/build_release.py`.
3. Test changed behavior and preserve existing user rules, Page IDs, schedules, and draft ownership records.
4. Commit and push reviewed source changes to `main` in the public repository. Check the remote version after pushing.
5. Tell users the released version and ask them to refresh the marketplace using the user guide. A source-code push is not proof that their installed plugin has updated.
6. Verify the version in a fresh chat and then verify the next scheduled cloud run if that capability passed the pilot. Do not create duplicate controllers to refresh a plugin.

The documented refresh command is `codex plugin marketplace upgrade unchained-email-assistant`. Verify the installed plugin version afterward. If it remains stale, inspect the supported plugin install/update controls and their outcome instead of assuming marketplace refresh updated every cached install. Do not promise automatic daily workspace sync to these individual accounts.

For rollback, publish the last tested content as a new version and use the same refresh/verification process. Pause affected actions first if a regression could change mail. A plugin rollback does not undo historical mailbox actions or replace users' rules.

## Support and rollout

Use [PILOT.md](../PILOT.md) and a private copy of [ROLLOUT-TRACKER.csv](ROLLOUT-TRACKER.csv). Complete the two-user pilot before onboarding thirteen more. Each user connects their own Outlook, Spaces, and optional Pocket/context apps and approves their own operating scope. A shared mailbox needs one policy owner/controller, not competing controllers from every user.

Agree a support contact and missed-run review procedure. A task that never starts cannot report its own failure. Verify actual account usage before widening cadence/backlog. Stop dependent writes on connection/state failures and reconcile receipts before retries. Do not delete or transfer user records without their authority. On offboarding, stop and verify schedules before removing connections or repository access; removing repository access does not prove that cached plugins or schedules stopped.

Official references checked October 6, 2026: [marketplace commands](https://learn.chatgpt.com/docs/developer-commands), [packaging and distribution](https://developers.openai.com/plugins/build/plugins), [cloud scheduled tasks](https://learn.chatgpt.com/docs/automations).
