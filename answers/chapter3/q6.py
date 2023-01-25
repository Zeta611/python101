def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


print(leap_year(2008), leap_year(2011), leap_year(2012))
print(leap_year(2000), leap_year(2100), leap_year(2200))
print(leap_year(2300), leap_year(2400), leap_year(3200))
