from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        delay(0.1)

        
def run_circle():
    print('circle')

    cx , cy ,r = 400,330,240
    for deg in range(-90,270,10):
        x = cx + r *math.cos(deg / 360 *2 * math.pi)
        y = cy + r *math.sin(deg / 360 *2 * math.pi)
        render_all(x,y)


def run_rectangle():
    print('rectangle')

    # bottom line
    for x in range(400 , 780 + 1, 20):
        render_all(x,90)
        
    # right line
    for y in range(90 , 560 +1, 20):
        render_all(780,y)

    # top line
    for x in range(780 , 50 -1, -20):
        render_all(x,560)
        
    #left line
    for y in range(560, 90 - 1, -20):
        render_all(20,y)
        
    # bottom line2
    for x in range(50 ,400+ 1, 20):
        render_all(x,90)


while True:
    run_rectangle()
    run_circle()
    # break

close_canvas()
