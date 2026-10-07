# Tugas 3: Tabel Perkalian dan Statistik

print("==========================================")
print("     TABEL PERKALIAN DAN STATISTIK")
print("==========================================")

# Meminta pengguna memasukkan bilangan positif
n = int(input("Masukkan nilai n: "))

# Validasi input
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan nilai n: "))

# Akumulator untuk menghitung total seluruh hasil
total_semua = 0

# Counter untuk menghitung banyak hasil yang genap
count_genap = 0

# Loop luar untuk menentukan baris
for i in range(1, n + 1):

    # Akumulator jumlah pada setiap baris
    total_baris = 0

    # Loop dalam untuk menentukan kolom
    for j in range(1, n + 1):

        # Menghitung hasil perkalian
        hasil = i * j

        # Menampilkan hasil perkalian dengan format rapi
        print(f"{hasil:4}", end="")

        # Menambahkan hasil ke jumlah baris
        total_baris += hasil

        # Menambahkan hasil ke total keseluruhan
        total_semua += hasil

        # Mengecek apakah hasil merupakan bilangan genap
        if hasil % 2 == 0:

            # Jika genap, counter bertambah satu
            count_genap += 1

    # Menampilkan jumlah pada baris tersebut
    print(f"   | jumlah baris = {total_baris}")

# Menampilkan hasil akhir
print("------------------------------------------")
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")