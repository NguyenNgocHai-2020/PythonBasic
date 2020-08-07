print("_______________________________________Kiểu dữ liệu string")
# str = "Hello"
#
# print(str[1:4])
#
# print(str[:3])
#
# print(str[2:])
#
# print(len(str))
#
# print("--------------------Toán tử thao tác với chuỗi")
# str_1="PYA0520E"
# print("------Cộng chuỗi")
# print(str+str_1)
# print("%s %s" %(str,str_1))
# print("------membership : In hay Not in")
# if 'PY' in str_1:
#     print("PY có nằm trong chuỗi")
# else:
#     print("PY không nằm trong chuỗi")
# print("------quan hệ : >,< ,>=,<=")
# print(str > str_1) #chuyển chuỗi qua chữ số rồi so sánh chứ không phải so sánh độ dài của chuỗi
#Xem thêm phương thức sử lý chuỗi tại drive bài 3

print("____________________________________________Kiểu dữ liệu List")
# fruits = ["apple","orange","banana","lemon","coconut"]
# for fruit in fruits:
#     print(fruit) # get element
# for fruit in range(0,len(fruits)):
#     print(fruit) #get index
#     print(fruit," : ",fruits[fruit]) #get element by index
#
# print(fruits[:4])
# print(fruits[2:])
# print(fruits[2:4])
# print(fruits[-3:])
print("------Cập nhật")
# fruits[1] = "water melon"
# fruits[0:1] = ["cherry","water melon"]
# fruits[0:4] = ["cherry","water melon"]
# print(fruits)
# print("------Thêm phần tử")
# # fruits.append('tomato') #Thêm mới 1 phần tử mặc định ở vị trí cuối cùng
# fruits.insert(2,"mango")
# print(fruits)
# fruits.insert(2,"patato")
# print(fruits)
# print("------Xóa phần tử")
# fruits.remove("patato")
# print(fruits)
# print("------Khác")
# print('lemon' in fruits)
# new_lst = [1,2,3]
# print(fruits+new_lst)
# print("------Một số hàm hay sử dụng( xem trong slide)")
#
# #convert từ tuple sang list
# tuple=(1,2,3)
# ls = list(tuple)
# print(ls)

#Bài 1
# _list = [1,2,3,4,5,6,7,8,9]
# total = 0
# for i in _list:
#     total += i
# print(total)
#Bài 2
# _list = [1,2,3,4,5]
# tich = 1
# for i in _list:
#     tich *= i
# print(tich)
#Bài 3
# _list = [1,2,3,4,5,6,7,8,9]
# even = []
# odd = []
# for i in _list:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print(even)
# print(odd)

#Bài 4
# _list = ["Red","Green","White","Black","Pink","Yellow"]
# _new = []
# x=_list[2:4]
# print(_new+x)

#Bài 5
# _list = ["zero","three"]
# _list.insert(1,"one")
# _list.insert(2,"two")
# print(_list)

#Bài 6
_list = ["abc","xyz","aba","1221","ii","ii2","5yhy5"]
count = 0
for i in _list :
    if len(i)>=3 and i[0] == i[len(i)-1]:
        count+=1
print(count)

#Bài 7
# _list = ["abc","xyz","abc","12","ii","12","5a"]


#Bài 8+9
# _list = [11,2,23,45,6,9]
# print(max(_list))
# print(min(_list))

#Bài 10
# new_lst = _list.copy()
# print(new_lst)

#Bài 11
# num = int(input("Nhập số n: "))
# fruits = ["apple","orange","banana","lemon","coconut"]
# for i in fruits:
#     if len(i) > num :
#         print(i)