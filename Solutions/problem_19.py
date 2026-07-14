days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)



weekday = 1  # Given: Monday (1 Jan 1900)
count = 0

for year in range(1900, 2001):
    for month in range(12):
        if year >= 1901 and weekday == 0:
            count += 1
        d = days[month]
        if month == 1 and leap(year):
            d = 29

        weekday = (weekday + d) % 7

print(count)