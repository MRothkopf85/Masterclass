# list_1 = []
# list_2 = list()
#
# # These lists are equal
#
# print("List 1: {}" .format(list_1))
# print("List 2: {}" .format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

#even = [2,4,6,8]

# another_even = even
# another_even.sort(reverse=True)
# print(even)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even,odd]
# #print(numbers)
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)


# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as done in lines 35-42

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

noSpam = []
for meal in menu:
    if not "spam" in meal:
        # noSpam += meal
        # print(noSpam[0],noSpam[1],noSpam[2])
        for ingredient in meal:
            print(ingredient)

