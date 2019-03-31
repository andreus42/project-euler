"""
# Problem 19 -- Counting Sundays
# https://projecteuler.net/problem=XXX
# 9-18-2018, 3:19am -

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Strategy:
#1 Calculate Sundays for a year, starting with a day of week and start looping
Make adjustments for leap year

#2 Calculate number of days in a year, adjust for leap years and century rules divide by seven

"""

# Timing Tools
import time
start = time.time()

"""Start Here"""

day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

month_of_year = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
sunday_count = 0

def leap_year(year):
    if year%400 == 0:
        return 1
    elif year%100 == 0:
        return 0
    elif year%4 == 0:
        return 1
    else:
        return 0

for year in range(1900, 2001):
    for month in range(1, 13):
        if leap_year(year):
            for day in range(1, leap_days_in_month[month]+1):
                count += 1
                if (day_of_week[count%7] == 'Sunday') and (day == 1):
                    print(f'{day_of_week[count%7]}, {month_of_year[month]}, {day}, {year}')
                    if year > 1900: sunday_count += 1
        else:
            for day in range(1, days_in_month[month]+1):
                count += 1
                if (day_of_week[count%7] == 'Sunday') and (day == 1):
                    print(f'{day_of_week[count%7]}, {month_of_year[month]}, {day}, {year}')
                    if year > 1900: sunday_count += 1

print(f'Days: {count}, Sunday Count: {sunday_count}')
print(f'Clocked in at {time.time()-start} second(s)')
