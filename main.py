# DDP LAB-4
# Nama: <Hery Sholihin>
# NIM: <0110220114>

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
nama = input("Masukan Nama : ")
i = 0 #variable angka penambahan
while i < len(nama) + 1: #berisi statement jika variable i lebih kecil dari panjang input, maka akan true dan berjalan, dan loop tergantung banyaknya panjang kata.
    print(nama[:i]) #mencetak nama dengan string slicing, :i untuk variable 0.
    i = i+1 # penambahan 1 ke variable per loop

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print("\n")
while True:
    inp =input("Masukan Sebuah Teks : ")
    fr = "nf" #membuat variable peraturan frase
    ak = "yyy" #membuat variable peraturan kata akhir
    angka = "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" #variable yang peraturan mengecek ada angka atau tidak, angka 0 harus berada di akhir, supaya 1-9 bisa berjalan dan terbaca

    if len(inp) >= 8: #berisi statement jika panjang input kurang dari 8.
        if fr in inp.lower(): #berisi statement jika variable peraturan frase ada di input.
            if angka in inp: #berisi statement jika variable peraturan angka ada di input.
                if inp[-3:] == ak or inp[-3:] == ak.upper(): #berisi statement jika variable peraturan kata akhir berada di akhir menggunakan string slicing dari index.
                    print("Teks Valid, Program dihentikan")
                    break #Jika semua statement berisi true maka program akan berhenti.
                else:
                    print("Teks Tidak Valid 4")
            else:
                print ("Teks Tidak Valid 3")
        else:
            print ("Teks Tidak Valid 2")
    else:
        print ("Teks Tidak Valid 1")