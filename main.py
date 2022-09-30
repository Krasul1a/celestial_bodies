import pygame as pg
import time
import math

pg.init()

run = True

dis_x = 1280
dis_y = 1280

white = (255, 255, 255)
blu = (0, 0, 255)
black = (0, 0, 0)

dis = pg.display.set_mode((dis_x, dis_y))

mass1 = 500  # star props

mass2 = 3  # planet props

x0 = dis_x / 2
y0 = dis_y / 2

vx = 0.5
vy = 1

x = x0 - 300
y = y0 - 110

timer = pg.time.Clock()

while (run):  # GAMELOOP
    timer.tick(120)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    r = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)

    ax = mass1 * (x0 - x) / r ** 3
    ay = mass1 * (y0 - y) / r ** 3

    # New spped based on accel
    vx += ax
    vy += ay

    # New pos based on speed
    x += vx
    y += vy

    print(vx / 2 + vy / 2)

    pg.draw.circle(dis, white, (x0, y0), 10)  # star
    pg.draw.circle(dis, blu, (x, y), mass2)  # planet

    pg.display.update()
    dis.fill(black)