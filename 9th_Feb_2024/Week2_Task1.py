def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Taking the year as input from the user
year = int(input("Enter a year: "))

# Checking if the year is a leap year and printing the result
if is_leap_year(year):
    print(f"{year} is a Leap year.")
else:
    print(f"{year} is not a Leap year.")
