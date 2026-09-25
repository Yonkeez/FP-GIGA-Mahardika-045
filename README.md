#FP LBE GIGA 2026

Nama: Mahardika Indra Pratama Ilyasa
NRP: 5054251045

# 🏆 Tuyul Finding Treasure

**Tuyul Finding Treasure** adalah game **2D Top-Down Maze / Dungeon Crawler** dengan elemen puzzle dan minigame yang dibuat menggunakan **Python dan Pygame 2.6.1**.

Pemain berperan sebagai Tuyul yang harus menjelajahi kuil kuno, melewati labirin dan jebakan panah, serta menyelesaikan berbagai minigame untuk mendapatkan **3 kunci** dan membuka peti harta karun.

> **Genre:** Adventure Puzzle
> **Platform:** PC / Desktop
> **Engine:** Pygame 2.6.1
> **Language:** Python 3
> **Resolution:** 800 × 600
> **Mode:** Single-player

## 🎮 Gameplay

Tujuan utama permainan adalah mengumpulkan **3 kunci** melalui tiga ruangan:

1. **Room 1** — Jelajahi labirin dan selesaikan **Quick Click**.
2. **Room 2** — Lewati jebakan dan selesaikan **Memory Sequence**.
3. **Room 3** — Hadapi lebih banyak jebakan dan selesaikan **Dodge**.
4. **Treasure Room** — Gunakan 3 kunci untuk membuka peti dan menyelesaikan permainan.

Setiap minigame memberikan satu kunci setelah berhasil diselesaikan. Jika terkena jebakan, pemain akan kembali ke titik awal ruangan, tetapi kunci yang telah diperoleh tetap tersimpan.

## 🕹️ Kontrol

| Aksi                        | Kontrol                    |
| --------------------------- | -------------------------- |
| Bergerak                    | `WASD` / `Arrow Keys`      |
| Interaksi dengan pintu/peti | `E`                        |
| Klik minigame               | `Left Mouse Button`        |
| Gerak pada Minigame 3       | `A/D` / `Left/Right Arrow` |
| Menu                        | `Left Mouse Button`        |

## 🧩 Minigame

### Quick Click

Klik target hijau yang berpindah secara acak.
**Target:** 10 klik dalam 10 detik.

### Memory Sequence

Pemain harus mengingat urutan kotak yang menyala dan mengkliknya kembali dengan urutan yang benar.

### Dodge

Gerakkan karakter ke kiri dan kanan untuk menghindari panah yang jatuh.
**Target:** Bertahan selama 15 detik.

## ⚙️ Instalasi & Menjalankan Game

Pastikan **Python 3** telah terpasang.

Clone atau download repository, kemudian install dependency:

```bash
pip install -r requirements.txt
```

Jalankan game dengan:

```bash
python main.py
```

Dependency yang digunakan:

```text
pygame==2.6.1
```

## 📁 Struktur Project

```text
Tuyul-Finding-Treasure/
├── assets/
│   ├── player.png
│   ├── chest.png
│   ├── door.png
│   ├── arrow.png
│   └── trap_block.png
├── config.py
├── game.py
├── main.py
├── minigames.py
├── player.py
├── traps.py
├── ui.py
├── requirements.txt
└── README.md
```

### Pembagian Modul

* `main.py` — Entry point dan game loop.
* `config.py` — Konfigurasi game dan layout labirin.
* `game.py` — State machine dan logika utama permainan.
* `player.py` — Pergerakan, input, animasi, dan collision pemain.
* `minigames.py` — Implementasi ketiga minigame.
* `traps.py` — Sistem jebakan dan proyektil panah.
* `ui.py` — Menu, tombol, dan UI permainan.

