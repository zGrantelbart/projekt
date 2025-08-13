import pygame
import sys
import random
import database


database.init_db()
pygame.init()
try:
    wand_sound = pygame.mixer.Sound("sounds/boop.wav")
    pong_sound = pygame.mixer.Sound("sounds/pong.wav") 
    score_sound = pygame.mixer.Sound("sounds/score.mp3")
except pygame.error as e:
    print(f"Kann Sounddateien nicht laden: {e}")
    wand_sound = pygame.mixer.Sound(buffer=b'')
    pong_sound = pygame.mixer.Sound(buffer=b'')
    score_sound = pygame.mixer.Sound(buffer=b'')
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINNING_SCORE = 5

BACKGROUND_COLOR = (0, 0, 0)
OBJECT_COLOR = (255, 255, 255)
LINE_COLOR = (128, 128, 128)
INPUT_BOX_ACTIVE_COLOR = pygame.Color('lightskyblue3')
INPUT_BOX_INACTIVE_COLOR = pygame.Color('gray15')

game_state = "menu" 
try:
    menu_font = pygame.font.Font("JUNGLEFE.TTF", 32)
    score_font = pygame.font.Font("JUNGLEFE.TTF", 40)
    input_font = pygame.font.Font("JUNGLEFE.TTF", 28)
except FileNotFoundError:
    print("Schriftart nicht gefunden!")
    score_font = pygame.font.Font("freesansbold.ttf", 32)
    menu_font = pygame.font.Font("freesansbold.ttf", 40)
    input_font = pygame.font.Font("freesansbold.ttf", 28)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")

player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
opponent = pygame.Rect(10, SCREEN_HEIGHT / 2 - 70, 10, 140) 
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)

input_box = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2, 200, 50)
user_name = ''
input_active = True

player_speed = 0
opponent_speed = 7
player_score, opponent_score = 0, 0
ball_speed_x, ball_speed_y = 0, 0 

def reset_game():
    global player_score, opponent_score, user_name, game_state
    player.center = (SCREEN_WIDTH - 15, SCREEN_HEIGHT / 2)
    opponent.center = (15, SCREEN_HEIGHT / 2)
    player_score = 0
    opponent_score = 0
    user_name = ''
    game_state = "playing" 
    ball_restart()

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball_speed_y = 7 * random.choice((1, -1))
    ball_speed_x = 7 * random.choice((1, -1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: player_speed += 7
                if event.key == pygame.K_UP: player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN: player_speed -= 7
                if event.key == pygame.K_UP: player_speed += 7

        elif game_state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset_game()
        elif game_state == "game_over":
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if user_name:
                            database.add_highscore(user_name, player_score)
                        game_state = "menu" 
                    elif event.key == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode
                elif event.key == pygame.K_RETURN:
                    game_state = "menu"

    if game_state == "playing":
        player.y += player_speed
        player.top = max(player.top, 0)
        if player.bottom >= SCREEN_HEIGHT: player.bottom = SCREEN_HEIGHT

        if opponent.top < ball.y: opponent.top += opponent_speed
        if opponent.bottom > ball.y: opponent.bottom -= opponent_speed
        opponent.top = max(opponent.top, 0)
        if opponent.bottom >= SCREEN_HEIGHT: opponent.bottom = SCREEN_HEIGHT

        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed_y *= -1 
            wand_sound.play()
        if ball.colliderect(player) or ball.colliderect(opponent): 
            ball_speed_x *= -1
            pong_sound.play()
        if ball.left <= 0:
            player_score += 1
            score_sound.play()
            ball_restart()
        if ball.right >= SCREEN_WIDTH:
            opponent_score += 1
            score_sound.play()
            ball_restart()

        if player_score >= WINNING_SCORE or opponent_score >= WINNING_SCORE:
            game_state = "game_over"
            input_active = True 

    screen.fill(BACKGROUND_COLOR)

    if game_state == "playing":
        pygame.draw.rect(screen, OBJECT_COLOR, player)
        pygame.draw.rect(screen, OBJECT_COLOR, opponent)
        pygame.draw.ellipse(screen, OBJECT_COLOR, ball)
        pygame.draw.aaline(screen, LINE_COLOR, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

        player_text = score_font.render(f"{player_score}", True, OBJECT_COLOR)
        screen.blit(player_text, (SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2))
        opponent_text = score_font.render(f"{opponent_score}", True, OBJECT_COLOR)
        screen.blit(opponent_text, (SCREEN_WIDTH / 2 - 45, SCREEN_HEIGHT / 2))

    elif game_state == "menu":
        title_text = menu_font.render("Ping Pong", True, OBJECT_COLOR)
        screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, 100))

        start_text = score_font.render("Leertaste zum starten drücken", True, OBJECT_COLOR)
        screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, 250))

        scores = database.get_highscores()
        score_title = score_font.render("Highscores", True, OBJECT_COLOR)
        screen.blit(score_title, (SCREEN_WIDTH/2 - score_title.get_width()/2, 350))
        for i, (name, score) in enumerate(scores):
            score_entry = score_font.render(f"{i+1}. {name}: {score}", True, OBJECT_COLOR)
            screen.blit(score_entry, (SCREEN_WIDTH/2 - score_entry.get_width()/2, 400 + i * 40))

    elif game_state == "game_over":
        end_text = menu_font.render("Game Over", True, OBJECT_COLOR)
        screen.blit(end_text, (SCREEN_WIDTH/2 - end_text.get_width()/2, 150))

        if player_score >= WINNING_SCORE:
            prompt_text = score_font.render("Glückwunsch! Name:", True, OBJECT_COLOR)
            screen.blit(prompt_text, (SCREEN_WIDTH/2 - prompt_text.get_width()/2, 250))

            pygame.draw.rect(screen, INPUT_BOX_ACTIVE_COLOR, input_box, 2)
            text_surface = input_font.render(user_name, True, OBJECT_COLOR)
            screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        else:
            lost_text = score_font.render("Noob mit Enter kannst du es nochmal versuchen", True, OBJECT_COLOR)
            screen.blit(lost_text, (SCREEN_WIDTH/2 - lost_text.get_width()/2, 300))
            input_active = False

    pygame.display.flip()
    clock.tick(60)