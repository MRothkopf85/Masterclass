# my_list = list(range(10))
# print(my_list)
#
# my_string = "abcdefghijklmnopqrstuvqxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# odd = range(1,10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7,1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven." .format (x))
#
# else:
#     print("{} is not divisible by seven." .format(x))
#
# r = range(0,100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('=' * 50)
#
# for i in range(99, 0, -2):
#     print(i)
#
# print('=' *50)
#
# print(range(0, 100)[::-2] == range(99, 0, -2))


o = range(0, 100, 4)
print(list(o))
p = o[::5]
print(list(p))
for i in p:
    print(i)

myRange = range(0, 20, 5)
print(myRange)
for i in myRange:
    print(i)

print(list(p))
