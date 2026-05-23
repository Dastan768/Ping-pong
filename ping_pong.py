import pygame
pygame.init()

lebar_scene = 500
tinggi_scene = 500
judul_scene = "Ping-pong terbaik"
gambar_papan = "asteroid.png"
Gambar_bola = "bullet.jpg" 
gambar_belakang = "Background.jpg"
musik_belakang = "space.ogg"
musik_pukul = "impactPunch_heavy_003.ogg"
Game_Run = True
Game_finish = False
scene = pygame.display.set_mode((lebar_scene, tinggi_scene))
scene.fill((255, 255, 255))
FPS = pygame.time.Clock()
belakang = pygame.transform.scale(pygame.image.load(gambar_belakang), (lebar_scene, tinggi_scene))

pygame.mixer.init()
pygame.mixer.music.load(musik_belakang)
pygame.mixer.music.play()

#membuat kelas
class GameSprite(pygame.sprite.Sprite):
   def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
       super().__init__()
       self.lebar = lebar
       self.tinggi = tinggi
       self.image = pygame.transform.scale(
           pygame.image.load(gambar), (self.lebar, self.tinggi))   
       self.speed = kecepatan
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
   def reset(self):
       scene.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update_kiri(self): #metoda untuk pergerakan
       tombol = pygame.key.get_pressed()
       #jika tombol atas
       if tombol[pygame.K_w] and self.rect.y>0:
           self.rect.y -= self.speed
       #jika tombol bawah
       if tombol[pygame.K_s] and self.rect.y<tinggi_scene-self.tinggi:
           self.rect.y += self.speed
   def update_kanan(self): #metoda untuk pergerakan
       tombol = pygame.key.get_pressed()
       #jika tombol atas
       if tombol[pygame.K_UP] and self.rect.y>0:
           self.rect.y -= self.speed
       #jika tombol bawah
       if tombol[pygame.K_DOWN] and self.rect.y<tinggi_scene-self.tinggi:
           self.rect.y += self.speed

player_kiri = Player(gambar_papan, 10, 10, 50, 100, 20)
player_kanan = Player(gambar_papan, lebar_scene-100, 10, 50, 100, 20)

while Game_Run:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            Game_Run == False

    if Game_finish == False:
        scene.blit(belakang, (0, 0))
        player_kiri.reset()
        player_kanan.reset()
        player_kiri.update_kiri()
        player_kanan.update_kanan()

    FPS.tick(60)
    pygame.display.update()