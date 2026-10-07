# Latihan 3: Jumlah Per Baris

# Loop luar untuk menentukan baris
for i in range(1, 5):

    # Akumulator untuk jumlah pada setiap baris
    total_baris = 0

    # Loop dalam untuk nilai j dari 1 sampai 3
    for j in range(1, 4):

        # Menghitung hasil perkalian
        nilai = i * j

        # Menambahkan hasil ke total baris
        total_baris += nilai

    # Menampilkan jumlah pada baris tersebut
    print(f"Jumlah baris {i} = {total_baris}")