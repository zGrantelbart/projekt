import pygame
import sys
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.colliderect(player):
        ball_speed_x *= -1
    if ball.left <= 0:
        ball.center = (SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
        ball_speed_x *= -1
    if ball.right >= SCREEN_WIDTH:
        ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        ball_speed_x *= -1
        
pygame.init()
clock = pygame.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
OBJECT_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")
player = pygame.Rect(SCREEN_WIDTH -20, SCREEN_HEIGHT // 2 - 70, 10, 140)
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player.y += player_speed

    player.top = max(player.top, 0)
    player.bottom = min(player.bottom, SCREEN_HEIGHT)
    
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, OBJECT_COLOR, player)
    pygame.draw.ellipse(screen, OBJECT_COLOR, ball)
    pygame.draw.aaline(screen, OBJECT_COLOR, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()