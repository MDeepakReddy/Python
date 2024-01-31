def toMilesPerHour(kilometersPerHour):
    if kilometersPerHour < 0:
        print("invalid entry")
    else:
        rounded = round(kilometersPerHour/1.609)
        print(rounded)

def printConversion(kilometersPerHour):
    if kilometersPerHour < 0:
        print("invalid entry")
    else:
        rounded = round(kilometersPerHour/1.609)
        print("{} km/h = {} mi/h".format(kilometersPerHour,rounded))

inpkil = float(input())
inKil = float(input())
toMilesPerHour(inpkil)
printConversion(inKil)