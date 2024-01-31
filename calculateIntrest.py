def calculateInterest(balance, interest, noOfYears):
    temp = noOfYears * interest / 100
    solu = (balance * (interest + temp) / 100)
    return solu


balance = float(input())
interest = float(input())
noOfYears = int(input())
sol = float(calculateInterest(balance, interest, noOfYears))
answer = round(sol,3)
print(answer)
