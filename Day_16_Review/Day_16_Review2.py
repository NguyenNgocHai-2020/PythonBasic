# #Bài 1
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

# #Bài 2
# str = input("Nhập vào một chuỗi : ")
# result = []
# for i in str:
#     if str.count(i) <= 1:
#         result.append(i)
# lower = []
# upper = []
# for i in result:
#     if i.islower():
#         lower.append(i)
#     elif i.isupper():
#         upper.append(i)
#     else:
#         pass
# print(result)
# print(lower)
# print(upper)

# #Bài 3
# str = input("Nhập vào chuỗi số và cách nhau bởi dấu phẩy : ")
# str = str.split(",")
# lst_1 = []
# lst_2 = []
# tich = 1
# tong = 0
# for i in str:
#     i = int(i)
#     if i > 0:
#         tich *= i
#     elif i < 0:
#         tong += i
#     else:
#         pass
# print("tong %d, tich %f" % (tong, tich))


