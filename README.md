# Lunchtime

Python script to set a "lunch reminder." 

The reminder should run everyday at the same time and alert the enduser that it is time to have lunch in a different language each day.

Alert message will be:

> "lunchtime :sandwich: #brb" [^1]\

[^1]: end goal is to share this message to slack.
Hench, using ":sandwich:" instead of "🥪".

### Initial thoughts

- use [`schedule`](https://schedule.readthedocs.io/en/stable/) or [`sched`](https://docs.python.org/3/library/sched.html) to schedule execution

- use Google Translate's [API](https://cloud.google.com/translate/docs/reference/rest) either once per day, or one time, and store all available translations locally