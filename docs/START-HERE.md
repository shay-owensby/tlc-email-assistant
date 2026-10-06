# Email Assistant — GitHub delivery

Release 0.7.0 · October 6, 2026 · Unchained

For approximately 15 users with individual ChatGPT Pro subscriptions. GitHub is the selected distribution route; the repository is public and users need no collaborator invitations. No shared ChatGPT workspace or custom MCP server is assumed.

1. Open [the public repository](https://github.com/shay-owensby/tlc-email-assistant); the deployment owner maintains it using [the owner guide](ADMIN-GUIDE.md).
2. Two pilot users follow [the user guide](USER-GUIDE.md).
3. Verify both installation and an update, then verify cloud scheduled access with computers disconnected. Local installation alone does not meet the cloud requirement.
4. Onboard the remaining thirteen after the required pilot checks pass.

Repository: [shay-owensby/tlc-email-assistant](https://github.com/shay-owensby/tlc-email-assistant), branch `main`. This archive is a validated source package, not an activated service.

The delivery contains the standalone plugin ZIP, marketplace source ZIP, guides, a blank rollout tracker, pilot checks, release notes, validation report, and checksums. Extract the marketplace ZIP and publish its CONTENTS at the repository root, including hidden `.agents` and `.codex-plugin` folders. Do not upload the outer delivery ZIP as the plugin.

Users refresh the Git marketplace for updates and verify their installed version. Their personal profiles and rules stay in Spaces. No customer data or credentials belong in the shared repository.
