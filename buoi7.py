# #1
# ten = "An"
# tuoi = 15
# chieu_cao = 1.65
# dang_di_hoc = True
# print("ten =", ten, "->", type(ten))
# print("tuoi =", tuoi, "->", type(tuoi))
# print("chieu_cao =", chieu_cao, "->", type(chieu_cao))
# print("dang_di_hoc =", dang_di_hoc, "->", type(dang_di_hoc))

# #3
# a = 17
# b = 5
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a // b =", a // b)
# print("a % b =", a % b)
# print("a ** b =", a ** b)
# n = int(input("Nhập một số nguyên: "))
# if n % 2 == 0:
#     print("Số chẵn")
# else:
#     print("Số lẻ")

# #4
# print("a", "b", "c", sep="-", end=" ")
# print("Xin chào!", end="")
# print("Tạm biệt!", end=" ")
# print("2025", "10", "25", sep="/")

# #5
# ten = input("Nhập tên: ")
# tuoi = int(input("Nhập tuổi: "))
# print(f"Xin chào {ten}! Sang năm bạn {tuoi + 1} tuổi.")
# chieu_dai = float(input("Nhập chiều dài: "))
# chieu_rong = float(input("Nhập chiều rộng: "))
# chu_vi = (chieu_dai + chieu_rong) * 2
# dien_tich = chieu_dai * chieu_rong
# print("Chu vi =", chu_vi)
# print("Diện tích =", dien_tich)

# #6
# chuoi = "Python"
# print("Ký tự đầu:", chuoi[0])
# print("Ký tự cuối:", chuoi[-1])
# print("3 ký tự đầu:", chuoi[:3])
# print("Chuỗi đảo ngược:", chuoi[::-1])
# print("Chuỗi lặp lại:", "-".join([chuoi] * 3))

# #7
# toan = float(input("Nhập điểm Toán: "))
# van = float(input("Nhập điểm Văn: "))
# print("Cả hai môn đều >= 5:", toan >= 5 and van >= 5)
# print("Có ít nhất một môn >= 8:", toan >= 8 or van >= 8)
# print("Có bị điểm liệt không:", not (toan >= 3 and van >= 3))
# diem_tb = (toan + van) / 2
# print("Đạt học sinh giỏi:", diem_tb >= 8 and toan >= 6 and van >= 6)

# #8
# ho_ten = input("Nhập họ tên: ").strip()
# print("Chữ hoa:", ho_ten.upper())
# print("Chữ thường:", ho_ten.lower())
# print("Số ký tự:", len(ho_ten))
# print(f'Họ tên "{ho_ten.upper()}" có {len(ho_ten)} ký tự.')