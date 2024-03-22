# Atur cara mengira luas permukaan dan isi padu tangki air berbentuk silinder
# Isytihar pemalar
pi = float(3.142)

# Kod input
jejari = float(input("Masukkan jejari:"))
tinggi = float(input("Masukkan tinggi:"))

# Kod proses
luas_permukaan = (2*jejari**2*pi)+(2*jejari*pi*tinggi)
isi_padu = pi*jejari**2*tinggi

# Kod output
print("Luas permukaan tangki air berbentuk silinder ialah",round(luas_permukaan),2)
print("Isi padu tangki air berbentuk silinder ialah",round(isi_padu),2)
