def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def num_days(year, month):
    assert 1 <= month <= 12
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2 and leap_year(year):
        return 29
    else:
        return 28


print(num_days(2000,1), num_days(2001,4), num_days(2004,8))
print(num_days(2004,9), num_days(2005,3), num_days(2005,7))
print(num_days(2008,2), num_days(2011,2), num_days(2012,2))
print(num_days(2000,2), num_days(2100,2), num_days(2200,2))
print(num_days(2300,2), num_days(2400,2), num_days(3200,2))
