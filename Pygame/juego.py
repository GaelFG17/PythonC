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

#Agregar enemigos
enemy_width = 50
enemy_heigth = 50
enemy_speed = 3
enemies = []
num_enemies = 5

#Generar enemigos
def create_enemies(num):
    for _ in range(num):
        x = random.randint(0, screen_width - enemy_width)
        y = random.randint(50, 150)
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_heigth))
        
#crear los enemigos
create_enemies(num_enemies)


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
            
    #Mover enemigos
    for enemy in enemies:
        enemy.x += enemy_speed
        if enemy.x <= 0 or enemy.x >= screen_width - enemy_width:
            enemy_speed *= -1 #Ca,biar direccion
            
    # Detección de colisiones entre proyectiles y enemigos
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Dibujar el jugador
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, WHITE, player_rect)

    # Dibujar los proyectiles
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
        
    #Dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Actualizar la pantalla
    pygame.display.flip()
    
    #Verificar si no quedan enemigos
    if not enemies:
        print("GANASTE")
        pygame.quit()
        sys.exit()
