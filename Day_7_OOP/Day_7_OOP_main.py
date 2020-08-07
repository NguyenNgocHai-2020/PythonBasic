from Day_7_OOP.Day_7_OOP_class import Student
from datetime import datetime


# emp_1 = Employee('Nguyen Chinh Son', 24, 1000)
# emp_2= Employee('Nguyen Ngọc Hải', 23, 800)
# emp_3= Employee('Hoàng Khánh An', 20)
# emp_1.height = 1.71
# emp_2.show_info()
# emp_3.show_info()
# print(emp_1.name)
# # son.show_employee_count()
# emp_3._TNCN()
# if hasattr(emp_1,'height'):
#     print(emp_1.height)
# else:
#     print("Không có tham số cho height")


# emp_4 = Employee("Lê Văn Việt",18)
# emp_4.show_info()
# print(datetime.now())
#
num = input("Nhập số nhân viên cần thêm : ")
num = int(num)
for i in range(0,num):
    i = Student()
for i in range(0,num):
    i = int(i)
    i.show_infor()

hoc_vien_1 = Student("Nguyen Ngoc Hai", "29051997", "abc","123456789", "Hoan Kiem", "DHTL")
# hoc_vien_1.show_info()
#
# hoc_vien_1.get_info(hoc_vien_1.name, hoc_vien_1.phone)
# hoc_vien_1.get_info(hoc_vien_1.name, hoc_vien_1.phone,
#                     hoc_vien_1.address, hoc_vien_1.place)
hoc_vien_1.get_info_2('Hai Ngoc', '01234')
# hoc_vien_1.get_info_2('Hai Ngoc', '01234', 'HCM', 'FPT')
