# Compute and print the current day of the week.

# import module to compute the seconds since midnight of 1/1/1970:
from time import time

def UTCDay(timeval):
    """Takes as input UTC time value (float), and returns the
    number of the day of the week (integer between 0 and 6 inclusive)"""
    timeval=int(timeval)
    mins=timeval//60
    hours=mins//60
    days=hours//24
    days_of_week=(days-3)%7
    return days_of_week


def localDay(timeval, offset):
    """Takes as input UTC time value  (float) and an offset (float),
    calls UTCDay to help compute the current day of the week
    for a timezone that is offset hours ahead of UTC.
    """
    timeval= timeval + (offset * 3600)
    print("The day of the week for the timezone that is {} offset hours ahead of UTC is: ".format(offset))
    return UTCDay(timeval)
def dayOfWeek(days_of_week):
    """Takes an integer between 0 and 6 (inclusive) as input and
    returns the name of that day as a string"""
    if days_of_week ==0:
        return "Sunday"
    elif days_of_week ==1:
        return "Monday"
    elif days_of_week==2:
        return "Tuesday"
    elif days_of_week==3:
        return "Wednesday"
    elif days_of_week==4:
        return "Thursday"
    elif days_of_week==5:
        return "Friday"
    else:
        return "Saturday"

# at this point, we have definitions necessary to support the computation
# add code, here, to print the day of the week in Williamstown (offset -5)
# according to the format described in the lab handout.

if __name__ == "__main__":         # run as a script?
    now = time()                   # UTC time
    dayNumber = localDay(now, -5)  # Eastern day of week number
    dayName = dayOfWeek(dayNumber) # get day name
    print("It's "+ dayName +"!")   # print it out
