import pygame
import sys

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

# FPS
clock = pygame.time.Clock()

# Jugador
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Proyectiles
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Función para manejar los disparos
def shoot_bullet(x, y):
    bullet = pygame.Rect(x + player_width // 2 - bullet_width // 2, y, bullet_width, bullet_height)
    bullets.append(bullet)

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
    if keys[pygame.K_SPACE]:
        shoot_bullet(player_x, player_y)

    # Mover los proyectiles
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Dibujar el jugador
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, WHITE, player_rect)

    # Dibujar los proyectiles
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Actualizar la pantalla
    pygame.display.flip()
