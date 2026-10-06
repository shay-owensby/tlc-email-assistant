---
name: pocket-meeting-summary
description: Create an executive report and meeting index from a Pocket AI meeting, then draft an attendee follow-up unless excluded.
---

# Pocket Meeting Summary

Write for an absent C-suite reader, leading with matters needing attention and then deeper context. Base claims on the complete Pocket AI transcript and metadata; generated summaries or search hits do not replace the transcript.

## Retrieve once

Read [retrieval](references/retrieval.md) for current tool selection, full-transcript retrieval and pagination. Use the requested recording; otherwise choose the latest by recording date. Verify identity and ask only when genuinely ambiguous. If Pocket AI or the full transcript is unavailable, report the limitation and stop without a report/index entry; do not substitute memory or another source.

Retain recording ID/source, title, confirmed attendees, meeting date and timezone. Unknown title/attendees are `Not provided`; owners, invitees and mentioned people are not automatically attendees. Preserve unidentified speakers. Use Pocket's date/timezone, or disclose the known client timezone fallback for a timestamp lacking one. Ask if the meeting date cannot be established; never substitute today.

Keep this recording and its evidence available through report and follow-up stages. Retrieve missing portions only; do not fetch the same transcript again for an email draft or copy the full transcript into handoffs.

## Write

Read [report format](references/report-format.md) while drafting; preserve its exact section order and table fields, omitting empty sections. Separate decisions from tasks, label analytical interpretations, and retain dissent/uncertainty. Do not invent owners, deadlines, promises or rationale. Unstated owners/deadlines are `Unassigned`; unstated decision rationale is `Not stated`. Preserve numerical wording, quotations and relative deadlines exactly; derive a calendar date only when unambiguous and retain the original wording.

## Save and verify

Read [storage and index](references/storage-and-index.md) before writing. Save reports and the meeting index as ChatGPT Spaces Pages in the user's approved account/client scope. This bundled version supports cloud execution; it does not require a local client folder. Keep complete source transcripts in Pocket AI rather than copying them into shared Pages.

Maintain one compact record per recording in the scoped Pocket Meeting Index Page, deduplicating by recording ID or exact available source metadata. Preserve unrelated index content and earlier reports. Verify transcript-supported claims/quotes, omitted empty sections, missing-field labels, correct meeting date and a working report Page link. If index save fails, report the saved report and failed index separately.

## Follow-up

When a controller explicitly owns the context/follow-up/Wrike stages, return the verified report and compact evidence to it and defer those automatic handoffs; the controller invokes each stage exactly once. Otherwise, after a reliable report is saved and verified, read [handoff requirements](references/follow-up-handoff.md) and apply [pocket-meeting-follow-up](../pocket-meeting-follow-up/SKILL.md) in the same task unless the user requested only the report or excluded email. Reuse a compact factual handoff: identity/date, confirmed attendance/address evidence, decisions, actions, commitments, questions, Page IDs/links and limitations. The follow-up should not reload the transcript or a report already represented adequately in context. Missing follow-up capability leaves the report deliverable with an explicit draft limitation.

## Assigned-task handoff

When the user requested Wrike capture or has an active standing instruction for this report scope, pass the verified report reference and assignment evidence to [pocket-summary-to-wrike](../pocket-summary-to-wrike/SKILL.md). The manager owns this stage in controller runs; return the handoff to it instead of invoking capture twice. Standalone authorized requests run it in the same task. A report-only request or missing capture authorization leaves Wrike unchanged. Track capture separately from the report/index and email follow-up so one failed stage does not replay the others.

Return concise report/index links, the saved Outlook draft receipt when included, task-capture results when authorized, and material limitations. The follow-up specialist saves mailbox drafts only within the authorized scope. Never send email or change Pocket records; do not display the email body in chat as the follow-up deliverable.
