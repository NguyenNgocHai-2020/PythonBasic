class HocVien:
    def __init__(self,id,name,toan,ly,hoa):
        self.ID = id
        self.Name = name
        self.P_Toan = toan
        self.P_Ly = ly
        self.P_Hoa = hoa

    def set_ID(self,id):
        self.ID = id

    def set_Name(self,name):
        self.Name = name

    def set_P_Toan(self,toan):
        # toan = float(toan)
        self.P_Toan = toan

    def set_P_Ly(self,ly):
        self.P_Ly = ly

    def set_P_Hoa(self,hoa):
        # hoa = float(hoa)
        self.P_Hoa = hoa


    def TBC(self):
        return (self.P_Toan + self.P_Ly + self.P_Hoa) / 3

    def to_string(self):
        print("Mã sinh viên : ",self.ID)
        print("Tên : ",self.Name)
        print("Điểm toán : ",self.P_Toan)
        print("Điểm lý : ",self.P_Ly)
        print("Điểm Hóa : ",self.P_Hoa)
        print("Điểm trung bình : ",self.TBC())
