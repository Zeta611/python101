def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_past_year(year, month, day):
    days = 0
    for i in range(1, month):
        if i == 2:
            if leap_year(year):
                days += 29
            else:
                days += 28
        elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            days += 31
        else:
            days += 30
    days += day
    return days


def day_diff(y1, m1, d1, y2, m2, d2):
    days = 0

    if y2 - y1 >= 2:
        for i in range(y1 + 1, y2):
            if leap_year(i):
                days += 366
            else:
                days += 365
    elif y1 == y2:
        return days_past_year(y2, m2, d2) - days_past_year(y1, m1, d1)

    if leap_year(y1):
        days += 366 - days_past_year(y1, m1, d1) + 1
    else:
        days += 365 - days_past_year(y1, m1, d1) + 1

    if leap_year(y2):
        days += days_past_year(y2, m2, d2)
    else:
        days += days_past_year(y2, m2, d2)
    return days - 1


def day_of_week(year, month, day):
    days_since_unix_epoch = day_diff(1970, 1, 1, year, month, day)  # Thu
    rem = days_since_unix_epoch % 7
    if rem == 0:
        return "Thu"
    elif rem == 1:
        return "Fri"
    elif rem == 2:
        return "Sat"
    elif rem == 3:
        return "Sun"
    elif rem == 4:
        return "Mon"
    elif rem == 5:
        return "Tue"
    elif rem == 6:
        return "Wed"


print(day_of_week(2023, 1, 19))  # Thu
print(day_of_week(1970, 1, 1))  # Thu
print(day_of_week(2029, 8, 31))  # Fri
