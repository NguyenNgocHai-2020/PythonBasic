# for i in range(0, 9):
#     print(i)

# for i in range(0, 9, 2):
#     print(i)

# for i in range(1, 5):
#     print(i * i)

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     for j in range(0, 5):
#         print('%d / %d' % (i, j))

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i * j)

# for i in range(1, 5):
#     if i % 2 == 0:
#         print('So chan ', i)
#     else:
#         print('So le ', i)

# so_tu_nhien = int(input('Nhap so tu nhien'))
# if so_tu_nhien > 0:
#     for i in range(1, so_tu_nhien):
#         print(i)


# n = int(input())
# for i in range(1, n, 1):
#     print(i * 2)
# print(' nhap mot so nguyen tu ban phim:')
# n = int(input())
# if n > 10:
#     print('hay nhap 1 so nho hon 10')
# else:
#     for n in range (0, 10):
#         if n % 2 == 0:
#             print(' so chan la :', n)


# n = int(input())
# if n < 20:
#     for i in range(0, n):
#         # if i % 5 == 0 or i % 7 == 0
#             # print(n)
#         if i % 5 != 0 and i % 7 != 0:
#             continue
#         print(i)


# num = int(input("Nhap so : "))
# if num < 2:
#     print("%d khong la so nguyen to" % num)
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
#         if count > 2:
#             break
# if count > 2:
#     print("%d khong la so nguyen to" % num)
# else:
#     print("%d la so nguyen to " % num)


# max_num = 9
# i = 1
# while i <= 9:
#     print(i)
#     i += 1
# n = ''
# while not n.isnumeric() or int(n) <= 0:
#     print('Phai nhap n la so va phai > 0')
#     n = input('n = ')
# n = int(n)
# i = 1
# while i <= n:
#     print(i * 2)
#     i += 1

# n = input("Nhap vao so n: ")
# while not n.isnumeric() or int(n) > 10 or int(n) < 0:
#     n = input('Nhap lai so n: ')
# n = int(n)
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# n = int(input("Nhap vao so n <20 : "))
# while n > 20:
#     print("Nhap vao so n <20")
#     n = int(input(" so n:"))
# i = 1
# while i < n:
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)
#     i += 1

# n = int(input('nhap so: '))
# giai_thua = 1
# i = n
# while i > 0:
#     giai_thua = giai_thua * i
#     i -= 1
# print(giai_thua)
#
# # n = int(input('nhap so: '))
# giai_thua_2 = 1
# i = 1
# while i <= n:
#     giai_thua_2 = giai_thua_2 * i
#     i += 1
# print(giai_thua_2)
