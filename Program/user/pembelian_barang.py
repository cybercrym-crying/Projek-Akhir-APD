import prettytable as PrettyTable
import questionary as qs


def pembelian(daftar_pesanan, daftar_barang):
    waktu_pembelian = None
    estimasi_sampai = datetime.now() + timedelta(minutes=random.choice([1, 2, 3]))
