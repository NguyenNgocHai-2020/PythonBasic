class Vehicle:
    def __init__(self,name,value,xylanh):
        self.Name = name
        self.Value = value
        self.Xylanh = xylanh
        self.Thue = 0


    def thue(self):
        if self.Xylanh < 100:
            self.Thue = self.Value * 0.01
        elif 100 <= self.Xylanh <= 200:
            self.Thue = self.Value * 0.03
        else:
            self.Thue = self.Value * 0.05

        return(self.Thue)

    def Create(self):
        name = input("Nhập tên xe : ")
        self.Name = name
        value = input("Nhập giá trị của xe : ")
        value = float(value)
        self.Value = value
        xylanh = input("Nhập dung tích xylanh : ")
        xylanh = int(xylanh)
        self.Xylanh = xylanh

    def to_string(self):
        print("Tên xe : ",self.Name)
        print("Dung tích xylanh : ",self.Xylanh)
        print("Giá trị : ",self.Value)
        print("Giá trị thuế trước bạ : ",self.thue())

# list_vehicle = []
# tobe_continue = 'C'
# while tobe_continue.upper() == 'C':
#     tobe_continue = input('Tiep tuc nhap (C/K)')
#     if tobe_continue.upper() == 'K':
#         break
#     dung_tich = input('Nhap dung tich')
#     gia_tri = input('Nhap gia tri')
#     xylanh = input('Nhap xylanh')
#     xe = Vehicle(dung_tich, gia_tri, xylanh)
#     list_vehicle.append(xe)
#
# for vehicle in list_vehicle:
#     print(vehicle.Xylanh)





class bus:
    def __init__(self,id,tai_xe,so_xe):
        self.ID = id
        self.Tai_Xe = tai_xe
        self.So_xe = so_xe
        self.Doanh_Thu = 0

    def Create(self):
        id = input("Nhập mã xe : ")
        self.ID = id
        tai_xe = input("Nhập tên tài xế : ")
        self.Tai_Xe = tai_xe
        so_xe = input("Nhập số xe : ")
        self.So_xe = so_xe

    def Show_Info(self):
        print("Mã chuyến xe : ",self.ID)
        print("Tên tài xế : ",self.Tai_Xe)
        print("Số xe : ",self.So_xe)
        # print("Doanh thu : ")

class bus_ngoai(bus):
    def __init__(self,id,tai_xe,so_xe,doanh_thu,noi_den,so_ngay):
        super(bus_ngoai, self).__init__(id,tai_xe,so_xe,doanh_thu)
        self.Noi_den = noi_den
        self.So_ngay = so_ngay

    def Create(self):
        super(bus_ngoai,self).Create()
        noi_den = input("Nơi đến : ")
        self.Noi_den = noi_den
        so_ngay = input("Số ngày : ")
        self.So_ngay = so_ngay

    def Show_Info(self):
        super(bus_ngoai,self).Create()


class bus_noi(bus):
    def __init__(self,id,tai_xe,so_xe,doanh_thu,so_km,so_tuyen):
        super(bus_noi, self).__init__(id,tai_xe,so_xe,doanh_thu)
        self.So_km = so_km

    def Create(self):
        super(bus_noi,self).Create()
        so_km = input("Nhập số km đi được : ")
        self.So_km = so_km
