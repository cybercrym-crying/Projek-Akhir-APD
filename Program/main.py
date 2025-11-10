from datetime import datetime, timedelta
import os, random
from register_akun import register

# from admin import tambah, hapus, kelola, lihat_data, update, diskon
from user import history, pembelian, status
import questionary as qs

history_pesanan = {}
akun = {"admin": ["admin123", "admin"]}
daftar_pesanan = {}
daftar_barang = {
    "Kecap 200ml": [10000, 12],
    "Sambal ABC 150ml": [15000, 4],
    "Coklat ABC": [5000, 10],
}  # "nama_produk:[harga,stock]"
waktu_pembelian = []
waktu_sampai = []
while True:
    # regist
    username = register(akun)
    hak_akun = akun[username][1]

    match hak_akun:

        # user program
        case "user":
            while True:
                pilihan = qs.select(
                    "Selamat Datang Di Toko Kami '-' ",
                    ["Pesan Barang", "Status Pesanan", "History Pesanan", "Keluar"],
                ).ask()
                match pilihan:
                    case "Pesan Barang":
                        pembelian(
                            daftar_pesanan,
                            daftar_barang,
                            waktu_pembelian,
                            waktu_sampai,
                            username,
                        )
                        continue

                    case "Status Pesanan":
                        status(
                            daftar_pesanan,
                            waktu_sampai,
                            waktu_pembelian,
                            history_pesanan,
                        )
                        continue

                    case "History Pesanan":
                        histort(history_pesanan)
                        continue

                    case "Keluar":
                        break
        # admin program
        case "admin":
            while True:
                pilihan = qs.select(
                    "Selamat Datang Admin '-'",
                    [
                        "Tambah Daftar Barang",
                        "Tampilkan Daftar Barang",
                        "Update Daftar Barang",
                        "Hapus Daftar Barang",
                        "Tampilkan Data Penjualan",
                        "Tambahkan Diskon Barang",
                        "Kelola Akun User",
                    ],
                ).ask()
        case "Keluar":
            break
