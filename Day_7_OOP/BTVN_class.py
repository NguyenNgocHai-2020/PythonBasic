class HinhChuNhat:

    def __init__(self):
        self.C_Dai = 0
        self.C_Rong = 0

    def set_Dai(self, cd):
        self.C_Dai = cd

    def set_Rong(self, cr):
        self.C_Rong = cr

    def get_Dai(self):
        return self.C_Dai

    def get_Rong(self):
        return self.C_Rong

    def Dien_Tich(self):
        s = self.C_Dai * self.C_Rong
        return s

    def Chu_Vi(self):
        P = (self.C_Dai + self.C_Rong) * 2
        return P

    def to_string(self):
        print("Chiều dài hình chữ nhật là : ", self.C_Dai)
        print("Chiều rộng hình chữ nhật là : ",self.C_Rong)
        print("Chu vi hình chữ nhật là : ",self.Chu_Vi())
        print("Diện tích hình chữ nhật là : ",self.Dien_Tich())
#
# class Student:
#     def __init__(self):
#         self.