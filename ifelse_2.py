nilai = int(input("NILAI : "))

print("Nilain anda :", nilai, "\n")

if nilai > 100:
    print("Nilai melebihi 100")
elif nilai >= 86:
    print('LULUS A')
elif nilai >= 75:
    print('LULUS B')
elif nilai >= 61:
    print('TIDAK LULUS C')
elif nilai >= 46:
    print('TIDAK LULUS D')
elif nilai >= 0:
    print('TIDAK LULUS E')
else:
    print("Nilai kurang dari 0")
