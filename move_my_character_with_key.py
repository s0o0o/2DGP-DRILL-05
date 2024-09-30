from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('standmiku1.png') #가만히 서있는거

def handle_events():
    global running

    global dirRL
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirRL += 1
            elif event.key == SDLK_LEFT:
                dirRL -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirRL -=1
            if event.key ==SDLK_LEFT:
                dirRL +=1


running = True
x = 800 // 2
frame = 0
dirRL =0

standFrame = 20
runFrame = 8

def standCha(): #가만히 서있을 때 함수
    global frame

    print("stand")
    character = load_image('standmiku1.png')  # 가만히 서있는거
    character.clip_draw(frame * 59, 0, 59, 67, x, 90)
    frame = (frame + 1) % standFrame

while running:
    clear_canvas()
    ground.draw(400,300,800,600)

    standCha()
    # 가만히 서있을 때
    # ~~

    # 달릴 때
    # ~~

    # 아래로 갈 때
    # ~~

    # 위로 갈 때
    # ~~

    update_canvas()
    handle_events()

    x += dirRL*15
    delay(0.05)

close_canvas()