# Dashboard untuk Dosen Wali: Studi Kasus IMK & Visualisasi Data

Studi kasus berdasarkan kuliah umum **Human-Computer Interaction & Data Visualization** (Dr. Arafat Febriandirza, BRIN) dalam *Informatics Practitioner Lecture Series*, Informatika Universitas Bengkulu.

Proyek ini merancang dashboard kehadiran dan nilai mahasiswa dengan pendekatan *User-Centered Design*: mulai dari persona, membandingkan grafik sebelum dan sesudah perbaikan, membuat prototipe interaktif, lalu mengevaluasinya dengan lima prinsip desain interaksi dan standar aksesibilitas WCAG.

🔗 **[Lihat laporan HTML (live)](https://aurelclara.github.io/studi-kasus-imk-visualisasi-data/)**

## Kerangka Studi Kasus

| Tahap (siklus desain interaksi) | Penjelasan |
| --- | --- |
| **Analisis** | Dua *user persona* (dosen wali dan ketua prodi) beserta tujuan, kendala, dan skenario interaksinya. |
| **Desain** | Perbandingan grafik sebelum dan sesudah, menerapkan *preattentive attributes*, prinsip Gestalt, dan sumbu yang jujur. |
| **Prototipe** | Dashboard interaktif (HTML, CSS, JavaScript murni) dengan filter *real-time* dan tampilan per peran. |
| **Evaluasi** | Pemetaan ke lima prinsip (*visibility, feedback, constraints, consistency, affordance*), rasio kontras WCAG, dan rencana uji kegunaan. |

## Struktur Proyek

```
studi-kasus-imk-visualisasi-data/
├── data_sim.py              # Pembangkit data simulasi (180 mahasiswa)
├── warna.py                 # Palet pastel + penghitung rasio kontras WCAG
├── visual_perbandingan.py   # Grafik sebelum vs sesudah (matplotlib)
├── template.html            # Kerangka laporan + dashboard interaktif
├── generate_report.py       # Menyusun template + data + grafik menjadi index.html
├── index.html               # Laporan (buka di browser)
├── data_mahasiswa_simulasi.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Cara Menjalankan

```bash
git clone https://github.com/USERNAME/studi-kasus-imk-visualisasi-data.git
cd studi-kasus-imk-visualisasi-data

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python data_sim.py               # opsional: lihat ringkasan data di terminal
python generate_report.py        # membuat ulang index.html
```

## Laporan HTML

- **Membuka lokal:** double-click `index.html` (gambar dan data sudah tertanam, tidak perlu internet atau server).
- **Lewat link:** aktifkan GitHub Pages di **Settings → Pages**, pilih branch `main` dan folder `/ (root)`.
- **Mengubah tampilan:** ubah `template.html`, lalu jalankan ulang `generate_report.py`.

## Catatan

- Data adalah **simulasi** untuk pembelajaran, bukan data mahasiswa sungguhan.
- Persona disusun dari asumsi untuk keperluan tugas, bukan dari wawancara. Prototipe belum diuji pada pengguna sungguhan.

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran.
