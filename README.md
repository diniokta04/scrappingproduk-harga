# Project Scraping Harga & Produk 
Tugas ini adalah bagian dari mata kuliah **Pemrograman Berbasis Web (PBW)** Semester 4. Program ini berfungsi untuk mengambil data produk dan harga secara otomatis dan mengelola datanya.
## Fitur Utama
* **Web Scraping:** Mengambil data produk secara otomatis.
* **CRUD System:** Bisa Menambah, Melihat, Mengubah, dan Menghapus data hasil scraping.
* **Export Data:** Data disimpan dalam format `JSON` dan `CSV`.
## Teknologi yang Digunakan
* **Python 3.x**
* **Library:** `BeautifulSoup` (Scraping), `Requests`, `JSON`, `CSV`
## Struktur File
* `scraping.py` - Script utama untuk mengambil data dari web.
* `crud.py` - Script untuk manajemen data (Create, Read, Update, Delete).
* `data.json` - Database lokal tempat menyimpan hasil data.
## Cara Menjalankan
1. Clone repositori ini:
   ```bash
   git clone [https://github.com/diniokta04/scrappingproduk-harga.git](https://github.com/diniokta04/scrappingproduk-harga.git)
2. alankan program scraping:
   Bash
   python scraping.py
3. Kelola data dengan:
   Bash
   python crud.py
