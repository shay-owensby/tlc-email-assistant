# Email Assistant

Includes manage-email-assistant, setup-email, email-triage, pocket-meeting-summary, pocket-meeting-follow-up, pocket-meeting-context, pocket-summary-to-wrike, and wrike-tasks. Install through a verified delivery route for the client’s individual ChatGPT Pro accounts and connect Outlook Email, Pocket AI, and ChatGPT Spaces/Pages capabilities separately. Outlook Calendar, Teams, SharePoint, and Write Like Me are optional context/style integrations. Wrike supplies read-only inbox context and is required for separately authorized task capture.

Use manage-email-assistant as the main entry point. It runs setup-email for initial preferences and manages later personal rule changes in Spaces. Review the proposed profile, then authorize email-triage within its approved scope. Meeting summaries save to Spaces and produce a follow-up draft unless excluded. The meeting follow-up skill saves unsent drafts in the user’s connected Outlook mailbox under the authorized scope, verifies them, and returns a brief receipt. Chat is not the email delivery destination. Use pocket-summary-to-wrike to read saved reports and add only clear assignments or accepted commitments through the bundled wrike-tasks skill. Resolve each user’s identity and existing writable destination, check duplicates, and verify saved tasks. The manager can coordinate this for future reports after explicit activation; installation alone does not enable capture. No skill sends email.

The hourly Pocket workflow runs summary, historical context, one attendee follow-up, and assigned-task capture. Successful checks with no new meetings produce no output or notification. Each stage has independent progress so retries do not duplicate reports, drafts, or tasks.

All recurring tasks must run in the cloud; local scheduled tasks and local report storage are not fallbacks. Installation does not start a schedule. Validate connected actions and one scheduled cloud run before relying on unattended triage.

This is a skills-only package. It contains no customer data, credentials, custom MCP server, or automatic integration installation. The marketplace release also includes onboarding and pilot instructions.

Personal settings and rules are stored separately from this shared plugin and preserved across upgrades. The manager coordinates enabled workflows through one authorized cloud task; specialist skills do not create duplicate schedules.

The client has no shared Business/Enterprise workspace. The marketplace source alone does not establish cloud installation or updates for these users. The delivery guide describes the remaining channel decision and pilot.
