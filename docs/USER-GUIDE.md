# Email Assistant Quick Start

Your assistant helps organize email, prepare replies, and summarize Pocket AI meetings using rules you approve. Emails stay in Outlook Drafts unless you explicitly ask the assistant to send one.

## 1  Open Codex and install

Open Codex on your computer and sign in with your ChatGPT Pro account. Paste this into a new chat. You do not need to visit GitHub or create a GitHub account.

> Install Email Assistant from https://github.com/shay-owensby/tlc-email-assistant using the unchained-email-assistant marketplace. Check that it is installed and enabled. Guide me through any steps I need to complete.

Follow the prompts, then start a new chat. If Codex is missing or installation fails, ask Shay for help.

## 2  Connect your accounts

Open the Plugins tab. Search for Outlook Email, then Pocket AI. Open each plugin, select the plus button to install it, and follow the prompts to connect your own account.

Use the same steps to add Outlook Calendar, Teams, Wrike, or SharePoint if needed. If a plugin is missing or will not connect, ask Shay for help. Your email rules will be saved in ChatGPT Spaces during setup.

## 3  Set your rules

> Set up my email assistant. First inventory my existing folders, labels and categories. Analyze 90 days of email to show the types I receive and how I file or categorize them. Preserve my current structure, ask about unclear patterns, and show me the proposed rules. Do not change my mailbox.

Review the folder/category inventory and email-type findings, then answer the questions and correct anything that looks wrong. A list of urgent messages is not the setup analysis. When ready, say: “I approve these rules. Save them in my private ChatGPT Space.” Wait for the saved profile link. Setup does not change your inbox.

## 4  Try it before turning it on

> Show me how you would organize a small sample of my inbox and which replies you would draft. Do not change anything yet.

Review the preview, then say which actions it may take. Saved email drafts appear in Outlook Drafts. Meeting follow-ups are saved in your connected Outlook Drafts folder for review. They are never sent automatically.

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

Select Scheduled, then New task, or update your existing Pocket task. Name it TLC Pocket Meetings and paste these instructions:

> Every hour, check my connected Pocket AI account for new meetings using TLC Email Assistant’s hourly Pocket workflow. For each new meeting, run $pocket-meeting-summary, $pocket-meeting-context, $pocket-meeting-follow-up, and $pocket-summary-to-wrike once. I authorize saving reports in ChatGPT Spaces, saving follow-up drafts in my connected Outlook mailbox, and adding tasks clearly assigned to me to my Wrike task list. Ask once if a required account or destination is unclear. Save progress, avoid duplicates, and leave unclear items for review. Never send email.

> If a complete check finds no new meeting, return nothing and send no notification. Otherwise return the report, saved Outlook draft link, and verified task links. Report access failures once. Run in the cloud only.

| Setting | Value |
| --- | --- |
| Repeat | Interval |
| Every | 60 minutes |
| Run on this computer | Off |
| Start each run in a new chat | User preference |
| Model | GPT-6.1 Sol |
| Effort | Medium |

Select Create. Verify the hourly schedule and review follow-ups in Outlook Drafts. They remain unsent.

## Other actions and Wrike completion

Ask directly: “Send this draft to the listed recipients,” “Unsubscribe me from this newsletter,” “Archive these messages,” “Schedule this meeting,” “Post this update in Teams,” or “Update this SharePoint document.” Include the intended people, destination and details. These actions depend on the connected plugin’s permissions and supported tools. Sending, unsubscribe, calendar changes, Teams posts and document changes require a direct request each time; recurring inbox and Pocket checks remain draft-only.

To keep Wrike up to date, paste:

> Enable $sync-wrike-completion in my existing inbox schedule. Check my sent Outlook email and the Teams chats or channels I select. Mark only clearly matched, fully completed tasks assigned to me as complete. Leave partial or unclear work for review and respect tasks I reopen. Ask me to choose the Teams sources, Wrike scope and starting point; save those settings. Keep quiet when nothing changes.

This runs with your inbox checks, independently of new Pocket meetings. Selecting Teams sources does not permit posting there. No completion checks start until you enable them; existing schedules and permissions are preserved.

## Make it yours

Try: “Save a rule to never archive invoices.” • “Show my drafts and follow-ups.” • “Pause my email assistant.” Check the confirmation when a rule is saved. Your personal rules stay in Spaces.

When Shay announces an update, ask: “Update Email Assistant and verify the installed version.” Then start a new chat. If anything fails, send Shay the error message.
