# #Bài 1
# num = int(input("Nhập vào số n : "))
# result = {}
# for i in range(1, num+1):
#     result[i] = i*i
# print(result)

#Bài 2
# str = input(" Nhập vào một chuỗi nào : ")
# str = str.strip(" ")
# result = ""
# for i in str:
#     if str.count(i) <= 1:
#         result += i
# print(result)
# print(result.s)

# #Bài 3
# lst = input("Nhập vào một list số cách nhau bởi dấu phẩy : ")
# lst = lst.split(",")
# lst_even_num = []
# sum_even_num = 0
# sum_odd_num = 0
# count_even = 0
# count_odd = 0
# lst_odd_num = []
# for i in lst:
#     i = int(i)
#     if i % 2 == 0:
#         lst_even_num.append(i)
#         sum_even_num += i
#         count_even += 1
#     else:
#         lst_odd_num.append(i)
#         sum_odd_num += i
#         count_odd += 1
# print("List chẵn là ", lst_even_num)
# print("TBC tổng chẵn : ", sum_even_num/count_even)
# print("List lẻ là ", lst_odd_num)
# print("TBC tổng lẻ : ", sum_odd_num/count_odd)

#Bài 4

class People:
    def __init__(self, name, age, add, phone, gender):
        self.name = name
        self.age = age
        self.add = add
        self.phone = phone
        self.gender = gender

    def get_Info(self):
        name = input("Nhập tên : ")
        self.name = name
        age = int(input("Nhập tuổi : "))
        self.age = age
        add = input("Nhập địa chỉ : ")
        self.add = add
        phone = input("Nhập số điện thoại : ")
        self.phone = phone
        gender = input("Nhập giới tính  : ")
        self.gender = gender

    def Display(self):
        print("Tên : ", self.name)
        print("Giới tính : ", self.gender)
        print("Tuổi : ", self.age)
        print("Số điện thoại : ", self.phone)



class Employee(People):
    def __init__(self, name, age, add, phone, gender, salary, position, department):
        super(Employee, self).__init__(name, age, add, phone, gender)
        self.salary = salary
        self.position = position
        self.department = department

    def get_Info(self):
        super(Employee, self).get_Info()
        salary = float(input("Nhập tiền lương : "))
        self.salary = salary
        position = input("Nhập chức vụ : ")
        self.position = position
        department = input("Nhập phòng ban : ")
        self.department = department

    def Display(self):
        super(Employee, self).Display()
        print("Tiền lương : ", self.salary)
        print("Chức vụ : ", self.position)
        print("Phòng ban : ", self.department)
        self.tax()
        print("_________________")

    def tax(self):
        if self.salary > 9000000:
            tax = self.salary * 0.1
            print("Tiền thuế : ", tax)
        else:
            print("Không cần đóng thuế")

num = int(input("Nhập vào số nhân viên : "))
lst_emp = []
i = 1
while i <= num:
    emp = Employee(0, 0, 0, 0, 0, 0, 0, 0)
    emp.get_Info()
    lst_emp.append(emp)
    i += 1
for emp in lst_emp:
    emp.Display()
total_salary = 0
for emp in lst_emp:
    total_salary += emp.salary
print("Tổng lương là : %.2f " % total_salary)



# import os
# ex_5 = open("/Volumes/DATA/GG_Drive/PythonBasic/noi_luu_file/ex_review", "w+")
# ex_5.write("1,2,3,4,5,6,7,8")
# ex_5.seek(0, 0)
# ex_5 = ex_5.read()
# str = ex_5.split(",")
# print(str)
# total = 0
# for i in str:
#     i = int(i)
#     total += i
# print(total)





