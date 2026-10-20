"""
Membuat laporan HTML (index.html) dari template.html.
Gambar pembanding disisipkan sebagai base64 dan data simulasi disisipkan
sebagai JSON, sehingga index.html bisa dibuka langsung tanpa server.
"""
import base64
import io
import json
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from data_sim import buat_data
from visual_perbandingan import rata_per_kelompok, gambar_sebelum, gambar_sesudah
from warna import PALET as P, css_variabel, rasio_kontras

BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
         "Agustus", "September", "Oktober", "November", "Desember"]


def ke_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=140, facecolor=fig.get_facecolor())
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode()


def tabel_kontras():
    pasangan = [
        ("Teks utama di atas krim", "tinta", "krim"),
        ("Teks utama di atas kertas", "tinta", "kertas"),
        ("Teks abu-abu lembut di atas kertas", "tinta-lembut", "kertas"),
        ("Teks di atas persik (catatan Bu Dewi)", "tinta", "persik"),
        ("Teks di atas lavender (catatan Pak Hendra)", "tinta", "lavender"),
        ("Teks di atas sage (ringkasan)", "tinta", "sage"),
        ("Teks di atas mentega (tab terpilih)", "tinta", "mentega"),
        ("Teks mawar tua di atas kertas", "mawar-tua", "kertas"),
    ]
    baris = []
    for nama, depan, belakang in pasangan:
        r = rasio_kontras(P[depan], P[belakang])
        kelas, status = ("lulus", "Lulus") if r >= 4.5 else ("gagal", "Belum")
        baris.append(f"<tr><td>{nama}</td><td>{r:.1f}:1".replace(".", ",") +
                     f"</td><td><span class='{kelas}'>{status}</span></td></tr>")
    return "\n        ".join(baris)


def main():
    df = buat_data()
    g = rata_per_kelompok(df)

    html = open("template.html", encoding="utf-8").read()
    hari = date.today()
    pengganti = {
        "/*CSS_WARNA*/": css_variabel(),
        "__DATA_JSON__": json.dumps(df[["id", "angkatan", "kelas", "hadir", "tugas", "uts", "uas", "akhir"]]
                                    .to_dict("records"), ensure_ascii=False, separators=(",", ":")),
        "__IMG_SEBELUM__": ke_base64(gambar_sebelum(g)),
        "__IMG_SESUDAH__": ke_base64(gambar_sesudah(g)),
        "__TABEL_KONTRAS__": tabel_kontras(),
        "__TANGGAL__": f"{hari.day} {BULAN[hari.month - 1]} {hari.year}",
        "__N_MHS__": str(len(df)),
    }
    for kunci, nilai in pengganti.items():
        html = html.replace(kunci, nilai)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    df.to_csv("data_mahasiswa_simulasi.csv", index=False)
    print(f"index.html dibuat ({len(html) // 1024} KB)")


if __name__ == "__main__":
    main()
