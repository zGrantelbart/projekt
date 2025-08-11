import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
OBJECT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")
spieler = pygame.Rect(SCREEN_WIDTH -20, SCREEN_HEIGHT // 2 - 70, 10, 140)
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, OBJECT_COLOR, spieler)
    pygame.draw.ellipse(screen, OBJECT_COLOR, ball)
    pygame.display.flip()


pygame.quit()
sys.exit()