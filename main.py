import datetime
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
from misskey import Misskey

def is_zorome(number):
    number_str = str(number)
    first_digit = number_str[0]
    for digit in number_str:
        if digit != first_digit:
            return False
    return True

def calculate_anniversaries(setup_date, current_date):
    anniversary_data = []

    # Calculate the number of days between setup_date and current_date
    days_difference = (current_date - setup_date).days

    # Check for 100n-day anniversary
    if days_difference >= 100 and days_difference % 100 == 0:
        anniversary_data.append(f"{days_difference}日記念")

    # Check for 100n+10n+n-day anniversary
    if days_difference > 100 and is_zorome(days_difference):
        anniversary_data.append(f"{days_difference}日記念")

    # Calculate the years between setup_date and current_date
    years_difference = (current_date.year - setup_date.year)

    # Check for n周年
    if setup_date.month == current_date.month and setup_date.day == current_date.day:
        anniversary_data.append(f"{years_difference}周年")

    # Check for n.5周年
    if current_date.month == 10 and current_date.day == 7:
        anniversary_data.append(f"{years_difference}.5周年")

    return anniversary_data

if __name__ == "__main__":
    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    MISSKEY_SERVER = os.environ.get("MISSKEY_SERVER")
    API_TOKEN = os.environ.get("API_TOKEN")

    YEAR = os.environ.get("SETUP_YEAR")
    MONTH = os.environ.get("SETUP_MONTH")
    DAYS = os.environ.get("SETUP_DAYS")
    
    setup_date = datetime.datetime(int(YEAR), int(MONTH), int(DAYS))

    mk = Misskey(address=MISSKEY_SERVER, i=API_TOKEN)
    last_note = datetime.datetime(1997, 8, 19)

    while True:
        dt_now = datetime.datetime.now()
        time.sleep(1)

        # Calculate anniversaries
        anniversaries = calculate_anniversaries(setup_date, dt_now)

        if last_note != dt_now:
            if anniversaries:
                for anniversary in anniversaries:
                    note_text = f"<center>今日は:polestar2023:が起動してから\n\n$[x2 $[jelly $[sparkle {anniversary}]]]</center>"
                    mk.notes_create(text=note_text)
                    last_note = dt_now
