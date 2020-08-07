# ex_tuple = (1, 3, 5, 6, 8, 10)
#
# for i in ex_tuple:
#     print(i)
#
# ls_result = list(ex_tuple)
# ls_result.append(11)
# ls_result.remove(1)
# print(ls_result)
# tuple_second = tuple(ls_result)
# print(ex_tuple)
# print(tuple_second)
#
# plus_tuple = ex_tuple + tuple_second
# print(plus_tuple)
#
# a = ('ab','b','e','c','d','e','ab')
# kq = []
# for i in a:
#     # if a.count(i) == 1:
#     #     kq.append(i)
#     if a.count(i) > 1:
#         continue
#     kq.append(i)
# kq = tuple(kq)
# print(kq)
#
#
# ls_input = [(1, 2), (2, 6), (3, 1, 5)]
# ls_input.sort(key=lambda ele: ele[-1], reverse=True)
# print(ls_input)

# dictionary
ex_dict = {'a': 'HELLO', 'b': 'PYA0520E'}
# print(ex_dict)
#
# print(ex_dict['2'])
#
# ex_dict['2'] = 'Pya0520e'
# print(ex_dict)
# ex_dict['4'] = 'ABC'
#
# ex_dict.update({'2': 'World'})
# ex_dict.update({4: 'DEF'})
# print(ex_dict)
#
# #print(ex_dict[5])
# if '2' in ex_dict:
#     print(ex_dict['2'])
# if 5 in ex_dict:
#     print(ex_dict[5])
# if ex_dict.get(5, False):
#     print(ex_dict[5])
# # print(ex_dict.get('2', 'Ko co key nay'))
#
# del ex_dict[1]
# print(ex_dict)
#
# ex_dict.__delitem__('4')
# print(ex_dict)

# for i in ex_dict:
#     print(i)
#     print(ex_dict[i])
#
# for i in ex_dict.items():
#     print(i)
# a = str(ex_dict)
# print(type(a))
# print(dir(dict))

# ex_dict.clear()
# print(ex_dict)

# new_dict = dict.fromkeys([1, 2, 3, 4], 'h')
# print(new_dict)
#  support python 2 only
#  return True if key exist in dict
# new_dict.has_key(1)


# print(ex_dict.keys())

# ex_dict.setdefault('c', 'Hello PYA')
# ex_dict.setdefault('a', 'Good Bye')
# print(ex_dict)

# print(ex_dict.values())

# ex_dict = {'a': 'HELLO', 'b': 'PYA0520E', 'a': 'test duplicate key'}
# print(ex_dict)

# #bai1
# n = int(input("nhap so duong :  "))
# _dict = {}
# for i in range(1, n + 1):
#     _dict[i] = i * i
# print(_dict)

#bai 2
# d1 = {'a': 15, 'b': 20, 'c': 30, 'e': 60}
# d2 = {'a': 30, 'b': 20, 'd': 50}
#
# result = d2
# for i in d1:
#     if i in d2:
#         result[i] = result[i] + d1[i]
#     else:
#         result[i] = d1[i]
# print(result)

_dict = {"IV": "S001", "V": "S002", "VI": "S001", "VII":
"S005", "VIII": "S005", "IX": "S009", "X": "S007"}
_result = []

# for i in _dict.values():
#     if _result.count(i) == 0:
#         _result.append(i)
# print(_result)

# for i in _dict:
#     if _result.count(_dict[i]) > 0:
#         continue
#     _result.append(_dict[i])
# print(_result)

input_str = 'hello world! 123'

count_num = 0
count_alpha = 0
count_other = 0
for i in input_str:
    if i.isnumeric():
        count_num += 1
    elif i.isalpha():
        count_alpha += 1
    else:
        count_other += 1
print({'alpha': count_alpha, 'digit': count_num, 'other': count_other})