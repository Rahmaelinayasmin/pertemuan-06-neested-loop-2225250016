# Latihan 1: Pasangan Indeks

# Counter untuk menghitung banyak pasangan
count = 0

# Loop luar untuk nilai i dari 1 sampai 3
for i in range(1, 4):

    # Loop dalam untuk nilai j dari 1 sampai 4
    for j in range(1, 5):

        # Menampilkan pasangan i dan j
        print(i, j)

        # Menghitung setiap pasangan
        count += 1

# Menampilkan jumlah seluruh pasangan
print(f"Banyak pasangan = {count}")