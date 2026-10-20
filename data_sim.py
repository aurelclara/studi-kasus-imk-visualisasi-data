"""
Data simulasi kehadiran dan nilai mahasiswa (3 angkatan x 3 kelas x 20 orang).
Bukan data sungguhan; dibangkitkan dengan seed tetap supaya bisa direproduksi.
"""
import numpy as np
import pandas as pd

BATAS_HADIR = 75   # persen kehadiran minimum
BATAS_NILAI = 60   # nilai akhir minimum


def buat_data(seed=2026, per_kelas=20):
    acak = np.random.default_rng(seed)
    baris, nomor = [], 1
    for angkatan in (2023, 2024, 2025):
        for kelas in ("A", "B", "C"):
            geser = acak.normal(0, 3)  # perbedaan kecil antar kelas
            for _ in range(per_kelas):
                hadir = float(np.clip(acak.normal(84, 11), 35, 100))
                kemampuan = acak.normal(0, 8)

                def skor(dasar):
                    nilai = dasar + kemampuan + 0.35 * (hadir - 84) + geser + acak.normal(0, 7)
                    return float(np.clip(nilai, 0, 100))

                tugas, uts, uas = skor(78), skor(68), skor(66)
                baris.append({
                    "id": f"M{nomor:03d}", "angkatan": angkatan, "kelas": kelas,
                    "hadir": round(hadir, 1), "tugas": round(tugas, 1),
                    "uts": round(uts, 1), "uas": round(uas, 1),
                    "akhir": round(0.3 * tugas + 0.3 * uts + 0.4 * uas, 1),
                })
                nomor += 1
    df = pd.DataFrame(baris)
    df["perlu_perhatian"] = (df["hadir"] < BATAS_HADIR) | (df["akhir"] < BATAS_NILAI)
    return df


if __name__ == "__main__":
    df = buat_data()
    df.to_csv("data_mahasiswa_simulasi.csv", index=False)
    print(df.describe().round(1))
    print("Perlu perhatian:", int(df["perlu_perhatian"].sum()), "dari", len(df))
