"""
Palet warna pastel + hitung rasio kontras WCAG.
Satu sumber warna dipakai oleh grafik matplotlib dan CSS laporan HTML,
supaya tampilannya konsisten (prinsip consistency).
"""

PALET = {
    "krim": "#fbf6ee",
    "kertas": "#fffdf8",
    "tinta": "#3a3744",
    "tinta-lembut": "#625e6e",
    "garis": "#ddd3c4",
    "persik": "#f6d5c6",
    "sage": "#d0e3d1",
    "sage-tua": "#4f7a57",
    "lavender": "#ddd6f0",
    "lavender-tua": "#6b5fa3",
    "langit": "#d0e2ef",
    "mentega": "#f7eebf",
    "mawar": "#eba7b3",
    "mawar-tua": "#9c4358",
}


def _kanal(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminans(hex_warna):
    h = hex_warna.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _kanal(r) + 0.7152 * _kanal(g) + 0.0722 * _kanal(b)


def rasio_kontras(depan, belakang):
    """Rasio kontras WCAG 2.x antara dua warna hex (1 sampai 21)."""
    a, b = luminans(depan), luminans(belakang)
    terang, gelap = max(a, b), min(a, b)
    return (terang + 0.05) / (gelap + 0.05)


def css_variabel():
    isi = "".join(f"--{nama}:{kode};" for nama, kode in PALET.items())
    return ":root{" + isi + "}"
