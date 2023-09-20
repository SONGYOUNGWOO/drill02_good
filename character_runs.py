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
    for deg in range(0,360,5):
        x = cx + r *math.cos(deg / 360 *2 * math.pi)
        y = cy + r *math.sin(deg / 360 *2 * math.pi)
        render_all(x,y)


def run_rectangle():
    print('rectangle')

    # bottom line
    #for x in range(50 , 780 + 1, 10):
        #render_all(x,90)

    # top line
    #for x in range(780 , 50 -1, -10):
        #render_all(x,560)

    # right line
    for y in range(90 , 560 -1, 10):
        render_all(780,y)
        



    
    pass






while True:
    run_rectangle()
    #run_circle()
    # break

close_canvas()
