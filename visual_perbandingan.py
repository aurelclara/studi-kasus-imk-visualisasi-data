"""
Dua versi grafik yang sama datanya: SEBELUM (sengaja dibuat buruk) dan
SESUDAH (menerapkan prinsip IMK dan visualisasi data dari materi kuliah).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from warna import PALET as P


def rata_per_kelompok(df):
    g = df.groupby(["angkatan", "kelas"])["akhir"].mean().round(1)
    g.index = [f"{a}-{k}" for a, k in g.index]
    return g


def gambar_sebelum(g):
    """Sumbu terpotong, warna pelangi, urutan acak, legenda terpisah, grid padat."""
    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    warna = plt.cm.jet(np.linspace(0.05, 0.95, len(g)))
    batang = ax.bar(range(len(g)), g.values, color=warna)
    ax.set_ylim(g.min() - 3, g.max() + 1)  # sumbu y dipotong
    ax.set_xticks(range(len(g)))
    ax.set_xticklabels(g.index, rotation=45, fontsize=8)
    ax.grid(True, color="black", alpha=0.4)
    ax.set_title("Rata-rata nilai")
    ax.legend(batang, g.index, fontsize=6, loc="upper left", ncol=3)
    fig.tight_layout()
    return fig


def gambar_sesudah(g):
    """Sumbu dari nol, satu warna + sorotan, terurut, label langsung."""
    urut = g.sort_values()
    rata_semua = float(g.mean())
    fig, ax = plt.subplots(figsize=(6.4, 4.3))
    fig.patch.set_facecolor(P["kertas"])
    ax.set_facecolor(P["kertas"])
    warna = [P["mawar"] if i < 2 else P["sage"] for i in range(len(urut))]
    tepi = [P["mawar-tua"] if i < 2 else P["sage-tua"] for i in range(len(urut))]
    ax.barh(urut.index, urut.values, color=warna, edgecolor=tepi, linewidth=1.2, height=0.7)
    for i, nilai in enumerate(urut.values):
        ax.text(nilai + 1, i, f"{nilai:.1f}".replace(".", ","), va="center",
                fontsize=9, color=P["tinta"])
    ax.axvline(rata_semua, color=P["tinta-lembut"], linestyle="--", linewidth=1)
    ax.text(rata_semua, len(urut) - 0.35, f"rata-rata {rata_semua:.1f}".replace(".", ","),
            ha="center", fontsize=8, color=P["tinta-lembut"])
    ax.set_xlim(0, 100)
    ax.set_xlabel("Rata-rata nilai akhir (skala 0 sampai 100)", color=P["tinta"], fontsize=9)
    for sisi in ("top", "right", "left"):
        ax.spines[sisi].set_visible(False)
    ax.spines["bottom"].set_color(P["garis"])
    ax.tick_params(colors=P["tinta"], labelsize=9, length=0)
    ax.set_title("Dua kelompok dengan rata-rata terendah disorot", loc="left",
                 fontsize=10, color=P["tinta"])
    fig.tight_layout()
    return fig
