"UTF-8"
import datetime
class Customer:
    def __init__(self,id,name,date,unit,sl):
        self.ID = id
        self.Name = name
        self.Date = date
        self.Unit = unit
        self.Amount = sl


    def Create(self):
        id = input("Nhập id khách hàng : ")
        self.ID = id
        name = input("Nhập họ tên khách hàng : ")
        self.Name = name
        day = int(input("Nhập ngày : "))
        month = int(input("Nhập tháng : "))
        year = int(input("Nhập năm : "))
        self.Date = datetime.date(year,month,day)
        unit = float(input("Nhập đơn vị giá : "))
        self.Unit = unit
        sl = float(input("Nhập sản lượng tiêu thụ : "))
        self.Amount = sl

    def Show_Customer(self):
        print("Mã khách hàng : ",self.ID)
        print("Tên khách hàng : ",self.Name)
        print("Ngày tháng xuất hóa đơn : ",self.Date)
        print("Đơn vị tính : ", self.Unit)
        print("Sản lượng tiêu thụ : ", self.Amount)
        # return "Mã khách hàng : %s \n"\
        #        "Tên khách hàng : %s \n"\
        #        "Ngày tháng xuất hóa đơn : %s \n"\
        #        "Đơn vị tính : %s \n"\
        #        "Sản lượng tiêu thụ : %s \n"%(self.ID,self.Name,self.Date,self.Unit,self.Amount)

class VN_Customer(Customer):

    def __init__(self, type, id, name, date, unit, sl, dinh_muc):
        super(VN_Customer, self).__init__(id, name, date, sl, unit)
        self.Type_Cus = type
        self.Level = dinh_muc

    def Create(self):
        super(VN_Customer, self).Create()
        select = int(input("Đối tượng sử dụng : \n"
                       "1.Hộ Sinh hoạt\n"
                       "2.Hộ Kinh doanh\n"
                       "3.Hộ Sản xuất \n"
                           "Mời chọn : "))
        type_cus = {1:"Hộ sinh hoạt",2:"Hộ kinh doanh",3:"Hộ sản xuất "}
        self.Type_Cus = type_cus[select]
        level = float(input("Nhập định mức : "))
        self.Level = level

    def Show_Customer(self):
        super(VN_Customer, self).Show_Customer()
        print("Đối tượng sử dụng : ", self.Type_Cus)
        print("Định mức : ",self.Level)
        self.Price()
        print("------------")

    def Price(self):
        price = 0
        if self.Amount <= self.Level:
            price = self.Amount * self.Unit
        else:
            price = self.Amount * self.Unit * ( self.Level + (self.Amount - self.Level)) * 2.5
        print("Giá tiền là : ",price)





class Foreigner(Customer):
    def __init__(self,nationality,id,name,date,unit,sl):
        super(Foreigner, self).__init__(id,name,date,sl,unit)
        self.Nationality = nationality

    def Create(self):
        super(Foreigner, self).Create()
        nation = input("Nhập quốc tịch : ")
        self.Nationality = nation

    def Show_Customer(self):
        super(Foreigner, self).Show_Customer()
        print("Quốc tịch : ", self.Nationality)
        print("Giá tiền : ", self.Price())
        print("------------")

    def Price(self):
        return self.Amount * self.Unit


# date = datetime.date(2020,12,6)
# date_2 = datetime.date(2020,12,5)
# print(date < date_2)
num = int(input("Nhập vào số : "))
lst = []
i = 1
while i <= num:
    cus = Customer(0, 0, 0, 0, 0)
    cus.Create()
    lst.append(cus)
    i += 1
for i in lst:
    i.Show_Customer()


