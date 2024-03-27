def hitung_nilai_kehadiran(jumlah_kehadiran):
    nilai_kehadiran = jumlah_kehadiran * 16
    return nilai_kehadiran

def hitung_total_tugas(nilai_tugas):
    total_tugas = sum(nilai_tugas)
    return total_tugas

def hitung_nilai_akhir(nilai_kehadiran, total_tugas, nilai_uts, nilai_uas):
    nilai_akhir = nilai_kehadiran + total_tugas + nilai_uts + nilai_uas
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return 'A'
    elif nilai_akhir >= 80:
        return 'B'
    elif nilai_akhir >= 70:
        return 'C'
    elif nilai_akhir >= 60:
        return 'D'
    else:
        return 'E'

def main():
    jumlah_kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))
    nilai_tugas = [float(input("Masukkan nilai tugas ke-{}: ".format(i+1))) for i in range(8)]
    nilai_uts = float(input("Masukkan nilai UTS mahasiswa: "))
    nilai_uas = float(input("Masukkan nilai UAS mahasiswa: "))

    nilai_kehadiran = hitung_nilai_kehadiran(jumlah_kehadiran)
    total_tugas = hitung_total_tugas(nilai_tugas)
    nilai_akhir = hitung_nilai_akhir(nilai_kehadiran, total_tugas, nilai_uts, nilai_uas)
    hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

    print("Nilai Akhir Mahasiswa: {:.2f}".format(nilai_akhir))
    print("Hasil Nilai Mahasiswa: ", hasil_nilai)

if __name__ == "__main__":
    main()
