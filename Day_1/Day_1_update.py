# print('hello world')

a = 1
b = 2
total = a + b
print(total)

name = 'Hoang'
print(name)

name_2 = "Linh"
print(name_2)

c = b - a
print(c)

#  print(2*3)

# print(total // 2)  # day la phep chia lay so nguyen

# print(5 % 2)  # day la phep chia lay so du

print(2 ** 3)  # day la phep nhan so mu

# toan tu quan he
print(total == c)  # so sanh bang
print(total > c)
print(total < c)
print(total != c)  # toan tu so sanh khac
print(4 >= 5)  # toan tu so sanh lon hon hoac bang
print(4 >= 4)
print(4 <= 2)  # toan tu so sanh nho hon hoac bang

# toan tu gan ket hop toan tu so hoc
x = 1
x += 10
# x = x + 10
# x = 10
print(x)

x -= 1
# x = x - 1
print(x)

x /= 2
# x = x / 2
print(x)

x *= 5
# x = x * 5
print(x)

print(5 == 5 and 5 >= 6)
print(5 == 5 and 5 >= 4)

# print(5 == 5 or 5 >= 6)
print(5 >= 6 or 5 == 5)

test = True
print(not test)

test_2 = False
print(not test_2)

print(not 5 > 4)

print((5 > 4 and 5 > 3) or 4 < 2)

dich_bit = 3
result = dich_bit << 4
# dich bao nhieu bit thi nhan bay nhieu lan voi 2 (2^n)
# 3 * 2 * 2 * 2 * 2
print(result)

dich_bit2 = 4
# dich bao nhieu bit thi chia bay nhieu lan cho 2 (2^n)
result = dich_bit2 >> 2
# 4 / 2 / 2
print(result)
