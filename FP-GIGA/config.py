import pygame
# --- UKURAN LAYAR & GRID ---
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 40
FPS = 60

# --- WARNA DASAR ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GOLD_DARK = (180, 130, 20)
GOLD_LIGHT = (240, 190, 40)
BROWN_DARK = (45, 25, 15)
BROWN_LIGHT = (90, 55, 30)
CREAM = (245, 230, 200)

# --- LAYOUT LABIRIN ---
# Keterangan Simbol:
# W = Wall (Dinding)
# S = Start (Posisi awal Player)
# B = Board Minigame
# D = Door (Pintu masuk minigame)
# T = Treasure (Peti Harta Karun)
# A = Arrow Trap (Tembak ke Kanan)
# V = Arrow Trap (Tembak ke Bawah)

ROOM_1_MAZE = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WS W               W",
    "W  W WWWWWWWWWWWWW W",
    "W  W W           W W",
    "W  W W WWWWWWWWW W W",
    "W  A W         W W W", 
    "W    W WWWWWWW W W W",
    "WWWW W       W W W W",
    "W    WWWWWWW W W W W",
    "W            W W W W",
    "W WWWWWWWWWWWW W W W",
    "W              W   W",
    "WWWWWWWWWWWWWWWW D W",  
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW"
]

ROOM_2_MAZE = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WS       V         W",  
    "WWWWWWWW   WWWWWWW W",
    "W        W         W",
    "W WWWWWWWWWWWWWWWW W",
    "W A              W W",  
    "W WWWWWWWWWWWWWW W W",
    "W V              W W",  
    "W   WWWWWWWWWWWW W W",
    "WWW W            W W",
    "W   W WWWWWWWWWWWW W",
    "W   W              W",
    "W WWWWWWWWWWWWWW  DW",  
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW"
]

ROOM_3_MAZE = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WS   V     V     V W",  
    "WWWW   WWW   WWW   W",
    "W    W     W     W W",
    "W WWWWWWWWWWWWWWWW W",
    "W A                W",  
    "W WWWWWWWWWWWWWWWW W",
    "W                V W",  
    "WWWWWWWWWWWWWWWW   W",
    "W A                W",  
    "W WWWWWWWWWWWWWWWW W",
    "W                 DW",  
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWW"
]

TREASURE_ROOM = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WS                 W",
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
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW"
]