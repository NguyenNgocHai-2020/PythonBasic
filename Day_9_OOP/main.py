# from Day_9_OOP.HinhChuNhat import HinhChuNhat
#
# hcn = HinhChuNhat(7,3)
# hcn.to_string()

# from Day_9_OOP.HocVien import HocVien
# hv_1 = HocVien("A26296","Nguyễn Ngọc Hải",8,7,6)
# hv_1.to_string()
# hv_2 = HocVien(0,0,0,0,0)
# id = input("Nhập mã sinh viên : ")
# hv_2.set_ID(id)
# name = input("Nhập tên sinh viên : ")
# hv_2.set_Name(name)
# toan = input("Nhập vào điểm toán : ")
# ly = input("Nhập vào điểm ly : ")
# hoa = input("Nhập vào điểm hoa : ")
# while not toan.isnumeric() and ly.isnumeric() and hoa.isnumeric():
#     print("Điểm cần nhập là một số. Mời nhập lại ...")
#     toan = input("Nhập lại vào điểm toán : ")
#     ly = input("Nhập lại vào điểm lý : ")
#     hoa = input("Nhập lại vào điểm hóa : ")
# toan = float(toan)
# ly = float(ly)
# hoa = float(hoa)
# hv_2.set_P_Toan(toan)
# hv_2.set_P_Hoa(ly)
# hv_2.set_P_Ly(hoa)
# hv_2.to_string()
# a = [hv_1,hv_2]
# print(a)

from Day_9_OOP.Vehicle import Vehicle

# veh = Vehicle("Blade 120",23000000,150)
# veh.to_string()
#Nhập chuỗi xe
# list_vehicle = []
# tobe_continue = "C"
# while tobe_continue.upper() == "C":
#     tobe_continue = input("Tiếp tục nhập (C/K)")
#     if tobe_continue == "K":
#         break
#     xe = Vehicle(0,0,0)
#     xe.Create()
#     list_vehicle.append(xe)
#In chuỗi vừa nhập
# for vehicle in list_vehicle:
#     vehicle.to_string()


from  Day_9_OOP.Book import *

# print("--------------Chương trình quản lý sách----------------------")
# print("1.Sách giáo khoa")
# print("2.Sách tham khảo")
# select = int(input("Chọn chức năng ... : "))
# if select == 1:
#     Manager_textBook()
# elif select == 2:
#     Manager_refeBook()
# else:
#     print("Chức năng không có sẵn.Tạm biệt")

from Day_9_OOP.Customer import *


list_cus = []
key = int(input("Nhập 1 để thêm khách hàng VN \n     2 để thêm khách hàng nước ngoài \n     0 để thoát : "))
while key == 1 or key == 2:
    if key == 1:
        vn = VN_Customer(0, 0, 0, 0, 0, 0, 0)
        vn.Create()
        list_cus.append(vn)
    else:
        foreigner = Foreigner(0, 0, 0, 0, 0, 0)
        foreigner.Create()
        list_cus.append(foreigner)
    key = int(input(" Nhập 1 để thêm khách hàng VN \n     2 để thêm khách hàng nước ngoài \n     0 để thoát : "))
else:
    print("Tạm biệt ^^")
if list_cus != []:
    print("----------Hiển thị thông tin khách hàng------------")
    for cus in list_cus:
        cus.Show_Customer()

# print("Lấy thông tin hóa đơn theo ngày ")
# day_start = int(input("Nhập ngày bắt đầu : "))
# month_start = int(input("Nhập tháng bắt đầu : "))
# year = int(input("Nhập năm : "))
# day_end = int(input("Nhập ngày kết thúc : "))
# month_end = int(input("Nhập tháng kết thúc : "))
# start = datetime.date(year,month_start,day_start)
# end = datetime.date(year,month_end,day_end)
# for cus in list_cus:
#     if start <= cus.Date <= end:
#         cus.Show_Customer()

#Lưu file
# file = open("D:\\PythonBasic\\Day_9_OOP\\cus_1.txt", 'w+', encoding="UTF-8")
# cus = Customer(0,0,0,0,0)
# cus.Create()
# info = cus.Show_Customer()
# file.write(info)
# file.close()
# cus = open("D:\\PythonBasic\\Day_9_OOP\\cus.txt",encoding="UTF-8")
# cus_ = cus.read()
# cus_ = Customer(cus_)
# print(type(cus_))















# for cus in list_cus:
#     if cus.Nationality:
#         fore = cus.Show_Customer()
#         file.write(fore)
#     else:
#         vn = cus.Show_Customer()
#         file.write











