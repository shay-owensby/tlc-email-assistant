# Email Assistant Quick Start

Your assistant helps organize email, prepare replies, and summarize Pocket AI meetings using rules you approve. You review and send every email yourself.

## 1  Open Codex and install

Open Codex on your computer and sign in with your ChatGPT Pro account. Paste this into a new chat. You do not need to visit GitHub or create a GitHub account.

> Install Email Assistant from https://github.com/shay-owensby/tlc-email-assistant using the unchained-email-assistant marketplace. Check that it is installed and enabled. Guide me through any steps I need to complete.

Follow the prompts, then start a new chat. If Codex is missing or installation fails, ask Shay for help.

## 2  Connect your accounts

Open the Plugins tab. Search for Outlook Email, then Pocket AI. Open each plugin, select the plus button to install it, and follow the prompts to connect your own account.

Use the same steps to add Outlook Calendar, Teams, Wrike, or SharePoint if needed. If a plugin is missing or will not connect, ask Shay for help. Your email rules will be saved in ChatGPT Spaces during setup.

## 3  Set your rules

> Set up my email assistant. Review my email habits, ask me about my preferences, and show me the proposed rules before changing anything.

Answer the questions and correct anything that looks wrong. When ready, say: “I approve these rules. Save them in my private ChatGPT Space.” Wait for the saved profile link. Setup does not change your inbox.

## 4  Try it before turning it on

> Show me how you would organize a small sample of my inbox and which replies you would draft. Do not change anything yet.

Review the preview, then say which actions it may take. Saved email drafts appear in Outlook Drafts. Meeting follow-ups appear in chat unless you ask to save them as drafts.

## 5  Schedule your inbox checks in ChatGPT Work

Open chatgpt.com in your browser, sign in with the same account, and choose Work for a new chat. This uses the cloud, so scheduled checks can run while your computer is off.

Paste the request below and add the saved profile link from step 3. ChatGPT will guide you through the schedule and any connection checks.

> Use Email Assistant to set up cloud inbox triage with my approved profile linked below. First check that you can access the plugin, its skills, Outlook, and my saved rules in this cloud chat, then run a preview without changing mail. Ask me for the days, times, timezone, and notifications I want. Show the schedule and permitted actions for my approval before activation. Create or update one task named Email Assistant for this mailbox, using manage-email-assistant and email-triage. Each run must read my current saved rules and perform only approved actions. Never send emails. If cloud access is missing, explain what I need to fix and do not activate the task.

Choose your schedule. For example: “Every weekday at 8 a.m. and 2 p.m., America/Chicago. Notify me when you need a decision or a run fails.” Change these times and preferences to suit you.

Review the proposed mailbox, actions, schedule, and timezone. When correct, approve activation. Open Scheduled in the sidebar, select Email Assistant, and check that the task is active and its next run is correct. A chat reply alone is not confirmation that a task was saved.

Verify the first run. Leave your computer off during a scheduled check, then open Scheduled and review the result. Confirm the task actually checked your inbox, rather than only sending a reminder. Review the first few runs before relying on it.

To change or pause it, open Scheduled and select the task, or ask in its chat: “Change my inbox checks to weekdays at 9 a.m.” or “Pause this scheduled task.” Verify the updated status in Scheduled.

If cloud access or scheduling is unavailable, leave the task inactive. Follow any connection prompts in Plugins and retry the preview. A desktop installation alone does not guarantee cloud access; do not switch to a local schedule.

## 6  Schedule hourly Pocket meetings

Use the TLC Email Assistant copies of the Productivity summary, context, and follow-up workflows so reports are saved in ChatGPT Spaces, plus pocket-summary-to-wrike. First paste this into ChatGPT Work:

> Update TLC Email Assistant from https://github.com/shay-owensby/tlc-email-assistant and verify that version 0.5.0 or later is installed and enabled. Check that the bundled $pocket-meeting-summary, $pocket-meeting-context, $pocket-meeting-follow-up, and $pocket-summary-to-wrike skills are accessible in ChatGPT Work with cloud execution. Confirm my connected Pocket AI account, which meetings to include, my timezone, where my private reports and meeting index will be saved in ChatGPT Spaces, and the existing Wrike space, folder, or project for tasks assigned to me. Start with new meetings after setup; ask before including older meetings. Save these choices and the existing-recording baseline in my private Email Assistant settings and runtime state. Check for an existing Pocket schedule so I do not create a duplicate. Show me one preview and any missing connections before I create the hourly task. Do not create Wrike tasks, send email, or activate a schedule during this setup.

Complete the preview and connection steps. Retain the returned settings and runtime Page links. Reuse an existing Pocket schedule if one already processes these meetings. Otherwise open Scheduled, select New task, and name it TLC Pocket Meetings. Paste these instructions and append those Page links:

> Every hour, use my saved Email Assistant settings and runtime state to check my connected Pocket AI account for new meetings in the agreed scope. Use the bundled TLC Email Assistant versions of $pocket-meeting-summary, $pocket-meeting-context, $pocket-meeting-follow-up, and $pocket-summary-to-wrike, following the manager’s hourly Pocket workflow.

> For each new meeting, read its complete transcript and save one verified report and index entry in ChatGPT Spaces. Add supported context from relevant earlier meetings, then prepare one attendee follow-up draft. Defer the summary skill’s automatic follow-up and Wrike handoffs so each stage runs only once. Use $pocket-summary-to-wrike and its bundled $wrike-tasks skill to add only tasks clearly assigned to me or commitments I clearly accepted, using my saved Wrike destination. I authorize those report, context, follow-up-text, and task-capture actions. Check for existing tasks and verify every saved task. Never send email or create mailbox drafts.

> Save progress separately for each stage and resume unfinished work without duplicating completed actions. Keep ambiguous assignments or deadlines for review. Do not silently include historical meetings outside my approved scope.

> After a successful complete check with no new meeting, return nothing: no message, notification, acknowledgment, or “no new meetings” update. Preserve any recovery results silently. When a new meeting is processed, return the report link, follow-up draft, and verified Wrike task links. If access fails, retrieval is incomplete, or a decision is needed, report that issue once; do not claim there were no new meetings or repeat an unchanged alert. Run in the cloud only.

| Setting | Value |
| --- | --- |
| Repeat | Interval |
| Every | 60 minutes |
| Run on this computer | Off |
| Start each run in a new chat | User preference |
| Model | GPT-6.1 Sol |
| Effort | Medium |

Select Create. Verify the saved hourly schedule, the first new-meeting result, and silence after a successful check without a new meeting. No email is sent automatically.

## Make it yours

Try: “Save a rule to never archive invoices.” • “Show my drafts and follow-ups.” • “Pause my email assistant.” Check the confirmation when a rule is saved. Your personal rules stay in Spaces.

When Shay announces an update, ask: “Update Email Assistant and verify the installed version.” Then start a new chat. If anything fails, send Shay the error message.
