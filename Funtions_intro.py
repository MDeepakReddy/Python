# def is_palindrome(string):
#     backward = string[::-1]
#     return backward.casefold() == string.casefold()
#
#
# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     #return string[::-1].casefold() == string.casefold()
#     return is_palindrome(string)
#
#
# word = input("please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
#
# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))

# ===========================================================================

# def sum_eo(n, t):
#     if t == 'e':
#         return sum(range(2,n,2))
#     elif t == 'o':
#         return sum(range(1,n,2))
#     return -1
#
#
# x = sum_eo(10, 'ir')
# print(x)

# ===========================================================================

# num = int(input("enter a number: "))
# flag = False
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
#
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# ===========================================================================

# num = int(input("enter a number: "))
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if num == reverse:
#     print('palindrome')
# else:
#     print('Not Palindrome')

# ===========================================================================

# num = int(input("enter a number: "))
# temp = num
# num1 = 0
# while temp > 0:
#     digit = temp % 10
#     num1 += digit ** 3
#     temp = temp // 10
# if num == num1:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# ===========================================================================

# def check(s1, s2):
#
#     if (sorted(s1) == sorted(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The stings aren't anagrams.")
#
# s1 = input("Enter string1: ").casefold()
# s2 = input("Enter string1: ").casefold()
#
# check(s1, s2)

# ===========================================================================

# num = int(input("Enter a number: "))

# factorial = 1
# if num < 0:
#     print("sorry, no factorial for negative numbers")
# elif num == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
#     print("The factorial of",num,"is",factorial)

# ==========================================================================

# def myfunc(n):
    # for i in range(0, n):
    #     for j in range(0, i+1):
    #         print("* ",end="")
    #     print("\r")
# ========================================
# def myfunc(n):
    # k = n - 1
    # for i in range(0, n):
    #     for j in range(0, k):
    #         print(end=" ")
    #     k = k - 1
    #     for j in range(0, i+1):
    #         print("* ",end="")
    #     print("\r")
# ========================================
# def myfunc(n):
#     """
#     This function will take a number as an input (std)
#     It will create a pyramid patter as below
#      1\n
#      1 2\n
#      1 2 3\n
#      1 2 3 4\n
#     :param n: Enter the numbers of lines you want the pyramid to be
#     :return: None
#     """
#     for i in range(0, n):
#         num = 1
#         for j in range(0, i+1):
#             print(num, end=" ")
#             num += 1
#         print("\r")
# ========================================

 def fibonacci(n):
     """
     Return the 'n'th Fibonacci number, for positive 'n'
     :param n: Number
     :return: nth Fibonacci number
     """
     if 0 <= n <= 1:
         return n

     n_minus1, n_minus2 = 1, 0

     result = None
     for f in range(n - 1):
         result = n_minus2 + n_minus1
         n_minus2 = n_minus1
         n_minus1 = result

     return result

 for i in range(36):
     print(i, fibonacci(i))
