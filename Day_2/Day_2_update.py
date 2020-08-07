# name = input("Please input your's name: ")
# # print(name)
# #
# dob = input("Please input your's dob: ")
# dob = int(dob)
# age = 2020 - dob
# # print(age)
#
# point = float(input('Please input your\'s point: '))
# # print(point)
# print('Name is ', name)
# print('Name is %s, age is %d' % (name, age))
# print('Point is %.7f' % (point,))
#
# show_info = 'Name is {name_value}, age is {age_value}'.format(
#     age_value=age, name_value=name)
# print(show_info)

# input('Please input your\'s name')

# bai 1
# 23


# bai 3
# a=int(input('num 1'))
# b=int(input('num 2'))
# c=int(input('num 3'))
#
# print(a+b)
# print(a*b)
# print(a-b)
# print(a/b)
# print(a%b)
# print(a//b)

# print('in ra %s' % (4,))
#
# name = input("Please input your's name: ")
# dob = input("Please input your's dob: ")
# dob = int(dob)
# age = 2020 - dob
# print(age)
# if 27 <= age <= 40:
#     print('lay vk duoc roi')
# elif age >= 40:
#     print('FA forever')
# elif age >= 20 and age < 27:
#     print('tre con')
# else:
#     print('Khong phan loai duoc')

# if 27 <= age <= 40:
#     print('lay vk duoc roi')
#     if 30 <= age <= 35:
#         print('sinh con di')
#     else:
#         print('gia roi de gi nua')
# if age >= 40:
#     print('FA forever')
# if age >= 20 and age < 27:
#     print('tre con')

# b = ''
# a = 0
# if a:
#     print(a)
# else:
#     print('test')

# bai 1 - if else
# a = input("Hay nhap vao 1 so : ")
# if a.isnumeric():
#     a = int(a)
#     b = a % 2
#     if b == 0:
#         print("Day la mot so chan !!!")
#     elif b == 1:
#         print("Day la mot so le !!!")

# bai 2
# a = int(input('canh a'))
# b = int(input('canh b'))
# c = int(input('canh c'))
# if a > b + c:
#     print('day ko phai tam giac')
# elif b > a + c:
#     print('day ko phai tam giac')
# elif c > a + b:
#     print('day ko phai tam giac')
# else:
#     print('day la mot tam giac')
#
# if (a >= b + c) or (b >= a + c) or (c >= a + b):
#     print('Day khong phai la tam giac')
# else:
#     print('Day la tam giac')
#
# if (a < b + c) and (b < a + c) and (c < a + b):
#     print('Day la tam giac')
# else:
#     print('Day khong phai la tam giac')

import time
x = time.localtime()
year = x[0]
a = input('nam sinh cua ban la:')
print(type(a))
if a.isnumeric():
    a = int(a)
    print(type(a))
    print('tuoi cua ban la:', year - a)