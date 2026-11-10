# Routine

================================

## Overview
Routine is like an assistance which keeps notes and reminders of tasks which user wants to be remembered and also gives notification to user if some task is due.

### Features

* **Note-taking**: Take notes on the go with our mobile app.
* **Organisation**: Organises the tasks based on the category.
* **Reminder**: Notifies users when a task is due.
* **Syncing**: Sync your notes across all your devices.

**How it works**:
1. Open the app.
2. Create your account with an email id and password.
3. After logging in, Click on the '+' sign to create a reminder or note.
4. Add the time when you want to be notified.
5. Save and Close the App.

**RULES**:
- Account: Password length should be atleast 8 characters, should have atleast 1 Upper case, 1 Number and 1 Special character. When account is deleted, the reminders and notes should get deleted as well for the respective account.
- Reminder time: fires at the same local wall-clock time the user set, in whatever time zone the device is currently in (09:00 Helsinki → 09:00 New York). DST shifts follow local time.
- Recurrences: Give option of Daily, Weekly, Monthly, Yearly and Custom option as well.
- Notification: If OS permission denied, user should get notified when user opens the app. If phone was switched off, then user should get past notifications when the phone is turned ON.
- Limits: maximum length of note is 500 words, maximum 3 categories for free tier account unless paid subscription is opted then it should be unlimited. Category can be deleted when it holds notes, but user should be notified about it and also given a option to move to other category.
- Past times: A reminder cannot be set in the past time.
- Sync: If same note is edited on 2 offline devices, chose the latest note with respect to time.