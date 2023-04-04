import pygame as pg
import sys

#initial setup
pg.init()
clock = pg.time.Clock()

#window setup
WIDTH = 1280
HEIGHT = 920
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("PyPong")

#drawing rect capsules for collisions
ball = pg.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
player = pg.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
opponent = pg.Rect(10, HEIGHT/2 - 70, 10, 140)

#colour variables
bg_colour = (0, 0, 0)
light_grey = (200, 200, 200)

#main loop; runs once per tick
while True:

    #input checher
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    #visuals
    screen.fill(bg_colour)
    pg.draw.rect(screen, light_grey, player)
    pg.draw.rect(screen, light_grey, opponent)
    pg.draw.ellipse(screen, light_grey, ball)
    pg.draw.aaline(screen, light_grey, (WIDTH/2,0), (WIDTH/2, HEIGHT))

    #update
    pg.display.flip()
    clock.tick(60) #max frames / second