from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x, y = 400, 90  # 시작 위치 설정 (화면 아래 가장자리)
r = 240
angle = -90

while True:
        # 오른쪽으로 이동
        while x < 780:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 20
            delay(0.01)   
        # 위로 이동
        while y < 560:  # 화면 위 가장자리까지 이동하도록 설정
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(780, y)
            y += 20
            delay(0.01)
        # 왼쪽으로 이동
        while x > 20:  # 화면 왼쪽 가장자리까지 이동하도록 설정
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 560)
            x -= 20
            delay(0.01)
        # 아래로 이동
        while y > 90:  # 화면 아래 가장자리까지 이동하도록 설정
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(20, y)
            y -= 20
            delay(0.01)
        while x <= 400:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 20
            delay(0.01)
        while angle < 270:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x + r * math.cos(math.radians(angle)), 330 + r * math.sin(math.radians(angle)))
            angle += 5
            delay(0.01)
        angle = -90

