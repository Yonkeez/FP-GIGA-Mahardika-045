import pygame
from config import *

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self, surface, font):
        # Efek warna saat kursor berada di atas tombol (hover)
        bg_color = BROWN_LIGHT if self.is_hovered else BROWN_DARK
        border_color = GOLD_LIGHT if self.is_hovered else GOLD_DARK

        # 1. Gambar Background Tombol (Cokelat)
        pygame.draw.rect(surface, bg_color, self.rect, border_radius=8)

        # 2. Gambar Border Ganda khas Temple (Emas)
        pygame.draw.rect(surface, border_color, self.rect, width=4, border_radius=8)
        inner_rect = self.rect.inflate(-8, -8)
        pygame.draw.rect(surface, border_color, inner_rect, width=2, border_radius=6)

        # 3. Teks Tombol
        text_surf = font.render(self.text, True, CREAM)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)


class UIOverlay:
    def __init__(self, font, big_font):
        self.font = font
        self.big_font = big_font

        # Inisialisasi Tombol Start Menu
        self.btn_start = Button(WIDTH // 2 - 120, HEIGHT // 2 - 10, 240, 50, "START GAME")
        self.btn_exit = Button(WIDTH // 2 - 120, HEIGHT // 2 + 60, 240, 50, "EXIT GAME")

        # Inisialisasi Tombol Win Menu
        self.btn_main_menu = Button(WIDTH // 2 - 140, HEIGHT // 2 + 80, 280, 50, "MAIN MENU")

    def _draw_temple_panel(self, surface, rect):
        """Fungsi pembantu untuk menggambar bingkai panel bergaya temple"""
        pygame.draw.rect(surface, BROWN_DARK, rect, border_radius=12)
        pygame.draw.rect(surface, GOLD_LIGHT, rect, width=5, border_radius=12)
        inner_rect = rect.inflate(-12, -12)
        pygame.draw.rect(surface, GOLD_DARK, inner_rect, width=2, border_radius=8)

    def draw_main_menu(self, surface, total_chests):
        surface.fill(BLACK)

        # Panel Utiliti / Bingkai Menu
        panel_rect = pygame.Rect(WIDTH // 2 - 220, HEIGHT // 2 - 190, 440, 370)
        self._draw_temple_panel(surface, panel_rect)

        # Judul Utama Game
        title = self.big_font.render("THE THREE KEYS", True, GOLD_LIGHT)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140))
        surface.blit(title, title_rect)

        # Tampilan Total Peti Terkumpul
        chest_text = self.font.render(f"Peti Terkumpul: {total_chests}", True, CREAM)
        chest_rect = chest_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
        surface.blit(chest_text, chest_rect)

        # Tombol-tombol Menu
        self.btn_start.draw(surface, self.font)
        self.btn_exit.draw(surface, self.font)

    def draw_win_menu(self, surface, total_chests):
        surface.fill(BLACK)

        # Panel Menu Kemenangan
        panel_rect = pygame.Rect(WIDTH // 2 - 240, HEIGHT // 2 - 180, 480, 340)
        self._draw_temple_panel(surface, panel_rect)

        # Teks Kemenangan
        win_title = self.big_font.render("VICTORY!", True, GOLD_LIGHT)
        win_rect = win_title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        surface.blit(win_title, win_rect)

        sub_text = self.font.render("KAMU MENDAPATKAN PETI!", True, CREAM)
        sub_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        surface.blit(sub_text, sub_rect)

        info_text = self.font.render(f"Total Peti Saat Ini: {total_chests}", True, GOLD_LIGHT)
        info_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 10))
        surface.blit(info_text, info_rect)

        # Tombol Kembali ke Main Menu
        self.btn_main_menu.draw(surface, self.font)