###---- IMPORTS ---###
import schedule  # https://schedule.readthedocs.io/en/stable/
import time
import csv
import random
import googletrans  # https://pypi.org/project/googletrans/
# [!] https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
from google_trans_new import google_translator


###--- GLOBAL VARIABLES ---###
translator = google_translator()
alert = "lunchtime"
available_languages = googletrans.LANGUAGES  # dict
number_of_available_languages = len(available_languages)


###--- FUNCTIONS ---###


def get_available_languages():
    # get list of available languages
    # save result in .csv
    global alert
    global translator
    global available_languages
    global number_of_available_languages

    translations = dict()

    for code, language in available_languages.items():
        translations[language] = translator.translate(alert, lang_tgt=code)

    resulting_csv = f'{number_of_available_languages}-{alert}-translations.csv'

    with open(resulting_csv, 'w', newline='') as csvfile:
        alwriter = csv.writer(csvfile)
        alwriter.writerow(['number',
                           'language name in English', 'alert-translation'])

        alwriter.writerows((i + 1, k, v)
                           for i, (k, v) in enumerate(translations.items()))


def alert_user():
    # for now, alert via CLI only
    with open('107-lunchtime-translations.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        random_row = random.choice(list(csv_reader))
        print(f"{random_row[1]}: ", random_row[2], ":sandwich: #brb")


# TEST
schedule.every(3).seconds.do(alert_user)
# schedule.every().day.at("11:59").do([INSERT JOB HERE])


###--- DRIVER CODE ---###
get_available_languages()

while __name__ == "__main__":
    schedule.run_pending()
    time.sleep(1)
