from datetime import datetime, timedelta
import os, random
from register_akun import register
from admin import tambah, hapus, kelola, lihat_data, update, diskon
from user import history, pembelian, status
import questionary as qs

history = {}
akun = {"admin": ["admin123", "admin"]}
daftar_pesanan = {}
daftar_barang = {"Kecap 200ml": [10000, 12]}  # "nama_produk:[harga,stock]"
while True:
    hak = register(akun)
    match hak:
        case "user":
            while True:
                pilihan = qs.select(
                    "Selamat Datang Di Toko Kami '-' ",
                    ["Pesan Barang", "Status Pesanan", "History Pesanan", "Keluar"],
                ).ask()
                match pilihan:
                    case "Pesan Barang":
                        pembelian(daftar_pesanan, daftar_barang)
                        continue
                    case "Status Pesanan":
                        status(pesanan, estimasi_sampai)
                        continue
                    case "History Pesanan":
                        continue
                    case "Keluar":
                        break

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
