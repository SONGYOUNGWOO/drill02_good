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
    for x in range(50 , 780,20):
        render_all(x,90)

    #for x in range(750 , 50, -20):
        #render_all(x,90)
         
        



    
    pass






while True:
    run_rectangle()
    run_circle()
    # break

close_canvas()
