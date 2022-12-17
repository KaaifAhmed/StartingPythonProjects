# import random as rd
# # Check if the first and last number of a list is the same
# numbers_x = [10, 20, 30, 40, 10]
#
# if numbers_x[0] == numbers_x[4]:
#     print(True)
# else:
#     print(False)
#
#
# numbers_y = [75, 65, 35, 75, 30]
#
# if numbers_y[0] == numbers_y[4]:
#     print(True)
# else:
#     print(False)
#
# # Display numbers divisible by 5 from a list
# lst = [10, 20, 33, 46, 55]
#
# for i in lst:
#     if i % 5 == 0:
#         print(f"The {i} is divisible by 5")
#     else:
#         print(f"The {i} is not divisible by 5")
#
# # Write a function called exponent(number) that returns an int value of base raises to the power of exp.
#
# # 2*3 = 6
# # 2**2 = 4
# # 2 ** 3 = 8
#
#
# def exponent(number):
#     # num = number **2
#     num = number * number
#     return num
#
#
# print(exponent(5))
#
# lst = ['f', 'c']
# print(rd.shuffle)
#
# print("s" in "pir" or "p" in "pir" or 'k' in "pir")
# print("paper" in "paperer")
#
#
# use_choice = "rock"
#
#
# if "rock" in use_choice or "paper" in use_choice or "scissor" in use_choice:
#     if "rock" in use_choice:
#         user_choice = "rock"
#         print(user_choice)
#     elif "paper" in use_choice:
#         user_choice = "paper"
#         print(user_choice)
#     else:
#         user_choice = "scissor"
#         print(user_choice)
#
# sue = 'rock'
# k = []
# for i in sue:
#     k.append(i)
#     print(i)
# print(k)
#
# k = ['r', 'a', 'o', 'c', 'k']
# rock = 'c'
# print(rock in k)
#
# comp_num = rd.randint(0, 3)
# print(comp_num)
#
# a = input("press enter")
# if a == "":
#     print("yes")
# else:
#     print("no")
stri = 'a'
ls = 'abcda'
index = [i for i, letter in enumerate(ls) if letter == stri]
for i, letter, o in enumerate(ls):
    print(i, letter, o)
print(enumerate(ls))
print(index)


