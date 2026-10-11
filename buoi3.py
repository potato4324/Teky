#1
print("\n--- Bài 1: Thông tin cá nhân ---")
name = "Nguyễn Văn An"
age = 16
height = 1.65
is_student = True

print("Tên:", name)
print("Tuổi:", age)
print("Chiều cao:", height)
print("Là học sinh:", is_student)

#2
print("\n--- Bài 2: Kiểm tra kiểu dữ liệu ---")
a = 15
b = 3.14
c = "Python"
d = True

print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool

#3
print("\n--- Bài 3: Tính tổng hai số ---")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Thương:", a / b)

#4
print("\n--- Bài 4: Chu vi & diện tích HCN ---")
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
chu_vi = (dai + rong) * 2
dien_tich = dai * rong
print("Chu vi:", chu_vi)
print("Diện tích:", dien_tich)

#5
print("\n--- Bài 5: Điểm trung bình ---")
toan = float(input("Toán: "))
van = float(input("Văn: "))
anh = float(input("Anh: "))
dtb = (toan + van + anh) / 3
print(f"Điểm trung bình: {dtb:.2f}")

#6
print("\n--- Bài 6: Đổi phút → giờ & phút ---")
n = int(input("Nhập số phút: "))
gio = n // 60
phut = n % 60
print(f"{gio} giờ {phut} phút")

#7
print("\n--- Bài 7: Tách số 3 chữ số ---")
n = int(input("Nhập số có 3 chữ số: "))
hang_tram = n // 100
hang_chuc = (n // 10) % 10
hang_don_vi = n % 10
print("Hàng trăm:", hang_tram)
print("Hàng chục:", hang_chuc)
print("Hàng đơn vị:", hang_don_vi)

#8
print("\n--- Bài 8: Tính lũy thừa ---")
a = int(input("Nhập a: "))
n = int(input("Nhập n: "))
print(f"{a}^{n} =", a ** n)

#9
print("\n--- Bài 9: Đổi nhiệt độ C → F ---")
C = float(input("Nhập nhiệt độ C: "))
F = C * 9 / 5 + 32
print(f"{C}°C = {F:.1f}°F")

#10
print("\n--- Bài 10: Tính tiền mua hàng ---")
ten = input("Sản phẩm: ")
don_gia = float(input("Đơn giá: "))
so_luong = int(input("Số lượng: "))
tong_tien = don_gia * so_luong
print(f"Bạn mua {so_luong} {ten}, tổng tiền là {tong_tien:.0f} đồng.")

print("\n" + "=" * 50)
print("🟠 MỨC 3 – SO SÁNH VÀ LOGIC")
print("=" * 50)

#11
print("\n--- Bài 11: Kiểm tra số dương ---")
n = int(input("Nhập số nguyên n: "))
print(n > 0)

#12
print("\n--- Bài 12: Kiểm tra tuổi 6–18 ---")
tuoi = int(input("Nhập tuổi: "))
print(6 <= tuoi <= 18)

#13
print("\n--- Bài 13: Kiểm tra 10 ≤ x ≤ 50 ---")
x = int(input("Nhập x: "))
print(x >= 10 and x <= 50)

#14
print("\n--- Bài 14: Điều kiện tham gia trò chơi ---")
age = int(input("Nhập tuổi: "))
has_ticket = input("Có vé? (True/False): ") == "True"
co_the_tham_gia = age >= 10 and has_ticket
print("Được tham gia:", co_the_tham_gia)

#15
print("\n--- Bài 15: Kiểm tra số chẵn ---")
n = int(input("Nhập n: "))
print(n % 2 == 0)

print("\n" + "=" * 50)
print("🔴 MỨC 4 – TỔNG HỢP")
print("=" * 50)

#16
print("\n--- Bài 16: Máy tính đơn giản ---")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

#17
print("\n--- Bài 17: Hóa đơn mua hàng ---")
ten = input("Tên sản phẩm: ")
don_gia = float(input("Đơn giá: "))
so_luong = int(input("Số lượng: "))
giam_gia = float(input("Phần trăm giảm giá: "))

thanh_tien = don_gia * so_luong
tien_giam = thanh_tien * giam_gia / 100
phai_tra = thanh_tien - tien_giam

print("\n===== HÓA ĐƠN =====")
print(f"Sản phẩm     : {ten}")
print(f"Đơn giá      : {don_gia:.0f}")
print(f"Số lượng     : {so_luong}")
print(f"Thành tiền   : {thanh_tien:.0f}")
print(f"Giảm giá     : {giam_gia}% → {tien_giam:.0f}")
print(f"Phải trả     : {phai_tra:.0f} đồng")

#18
print("\n--- Bài 18: Điều kiện học bổng ---")
toan = float(input("Toán: "))
van = float(input("Văn: "))
anh = float(input("Anh: "))
dtb = (toan + van + anh) / 3

du_dieu_kien = dtb >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5
print("Điểm trung bình:", round(dtb, 2))
print("Đủ điều kiện học bổng:", du_dieu_kien)

#19
print("\n--- Bài 19: Tính tuổi từ năm sinh ---")
nam_sinh = int(input("Năm sinh: "))
nam_hien_tai = int(input("Năm hiện tại: "))
tuoi = nam_hien_tai - nam_sinh
print("Tuổi:", tuoi)
print("Từ 13 tuổi trở lên:", tuoi >= 13)
print("Từ 13 đến 18 tuổi:", 13 <= tuoi <= 18)
print("Dưới 18 tuổi:", tuoi < 18)

#20
print("\n--- Bài 20: Thông tin học sinh tổng hợp ---")
ho_ten = input("Họ tên: ")
tuoi = int(input("Tuổi: "))
toan = float(input("Điểm Toán: "))
van = float(input("Điểm Văn: "))
anh = float(input("Điểm Anh: "))

dtb = (toan + van + anh) / 3

du_dtb = dtb >= 8
du_3_mon = toan >= 6.5 and van >= 6.5 and anh >= 6.5
dung_do_tuoi = 13 <= tuoi <= 18
thoa_man_tat_ca = du_dtb and du_3_mon and dung_do_tuoi

print("\n========== THÔNG TIN HỌC SINH ==========")
print(f"Họ tên          : {ho_ten}")
print(f"Tuổi            : {tuoi}")
print(f"Điểm Toán       : {toan}")
print(f"Điểm Văn        : {van}")
print(f"Điểm Anh        : {anh}")
print(f"Điểm trung bình : {dtb:.2f}")
print("----------------------------------------")
print(f"ĐTB >= 8              : {du_dtb}")
print(f"Cả 3 môn >= 6.5       : {du_3_mon}")
print(f"Tuổi từ 13 đến 18     : {dung_do_tuoi}")
print("----------------------------------------")
print(f"THỎA MÃN TẤT CẢ ĐIỀU KIỆN: {thoa_man_tat_ca}")
print("========================================")