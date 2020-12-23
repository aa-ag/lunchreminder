# Lunchtime

Python script to set a "lunch reminder." 

The reminder should run everyday at the same time and alert the enduser that it is time to have lunch in a different language each day.

Alert message will be:

> "lunchtime :sandwich: #brb" <sup>1<sup>

------------
** Footnotes **

<sup>1<sup> end goal is to share this message to slack.
Hench, using ":sandwich:" instead of "🥪".

### Initial thoughts

- use [`schedule`](https://schedule.readthedocs.io/en/stable/)

- use Google Translate's [API](https://cloud.google.com/translate/docs/reference/rest) one time, and store all available translations locally