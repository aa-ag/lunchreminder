###---- IMPORTS ---###
import schedule  # https://schedule.readthedocs.io/en/stable/
import time
import googletrans  # https://pypi.org/project/googletrans/
import csv

###--- GLOBAL VARIABLES ---###


###--- FUNCTIONS ---###
def translate():
    # get list of available languages
    # perform translation
    # save result in .txt
    announcement = "lunchtime :sandwich: #brb"

    available_languages = googletrans.LANGUAGES  # dict
    number_of_available_languages = len(available_languages)

    with open(f'{number_of_available_languages}-available-languages.csv', 'w', newline='') as csvfile:
        alwriter = csv.writer(csvfile)
        alwriter.writerow(['number', 'iso639-1 language codes',
                           'language name in English'])
        alwriter.writerows((i + 1, k, v)
                           for i, (k, v) in enumerate(available_languages.items()))


def job():
    print("I'm working!")


def lunchtime_alert():
    # translate message or grab from translations
    # alert end user
    pass


schedule.every(5).seconds.do(job)
# TO DO:
# schedule.every().day.at("11:59").do(lunchtime_alert)


###--- DRIVER CODE ---###
# while __name__ == "__main__":
# schedule.run_pending()
translate()
