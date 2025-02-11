def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def print_leap_years(n):
    count, year = 0, 2024
    while count < n:
        if is_leap_year(year):
            print(year, end=" ")
            count += 1
        year += 1

n = int(input("Enter a number: "))
print_leap_years(n)
