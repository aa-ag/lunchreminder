# Lunchtime

Python script to set a "lunch reminder." 

The reminder should run everyday at the same time and alert the enduser that it is time to have lunch in a different language each day.

Alert message will be:

> "lunchtime :sandwich: #brb" <sup>1</sup>

------------
** Footnotes **

<sup>1.</sup><small>end goal is to share this message to slack.
Hench, using "\:sandwich\:" instead of "🥪".</small>

### Technologies

- `conda install Flask`
- `conda install slackeventsapi`
- `conda install slack_sdk`
- `brew install --cask ngrok`