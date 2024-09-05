import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Disparos 2D")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fuente para el contador y vidas
font = pygame.font.Font(None, 36)

# FPS
clock = pygame.time.Clock()

# Jugador
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
lives = 3  # Vidas del jugador

# Proyectiles
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []
shoot_delay = 500  # Tiempo de retraso entre disparos en milisegundos (0.5 segundos)
last_shot_time = pygame.time.get_ticks()  # Control del tiempo del último disparo

# Enemigos
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemy_drop_speed = 5  # Velocidad a la que los enemigos se mueven hacia abajo
enemies = []
num_enemies = 5

# Generar enemigos
def create_enemies(num):
    for _ in range(num):
        x = random.randint(0, screen_width - enemy_width)
        y = random.randint(50, 150)
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Crear los enemigos
create_enemies(num_enemies)

score = 0

# Función para manejar los disparos
def shoot_bullet(x, y):
    bullet = pygame.Rect(x + player_width // 2 - bullet_width // 2, y, bullet_width, bullet_height)
    bullets.append(bullet)

# Función para mostrar el contador de puntuación
def draw_score(score):
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Función para mostrar las vidas del jugador
def draw_lives(lives):
    lives_text = font.render(f"Vidas: {lives}", True, WHITE)
    screen.blit(lives_text, (screen_width - 120, 10))

# Bucle principal del juego
running = True
while running:
    clock.tick(60)  # Limitar a 60 FPS
    screen.fill(BLACK)  # Fondo negro

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Control de disparo con retraso
    current_time = pygame.time.get_ticks()  # Obtener el tiempo actual
    if keys[pygame.K_SPACE] and current_time - last_shot_time > shoot_delay:
        shoot_bullet(player_x, player_y)
        last_shot_time = current_time  # Actualizar el tiempo del último disparo

    # Mover los proyectiles
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Mover enemigos
    for enemy in enemies[:]:
        enemy.y += enemy_drop_speed  # Mover enemigos hacia abajo

        # Si un enemigo llega al fondo de la pantalla, reaparecer arriba en una nueva posición
        if enemy.y >= screen_height:
            enemy.x = random.randint(0, screen_width - enemy_width)
            enemy.y = random.randint(50, 150)
            lives -= 1  # Quitar una vida al jugador
            if lives == 0:
                print("PERDISTE")
                pygame.quit()
                sys.exit()

        # Si el enemigo toca al jugador, también reaparece y se quita una vida
        if enemy.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            enemy.x = random.randint(0, screen_width - enemy_width)
            enemy.y = random.randint(50, 150)
            lives -= 1
            if lives == 0:
                print("PERDISTE")
                pygame.quit()
                sys.exit()

    # Detección de colisiones entre proyectiles y enemigos
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1  # Incrementar el contador
                # Crear un nuevo enemigo en una posición aleatoria arriba
                x = random.randint(0, screen_width - enemy_width)
                y = random.randint(50, 150)
                enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))
                break

    # Dibujar el jugador
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, WHITE, player_rect)

    # Dibujar los proyectiles
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Dibujar el contador de puntuación y las vidas
    draw_score(score)
    draw_lives(lives)

    # Actualizar la pantalla
    pygame.display.flip()

    # Verificar si no quedan enemigos
    if not enemies:
        print("GANASTE")
        pygame.quit()
        sys.exit()
