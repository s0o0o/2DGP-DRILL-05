from pico2d import *
from pygame.examples.scroll import DIR_UP
from pygame.examples.sprite_texture import event

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('standmiku1.png') #가만히 서있는거 기본

Right = True
Left = False

def handle_events():
    global running,Right,Left

    global dirRL,dirUD
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirRL = 1
                Right = True
                Left = False
            elif event.key == SDLK_LEFT:
                dirRL = -1
                Left = True
                Right = False
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dirUD =1
            elif event.key == SDLK_DOWN:
                dirUD =-1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirRL =0
            if event.key ==SDLK_LEFT:
                dirRL =0
            elif event.key == SDLK_UP:
                dirUD =0
            elif event.key == SDLK_DOWN:
                dirUD =0
            frame = 0


running = True

x = 180
y = 500
frame = 0
dirRL = 0
dirUD = 0

tempWidth = 0

standFrame = 20
runFrame = 8
jmFrame = 9
downFrame = 8

def standCha(): #가만히 서있을 때 함수
    global frame, Right, Left

    if(Right):
        print("right였음")
        character = load_image('standmiku1.png')  # 가만히 서있는거 오른쪽
        character.clip_draw(frame * 59, 0, 59, 67, x, y,100,110)
    elif(Left):
        print("left였음")
        character = load_image('standLmiku1.png')  # 가만히 서있는거 왼쪽
        character.clip_draw(frame * 59, 0, 59, 67, x, y, 100, 110)
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
    global frame,dirUD,Right,Left,tempWidth

    print("위아래")
    if (dirUD == 1):
        if(Right):
            character = load_image('jmRmiku.png')
            character.clip_draw(frame * 78, 0, 78, 101, x, y, 125, 145)
        elif(Left):
            character = load_image('jmLmiku.png')
            if (frame > 5): # frame 5 부터는 그림 가로 길이가 조금 더 짧아져서 프레임에 맞게...
                tempWidth = -4
            else:
                tempWidth = 0
            character.clip_draw((frame * 82)+tempWidth, 0, 82 + tempWidth, 101, x, y, 125, 145)
        frame = (frame + 1) % jmFrame

    elif(dirUD== -1):
        if(Right):
            print(frame, tempWidth)
            character = load_image('downRMiku.png')
            if(frame > 2):
                tempWidth = 3 # frame 3부터는 그림 가로 길이가 조금 더 길어져서 프레임에 맞게...
            else: tempWidth = 0
            character.clip_draw((frame * 84) + tempWidth, 0, 84 + tempWidth, 67, x, y, 124, 105)
        if(Left):
            character = load_image('downLMiku.png')
            if (frame > 2):
                tempWidth = 6  # frame 2부터는 그림 가로 길이가 조금 더 길어져서 프레임에 맞게...
            else:
                tempWidth = 0
            character.clip_draw((frame * 79) + tempWidth, 0, 79 + tempWidth, 67, x, y, 125, 105)

        frame = (frame + 1) % downFrame


while running:
    clear_canvas()
    ground.draw(400,300,800,600)

    # 가만히 서있을 때
    if(dirUD == 0 and dirRL == 0):
        standCha()
    # 달릴 때
    elif (dirRL == 1): # 오른쪽
        runCha()
    elif (dirRL == -1):  # 왼쪽
        runCha()
    # 아래로 갈 때
    elif(dirUD==1):
        updownCha()
    # 위로 갈 때
    elif (dirUD == -1):
        updownCha()

    update_canvas()
    handle_events()

    x += dirRL*15
    y += dirUD*8
    if(x > 780 or x < 0 or y > 650 or y< 0):
        running = False
    delay(0.05)

close_canvas()