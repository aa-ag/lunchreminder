###---- IMPORTS ---###
import schedule  # https://schedule.readthedocs.io/en/stable/
import time
import csv
import googletrans  # https://pypi.org/project/googletrans/
# [!] https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
from google_trans_new import google_translator


###--- GLOBAL VARIABLES ---###
translator = google_translator()
alert = "lunchtime"


###--- FUNCTIONS ---###


def get_available_languages():
    # get list of available languages
    # save result in .csv
    global alert
    global translator

    available_languages = googletrans.LANGUAGES  # dict
    number_of_available_languages = len(available_languages)

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


# TO DO:
# schedule.every().day.at("11:59").do([INSERT JOB HERE])


###--- DRIVER CODE ---###
while __name__ == "__main__":
    # schedule.run_pending()
    get_available_languages()
