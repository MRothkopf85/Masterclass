# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == "spam":
#         continue
#
#     print("Buy " + item)
#

meal = ["egg", "bacon", "orange", "spam", "sausages"]

nasty_food_item = ''

for item in meal:

    if item == 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can't I have anything without spam in it?")

else:
    print("That sounds quite nice.")

    # for i in range(0,100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
#


# for i in range(0,21):
#
#     if (i % 3 == 0) or (i % 5 == 0):
#         continue
#     print(i)
#
#
