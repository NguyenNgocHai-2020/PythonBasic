#Bài 1
# num = int(input("Nhập vào số n : "))
# result = {}
# for i in range(1, num+1):
#     result[i] = i*i
# print(result)

#Bài 2
# d1 = {'a': 15, 'b': 20, 'c': 30, 'e': 60}
# d2 = {'a': 30, 'b': 20, 'g': 50}
# result = d1
# for i in d2:
#     if i in d1:
#         result[i] = result[i] + d2[i]
#     else:
#         result[i] = d2[i]
# print(result)

#Bài 3
# dictionary = {"IV": "S001", "V": "S002", "VI": "S001", "VII": "S005", "VIII": "S005", "IX": "S009", "X": "S007"}
# _result = []
#
# for i in dictionary.values():
#     if _result.count(i) == 0:
#         _result.append(i)
# print(_result)

#Bài 4
# str = input(" Nhập vào một câu bất kỳ : ")
# count_alpha = 0
# count_digit = 0
# for i in str:
#     if i.isalpha():
#         count_alpha += 1
#     elif i.isnumeric():
#         count_digit += 1
# print({"alpha ": count_alpha,"digit ": count_digit})

#Bài 5
str = input("Nhập vào chuỗi bất kỳ : ")
result = {}
for i in str:
    result[i] = str.count(i)
print(result)

#Bài 6
# haha = {}
# for i in result:
#     for i+1 in result:
#         if i>j:
#             haha = result[i]
#             result[i] = result[j]
#             result[j] = haha
# for i in result:
#     print(result[i])


