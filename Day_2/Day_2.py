# print("____________________Nhập dữ liệu từ bàn phím")
# import time
# x = time.localtime()
# y=x[0]
# print(y)
# #Cách 1
# name = input("Mời bạn nhập tên : ")
# #Cách 2: ép kiểu
# year = int(input("Mời bạn nhập năm sinh : "))
# age = y-year
# point = float(input("Số điểm : "))
# print("____________________In dữ liệu ra ")
# #Cách 1
# print("Tên : ",name)
# #Cách 2
# print("Thông tin của bạn : ","Tên : %s , Tuổi %d , Điểm %.2f" %(name,age,point))
# #Trong đó : %s là kiểu string, %d là kiểu int, %f là kiểu float, %.2f là làm tròn đếm số thập phân thứ 2
# #Cách 3
# inf = "Tên của bạn là {Name_value}, {age_value} tuổi và bạn được {point_value} điểm".format(Name_value=name,point_value=point,age_value=age)
# print(inf)


#Bài 1: Tính tổng và in ra tổng của 3 số nguyên
# int_1 = int(input("Nhập số nguyên thứ 1 : "))
# int_2 = int(input("Nhập số nguyên thứ 2 : "))
# print("Tổng của 2 số là : ",int_1+int_2)

#Bài 4:Nhập 3 chuỗi và in ra chuỗi được ghép từ 3 chuỗi đó
# str_1 = input("Nhập chuỗi thứ 1 : ")
# str_2 = input("Nhập chuỗi thứ 2 : ")
# str_3 = input("Nhập chuỗi thứ 3 : ")
# print("Chuỗi được ghép là : ",str_1+str_2+str_3)

#Bài 5: Tính toán và in ra chu vi và diện tích hicnh tròn
# r = float(input("Nhập bán kính hình tròn : "))
# P = 2*r*3.14
# P = round(P,2)
# S = round(r*3.14*3.14,2) #Làm tròn đến chữ số thập phân thứ 2
# B_5 = "Hình tròn có chu vi là : {P_value} và diện tích là : {S_value}".format(S_value=S,P_value=P)
# print(B_5)


# print("____________________Cấu trúc rẽ nhánh")

# age = int(input("Nhập số tuổi : "))
# print("Tuối của bạn là : {age_value}".format(age_value=age))
# if age<18:
#     print("Bạn còn quá trẻ")
# elif 18<=age<=40:
#     print("Bạn trưởng thành")
# elif 40<age<=60:
#     print("Bạn trung niên")
# else:
#     print("Bạn già rồi !")

#Bài 1:
# num = input("Nhập số để kiểm tra tính chẵn lẻ : ")
# if num.isnumeric(): #Kiểm tra có phải số không
#     num=int(num) #ép cho nó kiểu số
#     if num%2 == 0:
#         print("Số {num_value} là số chẵn".format(num_value=num))
#     else:
#         print("Số {num_value} không là lẻ".format(num_value=num))

#Bài 2: Kiểm tra 3 số có phải cạnh của tam giác
# int_1 = int(input("Nhập số nguyên thứ 1 : "))
# int_2 = int(input("Nhập số nguyên thứ 2 : "))
# int_3 = int(input("Nhập số nguyên thứ 3 : "))
# if int_1+int_2>int_3 and int_1+int_3>int_2 and int_2+int_3>int_1:
#     print("Ba số vừa nhập là ba cạnh của tam giác ! ")
# else:
#     print("Đây không phải ba cạnh của tam giác !")

#Bài 3: Nhập vào năm sinh in ra tuổi
# import time
# x = time.localtime()
# year=x[0]
# ns = input("Mời nhập năm sinh : ")
# ns=int(ns)
# age = year - ns
# print("Bạn {age_value} tuổi ".format(age_value=age))

#Bài 4: Kiểm tra số chia hết cho 2,3 và cả 2 và 3
# num = input("Nhập số cần kiểm tra : ")
# if num.isnumeric():
#     num=int(num)
#     if num%2 == 0 and num%3 == 0:
#         print("Số {num_value} chia hết cho cả 2 và 3".format(num_value=num))
#     elif num%2 == 0:
#         print("Số {num_value} chia hết cho 2 nhưng không chia hết cho 3".format(num_value=num))
#     elif num%3 == 0:
#         print("Số {num_value} chia hết cho 3 nhưng không chia hết cho 2".format(num_value=num))
#     else:
#         print("Số {num_value} không chia hết cho 2 và 3".format(num_value=num))

#Bài 5:giải phương trình bậc 2:
# import math
# print ("Nhập hệ số cho phương trình bậc 2 : ")
# a = int(input("Nhập hệ số cho ẩn bậc 2 : "))
# b = int(input("Nhập hệ số cho ẩn bậc 1 : "))
# c = int(input("Nhập hệ số tự do : "))
#
# if a == 0:
#     print("Phương trình có một nghiệm x = ",-c/b)
# else:
#     delta = (b**2)-(4*a*c)
#
#     if delta > 0:
#         print("Phương trình có hai nghiệm phân biệt là x1 = {x1_value} và x2 = {x2_value}".format(x1_value=round((-b+math.sqrt(delta))/(2*a),2),x2_value=round((-b-math.sqrt(delta))/(2*a),2)))
#     elif delta == 0:
#         print("Phương trình có nghiệm kép là x = {x_value}".format(x_value=-b/(2*a)))
#     else:
#         print("Phương trình vô nghiệm !")




