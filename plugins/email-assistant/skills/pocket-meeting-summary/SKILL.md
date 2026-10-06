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

After a reliable report is saved and verified, read [handoff requirements](references/follow-up-handoff.md) and apply [pocket-meeting-follow-up](../pocket-meeting-follow-up/SKILL.md) in the same task unless the user requested only the report or excluded email. Reuse a compact factual handoff: identity/date, confirmed attendance/address evidence, decisions, actions, commitments, questions, Page IDs/links and limitations. The follow-up should not reload the transcript or a report already represented adequately in context. Missing follow-up capability leaves the report deliverable with an explicit draft limitation.

Return concise report/index links, the email draft when included, and material limitations. This workflow does not send email, create mailbox drafts, or change Pocket records.
