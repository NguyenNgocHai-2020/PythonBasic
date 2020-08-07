# -*- coding: utf-8 -*-
exp_str = 'Hello'
#
# # get substring by start:stop
# print(exp_str[1:4])

class_name = 'PYA0520E'

# get substring by :stop
# print(class_name[:3])
#
# # get substring by start:
# print(class_name[4:])
#
# # lay do dai
# print(len(class_name))

# if 'PY' in class_name:
#     print('PY co nam trong chuoi')
# else:
#     print('PY khong nam trong chuoi')
#
# print(exp_str + ' ' + class_name)
# # print('%s %s' % (exp_str, class_name))
#
# print(exp_str * 2)
#
# print(exp_str > class_name)
#
# print(chr(105))
#
# print(ord('i'))
#
# str_1 = 'Hello'
# str_2 = 'HELLO'
#
# print(str_1 >= str_2)
#
# test = 'pya0520e lean python'.capitalize()
# print(test)
#
# print(test.center(50, '*'))
#
# print(test.count('a'))
# print(test.count('a', 0, 7))

# test = 'Chào lớp PYA0520e'
#
# test = test.encode()
# print('Endcode ', test)
#
# test = test.decode()
# print('Decode', test)
#
# print(test.endswith('PYA0520E'))

# test = 'PYA0520e AA'
# print(test.expandtabs())
#
# print(test.find('e'))
# print(test.find('A'))
# print(test.rfind('A'))
#
# a = '321'
# b = 'd 321'
# print(a.isalnum())
# print(b.isalnum())
#
# a = 'Hello 1'
# b = 'Hello'
# print(a.isalpha())
# print(b.isalpha())
#
# a = '  Test 123  '
# print(a.strip())
#
# print(a.lstrip())
# print(a.rstrip())
#
# a = 'HELLO'
# print(a.isupper())
# print(a.islower())
#
# print(a.lower())
# print(a.upper())
#
# a = 'Hello World'
# a = a.replace('World', 'PYA0520E')
# print(a)

# ex_list = a.split(' ')
# ex_list = a.split()
# print(ex_list)

fruit_ls = ['apple', 'lemon', 'orange', 'coconut']
# for fruit in fruit_ls:
#     print(fruit)  # element
#
# for fruit in range(0, len(fruit_ls)):
#     print(fruit)  # index of list
#     print(fruit_ls[fruit])  # get element by index

# print(fruit_ls[0:2])
# print(fruit_ls[1:])
# print(fruit_ls[:2])
#
# print(fruit_ls[len(fruit_ls) - 1:len(fruit_ls)])
# print(fruit_ls[-3:-1])
# fruit_ls[1] = 'water melon'
# print(fruit_ls)

fruit_ls[0:1] = ['cherry', 'water melon']
# print(fruit_ls)

fruit_ls.append('banana')
fruit_ls.append('tomato')
# print(fruit_ls)
fruit_ls.insert(0, 'potato')
# print(fruit_ls)

fruit_ls.remove('potato')
# print(fruit_ls)

del fruit_ls[0]
# print(fruit_ls)

# print('lemon' in fruit_ls)
#
# new_ls = [1, 2, 3]
# print(max(new_ls))
# print(min(new_ls))
# # print(new_ls + fruit_ls)
# new_ls_2 = ['1', '2', '3']
# print('fruit is ', fruit_ls)
# print(max(fruit_ls))
# print(min(fruit_ls))
#
# ex_tuple = (1, 2, 3)
# ls = list(ex_tuple)
# print(ls)
# print(tuple(ls))
#
# print(fruit_ls.index('banana'))
#
# print(fruit_ls)
# fruit_ls.reverse()
# print(fruit_ls)
#
# fruit_ls.sort()
# print(fruit_ls)
# fruit_ls.sort(reverse=True)
# print(fruit_ls)
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# tong = 0
# for i in list_1:
#     tong = tong + i
# print(tong)
#

_list = ['zero', 'three']

# _list.insert(1, 'one')
# # _list.insert(2, 'two')
# # print(_list)
# #
# # list_1 = _list.copy()
# # list_1.remove('zero')
# # print(_list)
# # print(list_1)
# list= ['aba','xyz','abc','1221','ii','ii2']
# count = 0
# x= int(input("Nhap x"))
# for i in list:
#     if i[0] == i[len(i)-1] and len(i) >= x:
#         count +=1
# print(count)

# input_ls = input('Nhap mang')
# ls = input_ls.split(',')
# print(ls)

ls_input = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
result = []
for i in ls_input:
    # print(i)
    if ls_input.count(i) == 1:
        result.append(i)

    else:
        ls_input.remove(i)
print(ls_input)