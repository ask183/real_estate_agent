import schedule
import time
from crew import run_crew

schedule.every().day.at("08:00").do(run_crew)

print("Scheduler running. Will send email every day at 08:00AM...")

while True:
    schedule.run_pending()
    time.sleep(60)