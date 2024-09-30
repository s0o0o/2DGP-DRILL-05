from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
standmiku = load_image('standmiku1.png')

def handle_events():
    global running

    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -=1
            if event.key ==SDLK_LEFT:
                dir +=1


running = True
x = 800 // 2
frame = 0
dir =0
# fill here
while running:
    clear_canvas()
    ground.draw(400,0)
    standmiku.clip_draw(frame*77,0,77,67,x,90)
    update_canvas()
    handle_events()
    frame = (frame+1)%8
    x += dir*15
    delay(0.05)

close_canvas()