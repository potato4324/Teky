import random
#1
# xucxac = [1,2,3,4,5,6]
# print(random.choice(xucxac))

#2
# print("Kí tự may mắn của bạn là: " random.choice(input("Nhap tên của bạn: ")))

#3
# a = ["Cool", "Fast", "Smart", "Happy"]
# n = ["Tiger", "Eagle", "Panda", "Coder"]
# tu = random.choice(a)+random.choice(n)
# print("Username gợi ý cho bạn:", tu)

#4
# pin1 = str(random.choice([1,2,3,4,5,6,7,8,9,0]))
# pin2 = str(random.choice([1,2,3,4,5,6,7,8,9,0]))
# pin3 = str(random.choice([1,2,3,4,5,6,7,8,9,0]))
# pin4 = str(random.choice([1,2,3,4,5,6,7,8,9,0]))
# pin = pin1+pin2+pin3+pin4
# print(pin)

#5
# chu_cai = "abcdefghijklmnopqrstuvwxyz"
# matkhau = ""
# n = int(input("Nhập độ dài mk: "))
# for i in range(n):
#     matkhau = matkhau + random.choice(chu_cai)
# print(matkhau)

#6
a = random.shuffle(["hoc","lap","trinh","python","rat","vui"])
print(a)