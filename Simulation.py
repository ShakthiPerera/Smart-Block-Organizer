import pygame as pyg
import pygame.draw
import pymunk as pmk
from block_class import Block
import pymunk.pygame_util

pyg.font.init()

def add_table(space, width=900, height=100):
    body = pmk.Body(body_type=pmk.Body.STATIC)
    body.position = (500,700)
    shape = pmk.Poly.create_box(body, (width, height))
    space.add(body, shape)

def simulation(window, space):
    run = True
    block1 = Block('B1', 150, 600, space, window)
    block2 = Block('B2', 150, 525, space, window)
    add_table(space)
    fps = 60
    dt = 1/fps
    clock = pyg.time.Clock()
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
                break
        draw_background(window, space)
        block1.draw_name()
        block2.draw_name()
        clock.tick(fps)
        space.step(dt)
        pyg.display.update()


def initial_setup(width, height, gravity):
    window = pyg.display.set_mode((width, height))
    space = pmk.Space()
    space.gravity = gravity
    return window, space

def draw_background(window, space):
    window.fill((255, 255, 255))
    draw_options = pmk.pygame_util.DrawOptions(window)
    space.debug_draw(draw_options)

if __name__ == "__main__":
    width, height = 1000, 800
    window, space = initial_setup(width, height, (0, 1000))
    simulation(window, space)
