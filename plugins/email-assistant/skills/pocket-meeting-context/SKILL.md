---
name: pocket-meeting-context
description: "After pocket-meeting-summary saves a current client meeting report, compare it with two or three relevant indexed past meetings, insert a What changed since last time section, and reconcile the current meeting's open items in the index."
---

# Pocket Meeting Context

Run after `pocket-meeting-summary` has saved the current report. Use the supplied current meeting metadata, verified report Page ID/link, scoped Pocket Meeting Index Page ID/link, and authorized account/client destination in ChatGPT Spaces. Confirm the saved report exists and belongs to that scope before editing; if its identity or destination is missing, request the missing input. This bundled version works with cloud Pages rather than local files.

Reuse the current meeting evidence already in context; read only missing sections of its saved report. Historical comparisons still require the selected reports below. Do not retrieve the current transcript again or copy full reports into a downstream handoff.

## Select the historical context

Read the canonical Pocket Meeting Index Page for the authorized account/client. Use supplied Page IDs first; otherwise search and verify scope inside candidate Pages. Do not use a similarly named index from another user or client.

- If the index is missing or contains no relevant past meetings, skip the section and leave the report and index unchanged.
- Exclude the current meeting and meetings later than it. Rank past meetings using the index's topics, decisions, open items, and other available metadata. Prefer direct overlap with the current meeting's work, decisions, or commitments; use recency to break ties.
- Select the two or three most relevant past meetings. If only one is relevant, use that one; do not pad the selection with unrelated meetings.
- Open only those selected full reports, using their canonical Page IDs/links from the index. Do not scan other reports or transcripts for additional context or older dates.
- If a selected report is unavailable, use the remaining selected reports and note any material evidence gap. If none can be read, skip the section and report the limitation briefly.

## Compare what moved

Compare the selected reports in chronological order with the current report. Match items by their substance, owner, and deliverable even when wording changes. Use the current meeting's date as the comparison date, not the date this skill happens to run.

Write a concise, evidence-based **What changed since last time** section covering the applicable categories:

- **Decisions reversed or refined:** State the previous decision, the current decision, and what specifically changed. Include a reason only when recorded.
- **Open items now closed:** Identify the item and the evidence of completion, cancellation, or supersession. Distinguish those outcomes; silence or omission is not proof of closure.
- **Open items still outstanding:** Identify the item, owner when recorded, and how long it has been open. Use an explicit opening date when available. Otherwise say “tracked since [earliest evidenced date] — at least [elapsed time]” based on the index and selected reports. If the current meeting does not address it, say “last recorded open; no closure confirmed.” Do not invent an opening date or imply continuous verification.
- **Commitments past deadline:** Identify the commitment, owner when recorded, original due date, and time overdue as of the current meeting. Treat a deadline as passed only when the recorded date or time supports that conclusion. Resolve relative dates against the meeting that made the commitment; leave ambiguous deadlines explicitly uncertain. Distinguish still-overdue commitments from commitments closed late, and show old and revised dates when a deadline was moved.

Use dated links to the selected reports to support historical claims and keep related facts together rather than repeating the same item across categories. Use verified historical Page links. Do not manufacture continuity or infer reversal from different wording alone. If the comparison reveals no meaningful change, say so briefly; still mention material outstanding or overdue items supported by the evidence. Omit empty categories.

## Save the section and reconcile the index

1. Insert the section immediately after the complete **Executive summary** section and before the next peer section. Match the report's heading level and preserve the rest of the report. Match the summary heading case-insensitively. If it cannot be identified reliably, request clarification instead of inserting in an arbitrary location.
2. On reruns, replace the existing **What changed since last time** section rather than appending a duplicate.
3. Save the report with guarded Page edits, then update only the current meeting's entry in the index Page, matching by recording ID or canonical report Page ID and confirming the metadata. Preserve the index format, other fields, and all historical entries.
4. Reconcile that entry's open items with supported closures: remove confirmed closed items from an open-only list, or mark them closed when the index uses statuses. Keep unresolved items and unrelated current open items intact. If nothing is now closed, leave the entry unchanged. If the current entry is missing or ambiguous, preserve the index and report that limitation rather than changing a different meeting's entry.
5. Re-read the edited report section and index entry to verify placement, absence of duplicate sections, working historical Page links, and consistency of open-item status. Briefly report the updated Page links or the reason the section was skipped.

## Cloud runs and recovery

Reuse the controller’s run ID and verified current report. Do not create a schedule or a separate notification. Follow the user’s quiet-run preference; return this stage’s receipt to the controller. No relevant history is a successful skip, not a reason to stop the follow-up or Wrike stage. Use live Pages schemas and guarded edits; on conflicts reread and preserve unrelated/user changes. Re-read after an unknown write before retrying, and stop after one corrected edit fails. Report and index outcomes are separate; do not regenerate the summary to repair a context/index edit. Store stage status in the shared cloud runtime record. No local file fallback is supported in a cloud run.
