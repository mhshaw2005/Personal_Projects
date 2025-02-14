from datetime import datetime
import calendar
import random as rand
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os


load_dotenv()
EMAIL = os.getenv("GOOGLE_CALENDAR_EMAIL")
date = datetime.now()
redirect_URI = "http://localhost:8080/"


def days_func(day, month, year, length = rand.randint(0,3)):
    month_len = calendar.monthrange(year, month)[1]
    start_date = rand.randint(day, month_len)
    end_date = start_date + length

    while end_date > month_len:
        end_date -= 1

    return start_date, end_date


def addtocal(day, month, year, email=EMAIL, length = rand.randint(0,3)):
    start_date, end_date = days_func(day, month, year, length)
    cal = GoogleCalendar(email)
    event = Event(
        'T-Break',
        start= datetime(year, month, start_date),
        end= datetime(year, month, end_date)
    )

    cal.add_event(event)

    start_date = str(start_date)
    end_date = str(end_date)
    if start_date == end_date:
        print("Your break is on " + str(month) + "/" + start_date)
        return
    else:
        print("Your break is from " + str(month) + "/" + start_date +
              " to " + str(month) + "/" + end_date)
        return


def __gui():
    day = date.day
    month = date.month
    year = date.year

    print("Welcome to the T-Break Program!")
    len_b = input("Do you have a desired length, if not press ENTER: ")
    addcal = input("Do you want this to be added to your calender (Y/N): ")

    if addcal == "Y":
        email = input("What is your email? ")
        if email == "":
            if len_b == "":
                addtocal(day, month, year)
            elif int(len_b) <= 0:
                print("Invalid length. Randomizing.")
                addtocal(day, month, year)
            else:
                addtocal(day, month, year,None, int(len_b))
        else:
            if len_b == "":
                addtocal(day, month, year, email)
            elif int(len_b) <= 0:
                print("Invalid length. Randomizing.")
                addtocal(day, month, year, email)
            else:
                addtocal(day, month, year, email, int(len_b))
    elif addcal == "N":
        if len_b == "":
            start, end = days_func(day, month, year)
            start = str(start)
            end = str(end)
            if start == end:
                print("Your break is on " + str(month) + "/" + start)
                return
            else:
                print("Your break is from " + str(month) + "/" + start +
                      " to " + str(month) + "/" + end)
                return
        elif int(len_b) <= 0:
            print("Invalid length. Randomizing.")
            days_func(day, month, year)
        else:
            start, end = days_func(day, month, year, int(len_b))
            if start == end:
                print("Your break is on: " + str(month) + "/" + str(start))
                return
            else:
                print("Your break is from: " + str(month) + "/" + str(start) +
                      " to " + str(month) + "/" + str(start))
                return

__gui()
