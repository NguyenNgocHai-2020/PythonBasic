class HinhChuNhat:
    def __init__(self,dai, rong):
        self.Dai = dai
        self.Rong = rong

    def DienTich(self):
        return self.Dai * self.Rong

    def ChuVi(self):
        return (self.Dai + self.Rong) * 2

    def to_string(self):
        print("Chiều dài hình chữ nhật là : ",self.Dai)
        print("Chiều rộng hình chữ nhật là : ", self.Rong)
        print("Chu vi hình chữ nhật là : ",self.ChuVi())
        print("Diện tích hình chữ nhật là : ",self.DienTich())