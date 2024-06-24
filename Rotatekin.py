import pygame 
import math
from Utilities import scaleImage

from pygame.locals import(
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN
)

class Bean(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = scaleImage(pygame.image.load("Images\BAYTEKIN.jpg").convert_alpha(), 0.1)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(150, 150))  
        self.angle = 0
        self.mass = 10
        self.force = 10
        self.acceleration = self.force/self.mass
        self.rotation_speed = 5  
        self.velocity = 0
        self.drag = self.velocity/(100*math.sqrt(self.mass))
    
    def rotate(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.angle += self.rotation_speed
        if keys[K_RIGHT]:
            self.angle -= self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center) 

    def move(self):
        keys = pygame.key.get_pressed()
        radiansAngle = math.radians(self.angle)
        if keys[K_UP]:
            self.velocity += self.acceleration
        if keys[K_DOWN]:
            self.velocity -= self.acceleration

        move_x = self.velocity*math.sin(radiansAngle)
        move_y = self.velocity*math.cos(radiansAngle)
        self.rect.x -= move_x
        self.rect.y -= move_y

        
            
    def update(self):
        self.drag = self.velocity/20
        self.velocity -= self.drag
        self.rotate()
        self.move()


background_colour = (234, 212, 252) 
screen = pygame.display.set_mode((1000, 1000)) 
pygame.display.set_caption('Rotatekin') 
screen.fill(background_colour)   

bean = Bean()

fps = 60
clock = pygame.time.Clock()

running = True
  

while running:
    clock.tick(fps)
    screen.fill(background_colour)
    bean.update()
    screen.blit(bean.image, bean.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False