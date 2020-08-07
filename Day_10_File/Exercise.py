import os
#Bài 1
# ex_1 = open("D:\\PythonBasic\\Day_9_OOP\\cus.txt")
# ex_1_ = ex_1.read()
# print(ex_1_)

#Bài 2
# ex_2 = open("D:\\noi_luu_file\\Ex_1.txt")
# line_1 = ex_2.readline()
# line_2 = ex_2.readline()
# print(line_1, "---", line_2)

#Bài 3
# ex_3 = open("D:\\noi_luu_file\\Ex_3.txt", "w+", encoding="UTF-8")
# info = "Name : Nguyen Ngoc Hai \n" \
#        "Class : PYA0520E"
# ex_3.write(info)
# ex_3.seek(0, 0)
# ex_3_ = ex_3.read()
# print(ex_3_)

#Bài 4
# ex_4 = open("D:\\noi_luu_file\\Ex_4.txt", 'w+', encoding="UTF-8")
# text = "Thuc \n hanh \n voi \n file\n IO\n"
# ex_4.write(text)

#Bài 5
# name = input("Nhập tên : ")
# age = int(input("Nhập tuổi : "))
# email = input("Nhập email : ")
# skype = input("Nhập skype : ")
# address = input("Nhập địa chỉ : ")
# work_place = input("Nhập nơi làm việc : ")
# ex_5 = open("D:\\noi_luu_file\\Ex_5.txt", "w+", encoding="UTF-8")
# ex_5.write("Tên : %s \nTuổi : %d \nEmail : %s \nSkype : %s \nĐịa chỉ : %s \nNơi làm việc : %s \n" % (name, age, email, skype, address, work_place))
# ex_5.seek(0,0)
# ex_5_ = ex_5.read()
# print(ex_5_)
#Bài 6
# ex_6 = open("D:\\noi_luu_file\\Ex_6.txt")
# ex_6_ = ex_6.read()
# str = ex_6_.split()
# print(str)
#cách 1
# result = []
# result_1 = []
# for str in a:
#     if result.count(str) == 0:
#         result.append(str)
# print(result)
#
# for str in result:
#     count = 0
#     for i in a:
#         if str == i:
#             count += 1
#     result_1.append("%s : %d" % (str,count))
#     # result_1.append({str:count})
# print(result_1)
#cách 2
# result = {}
# for i in str:
#     result[i] = str.count(i)
# print(result)









