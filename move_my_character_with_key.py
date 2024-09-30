from pico2d import *
from pygame.examples.scroll import DIR_UP
from pygame.examples.sprite_texture import event

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('standmiku1.png') #가만히 서있는거

def handle_events():
    global running

    global dirRL,dirUD
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
            elif event.key == SDLK_UP:
                dirUD +=1
            elif event.key == SDLK_DOWN:
                dirUD -=1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirRL -=1
            if event.key ==SDLK_LEFT:
                dirRL +=1
            elif event.key == SDLK_UP:
                dirUD -=1
            elif event.key == SDLK_DOWN:
                dirUD +=1


running = True
x = 80
y = 150
frame = 0
dirRL = 0
dirUD = 0

standFrame = 20
runFrame = 8
jmFrame = 9

def standCha(): #가만히 서있을 때 함수
    global frame

    print("stand")
    character = load_image('standmiku1.png')  # 가만히 서있는거
    character.clip_draw(frame * 59, 0, 59, 67, x, y,100,110)
    frame = (frame + 1) % standFrame
    
def runCha(): # 달릴때 함수
    global frame,dirRL

    print("run")
    if(dirRL == 1):
        character = load_image('runRmiku.png')  # 달리는거 오른쪽
        character.clip_draw(frame * 78, 0, 78, 67, x, y, 120, 110)  # 오른쪽
    elif(dirRL== -1):
        character = load_image('runLmiku.png')  # 달리는거 왼쪽
        character.clip_draw(frame * 78, 0, 78, 67, x, y, 120, 110)  # 왼쪽

    frame = (frame + 1) % runFrame

def updownCha():
    global frame,dirUD

    print("위아래")

    if (dirUD == 1):
        character = load_image('jmRmiku.png')
        character.clip_draw(frame * 79, 0, 79, 101, x, y, 120, 140)

    frame = (frame + 1) % jmFrame

while running:
    clear_canvas()
    ground.draw(400,300,800,600)
    
    print("UPDOWN 확인:",dirUD)
    print("RIGHTLEFT 확인:", dirRL)

    # 가만히 서있을 때
    if(dirUD == 0 and dirRL == 0):
        standCha()

    # 달릴 때
    elif (dirRL == 1): # 오른쪽
        runCha()
    elif (dirRL == -1):  # 왼쪽
        runCha()
    # ~~

    # 아래로 갈 때
    elif(dirUD==1):
        updownCha()
    # ~~

    # 위로 갈 때
    elif (dirUD == -1):
        updownCha()
    # ~~

    update_canvas()
    handle_events()

    x += dirRL*15
    y+=dirUD*10
    delay(0.03)

close_canvas()