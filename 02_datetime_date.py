"""
Is it Time for Milk and Cookies?
Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.

Examples
time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True

time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False

time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True

"""
import datetime
def time_for_milk_and_cookies(date):
    if date.day == 24 and date.month==12:
        return True
    else:
        return False

time_for_milk_and_cookies(datetime.date(2013, 12, 23))