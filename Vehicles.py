import pygame
import math
from pygame.locals import(
    K_a,
    K_d,
    K_w,
    K_s,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)
from Utilities import scaleImage, rotateAroundCenter, LinkedList, Node

#Parent class that different types of vehicle will inherit from
class Vehicle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global colourList
        self.sprites = {"RED":None, "BLUE":None, "GREEN":None, "PURPLE":None}
        self.originalImage = pygame.image.load("Images\\BAYTEKIN.jpg").convert_alpha()
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=(0,0))
        self.lives = 0
        self.mass = 1
        self.enginePower = 1
        self.acceleration = (self.enginePower)/(self.mass)
        self.angle = 0
        self.rotationSpeed = (self.enginePower)/(self.mass)
        self.velocity = 0
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity) #Stoke's law for fluid desnity to realistically apply drag using constants for air
        self.moving = False

#Method to rotate the vehicle
    def rotate(self):
        keyPressed = pygame.key.get_pressed()
        if keyPressed[K_a] or keyPressed[K_LEFT]:                     #Changes the angle value when 'a' or 'd' is pressed
            self.angle += self.rotationSpeed
        if keyPressed[K_d] or keyPressed[K_RIGHT]:
            self.angle -= self.rotationSpeed
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)     

#Method to apply acceleration to the vehicles velocity
    def accelerate(self):
        keyPressed = pygame.key.get_pressed()

        #Increases velocity by the acceleration when 'w' pressed
        if keyPressed[K_w] or keyPressed[K_UP]:
            self.velocity += self.acceleration
            self.moving = True
        elif not keyPressed[K_s] or not keyPressed[K_DOWN]:
            self.moving = False

        #Decreases velocity by the acceleration when 's' pressed
        if keyPressed[K_s] or keyPressed[K_DOWN]:
            self.velocity -= self.acceleration
            self.moving = True
        elif not keyPressed[K_w] or not keyPressed[K_UP]:
            self.moving = False

        

#Method to take velocity and rotation values from the vehicle and convert into movement
    def move(self):
        radians = math.radians(self.angle)
        movementX = self.velocity * math.sin(radians)
        movementY = self.velocity * math.cos(radians)
        self.rect.x += movementX
        self.rect.y += movementY

#Method to update the position and rotation of the vehicle
    def update(self):
        global colourList
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 1)
        self.rotate()
        self.accelerate()
        self.move()
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.velocity -= self.drag
        self.rotationSpeed = self.velocity/2

#Method to set a number of lives
    def setLives(self, lives):
        self.lives = lives

#Method to remove a life
    def loseLife(self):
        self.lives -= 1

#Linked List for changing vehicle colours
colourList = LinkedList()
colourList.insertAtFront("PURPLE")
colourList.insertAtFront("BLUE")
colourList.insertAtFront("GREEN")
colourList.insertAtFront("RED")
colourList.loop()

#Creates a Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        global colourList
        self.sprites = {"RED":"Images\\Cars\\RedStrip.png", "BLUE":"Images\\Cars\\BlueStrip.png", "GREEN":"Images\\Cars\\GreenStrip.png", "PURPLE":"Images\\Cars\\PinkStrip.png"}
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 1)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=(540,360))
        self.lives = 0
        self.mass = 1000
        self.enginePower = 100
        self.acceleration = (self.enginePower)/(self.mass)
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.angle = 0
        self.rotationSpeed = self.velocity/2
        self.velocity = 0
        self.moving = False

#Creates a Sports Car class that inherits from Vehicle
class SportsCar(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        global colourList
        self.sprites = {"RED":"Images\Sports Cars\RedRacecar.png", "BLUE":"Images\Sports Cars\BlueRacecar.png", "GREEN":"Images/Sports Cars/GreenRacecar.png", "PURPLE":"Images\Sports Cars\PurpleRacecar.png"}
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 0.6)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=(540,360))
        self.lives = 0
        self.mass = 600
        self.enginePower = 120
        self.acceleration = (self.enginePower)/(self.mass)
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.angle = 0
        self.rotationSpeed = self.velocity/2
        self.velocity = 0
        self.moving = False

    def update(self):
        global colourList
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 0.6)
        self.rotate()
        self.accelerate()
        self.move()
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.velocity -= self.drag
        self.rotationSpeed = self.velocity/2

#Creates a Truck class that inherits from Vehicle
class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        global colourList
        self.sprites = {"RED":"Images\Trucks\Red Truck.png", "BLUE":"Images\Trucks\Blue Truck.png", "GREEN":"Images\Trucks\Green Truck.png", "PURPLE":"Images\Trucks\Purple Truck.png"}
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 0.6)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=(540,360))
        self.lives = 0
        self.mass = 1500
        self.enginePower = 140
        self.acceleration = (self.enginePower)/(self.mass)
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.angle = 0
        self.rotationSpeed = self.velocity/2
        self.velocity = 0
        self.moving = False

    def update(self):
        global colourList
        self.originalImage = scaleImage(pygame.image.load(self.sprites[colourList.head.data]).convert_alpha(), 0.6)
        self.rotate()
        self.accelerate()
        self.move()
        self.drag = 10*(6 * math.pi * 1.81e-5 * 5 * self.velocity)
        self.velocity -= self.drag
        self.rotationSpeed = self.velocity/2
