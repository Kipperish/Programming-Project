import math
import pygame
from pygame.locals import *


class Player:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.angle = PI / 2
        self.y_velocity = 0
        self.x_velocity = 0
        self.max_vel = 5

    def update(self):
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.rotate(keys)

    def move(self, keys):
        if keys[K_w]:
            self.x_velocity -= 0.3 * math.cos(self.angle)
            self.y_velocity -= 0.3 * math.sin(self.angle)
        elif keys[K_s]:
            self.x_velocity += 0.3 * math.cos(self.angle)
            self.y_velocity += 0.3 * math.sin(self.angle)
        elif not (keys[K_a] or keys[K_d]):
            self.x_velocity *= 0.95
            self.y_velocity *= 0.95

        if keys[K_a]:
            self.x_velocity -= 0.3 * math.sin(self.angle)
            self.y_velocity += 0.3 * math.cos(self.angle)
        elif keys[K_d]:
            self.x_velocity += 0.3 * math.sin(self.angle)
            self.y_velocity -= 0.3 * math.cos(self.angle)
        elif not (keys[K_w] or keys[K_s]):
            self.x_velocity *= 0.95
            self.y_velocity *= 0.95

        self.x_velocity *= 0.96
        self.y_velocity *= 0.96

        self.y -= self.y_velocity
        self.x -= self.x_velocity

    def rotate(self, keys):
        if keys[K_LEFT]:
            self.angle -= 0.1
            if self.angle < 0:
                self.angle += 2 * PI
        elif keys[K_RIGHT]:
            self.angle += 0.1
            if self.angle > 2 * PI:
                self.angle -= 2 * PI

    def draw(self, line_start):
        line_end = (int(self.x + 15 * math.cos(self.angle)),
                    int(self.y + 15 * math.sin(self.angle)))
        pygame.draw.line(WINDOW, (255, 0, 0), line_start, line_end, 3)
        pygame.draw.circle(WINDOW, (255, 0, 0), (int(self.x), int(self.y)), 5)


def draw():
    WINDOW.fill((0, 0, 0))
    player_pos = (int(player.x), int(player.y))
    draw_map()
    cast_rays(player_pos)
    player.draw(player_pos)
    pygame.display.flip()


def draw_map():
    for i in range(len(map_1)):
        for j in range(len(map_1[0])):
            if map_1[i][j] == "#":
                pygame.draw.rect(WINDOW, (0, 0, 255), pygame.Rect(
                    j * CELL_LENGTH, i * CELL_LENGTH, CELL_LENGTH, CELL_LENGTH))


def cast_rays(ray_start):
    ray_end = check_horizontal()
    if ray_end is None:
        ray_end = (int(player.x + 512 * math.cos(player.angle)),
                   int(player.y + 512 * math.sin(player.angle)))
    pygame.draw.line(WINDOW, (255, 255, 255), ray_start, ray_end)


def check_horizontal():
    player_map_x = int(player.x / 64)
    player_map_y = int(player.y / 64)
    ray_angle = player.angle

    if ray_angle == 0 or ray_angle == PI:
        return None

    if ray_angle < PI:
        y_step = 64
        first_intercept_y = (player_map_y + 1) * 64
    else:
        y_step = -64
        first_intercept_y = player_map_y * 64 - 1

    first_intercept_x = player.x + \
        (first_intercept_y - player.y) / math.tan(ray_angle)
    x_step = 64 / math.tan(ray_angle)
    if ray_angle > PI / 2 and ray_angle < 3 * PI / 2:
        x_step = -abs(x_step)
    else:
        x_step = abs(x_step)

    next_x = first_intercept_x
    next_y = first_intercept_y

    while 0 <= next_x < WIDTH and 0 <= next_y < HEIGHT:
        map_x = int(next_x / 64)
        map_y = int(next_y / 64)
        if map_x >= 0 and map_x < len(map_1[0]) and map_y >= 0 and map_y < len(map_1):
            if map_1[map_y][map_x] == "#":
                return (int(next_x), int(next_y))
        next_x += x_step
        next_y += y_step

    return None


WIDTH = 1024
HEIGHT = 768
CELL_LENGTH = 64
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
PI = math.pi
RAY_ANGLE = PI / 360
player = Player()

map_1 = [
    "############",
    "#     #    #",
    "#     #    #",
    "#   ####   #",
    "#          #",
    "#          #",
    "#######    #",
    "#     #    #",
    "#     #    #",
    "#          #",
    "#          #",
    "############",
]


def main():
    global player
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        pygame.display.set_caption(str(int(clock.get_fps())))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        player.update()
        draw()


main()
