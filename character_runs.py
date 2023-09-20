from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('circle')

    cx , cy ,r = 400,330,240
    for deg in range(0,360,5):
        x = cx + r *math.cos(deg / 360 *2 * math.pi)
        y = cy + r *math.sin(deg / 360 *2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        delay(0.1)
            

def run_rectangle():
    print('rectangle')
    



    
    pass






while True:
    # run_circle()
    run_rectangle()
    # break

close_canvas()
