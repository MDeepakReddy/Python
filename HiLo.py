def fizz_buzz(number: int) -> str:
    """
    fizz buzz game.
    If number divisible by 3 return fizz
    If number divisible by 5 return buzz
    If number divisible by both 3 and 5 return fizz buzz
    If number not divisible by both 3 and 5 return number
    :param number: inuput number
    :return: string value
    """
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif (number % 3 == 0):
        return "fizz"
    elif (number % 5 == 0):
        return "buzz"
    else:
        return str(number)


# for num in range(1, 101):
#     answer = fizz_buzz(num)
#     print(answer)

input("Play Fizz Buzz. Press Enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print("you lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
