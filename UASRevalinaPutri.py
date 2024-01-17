class HP:
    def __init__(self, merk, harga, stok):
        self.merk = merk
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"Merk: {self.merk}, Harga: {self.harga} USD, Stok: {self.stok} unit")

def beli_hp(hp, jumlah):
    if hp.stok >= jumlah:
        total_harga = hp.harga * jumlah
        hp.stok -= jumlah
        return f"Anda telah membeli {jumlah} unit {hp.merk}. Total harga: {total_harga} USD."
    else:
        return f"Maaf, stok {hp.merk} tidak mencukupi untuk pembelian ini."

def main():
    daftar_hp = [
        HP("Samsung", 500, 10),
        HP("oppo", 450, 15),
        HP("poco", 600, 8),
        HP("iphone",700, 50),
        HP("asus",350, 40),
        HP("xioami", 500 , 35)
    ]

    while True:
        print("\nMenu:")
        print("1. Tampilkan HP")
        print("2. Beli HP")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\nDaftar HP:")
            for hp in daftar_hp:
                hp.tampilkan_info()
        elif pilihan == "2":
            merk_hp = input("Masukkan merk hp yang ingin dibeli: ")
            hp_terpilih = next((hp for hp in daftar_hp if hp.merk.lower() == merk_hp.lower()), None)

            if hp_terpilih:
                jumlah_pembelian = int(input(f"Masukkan jumlah {hp_terpilih.merk} yang ingin dibeli: "))
                hasil_pembelian = beli_hp(hp_terpilih, jumlah_pembelian)
                print(hasil_pembelian)
            else:
                print("Merk HP tidak ditemukan.")
        elif pilihan == "3":
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()