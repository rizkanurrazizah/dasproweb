# mahasiswa = [
#     {
#         "nama_lengkap":"Fulan Fulus",
#         "prodi": "Informatika",
#         "umur": 19
#     },
#     {
#         "nama_lengkap":"Budi Budiman",
#         "prodi": "RKS",
#         "umur": 21
#     }
# ]
# print(mahasiswa[0]["prodi"])
















# # fulan = {
# #     "nama_lengkap":"Fulan Fulus",
# #     "prodi": "Informatika",
# #     "umur": 19
# # }

# # fulan["nama_lengkap"] = "Muhammad Fulan"
# # fulan["nim"] = 123456
# # fulan.pop("umur") #untuk menghapus key yang sudah ditentukan
# # fulan.popitem() #untuk menghapus elemen yang terakhir di masukkan 
# # print(fulan)


# # print(fulan["umur"])

# # print(fulan)

import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game dengan List & Dictionary")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
BLUE = (50, 150, 255)

# --------------------- PLAYER (dictionary) ---------------------
player = {
    "rect": pygame.Rect(100, HEIGHT//2, 40, 40),
    "speed": 5
}

# --------------------- MUSUH (list of dictionaries) ---------------------
enemies = []
for i in range(5):
    enemies.append({
        "rect": pygame.Rect(random.randint(500, 900), random.randint(50, HEIGHT-50), 40, 40),
        "speed": random.randint(2, 4)
    })

# --------------------- PELURU (list) ---------------------
bullets = []  # setiap elemen = pygame.Rect


while True:
    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tembak
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player["rect"].right,
                                           player["rect"].centery - 5, 10, 10))

    keys = pygame.key.get_pressed()

    # Gerak player
    if keys[pygame.K_UP]:
        player["rect"].y -= player["speed"]
    if keys[pygame.K_DOWN]:
        player["rect"].y += player["speed"]

    # Batas layar
    player["rect"].y = max(0, min(HEIGHT - 40, player["rect"].y))

    # --------------------- GERAKKAN PELURU ---------------------
    for b in bullets[:]:
        b.x += 10
        if b.x > WIDTH:
            bullets.remove(b)

    # --------------------- GERAKKAN MUSUH ---------------------
    for e in enemies:
        e["rect"].x -= e["speed"]

        # respawn jika keluar layar
        if e["rect"].x < -50:
            e["rect"].x = random.randint(900, 1200)
            e["rect"].y = random.randint(50, HEIGHT-50)

    # --------------------- TABRAKAN PELURU → MUSUH ---------------------
    for e in enemies:
        for b in bullets:
            if e["rect"].colliderect(b):
                bullets.remove(b)
                e["rect"].x = random.randint(900, 1200)
                e["rect"].y = random.randint(50, HEIGHT-50)

    # --------------------- RENDER ---------------------
    screen.fill(WHITE)

    # Player
    pygame.draw.rect(screen, BLUE, player["rect"])

    # Musuh
    for e in enemies:
        pygame.draw.rect(screen, RED, e["rect"])

    # Peluru
    for b in bullets:
        pygame.draw.rect(screen, BLACK, b)

    pygame.display.update()
    clock.tick(60)
