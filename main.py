import pygame
import random

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2

food_x = random.randint(0, SCREEN_WIDTH)
food_y = random.randint(0, SCREEN_HEIGHT)

snake = pygame.Rect((snake_x, snake_y, 40, 40))

movement_map = {
    pygame.K_UP: (0, -1, "UP"),
    pygame.K_DOWN: (0, 1, "DOWN"),
    pygame.K_LEFT: (-1, 0, "LEFT"),
    pygame.K_RIGHT: (1, 0, "RIGHT"),
    pygame.K_p: (0, 0, "PAUSE")
}

vel = 0.5

clock = pygame.time.Clock()

last_key_pressed = movement_map[pygame.K_p]

run = True

while run:
    screen.fill((0,0,0))
    dt = clock.tick(60)

    pygame.draw.rect(screen, (0, 255, 0), snake)

    food = pygame.draw.circle(screen, (255, 0, 0), (food_x, food_y), 10)

    if snake.colliderect(food):
        food_x = random.randint(0, SCREEN_WIDTH)
        food_y = random.randint(0, SCREEN_HEIGHT)


    key = pygame.key.get_pressed()

    #go in direction last set until direction changes
    if any(key):
        for k, (dx, dy, direction) in movement_map.items():
            if key[k]:
                snake.x += dx * vel * dt
                snake.y += dy * vel * dt
                last_key_pressed = movement_map.get(k)
                break
    else:
        dx, dy, _ = last_key_pressed
        snake.x += dx * vel * dt
        snake.y += dy * vel * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
