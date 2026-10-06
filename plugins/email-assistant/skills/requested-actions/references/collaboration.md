# Calendar, Teams, and SharePoint actions

Discover each connected plugin's current schemas. These are conditional workflows, not claims that every connector supports every write or file type. An unavailable write leaves the prepared action pending. Reading an app for email context grants no write permission.

## Outlook Calendar

Support directly requested event creation, rescheduling, and specific detail changes. Resolve the calendar, organizer rights, event/occurrence when editing, title, timezone, start/end or all-day dates, attendees and location/online meeting requirements. Sending invitations or updates must be within the user's requested booking/change; do not add attendees or notify unrelated people. If a cancellation is requested, resolve its exact event and scope; never infer cancellation from a task's completion.

Read the relevant interval with recurring occurrences and all-day events, including attendee availability when supported and applicable. Recheck immediately before writing. If a conflict exists, explain it and ask how to proceed unless the user already explicitly authorized that conflict. If availability cannot be checked, disclose that before booking; do not claim the slot is free. Resolve ambiguous timezone/date/duration before creating. A recurring series edit requires an explicit series versus single-occurrence scope.

Search for an existing matching event or prior request receipt before creation. Use the native operation, preserve unrelated event properties, and verify dates, timezone, attendees, location, recurrence and returned invitation/update state. Request a Teams meeting only when asked and supported; never invent a join link. Reconcile unknown creation/update outcomes before retrying so duplicate invitations are not sent.

## Teams

Support directly requested posts and replies. Resolve the exact tenant, chat or team/channel, and thread for a reply; similarly named channels are not interchangeable. Resolve intended recipients and verified mention identities. Prepare the requested text in the user's style and preserve internal/external audience boundaries. A request for a draft or summary alone is not permission to post.

Post once using the connector's supported operation, retaining reply linkage and only requested attachments/mentions. Read back the message ID, target, author and content. If readback is unavailable, report acceptance and the verification gap. On unknown outcomes, inspect the target before retry; stop if duplication cannot be ruled out. Do not create a chat, edit someone else's message, or expand channel membership as an implied step.

## SharePoint

Support directly requested document creation and targeted content edits when the connector exposes appropriate operations for that file type. Resolve exact tenant/site/library/folder and existing document ID, not merely a filename. Verify the intended audience and current access without changing permissions.

For edits, read the latest document and version/ETag where exposed, preserve unrelated content/formatting/comments, and prepare the requested change. Use a supported format-aware editor for Word/Excel/other structured files; metadata-only edits or uploading plain text over a document are not content editing. Use guarded updates or the provider's checkout/version mechanism when supported. If concurrent changes prevent safe merging, reread and reconcile; do not overwrite the whole file to force a narrow edit.

For creation, inspect the destination for an existing document from this request before uploading. Do not overwrite a same-name file without authorization. Verify saved content and returned version/link, including unaffected material relevant to the edit. Do not claim success from a filename or upload acknowledgment alone. Publishing a major version, checking in a document, or replacing an existing file may affect readers; perform only the steps required by the user's specific request and supported tool semantics. Changes to access, public sharing, deletion, or unrelated files require their own request.
