# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

def count_days(year, month, whichday):
    # Your code goes here.
    calendar.Calendar()
    weeks = calendar.monthcalendar(year,month)
    count = 0
    for i in weeks:
        if i[whichday] != 0:
            count += 1
    return count
