class Book:
    def __init__(self,id,n_nhap,gia,sl,nxb):
        self.ID = id
        self.Date_Start = n_nhap
        self.Cost = gia
        self.Amount = sl
        self.Publishing = nxb

    def Create(self):
        id = input("Nhập mã sách : ")
        self.ID = id
        date = input("Ngày nhập sách : ")
        self.Date_Start = date
        gia = input("Nhập giá tiền cho sách : ")
        while not gia.isnumeric():
            print("Giá tiền cần nhập là dạng số .Mời nhập lại ")
            gia = input("Nhập lại giá tiền cho sách : ")
        gia = float(gia)
        self.Cost = gia
        sl = input("Nhập số lượng cho sách : ")
        while not sl.isnumeric():
            print("Số lượng sách phải là dạng số .Mời nhập lại ")
            sl = input("Nhập lại số lượng sách : ")
        sl = int(sl)
        self.Amount = sl
        nxb = input("Nhập nhà xuất bản : ")
        self.Publishing = nxb

    def Show_Book(self):
        print("Mã sách : ",self.ID)
        print("Ngày nhập : ",self.Date_Start)
        print("Giá tiền : ",self.Cost)
        print("Số lượng : ",self.Amount)
        print("Nhà xuất bản : ",self.Publishing)


class textBook(Book):
    def __init__(self,id,date,gia,sl,nxb,tt):
        super(textBook, self).__init__(id,date,gia,sl,nxb)
        self.Status = tt

    def Create(self):
        super(textBook,self).Create()
        status = input("Nhập trạng thái của sách. Mới(N)-Cũ(O)")
        while status != "O" and status != "N":
            print("Bạn cần nhập : N nếu là sách mới và O nếu là sách cũ")
            status = input("Nhập trạng thái của sách. Mới(N)-Cũ(O)")
        if status == "N":
            self.Status = True
        else:
            self.Status = False

    def Show_Book(self):
        super(textBook, self).Show_Book()
        if self.Status:
            print("Tình trạng : sách mới ")
        else:
            print("Tình trạng : sách cũ")
        self.Price()

    def Price(self):
        price = 0
        if self.Status:
            price = self.Amount * self.Cost
            print("Giá cho cuốn %s (sách mới) là %.2f" % (self.ID, price))
        else:
            price = self.Amount * self.Cost * 0.5
            print("Giá cho cuốn %s (sách cũ) là %.2f" % (self.ID, price))

class referBook(Book):
    def __init__(self,id,date,gia,sl,nxb,thue):
        super(referBook, self).__init__(id,date,gia,sl,nxb)
        self.Tax = thue

    def Create(self):
        super(referBook, self).Create()
        thue = input("Nhập số thuế : ")
        while not thue.isnumeric():
            print("Nhập lại số thuế. Viết dưới dạng số!")
            thue = input("Nhập số thuế : ")
        thue = float(thue)
        self.Tax = thue

    def Price(self):
        price = self.Amount * self.Cost + self.Tax
        print("Giá tiền : ", price)
    def Show_Book(self):
        super(referBook, self).Show_Book()
        self.Price()


def Manager_refeBook():
    list_refeBook = []
    num_refe = int(input("Nhập số sách tham khảo cần thêm : "))
    for i in range(0,num_refe):
        refe = referBook(0,0,0,0,0,0)
        refe.Create()
        list_refeBook.append(refe)

    # Tính trung bình cộng các đơn giá của sách tham khảo
    if num_refe > 0:
        sum_refe = 0
        for refe in list_refeBook:
            sum_refe = sum_refe + refe.Cost
        print("Trung bình cộng các đơn giá là : %.2f" % (sum_refe / num_refe))
    else:
        print("Trung bình cộng các đơn giá là : 0")

def Manager_textBook():
    list_textBook = []
    num_text = int(input("Nhập số sách giáo khoa cần thêm : "))
    for i in range(0, num_text):
        text = textBook(0, 0, 0, 0, 0, 0)
        text.Create()
        list_textBook.append(text)
    # Xuất ra các sách giáo khoa của nhà xuất bản X
    publishing = input("Nhập nhà xuất bản cần tìm : ")
    for text in list_textBook:
        if text.Publishing == publishing:
            print(text.ID)
