---
name: wrike-tasks
description: Add action items assigned to the user, or tasks the user explicitly asks to add, to their task list through the Wrike plugin. Use for requests such as "add this to my tasks" or "put my assigned action items in Wrike" from messages, meetings, or supplied notes; reuse existing Wrike tasks and avoid duplicates. Reading or summarizing a source alone does not authorize task creation.
---

# Wrike Tasks

Capture the user's work in Wrike using the connected Wrike plugin. Support both clear assignments to the user in the requested source and manually requested tasks, even when the source has no assignment.

For matching sent Outlook/Teams completion statements to existing tasks, use [sync-wrike-completion](../sync-wrike-completion/SKILL.md). Capture permission alone does not enable completion checks. Preserve completed tasks on capture replay; task status synchronization is owned by that separate workflow.

## Scope and inputs

- A request to add tasks, or an established instruction to capture assigned work from a particular source, authorizes the corresponding Wrike writes. Proceed within that scope without a second confirmation.
- For source-based capture, include concrete actions explicitly assigned to the user or commitments they clearly accepted. Being copied, mentioned, present at a meeting, or interested in an idea is not an assignment. Skip other people's work unless the user explicitly asks to add it to their own list.
- For a manual request, use the stated or clearly implied action as the title and assign it to the user. Ask only if the action itself cannot be determined.
- Read only the sources needed for the request. If a referenced message or meeting is unavailable, request the missing source rather than inventing tasks or claiming none exist.
- Skill availability is not a background monitor. Ongoing scans or schedules require a separate user request. Creating or editing this skill does not itself authorize live task creation.

## Resolve the user and destination

Discover the currently available Wrike plugin tools and use their live schemas. Tool names below refer to the Wrike plugin, commonly exposed with the `wrike_` prefix. If the plugin is unavailable or disconnected, explain the blocker and provide the prepared task details without claiming they were saved.

1. Resolve the connected user with `get_users(me=true)` and retain the returned canonical user ID. For external sources, match the assignee to this identity using available names, emails, and source context. Clarify an ambiguous identity before assigning work.
2. Use the task destination explicitly requested or previously established for this user and account. Verify its identity and type through the plugin. Do not treat an ambient browser tab as a chosen destination or reuse IDs from another user/account.
3. Resolve a named space with `search_spaces`; resolve a folder or project with `search_items` scoped to its known space or parent. Use `get_items_children` when needed to inspect a known hierarchy. If a named space is not found among memberships, try `onlyMySpaces=false`.
4. Creation requires a real parent: a space, folder, project, or an explicitly requested parent task. A task parent creates a subtask. A personal task view is not sufficient evidence of a writable parent. If the user's established destination cannot be resolved uniquely, ask which existing space, folder, or project to use, presenting recognizable choices instead of asking for IDs.

Keep IDs and personal defaults in the current user's context; do not hardcode them into this reusable skill. Do not create a new folder or project merely to resolve a missing destination.

## Prepare each task

Use the user's title when provided; otherwise write a concise action title faithful to the source. Include only relevant source context, deliverables, and a source link when available. Distinguish an explicit deadline from a meeting date or a proposed date.

- Set the assignee to the resolved user for new tasks.
- Include dates only when stated or clearly established. Interpret relative dates using the source timestamp and user's timezone; if multiple interpretations materially change the deadline, ask. Omit an unspecified deadline.
- Convert supplied description text to HTML, escaping text and links appropriately. Do not add unsupported details.
- Omit optional status, custom item type, priority, and scheduling fields unless requested or supported by an established instruction.
- Follow the tool's date semantics: creation with only `dueDate` produces a milestone. Do not invent a start date or duration to obtain a date range.

## Reuse existing work before creating

For a supplied Wrike task link or known ID, read the task directly with `get_item_details`. For other candidates, search the intended destination using `search_items(baseItemTypes=["TASK"], ...)` and distinctive title keywords. Also check the user's assigned tasks for the same source/action when a task may already live elsewhere. Follow relevant pagination; do not treat a truncated search as exhaustive.

Compare the action, source link or identifier, context, and owner, not merely a similar title. Read candidate details with `fullDescriptions=true` when necessary.

- If the same task already exists and is assigned to the user, report it as already present. Do not create a second task solely to make it appear in another list.
- If the user asks to add an existing task to their own work, use `update_items(addAssignees=[userId])` when needed, preserving other assignees. If they explicitly request placement in an additional folder/project, resolve it and use `addParents` while preserving existing parents.
- Do not silently move, rename, reopen, complete, or replace the description of an existing task. A completed match may represent finished work or a new occurrence; use explicit recurrence/source evidence or clarify before reopening or duplicating it.
- If the match is uncertain, clarify that candidate while continuing unrelated tasks whose identity and destination are clear.

## Write and verify

Use `create_task_item` with an `items` array containing each resolved `parentId`, title, `assigneeId`, and supported optional fields. Batch independent tasks when useful. Create parents before children only when the hierarchy was requested, using returned IDs.

For each creation or update, read the affected task back with `get_item_details` and verify the title, user assignment, intended parent when applicable, and any supplied dates or description. Read details in batches within the tool's current limits. Report creation and verification separately if readback fails; do not retry creation because verification failed.

After a partial batch success, retain successful IDs and retry only items explicitly reported as failed when the cause can be corrected safely. After a timeout or unknown creation outcome, search the intended parent for the exact title and compare source context before any retry. If the outcome remains inconclusive, ask before retrying; do not risk duplicate creation.

Return a concise result with links to created or updated tasks. Distinguish already-present tasks, skipped unassigned items, and unresolved or failed items. Show deadlines when provided. If nothing qualified, say so; if retrieval was incomplete, state that limitation instead of claiming there were no tasks.

## Typical requests

- "Add a task for me to review the vendor proposal by Friday." Resolve the user's established destination and relative date, check for duplicates, then create and verify.
- "Add my action items from this meeting to Wrike." Capture clear assignments and accepted commitments to the user, preserving supported deadlines and source context.
- "Add this Wrike task to my list." Read the linked task; retain it if already assigned or add the user as an assignee while preserving existing assignments.
- "Summarize this email." Summarize only; task creation requires a capture request or applicable standing instruction.
