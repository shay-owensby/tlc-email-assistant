# Meeting storage and index in ChatGPT Spaces

## Resolve the destination

Use ChatGPT Spaces Pages as the durable report store for this cloud deployment. Reuse the user's established meeting-report destination and account/client scope. If the user specifies a Space or parent Page, read it and its guidance first. When no destination is established, use private Pages and disclose their location. Ask only when the intended account/client or competing existing destinations are ambiguous. Do not choose a shared Space solely because the user can access it.

Find an existing scoped `Pocket Meeting Index` Page before creating one. Verify its account/client metadata, not just its title. Do not mix clients or copy a private executive report into a broadly shared index. Record canonical Page IDs and returned links in the handoff so later cloud runs do not depend on the chat or local files.

## Save the report

Use a title containing the actual meeting date and title, such as `2026 10 06 Operations meeting report`. Keep the original title, meeting date/time/timezone, recording ID/source, attendees, and account/client scope in the body. Follow the report-format reference with a native Page title rather than repeating the document heading.

Before creating, search/read the index and candidate reports for the exact recording ID. For an ordinary retry or scheduled replay, reuse the verified saved report; do not create another Page. If the user explicitly requests a revised report, create a new version while preserving the earlier report and update that recording's index entry to the new report. Same title alone is not the same recording. Without a recording ID, compare all available source metadata and ask when identity is uncertain.

Use the live Page creation/edit schemas and follow `pages:write-page` when available. Keep only the executive report and minimal provenance, not a transcript dump. On an unknown create outcome, locate/read the possible existing Page before retrying. On edit conflicts, refresh hashes/sequences and preserve unrelated content; stop after a corrected request fails rather than issuing blind retries.

Read back the report and verify identity/date, source-supported claims/quotes, correct headings, omitted empty sections, and missing-field labels before calling it saved and verified.

## Meeting index

Maintain one compact entry per recording, in this field order:

- Meeting date and original title.
- Attendees: confirmed names or `Not provided`.
- Description: one sentence.
- Open items: concise outstanding tasks, blockers, and questions.
- Decisions: concise settled choices.
- Report: returned Page link and canonical Page ID.
- Pocket recording ID or exact available source metadata.

For index fields with no supported items, use `None identified in transcript`; do not add empty report sections. Preserve unrelated entries and earlier report Pages. Use guarded Page edits, then read back exactly one entry for this recording and verify its report link.

If the report save succeeds but the index fails, disclose both states separately. An index failure does not justify recreating the report. Return the report link and failed-index limitation; retry the index only after reading its current state.

## Scheduled use

These skills do not create a schedule by themselves. Any separately requested schedule must be a verified cloud scheduled task using the installed plugin, connected Pocket AI, and Spaces. Save its authorized recording scope and durable progress references in the cloud. On a scheduled run, process only the requested new-recording window/scope, paginate completely before a no-new-recordings claim, and deduplicate against the index. Do not repeatedly regenerate the latest meeting. Missing authorization, destination, or full transcript leaves that item pending with a concise notification. No local scheduler or local storage fallback is allowed.
