def factorial(number: int) -> int:
    """
    Factorial of a number ex: 4! = 1*2*3*4 = 24
    :param number: factorial of this number
    :return: factorial
    """
    answer = 1
    if number > 0:
        for i in range(1, number + 1):
            answer *= i
        return answer
    else:
        return 1

for n in range(36):
    print(n, factorial(n))
