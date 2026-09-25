import pygame
import sys
import time
from config import *
from player import Player
from minigames import Minigame1, Minigame2, Minigame3
from ui import UIOverlay
from traps import ArrowTrap  

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 64)
        
        self.ui = UIOverlay(self.font, self.big_font)
        
        self.state = "MAIN_MENU"
        self.total_chests = 0
        self.keys = 0
        self.current_minigame = None
        self.message = ""
        self.message_timer = 0
        
        self.start_pos = (0, 0)
        self.traps = []

    def start_new_game(self):
        self.state = "ROOM_1"
        self.keys = 0
        self.current_minigame = None
        self.set_message("Hati-hati terhadap jebakan panah!", 3)
        self.load_room(ROOM_1_MAZE)

    def load_room(self, layout):
        self.walls = []
        self.traps = []
        self.board = None
        self.door = None
        self.treasure = None

        for y, row in enumerate(layout):
            for x, char in enumerate(row):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if char == 'W':
                    self.walls.append(rect)
                elif char == 'S':
                    self.start_pos = (x * TILE_SIZE + 5, y * TILE_SIZE + 5)
                    self.player = Player(*self.start_pos)
                elif char == 'B':
                    self.board = rect
                elif char == 'D':
                    self.door = rect
                elif char == 'T':
                    self.treasure = rect
                elif char == 'A':  # Trap tembak Kanan
                    self.traps.append(ArrowTrap(x * TILE_SIZE, y * TILE_SIZE, direction="RIGHT", cooldown_seconds=1.8))
                    self.walls.append(rect)
                elif char == 'V':  # Trap tembak Bawah
                    self.traps.append(ArrowTrap(x * TILE_SIZE, y * TILE_SIZE, direction="DOWN", cooldown_seconds=1.8))
                    self.walls.append(rect)

    def set_message(self, text, duration=3):
        self.message = text
        self.message_timer = time.time() + duration

    def respawn_player(self):
        """Mereset posisi player ke tempat awal saat terkena jebakan"""
        self.player.rect.x, self.player.rect.y = self.start_pos
        self.set_message("Kena Jebakan Panah! Kembali ke awal.", 2.5)

    # --- MINIGAME CALLBACKS ---
    def start_minigame(self):
        if self.state == "ROOM_1":
            self.state = "MINIGAME_1"
            self.current_minigame = Minigame1(self.win_minigame, self.lose_minigame_1)
        elif self.state == "ROOM_2":
            self.state = "MINIGAME_2"
            self.current_minigame = Minigame2(self.win_minigame, self.lose_minigame_2)
        elif self.state == "ROOM_3":
            self.state = "MINIGAME_3"
            self.current_minigame = Minigame3(self.win_minigame, self.lose_minigame_3)

    def win_minigame(self):
        self.keys += 1
        self.set_message(f"Kunci Diperoleh! ({self.keys}/3)")
        self.current_minigame = None
        
        if self.state == "MINIGAME_1":
            self.state = "ROOM_2"
            self.load_room(ROOM_2_MAZE)
        elif self.state == "MINIGAME_2":
            self.state = "ROOM_3"
            self.load_room(ROOM_3_MAZE)
        elif self.state == "MINIGAME_3":
            self.state = "TREASURE_ROOM"
            self.load_room(TREASURE_ROOM)

    def lose_minigame_1(self):
        self.set_message("Waktu Habis! Coba lagi.")
        self.state, self.current_minigame = "ROOM_1", None
        
    def lose_minigame_2(self):
        self.set_message("Urutan Salah! Coba lagi.")
        self.state, self.current_minigame = "ROOM_2", None
        
    def lose_minigame_3(self):
        self.set_message("Tertabrak! Coba lagi.")
        self.state, self.current_minigame = "ROOM_3", None

    # --- CORE LOOP ---
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.state == "MAIN_MENU":
                if self.ui.btn_start.handle_event(event):
                    self.start_new_game()
                elif self.ui.btn_exit.handle_event(event):
                    pygame.quit()
                    sys.exit()

            elif self.state == "WIN":
                if self.ui.btn_main_menu.handle_event(event):
                    self.state = "MAIN_MENU"

            elif self.current_minigame:
                self.current_minigame.handle_event(event)

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    if self.door and self.player.rect.colliderect(self.door.inflate(10, 10)):
                        self.start_minigame()
                    if self.treasure and self.player.rect.colliderect(self.treasure.inflate(20, 20)):
                        if self.keys >= 3:
                            self.total_chests += 1
                            self.state = "WIN"
                        else:
                            self.set_message("Kamu butuh 3 kunci untuk membuka ini!")

    def update(self):
        if self.state in ["MAIN_MENU", "WIN"]:
            return

        keys = pygame.key.get_pressed()
        
        if self.current_minigame:
            self.current_minigame.update(keys)
        elif self.state in ["ROOM_1", "ROOM_2", "ROOM_3", "TREASURE_ROOM"]:
            self.player.update(keys, self.walls)
            
            # Update jebakan panah dan cek tabrakan
            for trap in self.traps:
                trap.update(self.walls)
                if trap.check_player_collision(self.player.rect):
                    self.respawn_player()

            if self.door and self.player.rect.colliderect(self.door.inflate(20, 20)):
                self.set_message("Tekan E untuk masuk Mini-game", 0.5)

    def draw(self):
        self.screen.fill(BLACK)

        if self.state == "MAIN_MENU":
            self.ui.draw_main_menu(self.screen, self.total_chests)

        elif self.state == "WIN":
            self.ui.draw_win_menu(self.screen, self.total_chests)

        elif self.current_minigame:
            self.current_minigame.draw(self.screen, self.font)

        else:
            for wall in self.walls: 
                pygame.draw.rect(self.screen, GRAY, wall)
                
            # Gambar Jebakan Panah
            for trap in self.traps:
                trap.draw(self.screen)

            if self.board:
                pygame.draw.rect(self.screen, YELLOW, self.board)
                self.screen.blit(self.font.render("MG", True, BLACK), (self.board.x + 2, self.board.y + 10))
            if self.door: 
                pygame.draw.rect(self.screen, GREEN, self.door)
            if self.treasure:
                pygame.draw.rect(self.screen, YELLOW, self.treasure)
                self.screen.blit(self.font.render("PETI", True, BLACK), (self.treasure.x-10, self.treasure.y+5))
            
            self.player.draw(self.screen)

            # Draw HUD & Messages
            self.screen.blit(self.font.render(f"Keys: {self.keys}/3 | Room: {self.state}", True, WHITE), (10, HEIGHT - 40))
            if time.time() < self.message_timer:
                msg = self.font.render(self.message, True, ORANGE)
                self.screen.blit(msg, (WIDTH//2 - msg.get_width()//2, 20))
            
        pygame.display.flip()