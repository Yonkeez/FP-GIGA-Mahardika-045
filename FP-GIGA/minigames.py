import pygame
import random
import time
from config import *

class Minigame1:
    def __init__(self, on_win, on_lose):
        self.score = 0
        self.timer = time.time() + 10 #EDIT TIMER WAKTU
        self.target = pygame.Rect(WIDTH//2 - 25, HEIGHT//2 - 25, 50, 50)
        self.on_win = on_win
        self.on_lose = on_lose

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.target and self.target.collidepoint(event.pos):
                self.score += 1
                self.target = pygame.Rect(random.randint(50, WIDTH-100), random.randint(100, HEIGHT-100), 50, 50)
                if self.score >= 10: #EDIT SCORE TARGET
                    self.on_win()

    def update(self, keys):
        if time.time() > self.timer:
            self.on_lose()

    def draw(self, screen, font):
        title = font.render("Quick Click! Klik kotak hijau 10 kali.", True, WHITE)
        screen.blit(title, (20, 20))
        time_left = max(0, int(self.timer - time.time()))
        timer_text = font.render(f"Waktu: {time_left}s | Score: {self.score}/10", True, WHITE)
        screen.blit(timer_text, (20, 60))
        if self.target:
            pygame.draw.rect(screen, GREEN, self.target)



class Minigame2:
    def __init__(self, on_win, on_lose):
        self.state = "SHOWING"  
        self.boxes = [pygame.Rect(150 + (i % 3) * 200, 200 + (i // 3) * 150, 100, 100) for i in range(6)]
        
        self.sequence = random.sample(range(6), 4)  
        
        self.player_seq = []
        self.timer = time.time()
        self.showing_index = 0
        self.on_win = on_win
        self.on_lose = on_lose

        self.clicked_box_index = None
        self.delay_timer = 0

    def handle_event(self, event):
        if self.state == "PLAYING" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, box in enumerate(self.boxes):
                if box.collidepoint(event.pos):
                    self.clicked_box_index = i
                    self.player_seq.append(i)
                    
                    if self.sequence[len(self.player_seq) - 1] != i:
                        self.state = "WAIT_LOSE"
                        self.delay_timer = time.time() + 0.3  
                    elif len(self.player_seq) == len(self.sequence):
                        self.state = "WAIT_WIN"
                        self.delay_timer = time.time() + 0.3  
                    else:
                        self.delay_timer = time.time() + 0.15

    def update(self, keys):
        if self.state == "SHOWING":
            if time.time() - self.timer > 0.8: 
                self.showing_index += 1
                self.timer = time.time()
                if self.showing_index >= len(self.sequence):
                    self.state = "PLAYING"

        elif self.state == "PLAYING":
            if self.clicked_box_index is not None and time.time() > self.delay_timer:
                self.clicked_box_index = None

        elif self.state == "WAIT_WIN":
            if time.time() > self.delay_timer:
                self.on_win()

        elif self.state == "WAIT_LOSE":
            if time.time() > self.delay_timer:
                self.on_lose()

    def draw(self, screen, font):
        title = font.render("Memory Sequence! Ingat urutannya.", True, WHITE)
        screen.blit(title, (20, 20))

        box_font = pygame.font.SysFont(None, 54)

        for i, box in enumerate(self.boxes):
            color = WHITE
            text_color = BLACK

            if self.state == "SHOWING" and self.showing_index < len(self.sequence):
                if self.sequence[self.showing_index] == i:
                    color = GREEN

            elif self.state in ["PLAYING", "WAIT_WIN", "WAIT_LOSE"]:
                if i in self.player_seq and i != self.clicked_box_index:
                    color = YELLOW

                if self.clicked_box_index == i:
                    color = BLUE
                    text_color = WHITE

            pygame.draw.rect(screen, color, box)
            
            num_surface = box_font.render(str(i + 1), True, text_color)
            num_rect = num_surface.get_rect(center=box.center)
            screen.blit(num_surface, num_rect)

        if self.state == "PLAYING":
            txt = font.render("Giliranmu! Klik sesuai urutan.", True, YELLOW)
            screen.blit(txt, (20, 60))
class Minigame3:
    def __init__(self, on_win, on_lose):
        # Hitbox player di Minigame 3
        self.player = pygame.Rect(WIDTH // 2 - 18, HEIGHT - 60, 36, 40)
        self.enemies = []
        self.timer = time.time() + 15
        self.on_win = on_win
        self.on_lose = on_lose

        sheet = pygame.image.load("assets/player.png").convert_alpha()
        cols, rows = 6, 4
        frame_w = sheet.get_width() // cols
        frame_h = sheet.get_height() // rows


        frame_baris_2 = pygame.transform.scale(
            sheet.subsurface(pygame.Rect(0, 1 * frame_h, frame_w, frame_h)), (80, 80)
        )
        frame_baris_3 = pygame.transform.scale(
            sheet.subsurface(pygame.Rect(0, 2 * frame_h, frame_w, frame_h)), (80, 80)
        )

        self.img_left = frame_baris_2
        self.img_right = frame_baris_3
        
        self.current_player_img = self.img_right

        # ARROW JATUH
        raw_arrow = pygame.image.load("assets/arrow.png").convert_alpha()
        scaled_arrow = pygame.transform.scale(raw_arrow, (32, 16))
        self.arrow_img = pygame.transform.rotate(scaled_arrow, -90)
    def handle_event(self, event):
        pass

    def update(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: 
            self.player.x -= 6
            self.current_player_img = self.img_left
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
            self.player.x += 6
            self.current_player_img = self.img_right

        if self.player.left < 0: self.player.left = 0
        if self.player.right > WIDTH: self.player.right = WIDTH

        if random.random() < 0.05:
            self.enemies.append(pygame.Rect(random.randint(0, WIDTH - 30), -30, 16, 32))

        for enemy in self.enemies[:]:
            enemy.y += 5
            if enemy.colliderect(self.player):
                self.on_lose()
            if enemy.top > HEIGHT:
                self.enemies.remove(enemy)

        if time.time() > self.timer:
            self.on_win()

    def draw(self, screen, font):
        title = font.render("Dodge! Hindari panah jatuh.", True, WHITE)
        screen.blit(title, (20, 20))
        time_left = max(0, int(self.timer - time.time()))
        timer_text = font.render(f"Bertahan: {time_left}s", True, WHITE)
        screen.blit(timer_text, (20, 60))

        player_draw_rect = self.current_player_img.get_rect(midbottom=self.player.midbottom)
        # Geser sedikit ke atas agar kaki sejajar
        player_draw_rect.y -= 10
        screen.blit(self.current_player_img, player_draw_rect)

        for enemy in self.enemies:
            screen.blit(self.arrow_img, enemy)