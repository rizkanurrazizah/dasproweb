import pygame
import sys

# ============================================================
# BREAKOUT / BRICK BREAKER (PYGAME)
# Versi Game Over + Restart
# Menggunakan LIST dan DICTIONARY
# ============================================================

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Jadul")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# Warna
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 60, 60)
GREEN = (60, 255, 60)
BLACK = (0, 0, 0)

# ------------------------------------------------------------
# FUNGSI RESET GAME
# ------------------------------------------------------------
def reset_game():
    global paddle, ball, bricks

    # Paddle
    paddle = {
        "x": WIDTH // 2 - 60,
        "y": HEIGHT - 40,
        "w": 120,
        "h": 15,
        "speed": 7
    }

    # Ball
    ball = {
        "x": WIDTH // 2,
        "y": HEIGHT // 2,
        "size": 12,
        "dx": 4,
        "dy": -4
    }

    # Bricks (list berisi dictionary)
    bricks = []
    rows = 6
    cols = 10
    brick_w = WIDTH // cols
    brick_h = 25

    for row in range(rows):
        for col in range(cols):
            brick = {
                "x": col * brick_w,
                "y": row * brick_h + 60,
                "w": brick_w,
                "h": brick_h,
                "color": (150, 50 + row * 30, 50 + col)
            }
            bricks.append(brick)

reset_game()  # jalankan sekali di awal

# Status game
game_over = False


# ------------------------------------------------------------
# GAMERUN LOOP
# ------------------------------------------------------------
running = True
while running:
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # ============================
    #  MODE GAME OVER
    # ============================
    if game_over:
        win.fill(BLACK)
        text1 = font.render("GAME OVER", True, RED)
        text2 = font.render("Tekan R untuk Restart", True, WHITE)

        win.blit(text1, (WIDTH//2 - text1.get_width()//2, 220))
        win.blit(text2, (WIDTH//2 - text2.get_width()//2, 300))
        pygame.display.update()

        # Tekan R → restart permainan
        if keys[pygame.K_r]:
            reset_game()
            game_over = False

        continue  # skip game logic

    # ============================
    #  MOVEMENT PADDLE
    # ============================
    if keys[pygame.K_LEFT] and paddle["x"] > 0:
        paddle["x"] -= paddle["speed"]
    if keys[pygame.K_RIGHT] and paddle["x"] < WIDTH - paddle["w"]:
        paddle["x"] += paddle["speed"]

    # ============================
    #  MOVEMENT BALL
    # ============================
    ball["x"] += ball["dx"]
    ball["y"] += ball["dy"]

    # Benturan kiri/kanan
    if ball["x"] <= 0 or ball["x"] >= WIDTH - ball["size"]:
        ball["dx"] *= -1

    # Benturan atas
    if ball["y"] <= 0:
        ball["dy"] *= -1

    # Rect untuk collision detection
    paddle_rect = pygame.Rect(paddle["x"], paddle["y"], paddle["w"], paddle["h"])
    ball_rect = pygame.Rect(ball["x"], ball["y"], ball["size"], ball["size"])

    # Benturan dengan paddle
    if ball_rect.colliderect(paddle_rect):
        ball["dy"] *= -1

    # ============================
    #  COLLISION BALL VS BRICKS
    # ============================
    for brick in bricks[:]:
        brick_rect = pygame.Rect(brick["x"], brick["y"], brick["w"], brick["h"])
        if ball_rect.colliderect(brick_rect):
            ball["dy"] *= -1
            bricks.remove(brick)
            break

    # Jika bola jatuh → game over
    if ball["y"] >= HEIGHT:
        game_over = True

    # ============================
    #  DRAW
    # ============================
    win.fill(BLACK)

    pygame.draw.rect(win, BLUE, paddle_rect)  # paddle
    pygame.draw.rect(win, WHITE, ball_rect)   # bola

    for brick in bricks:
        pygame.draw.rect(win, brick["color"], (brick["x"], brick["y"], brick["w"], brick["h"]))

    pygame.display.update()
