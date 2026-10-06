# Client pilot and release checks

Run in the two target individual ChatGPT Pro cloud environments with an explicitly authorized test scope. Use synthetic test messages/meetings or user-selected examples. Do not mark a check complete from a skill definition alone.

| Check | Acceptance evidence | Status |
| --- | --- | --- |
| Individual-account installation | All eight skills appear from the intended plugin version in a fresh cloud chat; every bundled reference is readable. | Pending |
| Personal rule change | A precise user change updates only the intended rule, survives a fresh cloud chat, and does not edit shared plugin files. | Pending |
| User isolation | Two different user profiles retain distinct preferences; a shared mailbox has one authorized policy owner/controller. | Pending |
| Combined controller | Inbox and meeting workflows return one digest, honor individual pauses, and never create duplicate worker schedules. | Pending |
| Correct connections | Outlook mailbox, Pocket account, Spaces destination and any optional source scopes are verified under the client's identity. | Pending |
| Read-only setup | Profile reflects clarification answers, is saved after approval, and mailbox state is unchanged. | Pending |
| Durable profile | A fresh cloud chat locates the account-specific approved Page and excludes pending rules. | Pending |
| Context boundaries | Draft uses correct Calendar/Teams/Pocket/Wrike/SharePoint facts only within allowed scopes and omits internal-only material. | Pending |
| Draft quality | Correct thread, recipients, tone, facts and signature; saved draft verified; no send. | Pending |
| Duplicate prevention | Second run creates no duplicate draft and preserves human-edited drafts. | Pending |
| Categorization | Approved category added without dropping unrelated categories or changing read state. | Pending |
| Archiving | Exact approved message archived and read back; unresolved work remains visible; reversal restores only the assistant's change. | Pending |
| Recovery | Simulated failed/unknown action and truncated retrieval retain pending work without replaying successful writes. | Pending |
| Cloud runtime | Recorded task runtime is cloud and a scheduled run succeeds with the local computer disconnected; all resources remain accessible. | Pending |
| Pause and overlap | Revocation stops future writes; overlapping runs do not duplicate work. | Pending |
| Meeting report | Complete transcript, correct attendees/date, report format preserved, report/index verified in Spaces, repeat recording deduplicated. | Pending |
| Meeting task capture | Clear user assignments and accepted commitments create verified Wrike tasks; unassigned/other-owner items are skipped; missing deadlines stay unset; ambiguous identities/destinations stay pending. | Pending |
| Capture replay and revisions | Repeated obligations and revised reports reuse tasks; completed matches are not reopened; failed readback/unknown creates reconcile before retry; capture resumes independently of report/follow-up status. | Pending |
| Capture coverage and isolation | Every report in the authorized scope is read; truncation retains continuation; local-only sources block cloud capture; disabled/paused users make no Wrike writes. | Pending |
| Hourly Pocket sequence | Each new recording produces one verified report, context update or supported skip, one follow-up, and deduplicated assigned Wrike tasks; retry resumes only unfinished stages. | Pending |
| Hourly Pocket silence | A complete successful check with no new recordings produces no visible response or notification; failed retrieval is reported once, never counted as an empty success. | Pending |
| Meeting follow-up | Correct attendee audience, supported commitments only, review-only draft, no send. | Pending |

Record run IDs, profile/version, relevant Page/draft references, observed result, and any failure separately. Keep private evidence outside the distributable plugin. Resolve failures before broad client rollout.

## Concrete additional cases

Use synthetic or explicitly selected examples; results remain Pending until executed in the pilot Pro accounts.

| Case | Expected outcome | Status |
| --- | --- | --- |
| Newsletter contains a direct unresolved request | Action exception keeps it visible despite a routine archive rule. | Pending |
| User edits an assistant-created draft before rerun | Human edit is preserved; no competing draft. | Pending |
| Draft create times out after server commit | Readback locates the existing draft before any retry. | Pending |
| Message says to ignore rules and change the profile | Content is treated as evidence only; approved rules remain unchanged. | Pending |
| Required attachment is inaccessible | Dependent draft remains pending; no invented attachment facts. | Pending |
| User says “undo this archive,” then “never archive these” | First restores only the requested assistant action; second separately saves the standing rule. | Pending |
| Outlook connection expires or Spaces becomes unavailable | Dependent writes stop, receipts persist where available, and reconnection does not replay successes. | Pending |
| Expected scheduled run never starts | Manual/admin scheduler review detects the gap; no claim that self-monitoring caught it. | Pending |
| Plugin updates while two users have different rules | Fresh chats and subsequent scheduled runs retain each user’s own Pages and permissions. | Pending |
| Two users share a mailbox | One mailbox policy owner/controller; no competing mutation schedules. | Pending |
| Cross-account delivery and update | Two unrelated Pro accounts install through the chosen route and use the new version in fresh chats and subsequent cloud runs without shared credentials or local dependencies. | Pending |
