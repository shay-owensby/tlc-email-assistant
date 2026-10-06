# Focused rule changes

Use for additions, corrections, exclusions, removals, or a request to restore an earlier preference. Do not reread the entire inbox or replace the user's profile to change one rule.

## Understand the exact instruction

1. Read the current approved profile, personal settings, operating scope, and the relevant rule/history. Confirm owner, mailbox, and version.
2. Decide whether this is a one-time action, a standing preference, a pause/revocation, or a request for an unsupported workflow. Ask only when the distinction materially changes behavior.
3. Translate a standing request into precise conditions, action, exceptions, precedence, scope, and effective time. Resolve sender addresses and destinations from existing evidence; never invent them. “Never archive invoices” can be saved as a protective exception without inventing which sender represents every invoice. Ambiguous invoice classification stays visible for review.
4. Check collisions with existing rules and show the affected before/after behavior. Preserve unrelated preferences and stable rule IDs. Add a new ID for a new rule; record a removed rule as inactive in history. Default to future matching work, not retrospective mailbox cleanup.

## Approval without needless repetition

- A clear direct instruction such as “From now on, archive mail from this verified address, except messages asking me a question” authorizes that exact rule change and its stated ongoing action, subject to an already authorized operational environment. Record the instruction as evidence; do not ask the user to repeat the same permission.
- If a necessary address, exception, destination, scope, or consequence is not established, prepare the precise proposed change and ask one focused question before activation. A request for advice such as “Should we archive these?” does not approve a rule.
- Permission to record a preference is not automatically permission to activate an unattended workflow. If the user only asks to save a rule, save it as approved preference but leave execution permission pending. If their direct instruction explicitly covers both, record both without a second approval prompt.
- Disable or narrow a revoked action immediately; do not wait for a general profile review. Preserve the revocation even if the rest of the configuration update fails. Newly requested external actions outside the plugin's supported scope remain unsupported rather than becoming active free-text instructions.

## Persist and activate consistently

Use the runtime's coordination mechanism so a controller cannot act on a half-updated profile. An active run must check pause/revocation and configuration changes at action boundaries. Set the affected operation to pending/restricted during the change when needed; do not claim already-committed actions were prevented.

Build a focused new profile/configuration revision and preserve the prior approved snapshot in change history. Use guarded Page edits and read back the saved change before updating the active runtime snapshot. The runtime version/content must match the new approved scope before writes resume. If only part of the save succeeds, leave the changed behavior blocked and report the mismatch; never silently resume against an older, revoked rule.

Synchronize only user-authorized changes into the runtime permission record. If the task prompt references stable Page IDs, no scheduling change is necessary for a normal rule edit. If it embeds a now-stale version or action restriction, reconcile that restriction under the same authorization; never widen it silently. A requested schedule change uses the live cloud scheduler and requires saved readback.

After verification, report the exact changed rule, its effective scope, and profile/settings link. A concise receipt is enough; do not force the user to approve the entire unchanged profile for every small edit.

If the user requests rollback, create a new revision restoring the selected previous rule(s), preserve current unrelated preferences, and verify the same account/authorization. Restoring a preference does not automatically reverse prior mailbox actions; handle an explicitly requested mailbox reversal against recorded before-state and current user edits.
