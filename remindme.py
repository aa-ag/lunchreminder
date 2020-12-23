###---- IMPORTS ---###
import schedule  # https://schedule.readthedocs.io/en/stable/
import time


###--- FUNCTIONS ---###
def job():
    print("I'm working!")


schedule.every(5).seconds.do(job)


###--- DRIVER CODE ---###
while True:
    schedule.run_pending()
