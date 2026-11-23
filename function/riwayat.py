"""
Modul Riwayat Penanganan Tiket (Tahap 2 - Singly Linked List)
Fitur R1: Catat Riwayat Otomatis
Fitur R2: Tampilkan Seluruh Riwayat
"""

from datetime import datetime


class Node:
    """Node tunggal untuk Singly Linked List."""

    def __init__(self, data):
        self.data = data  # Menyimpan 1 dictionary catatan riwayat
        self.next = None  # Pointer ke node berikutnya


class LinkedListRiwayat:
    """Singly Linked List buatan sendiri tanpa tail (Minggu 9)."""

    def __init__(self):
        self.head = None
        self.nomor_terakhir = 0  # Counter otomatis untuk no_urut unik

    def buat_nomor_urut(self):
        """Menghasilkan no_urut naik otomatis mulai dari 1."""
        self.nomor_terakhir += 1
        return self.nomor_terakhir

    def insert_akhir(self, data):
        """Menambahkan node baru di ujung paling belakang (O(n) tanpa tail)."""
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
            return

        # Telusuri dari head sampai node terakhir
        sekarang = self.head
        while sekarang.next is not None:
            sekarang = sekarang.next
        sekarang.next = node_baru

    def tampilkan_semua(self):
        """Traversal dari head sampai ujung untuk menampilkan tabel & ringkasan."""
        print("\n--- RIWAYAT PENANGANAN TIKET ---")

        if self.head is None:
            print("Belum ada riwayat.")
            return

        # Lebar kolom tabel agar rapi
        w_no, w_waktu, w_aksi, w_kode, w_nama, w_lama, w_baru = 4, 19, 12, 9, 18, 20, 20
        garis = "-" * (w_no + w_waktu + w_aksi + w_kode + w_nama + w_lama + w_baru + (6 * 3))

        print(garis)
        print(
            f"{'No':<{w_no}} | {'Waktu':<{w_waktu}} | {'Aksi':<{w_aksi}} | "
            f"{'Kode':<{w_kode}} | {'Nama Pelapor':<{w_nama}} | "
            f"{'Nilai Lama':<{w_lama}} | {'Nilai Baru':<{w_baru}}"
        )
        print(garis)

        # Variabel integer biasa untuk menghitung ringkasan saat traversal
        jml_tambah = 0
        jml_ubah = 0
        jml_hapus = 0
        total = 0

        sekarang = self.head
        while sekarang is not None:
            d = sekarang.data
            aksi = d["aksi"]

            # Hitung jumlah per aksi selama traversal
            if aksi == "TAMBAH":
                jml_tambah += 1
            elif aksi == "UBAH_STATUS":
                jml_ubah += 1
            elif aksi == "HAPUS":
                jml_hapus += 1
            total += 1

            # Potong teks jika melebihi lebar kolom agar tabel tidak berantakan
            nama_fmt = (d["nama_pelapor"][:15] + "...") if len(d["nama_pelapor"]) > w_nama else d["nama_pelapor"]
            lama_fmt = (d["nilai_lama"][:17] + "...") if len(d["nilai_lama"]) > w_lama else d["nilai_lama"]
            baru_fmt = (d["nilai_baru"][:17] + "...") if len(d["nilai_baru"]) > w_baru else d["nilai_baru"]

            print(
                f"{d['no_urut']:<{w_no}} | {d['waktu']:<{w_waktu}} | {aksi:<{w_aksi}} | "
                f"{d['kode_tiket']:<{w_kode}} | {nama_fmt:<{w_nama}} | "
                f"{lama_fmt:<{w_lama}} | {baru_fmt:<{w_baru}}"
            )
            sekarang = sekarang.next

        print(garis)
        print(f"Ringkasan: TAMBAH {jml_tambah} | UBAH_STATUS {jml_ubah} | HAPUS {jml_hapus} | Total {total}")


# Instance tunggal di memori selama program berjalan
daftar_riwayat = LinkedListRiwayat()


def catat_riwayat(aksi, kode, nama, nilai_lama, nilai_baru):
    """
    Fitur R1: Satu pintu pencatatan riwayat otomatis.
    Dipanggil dari F1, F4, dan F6 hanya setelah aksi berhasil.
    """
    catatan = {
        "no_urut": daftar_riwayat.buat_nomor_urut(),
        "aksi": aksi,
        "kode_tiket": kode,
        "nama_pelapor": nama,
        "nilai_lama": nilai_lama,
        "nilai_baru": nilai_baru,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    daftar_riwayat.insert_akhir(catatan)
    print("Riwayat tercatat.")


def tampilkan_riwayat():
    """Fitur R2: Menampilkan seluruh catatan riwayat dari terlama ke terbaru."""
    daftar_riwayat.tampilkan_semua()