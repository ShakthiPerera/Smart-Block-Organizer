import random
import pygame as pyg
import pymunk as pmk
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]

class Block:
    def __init__(self, name, x, y, space, window, width=75, height=75, mass=10):
        self.body = None
        self.shape = None

        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window

        self.space = space
        self.color = random.choice(colors)
        self.add_block()

    def add_block(self):
        self.body = pmk.Body()
        self.body.position = (self.x, self.y)
        self.shape = pmk.Poly.create_box(self.body, (self.width, self.height))
        self.shape.mass = self.mass
        self.shape.color = (*self.color,1)
        self.shape.friction = 1
        self.space.add(self.body, self.shape)

    def draw_name(self):
        x, y = int(self.body.position.x), int(self.body.position.y)
        font = pyg.font.SysFont('Comic sans MS', 15)
        text = font.render(self.name,False, (0,0,0))
        self.window.blit(text, (x+5-self.width/4, y-self.height/4))
        pyg.display.update()

