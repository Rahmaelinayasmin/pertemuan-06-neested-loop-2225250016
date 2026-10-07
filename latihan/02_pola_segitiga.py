# Latihan 2: Pola Segitiga

# Meminta pengguna memasukkan nilai n
n = int(input("Masukkan nilai n: "))

# Loop luar menentukan jumlah baris
for i in range(1, n + 1):

    # Loop dalam menentukan jumlah bintang pada setiap baris
    for j in range(i):

        # Mencetak bintang tanpa pindah baris
        print("*", end=" ")

    # Pindah ke baris berikutnya
    print()