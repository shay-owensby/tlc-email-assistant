# Context sources for email drafts

Use this guide only when a draft needs information beyond the email thread. Installing an app does not authorize unrestricted searches or additional external actions. Resolve the exact connected identity and the profile's allowed resource scope before retrieving context. If scope is missing, ask a focused question and leave the dependent draft pending.

| Source | Appropriate use | Check before including it in a draft |
| --- | --- | --- |
| Outlook Email | Prior replies, commitments, tone, and the live conversation | Latest inbound and sent messages; draft ownership; sender and recipients |
| Outlook Calendar | Availability and existing meeting details | Relevant authorized calendars, date/timezone, overlapping and all-day events; availability is not a booking |
| Teams | Decisions and project context from approved chats or channels | Read the relevant conversation, not a search excerpt; distinguish tentative ideas from decisions and respect internal-only content |
| Pocket AI | Meeting decisions, commitments, and action items | Recording identity, participants and date; read enough transcript to verify the claim; notes alone may omit qualifications |
| Wrike | Current task owner, status, due date, and project progress | Exact project/task and latest state; an old comment or a completed subtask is not proof the whole project is complete |
| SharePoint | Policies, approved documents, specifications, and reference material | Exact site/library/document, version or modified date, applicable audience, and whether the content is approved/current |
| ChatGPT Spaces | Approved triage profile and user-selected durable preferences/context | Account-specific canonical Page, approval/version, and scope; the runtime log is not a source for business facts |

Start with the live email thread. Follow explicit relevant references, then perform narrow searches in approved sources only when a specific fact is missing. Do not search every app for every message. Use available connector APIs and actual returned IDs; never invent a tool, document link, or recipient.

Keep a small fact/source/date note in the current run when useful for verification. The draft should sound natural; do not insert an internal source URL into an external reply unless appropriate and authorized for its recipients. Permission to read internal information is not permission to disclose it.

If current sources disagree, prefer a clearly authoritative, applicable source only when its authority is established by the user or profile. Otherwise ask for clarification; do not silently choose the newest message. Missing or unavailable context should block only the dependent draft or claim, not unrelated authorized inbox work.

Do not create or update calendar events, send Teams messages, modify Wrike tasks, edit SharePoint files, or start recordings as part of context retrieval. Those are separate workflows. Never claim an action occurred because it was discussed in a meeting or requested by email.

Calendar checks produce possible times, not reserved time slots. Recheck availability immediately before saving a scheduling-related draft, and avoid promising that the time will remain free until the user sends it.

Where a plugin is missing, discover the relevant provider plugin and explain the connection needed. Installed or discoverable in the author's environment does not mean installed, authorized, or supported in the client's scheduled runtime.
