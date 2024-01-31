def isLeapYear(year):
    if year in range(1,10000):
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    print("True, {} is year a Leap year".format(year))
                else:
                    print(f"False, {year} is not a Leap Year")
            else:
                print("True, {} is a Leap Year".format(year))
        else:
            print(f"False, {year} is not a Leap Year")
    else:
        print("Invalid Entry")

print("Enter the year: ")
year = int(input())
isLeapYear(year)