import pygame
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações da janela
WIDTH = 800
HEIGHT = 600
FPS = 60

# Configurando a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Definindo as raquetes e a bola
paddle_width = 15
paddle_height = 100
ball_radius = 10

# Velocidades
paddle_speed = 10
ball_speed_x = 7
ball_speed_y = 7

# Criando as raquetes e a bola
player1_y = HEIGHT // 2 - paddle_height // 2
player2_y = HEIGHT // 2 - paddle_height // 2
ball_x = WIDTH // 2 - ball_radius
ball_y = HEIGHT // 2 - ball_radius

# Contadores de pontos
player1_score = 0
player2_score = 0

# Função para desenhar a tela
def draw():
    global player1_y, player2_y, ball_x, ball_y, player1_score, player2_score

    screen.fill(BLACK)

    # Desenhando as raquetes
    pygame.draw.rect(screen, WHITE, (10, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (WIDTH - 10 - paddle_width, player2_y, paddle_width, paddle_height))

    # Desenhando a bola
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Desenhando a linha do meio
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Exibindo a pontuação
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{player1_score}  -  {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

# Função para mover a bola
def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, player1_score, player2_score

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisão com as paredes
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y *= -1

    # Colisão com as raquetes
    if ball_x <= 10 + paddle_width and player1_y < ball_y < player1_y + paddle_height:
        ball_speed_x *= -1
    elif ball_x >= WIDTH - 10 - paddle_width - ball_radius and player2_y < ball_y < player2_y + paddle_height:
        ball_speed_x *= -1

    # Marcar ponto
    if ball_x < 0:
        player2_score += 1
        reset_ball()
    elif ball_x > WIDTH:
        player1_score += 1
        reset_ball()

# Função para resetar a bola
def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = WIDTH // 2 - ball_radius
    ball_y = HEIGHT // 2 - ball_radius
    ball_speed_x *= random.choice([1, -1])
    ball_speed_y *= random.choice([1, -1])

# Função principal
def game():
    global player1_y, player2_y

    clock = pygame.time.Clock()

    # Loop do jogo
    running = True
    while running:
        clock.tick(FPS)

        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movendo as raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= paddle_speed
        if keys[pygame.K_s] and player1_y < HEIGHT - paddle_height:
            player1_y += paddle_speed
        if keys[pygame.K_UP] and player2_y > 0:
            player2_y -= paddle_speed
        if keys[pygame.K_DOWN] and player2_y < HEIGHT - paddle_height:
            player2_y += paddle_speed

        # Mover a bola
        move_ball()

        # Atualizar a tela
        draw()

    pygame.quit()

# Iniciar o jogo
game()
