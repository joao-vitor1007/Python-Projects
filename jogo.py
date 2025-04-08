import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong com Duas Bolas Independentes")

paddle_width = 15
paddle_height = 100
ball_radius = 10

paddle_speed = 12

player1_y = HEIGHT // 2 - paddle_height // 2
player2_y = HEIGHT // 2 - paddle_height // 2
ball1_x = WIDTH // 2 - ball_radius
ball1_y = HEIGHT // 2 - ball_radius
ball2_x = WIDTH // 4 - ball_radius
ball2_y = HEIGHT // 4 - ball_radius

ball1_speed_x = random.choice([9, -9])
ball1_speed_y = random.choice([9, -9])
ball2_speed_x = random.choice([10, -10])
ball2_speed_y = random.choice([10, -10])

player1_score = 0
player2_score = 0

def draw():
    global player1_y, player2_y, ball1_x, ball1_y, ball2_x, ball2_y, player1_score, player2_score

    screen.fill(BLACK)

    pygame.draw.rect(screen, BLUE, (10, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, RED, (WIDTH - 10 - paddle_width, player2_y, paddle_width, paddle_height))

    pygame.draw.circle(screen, WHITE, (ball1_x, ball1_y), ball_radius)
    pygame.draw.circle(screen, WHITE, (ball2_x, ball2_y), ball_radius)

    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    font = pygame.font.Font(None, 36)
    player1_score_text = font.render(str(player1_score), True, BLUE)
    player2_score_text = font.render(str(player2_score), True, RED)

    screen.blit(player1_score_text, (WIDTH // 2 - 100 - player1_score_text.get_width() // 2, 20))
    screen.blit(player2_score_text, (WIDTH // 2 + 100 - player2_score_text.get_width() // 2, 20))

    pygame.display.flip()

def move_balls():
    global ball1_x, ball1_y, ball1_speed_x, ball1_speed_y, ball2_x, ball2_y, ball2_speed_x, ball2_speed_y, player1_score, player2_score

    ball1_x += ball1_speed_x
    ball1_y += ball1_speed_y

    ball2_x += ball2_speed_x
    ball2_y += ball2_speed_y

    if ball1_y <= 0 or ball1_y >= HEIGHT:
        ball1_speed_y *= -1

    if ball2_y <= 0 or ball2_y >= HEIGHT:
        ball2_speed_y *= -1

    if ball1_x <= 10 + paddle_width and player1_y < ball1_y < player1_y + paddle_height:
        ball1_speed_x *= -1
    elif ball1_x >= WIDTH - 10 - paddle_width - ball_radius and player2_y < ball1_y < player2_y + paddle_height:
        ball1_speed_x *= -1

    if ball2_x <= 10 + paddle_width and player1_y < ball2_y < player1_y + paddle_height:
        ball2_speed_x *= -1
    elif ball2_x >= WIDTH - 10 - paddle_width - ball_radius and player2_y < ball2_y < player2_y + paddle_height:
        ball2_speed_x *= -1

    if ball1_x < 0:
        player2_score += 1
        reset_ball(1)
    elif ball1_x > WIDTH:
        player1_score += 1
        reset_ball(1)

    if ball2_x < 0:
        player2_score += 1
        reset_ball(2)
    elif ball2_x > WIDTH:
        player1_score += 1
        reset_ball(2)

def reset_ball(ball_number):
    global ball1_x, ball1_y, ball2_x, ball2_y, ball1_speed_x, ball1_speed_y, ball2_speed_x, ball2_speed_y

    if ball_number == 1:
        ball1_x = WIDTH // 2 - ball_radius
        ball1_y = HEIGHT // 2 - ball_radius
        ball1_speed_x = random.choice([9, -9])
        ball1_speed_y = random.choice([9, -9])
    elif ball_number == 2:
        ball2_x = WIDTH // 4 - ball_radius
        ball2_y = HEIGHT // 4 - ball_radius
        ball2_speed_x = random.choice([10, -10])
        ball2_speed_y = random.choice([10, -10])

def ai_move():
    global player1_y, player2_y

    distance_ball1 = abs(player1_y + paddle_height // 2 - ball1_y)
    distance_ball2 = abs(player1_y + paddle_height // 2 - ball2_y)

    if distance_ball1 < distance_ball2:
        if player1_y + paddle_height // 2 < ball1_y:
            player1_y += paddle_speed
        elif player1_y + paddle_height // 2 > ball1_y:
            player1_y -= paddle_speed
    else:
        if player1_y + paddle_height // 2 < ball2_y:
            player1_y += paddle_speed
        elif player1_y + paddle_height // 2 > ball2_y:
            player1_y -= paddle_speed

    distance_ball1 = abs(player2_y + paddle_height // 2 - ball1_y)
    distance_ball2 = abs(player2_y + paddle_height // 2 - ball2_y)

    if distance_ball1 < distance_ball2:
        if player2_y + paddle_height // 2 < ball1_y:
            player2_y += paddle_speed
        elif player2_y + paddle_height // 2 > ball1_y:
            player2_y -= paddle_speed
    else:
        if player2_y + paddle_height // 2 < ball2_y:
            player2_y += paddle_speed
        elif player2_y + paddle_height // 2 > ball2_y:
            player2_y -= paddle_speed

    if player1_y < 0:
        player1_y = 0
    elif player1_y > HEIGHT - paddle_height:
        player1_y = HEIGHT - paddle_height

    if player2_y < 0:
        player2_y = 0
    elif player2_y > HEIGHT - paddle_height:
        player2_y = HEIGHT - paddle_height

def game():
    global player1_y, player2_y

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ai_move()

        move_balls()

        draw()

    pygame.quit()

game()
