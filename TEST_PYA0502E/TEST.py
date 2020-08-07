# #Bài 1
# lst = input("Nhập chuỗi số : ")
# lst = lst.split(",")
# print(lst)
# lst_chan = []
# total = 0
# count = 0
# for i in lst:
#     i = int(i)
#     if i % 2 == 0:
#         lst_chan.append(i)
#
#         total += i
#         count +=1
# print(lst_chan)
# print("TBC số chẵn là ", total/count)

# #Bài 2
# str = input("Nhập vào chuỗi ký tự : ")
# upper = ""
# count_upper = 0
# lower = ""
# count_lower = 0
# for i in str:
#     if i.isupper():
#         upper +=i
#         count_upper += 1
#     elif i.islower():
#         lower += i
#         count_lower += 1
#     else:
#         pass
# print("Ký tự viết hoa: %s - %d" % (upper, count_upper))
# print("Ký tự viết thường: %s - %d" % (lower, count_lower))

# #Bài 3
# str = input("Nhập vào chuỗi bất kỳ : ")
# result = {}
# for i in str:
#     result[i] = str.count(i)
# print(result)

#Bài 4
import os
ex_4 = open("D:\\GG_Drive\\PythonBasic\\TEST_PYA0502E\\Test_1.txt")
ex_4_ = ex_4.read()
result = ex_4_.split()
print(result)
str = ""
for i in result:
    str += i
    str += " "
print(str)
new = open("D:\\GG_Drive\\PythonBasic\\TEST_PYA0502E\\Test_1.txt", "w+")
new.write(str)

# #Bài 5
# from TEST_PYA0502E.Ex_5 import *
# Std = Student("A26296", "Nguyễn Ngọc Hải", "1997", "Haiminhtlu@gmail.com", "Hà Nội", "ĐH Thăng Long", "PYA0502E", "Python")
# Std.Show_info()

#Bài 6

# from TEST_PYA0502E.postgres import *
# test = Test()
# test.create_job()
# test.create_employee()

