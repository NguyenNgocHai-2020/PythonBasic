# print("-------------------------------Cấu trúc vòng lặp")
# print("__________________________for với range")
# print("In ra các số từ 1 đến 9")
# for i in range(1,10):
#     print(i)
# print("In ra các số chẵn từ 0 đến 10")
# for i in range(0,11,2):
#     print(i)
# print("In ra các số bình phương từ 1 đến 5")
# #cách 1
# for i in range(1,6):
#     print(i*i)
# #cách 2
# for i in range(1,6):
#     a = i * i
#     print(a)
#
# print("_____________Vòng lặp for lồng nhau")
# for i in range(1,5):
#     for j in range(0,6):
#         print("%d / %d" %(i,j))
# for i in range(1,6):
#     for j in range(3,5):
#         a = i * j
#         print(a)

# print("________________vòng for có lồng if_else")
# for i in range(1,10):
#     if i%2 == 0:
#         print("số chẵn là %d" %(i))
#     else:
#         print("số lẻ là %d" %(i))


# print("Bài 1 : Nhập vào số tự nhiên, in ra tích từ 2 đến n")
#
# n = int(input("Nhập số tự nhiên : "))
# tich = 2
#
# for i in range(1,n):
#     tich *= i
# print(tich)

# print("Bài 2")
# n = int(input("Nhập số tự nhiên : "))
# if n>10:
#     print("Số nhập phải bé hơn 10 ! ")
# else:
#     for i in range(1,n):
#         print(i)

# print("Bài 3")
# for i in range(80,101):
#     if (i%2==0 and i%3==0):
#         print(i)
# print("Bài 4")
# n = int(input("Nhập vào số n : "))
# if n < 20 :
#     for i in range(n,20):
#         if i%5==0 or i%7==0:
#             print(i)

# print("___________Kiểm tra số nguyên tố")
# num = int(input("Nhập vào số  : "))
# if num == 0 or num == 1 :
#     print("Đây không là số nguyên tố !")
# else:
#     count = 0
#     for i in range(2,int(num/2)+1):
#         i = int(i)
#         if num % i == 0:
#             count+=1
#     if count>2:
#         print("%d không là số nguyên tố " %num)
#     else:
#         print("%d là số nguyên tố " % num)

# print("Vòng lặp while - không tự động tăng giá trị, thường dùng cho vòng lặp khi chưa biết đích")
# max_num = 10
# i=1
# while i:
#     if i<max_num:
#         i+=1
#         print(i)

# print("convert bài tập dùng for sang while")
# print("bài 1")
# n = int(input("Nhập số tự nhiên : "))
# tich = 2
# i=1
# while i <= n :
#     tich *=2
#     i+=1
# print(tich)
#Bài 2
# n = input("Nhập số tự nhiên : ")
# while not n.isnumeric() or int(n)>10 or int(n)<0:
#     print("Số cần nhập bé hơn 10 !")
#     n=input("Nhập lại số tự nhiên : ")
# i=1
# n=int(n)
# while i <n:
#     if i % 2 == 0:
#         print(i)
#     i+= 1
# print("Bài 3")
# i = 80
# while i<=100:
#     if (i%2==0 and i%3==0):
#         print(i)
#     i+=1
#Bài tập về while
#BÀi 1
# i=0
# tich = 1
# while i<10:
#     tich *= i
#     i+=1
# print(tich)
#Bài 2 tương tự bài 1

#Bài 3:
# num = int(input("Nhập vào số  : "))
# if num == 0 or num == 1 :
#     print("Đây không là số nguyên tố !")
# else:
#     count = 0
#     i=1
#     while i<int(num/2)+1:
#         i = int(i)
#         if num % i == 0:
#             count+=1
#         i+=1
#     if count>2:
#         print("%d không là số nguyên tố !" %num)
#     else:
#         print("%d là số nguyên tố " % num)

#BÀi 4: Nhập vào số n, in ra tổng các số thỏa mãn nhỏ hơn n và là số chẵn
# num = input("Nhập số nguyên n : ")
# i = 1
# tong_chan = 0
# i = int(i)
# while not num.isnumeric():
#     print("Bạn cần nhập số nguyên!")
#     num = input(     "Nhập lại n : ")
# num = int(num)
# while i <= num:
#     if i % 2 == 0:
#         tong_chan += i
#         print(i)
#     i += 1
# print("Tổng các số chẵn là : ",tong_chan)
str = "hello các bạn"
print(str.find("các"))


