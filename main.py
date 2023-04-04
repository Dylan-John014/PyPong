import pygame as pg
import sys, random

def ball_animation():

    global ball_speed_x, ball_speed_y

    #movement + collisions
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():

    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponent_animation():

    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

def ball_restart():

    global ball_speed_x,ball_speed_y

    ball.center = (WIDTH/2, HEIGHT/2)
    ball_speed_y *= random.choice((+1, -1))
    ball_speed_x *= random.choice((+1, -1))

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

#speeeeeeeeeeeeeeeed
ball_speed_x = 3 * random.choice((+1, -1))
ball_speed_y = 3 * random.choice((+1, -1))
player_speed = 0
opponent_speed = 7

#main loop; runs once per tick
while True:

    #input checher
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                player_speed += 5
            if event.key == pg.K_UP:
                player_speed -= 5
        if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                player_speed -= 5
            if event.key == pg.K_UP:
                player_speed += 5
            

    ball_animation()
    player_animation()
    opponent_animation()

    #visuals
    screen.fill(bg_colour)
    pg.draw.rect(screen, light_grey, player)
    pg.draw.rect(screen, light_grey, opponent)
    pg.draw.ellipse(screen, light_grey, ball)
    pg.draw.aaline(screen, light_grey, (WIDTH/2,0), (WIDTH/2, HEIGHT))

    #update
    pg.display.flip()
    clock.tick(144) #max frames / second