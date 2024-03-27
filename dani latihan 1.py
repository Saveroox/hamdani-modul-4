def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        print("Diskon yang diberikan sebesar Rp.", diskon)
    else:
        print("Anda tidak menerima diskon karena total belanjaan tidak mencapai Rp. 250.000")

total_belanja = int(input("Masukkan total belanjaan: Rp. "))
hitung_diskon(total_belanja)
