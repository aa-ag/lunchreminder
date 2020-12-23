###---- IMPORTS ---###
import schedule  # https://schedule.readthedocs.io/en/stable/
import time
import googletrans  # https://pypi.org/project/googletrans/

###--- GLOBAL VARIABLES ---###


###--- FUNCTIONS ---###
def translate():
    # get list of available languages
    # perform translation
    # save result in .txt
    available_languages = googletrans.LANGUAGES  # dict

    print(f"API suports {len(available_languages)} languages:\n")  # 106

    for i, (k, v) in enumerate(available_languages.items()):
        print(f"{i + 1} - {k}: {v}")


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
