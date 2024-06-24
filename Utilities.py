import pygame
import json

#Function for scaling an image in size by a given scale factor
def scaleImage(image, scaleFactor):
    newSize = round(image.get_width() * scaleFactor), round(image.get_height() * scaleFactor)
    return pygame.transform.scale(image, newSize)

#Function for making an image rotate around the centre rather than the top left corner
def rotateAroundCenter(originalImage, image, rect, angle):
    image = pygame.transform.rotate(originalImage, angle)
    rect = image.get_rect(center=rect.center)

#Node class that can be used in data structures like linked lists and graphs
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
#Linked list class that can be used to store data in a list
class LinkedList():
    def __init__(self):
        self.head = None

#Method to check if the list is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

#Method to add data at the front        
    def insertAtFront(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

#Method to insert new data in order
    def insertInOrder(self, data):
        newNode = Node(data)
        current = self.head
        if self.isEmpty():
            self.head = newNode
        elif newNode.data() < current.data():
            newNode.next = self.head
            self.head = newNode
        else:
            while current.next() != None and current.next().data() < newNode.data():
                current = current.next()
            newNode.next = current.next()
            current.next = newNode

#Method to delete unwanted data
    def delete(self, data):
        if self.isEmpty():
            return
        else:
            current = self.head
            if current.data() == data:
                self.head = current.next()
            else:
                while current.next().data() != data:
                    current = current.next()
                current.next = current.next().next()

#Method to turn the list into a circular linked list
    def loop(self):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = self.head

#Method to rotate cicular list by one element and make the next element the new head
    def rotate(self):
        self.head = self.head.next

#Function to load a JSON file
def readJson(jsonFile):
  with open(jsonFile, "r") as file:
    return json.loads(file.read())

#Procedure to write to a JSON file
def writeJson(jsonFile, data):
  with open(jsonFile,"w") as file:
    file.write(json.dumps(data))