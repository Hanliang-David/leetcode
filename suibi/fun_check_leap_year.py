# fun_check_leap_year.py
def fun_check_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(fun_check_leap_year(2024))
print(fun_check_leap_year(2023))
