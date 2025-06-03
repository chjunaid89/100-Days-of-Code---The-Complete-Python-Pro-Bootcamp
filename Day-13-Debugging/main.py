# # 1. Describe the problem
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
# my_function()
#
# # Describe the Problem - Write your answers as comments:
# # 1. What is the for loop doing?
# # 2. When is the function meant to print "You got it"?
# # 3. What are your assumptions about the value of i?
#
# # 1. Solution
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
# my_function()
#
# # -----------------------------------------------------------------------------#
# # 2.Reproduce the Bug
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_images[dice_num])
#
# # 2. Solution
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])
#
# # -----------------------------------------------------------------------------#
# # 3. Play Computer
# year = int(input("What's your year of birth?"))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
#
# # 3. Solution
# year = int(input("What's your year of birth?"))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")
#
# # -----------------------------------------------------------------------------#
# # 4. Fix the errors
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")
#
# # 4. Solution
# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("You have typed in a an invalid number. Please try again with a numerical response such as 15.")
#     age = int(input("How old are you?"))
#
# if age > 18:
#     print(f"You can drive at age {age}.")
#
# # -----------------------------------------------------------------------------#
# # 5. Use Print
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#
# # 5. Solution
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
#
# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)
#
# # -----------------------------------------------------------------------------#
# # 6. Use a Debugger
# import random
# import maths
#
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
#
# # 6. Solution
# import random
# import maths
#
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
#
