#1
chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))
chu_vi = (chieu_dai+chieu_rong)*2
dien_tich = chieu_rong*chieu_dai
print(f"Chu vi: {chu_vi}")
print(f"Diện tích: {dien_tich}")
print()

#2
so_phut = int(input("Nhập số phút: "))
gio = so_phut // 60
phut = so_phut % 60
print(f"Giờ: {gio} Phút: {phut}")