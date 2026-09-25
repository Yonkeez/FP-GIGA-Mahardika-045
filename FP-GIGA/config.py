import pygame

# --- KONFIGURASI AWAL ---
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# --- WARNA ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 150, 255)      # Player
GREEN = (50, 200, 50)      # Pintu / Sukses
RED = (255, 50, 50)        # Bahaya / Gagal
YELLOW = (255, 200, 0)     # Papan / Kunci / Peti Harta
ORANGE = (255, 150, 0)
# --- WARNA TEMA TEMPLE ---
GOLD_DARK = (180, 130, 20)
GOLD_LIGHT = (240, 190, 40)
BROWN_DARK = (45, 25, 15)
BROWN_LIGHT = (90, 55, 30)
CREAM = (245, 230, 200)

# ROOM 1 (EASY): Jalur relatif longgar, cabang sedikit, B dan D mudah ditemukan

ROOM_1_MAZE = [

    # "WWWWWWWWWWWWWWWWWWWW",
    # "WS     W           W",
    # "W WWWW W WWWWWWWWW W",
    # "W W    W         W W",
    # "W W WWWWWWWWWWWW W W",
    # "W W            W W W",
    # "W WWWWWWWWWWWW W W W",
    # "W          W   W W W",
    # "WWWWWWWWWW W WWW W W",
    # "W        W W     W W",
    # "W WWWWWW W WWWWWWW W",
    # "W      W W         W",
    # "WWWWWW W WWWWWWWW  W",
    # "W              BD  W",
    # "WWWWWWWWWWWWWWWWWWWW",

    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W         S BD     W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W", 
    "W                  W", 
    "WWWWWWWWWWWWWWWWWWWW",
]

# ROOM 2 (MEDIUM): Jalur ketat 1-tile, rute memutar, B harus diambil sebelum ke D
ROOM_2_MAZE = [
    # "WWWWWWWWWWWWWWWWWWWW",
    # "WS  W       W      W",
    # "WWW W WWWWW W WWWW W",
    # "W   W     W W W    W",
    # "W WWWWWWW W W W WWWW",
    # "W W     W W   W    W",
    # "W W WWW W WWWWWWWW W",
    # "W W W   W W        W",
    # "W W W WWW W WWWWWW W",
    # "W   W     W W      W",
    # "WWWWWWWWWWW W WWWW W",
    # "W         W W W    W",
    # "W WWWWWWW W W W WWWW",
    # "W       W   W   DB W",
    # "WWWWWWWWWWWWWWWWWWWW",

    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W         S BD     W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W", 
    "W                  W", 
    "WWWWWWWWWWWWWWWWWWWW",
]

# ROOM 3 (HARD): Labirin padat bercabang banyak, B di pojok kanan atas, D di kanan bawah
ROOM_3_MAZE = [
    # "WWWWWWWWWWWWWWWWWWWW",
    # "WSW     W     W    W",
    # "W W WWW W WWW W WWWW",
    # "W   W   W   W W    W",
    # "WWW W WWWWW W WWWW W",
    # "W   W W     W    W W",
    # "W WWW W WWWWWWWW W W",
    # "W   W   W   W    W W",
    # "WWW WWW W W W WWWW W",
    # "W     W W W W W    W",
    # "W WWW W W W W W WWWW",
    # "W   W W W W   W    W",
    # "WWW W W W WWWWWW W W",
    # "W       W        DBW",
    # "WWWWWWWWWWWWWWWWWWWW",

    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W         S BD     W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W", 
    "W                  W", 
    "WWWWWWWWWWWWWWWWWWWW",
]

TREASURE_ROOM = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W         T        W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W", 
    "W                  W", 
    "WWWWWWWWWWWWWWWWWWWW",
]