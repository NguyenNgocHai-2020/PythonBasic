from Day_7_OOP.BTVN_class import HinhChuNhat

# hcn_2 = HinhChuNhat()
# cd = int(input("Nhập chiều dài hình chữ nhật : "))
# cr = int(input("Nhập chiều rộng hình chữ nhật : "))
# print("--------------------------------------------------")
# HinhChuNhat.set_Dai(hcn_2,cd)
# HinhChuNhat.set_Rong(hcn_2,cr)
# hcn_2.to_string()

lst = []
num = 2
# for i in range(0,num):
#
#     lst.append(i)
# print(lst)
for i in range(0,num):
    i = HinhChuNhat()
    cd = int(input("Nhập chiều dài hình chữ nhật : "))
    cr = int(input("Nhập chiều rộng hình chữ nhật : "))
    HinhChuNhat.set_Dai(i,cd)
    HinhChuNhat.set_Rong(i,cr)
    # lst.append(i)
print(lst)



