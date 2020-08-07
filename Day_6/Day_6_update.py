from fractions import Fraction

# global variable
a_global = 1


def tong(a, b):
    # local variable
    return a + b
    # tong = a + a
    # return tong


def tong_2(a, b):
    print(a + b)
    print(a_global)


# result = tong(3, 4)
# print(result)
#
# print(tong(4, 5))

# result_2 = tong_2(3, 4)
# print(result_2)

# print(a_global)

# def tong_default(a, b=10):
#     return a + b
#
#
# print(tong_default(5))
# print(tong_default(5, 11))
#
#
# def show_info(name, age):
#     print('Name is', name)
#     print('Age is', age)
#
#
# def tong_3(a, *number):
#     tong = a
#     for i in number:
#         tong += i
#     return tong
#
# show_info(31, 'Le Manh Hoang')
# show_info(age=31, name='Le Manh Hoang')
#
# kq = tong_3(1, 2, 3, 4, 5)
# print(kq)
#
#
# def bai1(r):
#     dt_tron = r*r*3.14
#     print(dt_tron)
#
#
# bai1(2)

# def xoa(_list, ls_remove):
#     result = []
#     for i in _list:
#         if i not in ls_remove:
#             result.append(i)
#     return result
#
#
# input_ls = [1, 1, 2, 3, 4, 5, 5]
# remove_ls = [1, 5]
# print(xoa(input_ls, remove_ls))

# bai3
# def sogiaithua(n):
#     if n == 1:
#         return 1
#     return (n * sogiaithua(n - 1))
# num = int(input('so can tinh: '))
# print('so ',num,'co giai thua la',sogiaithua(num))

# def kq(input_data):
#     hoa = 0
#     thuong = 0
#     for i in input_data:
#         if i.isupper():
#             hoa += 1
#         elif i.islower():
#             thuong += 1
#     print('So chu hoa la: ', hoa)
#     print('So chu thuong la ', thuong)
#
#
# # input_str = input('Moi nhap chuoi ky tu: ')
# # kq(input_str)
#
# print(Fraction(3, 9))


# BAI 6
# def bai_6():
#     ex_ls = [9, 8, 1, 3, 5, 6]
#     print(max(ex_ls))
#     print(min(ex_ls))
#     tong = sum(ex_ls)
#     length = len(ex_ls)
#     tbc = tong/length
#     print(tbc)
#     nho_hon = []
#     lon_hon = []
#     for i in ex_ls:
#         if i < tbc:
#             nho_hon.append(i)
#         else:
#             lon_hon.append(i)
#     print(nho_hon)
#     print(lon_hon)

