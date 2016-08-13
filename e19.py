def calcDaysInMonth(year,month):
    if month in [0,2,4,6,7,9,10,11]:
        return 31
    if month in [3,5,8,10]:
        return 30
    if month == 1:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            return 29
        return 28
    raise ValueError

if __name__ == "__main__":
    day = 0
    count = 0
    for year in range(1,101):
        for month in range(12):
            day += calcDaysInMonth(year,month)
            if day % 7 == 6:
                count += 1
    print(count)
