print("---------------------------------Function")
#Ví dụ
# def tong(a,b):
#     tong = a+b
#     return tong
# #Hàm trả về kết quả
# result = tong(2,3)
# print(result)
# print(tong(7,3))
# #Hàm không trả về kết quả
# def tong_(a,b):
#     print(a+b)
# tong_(10,15)
# #Biến thay đổi
# def sum(a,*num):
#     tong = a
#     for i in num:
#         tong+=i
#     return tong
# sum(1,2,3,4,5)
#Bài 1
# def S_hinhtron(r):
#     S = r*r*3.14
#     print(S)
# r = input("Nhập bán kính hình tròn : ")
# while not r.isnumeric():
#     print("Bạn cần nhập bán kính là chữ số !")
#     r = input("Nhập lại bán kính : ")
# r = int(r)
# S_hinhtron(r)

#Bài 2
# def B2(r,m,n):
#     result = []
#     for i in r:
#         i = int(i)
#         if i != m and i != n:
#             result.append(i)
#     print(result)
# lst = input("Nhập list : ")
# lst = lst.split(" ")
# B2(lst,8,11)

#Bài 3
# def giai_thua(n):
#     if n == 1:
#         return 1
#     return (n * giai_thua(n-1))
# print(giai_thua(3))
#Bài 4

# def B4(str):
#     count_upper = 0
#     count_lower = 0
#     for i in str:
#         if i.isupper():
#             count_upper+=1
#         elif i.islower():
#             count_lower+=1
#     print("Có %d chữ hoa và %d chữ thường" %(count_upper,count_lower))
# B4("Xin Chao Cac Ban")

#Bài 6
lst = input(("Nhập dãy số nào : "))
lst = lst.split(" ")
def B6(list):
    min = list[0]
    max = list[0]
    min = int(min)
    max = int(max)
    tong = 0
    TBC = 0
    count = 0
    for i in list:
        i = int(i)
        if i <= min:
            min = i
        if i >= max:
            max = i
        tong = tong + i
        count += 1
        TBC = tong/count
    lon_hon_TBC = []
    nho_hon_TBC = []
    bang_TBC = []
    for i in list:
        i = int(i)
        if i > TBC:
            lon_hon_TBC.append(i)
        elif i < TBC:
            nho_hon_TBC.append(i)
        else:
            bang_TBC.append(i)
    print("Số bé nhất là ",min)
    print("Số lớn nhất là ", max)
    print("Trung bình cộng của chuỗi là ", tong / count)
    print("Chuỗi lớn hơn TBC ",lon_hon_TBC)
    print("Chuỗi nhỏ hơn TBC ",nho_hon_TBC)
    print("Bằng số TBC ",bang_TBC)
B6(lst)
# def day_tang(list):
#     for i in list:
#         dem = 0
#         i=0
#         while list[i]<list[i+1]:
#             if list[i]<list[i+1]:
#                 print(list[i],list[i+1])
#             else:
#                 print(list[i+1])
#             i+=1
#             dem +=1
#
#
# day_tang([1,2,3,4,6,5,3])

# str = "Hello"
# def doi_xung(str):
#     for i in str:
#         if str[i] != str[(len(str))/2-1]:
#             print(1)
# doi_xung(1221)
