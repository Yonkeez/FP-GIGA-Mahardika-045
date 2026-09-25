import pygame
from config import *

class Arrow:
    def __init__(self, x, y, direction, speed=6):
        # Hitbox proyektil panah
        if direction in ["LEFT", "RIGHT"]:
            self.rect = pygame.Rect(x, y + TILE_SIZE // 2 - 3, 16, 6)
        else:
            self.rect = pygame.Rect(x + TILE_SIZE // 2 - 3, y, 6, 16)
            
        self.direction = direction
        self.speed = speed

    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed

    def draw(self, surface):
        # Menggambar panah sederhana berwarna oranye/merah
        pygame.draw.rect(surface, ORANGE, self.rect)


class ArrowTrap:
    def __init__(self, x, y, direction="RIGHT", cooldown_seconds=2.0):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.direction = direction
        self.cooldown_ms = int(cooldown_seconds * 1000)
        self.last_shot_time = pygame.time.get_ticks()
        self.arrows = []

    def update(self, walls):
        current_time = pygame.time.get_ticks()
        
        # Temba_kan panah baru jika cooldown sudah habis
        if current_time - self.last_shot_time >= self.cooldown_ms:
            spawn_x, spawn_y = self.rect.x, self.rect.y
            
            # Spawn panah tepat 1 langkah di luar blok perangkap
            if self.direction == "RIGHT":
                spawn_x += TILE_SIZE
            elif self.direction == "LEFT":
                spawn_x -= 16
            elif self.direction == "DOWN":
                spawn_y += TILE_SIZE
            elif self.direction == "UP":
                spawn_y -= 16

            self.arrows.append(Arrow(spawn_x, spawn_y, self.direction))
            self.last_shot_time = current_time

        # Update posisi panah & hapus jika menabrak dinding
        for arrow in self.arrows[:]:
            arrow.update()
            
            # Cek tabrakan dengan dinding
            for wall in walls:
                if arrow.rect.colliderect(wall):
                    if arrow in self.arrows:
                        self.arrows.remove(arrow)
                    break

    def check_player_collision(self, player_rect):
        """Mengembalikan True jika player terkena panah"""
        for arrow in self.arrows[:]:
            if arrow.rect.colliderect(player_rect):
                self.arrows.remove(arrow)
                return True
        return False

    def draw(self, surface):
        # Gambar lubang jebakan panah (warna abu-abu gelap dengan indikator)
        pygame.draw.rect(surface, (60, 60, 60), self.rect)
        pygame.draw.rect(surface, RED, self.rect, width=2)
        
        # Gambar semua panah aktif yang sedang meluncur
        for arrow in self.arrows:
            arrow.draw(surface)