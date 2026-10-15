import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 220, 100)

# Paddle
paddle = pygame.Rect(350, 550, 100, 15)
paddle_speed = 7

# Ball
ball = pygame.Rect(390, 300, 20, 20)
ball_dx = 4
ball_dy = -4

# Bricks
bricks = []

for row in range(5):
    for col in range(8):
        brick = pygame.Rect(
            60 + col * 85,
            50 + row * 30,
            75,
            20
        )
        bricks.append(brick)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True

while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed

    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed

    # Keep paddle inside the screen
    paddle.x = max(0, min(paddle.x, WIDTH - paddle.width))

    # Move ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Bounce off left and right walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1

    # Bounce off the top wall
    if ball.top <= 0:
        ball_dy *= -1

    # Bounce off paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy *= -1

    # Check brick collisions
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy *= -1
            score += 10
            break

    # Check whether the ball falls below the screen
    if ball.top > HEIGHT:
        running = False

    # Draw background
    screen.fill(BLACK)

    # Draw paddle and ball
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw score
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

    # Check whether all bricks are destroyed
    if not bricks:
        win_text = font.render("YOU WIN!", True, GREEN)
        screen.blit(
            win_text,
            win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        )

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
