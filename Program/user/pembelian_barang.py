import prettytable as PrettyTable
import questionary as qs


# Fungsi pemesanan barang yang akan mencatat daftar pembelian, waktu pembelian, dan waktu sampai sehingga user bisa memperkirakan barang sampai
def pembelian(daftar_pesanan, daftar_barang, waktu_pembelian, waktu_sampai, username):
    estimasi_sampai = datetime.now() + timedelta(minutes=random.choice([1, 2, 3]))
    pass
