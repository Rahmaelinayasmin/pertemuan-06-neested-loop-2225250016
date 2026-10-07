# Latihan 4: Menghitung Pasangan

# Meminta input n
n = int(input("Masukkan nilai n: "))

# Counter untuk menghitung pasangan yang memenuhi syarat
count = 0

# Loop untuk i dari 1 sampai n
for i in range(1, n + 1):

    # Loop untuk j dari 1 sampai n
    for j in range(1, n + 1):

        # Mengecek apakah i + j kurang dari atau sama dengan n
        if i + j <= n:

            # Jika memenuhi syarat, counter bertambah
            count += 1

# Menampilkan hasil
print(f"Banyak pasangan = {count}")