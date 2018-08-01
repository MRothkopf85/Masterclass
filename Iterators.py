# string = "1234567890"
#
# # for char in string:
# #     print(char)
#
# # my_iterator = iter(string)
# # print(my_iterator)
# # print(next(my_iterator))
# # print(next(my_iterator))
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

myList = "abcdefghijklmnop"
myIterator = iter(myList)
n = len(myList)

for i in range(0,n):
    (print(next(myIterator)))