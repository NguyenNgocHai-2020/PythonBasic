# __author__ = 'Harve'


class Employee:


    dem = 0
    def __init__(self, str_name, age, salary=300):
        self.name = str_name
        self.age = age
        self.salary = salary
        Employee.dem +=1
        self.order = Employee.dem

    def show_info(self):

        print("Số thứ tự : ", self.order)
        print("Tên  : ", self.name)
        print("Tuổi : ", self.age)
        print("Mức lương : ", self.salary)

    def show_employee_count(self):
        print(Employee.dem)

    def _TNCN(self):
        if self.salary >= 1000:
            print("Thuế thu nhập cá nhân là 100")
        else:
            print(" Không cần đóng thuế thu nhập cá nhân ^^")

class Student:


    def __init__(self,ten,ns,mail,sdt,dc,donvi):
        self.name = ten
        self.date = ns
        self.mail = mail
        self.phone = sdt
        self.address = dc
        self.place = donvi

    def show_info(self):
        print("Tên : ", self.name)
        print("Ngày sinh : ", self.date)
        print("Email : ", self.mail)
        print("Điện thoại : ", self.phone)
        print("Địa chỉ : ", self.address)
        print("Đơn vị công tác : ", self.place)

    def get_infor(self,ten,date,mail,dt,dc="Hà Nội",dv="ITPLUS"):
        print(ten)
        print(date)
        print(mail)
        print(dt)
        print(dc)
        print(dv)

    def get_info_2(self, ten, phone, dc="Ha Noi", dv="ITPlus"):
        self.name = ten
        self.phone = phone
        self.address = dc
        self.place = dv
        self.show_info()








