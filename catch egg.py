import play
import time
from random import randint

import play
import time
import pygame
from random import randint

#pygame.mixer_music.load('hello.mp3')
#pygame.mixer_music.play()
play.set_backdrop("sky blue")
def cloud():
    cloud = play.new_circle(color=(197, 139, 231), size = 50, x = -180, y = 180)
    cloud1 = play.new_circle(color=(197, 139, 231), size = 50, x = -120, y = 165)
    cloud2 = play.new_circle(color=(197, 139, 231), size = 50, x = -80, y = 155)
    cloud3 = play.new_circle(color=(197, 139, 231), size = 50, x = -35, y = 130)
    cloud4 = play.new_circle(color=(197, 139, 231), size = 50, x = 0, y = 115)
    cloud5 = play.new_circle(color=(197, 139, 231), size = 50, x = -255, y = 155)
    cloud6 = play.new_circle(color=(197, 139, 231), size = 50, x = -310, y = 130)
    cloud7 = play.new_circle(color=(197, 139, 231), size = 50, x = -360, y = 95)
    cloud8 = play.new_circle(color=(197, 139, 231), size = 50, x = -310, y = 65)
    cloud9 = play.new_circle(color=(197, 139, 231), size = 50, x = -250, y = 55)
    cloud10 = play.new_circle(color=(197, 139, 231), size = 50, x = -165, y = 65)
    cloud11 = play.new_circle(color=(197, 139, 231), size = 50, x = -115, y = 55)
    cloud12 = play.new_circle(color=(197, 139, 231), size = 50, x = -75, y = 65)
    cloud13 = play.new_circle(color=(197, 139, 231), size = 50, x = -160, y = 85)
    cloud14 = play.new_circle(color=(197, 139, 231), size = 50, x = -185, y = 85)
    cloud15 = play.new_circle(color=(197, 139, 231), size = 50, x = -140, y = 85)
    cloud16 = play.new_circle(color=(197, 139, 231), size = 50, x = -195, y = 85)
    cloud17 = play.new_circle(color=(197, 139, 231), size = 75, x = -210, y = 85)

cloud()

def cloud():
    cloud18 = play.new_circle(color=(255,255,51), size = 50, x = 180, y = -180)
    cloud19 = play.new_circle(color=(255,255,51), size = 50, x = 120, y = -165)
    cloud20 = play.new_circle(color=(255,255,51), size = 50, x = 80, y = -155)
    cloud21 = play.new_circle(color=(255,255,51), size = 50, x = 35, y = -130)
    cloud22 = play.new_circle(color=(255,255,51), size = 50, x = 0, y = -115)
    cloud23 = play.new_circle(color=(255,255,51), size = 50, x = 255, y = -155)
    cloud24 = play.new_circle(color=(255,255,51), size = 50, x = 310, y = -130)
    cloud25 = play.new_circle(color=(255,255,51), size = 50, x = 360, y = -95)
    cloud26 = play.new_circle(color=(255,255,51), size = 50, x = 310, y = -65)
    cloud27 = play.new_circle(color=(255,255,51), size = 50, x = 250, y = -55)
    cloud28 = play.new_circle(color=(255,255,51), size = 50, x = 165, y = -65)
    cloud29 = play.new_circle(color=(255,255,51), size = 50, x = 115, y = -55)
    cloud30 = play.new_circle(color=(255,255,51), size = 50, x = 75, y = -65)
    cloud31 = play.new_circle(color=(255,255,51), size = 50, x = 160, y = -85)
    cloud34 = play.new_circle(color=(255,255,51), size = 50, x = 185, y = -85)
    cloud35 = play.new_circle(color=(255,255,51), size = 50, x = 140, y = -85)
    cloud36 = play.new_circle(color=(255,255,51), size = 50, x = 195, y = -85)
    cloud37 = play.new_circle(color=(255,255,51), size = 75, x = 210, y = -85)

cloud()

hello_txt=play.new_text(words='CATCH 10 EGGS!', x=0, y=play.screen.height/2-30, color=(254, 1, 154))

egg = play.new_circle(color=(224,231,34), x = 0, y=180, radius= 30)

eggs_amount=play.new_text(words='0', x=300, y=play.screen.height/2-30, color='yellow')
eggs = [egg]

backet=play.new_image(image='basket.png', x=0, y=-play.screen.height/2+50, size=20)
#backet=play.new_image(image='archi.png', x=0, y=-play.screen.height/2+80, size=80)
frames = 48 
old_time = 0

@play.when_program_starts
def start():
    backet.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=10
    )

@play.repeat_forever
async def game():
    if play.key_is_pressed("right"):
        backet.physics.x_speed=50
    elif play.key_is_pressed("left"):
        backet.physics.x_speed=-50
    else:
        backet.physics.x_speed=0

    for egg in eggs:
        egg.y -= 5

        if egg.y < -500:
            backet.hide()
            egg.hide()
            eggs_amount.hide()
            hello_txt.hide()
            lose = play.new_text(words = "gAmE oVER", color = "red", font_size = 100)

            await play.timer(1)
            quit()

        if egg.is_touching(backet):
            eggs.remove(egg)
            egg.hide()
            eggs_amount.words = str(int(eggs_amount.words) + 1)

            egg = play.new_circle(color = (224,231,34), x = randint(-play.screen.width/2, play.screen.width/2), y = 150, radius = 30)
            eggs.append(egg)

        if int(eggs_amount.words) == 10:
            backet.hide()
            egg.hide()
            eggs_amount.hide()
            hello_txt.hide()
            win = play.new_text(words = "YAY YOU WON THE VICTORY EGG", color = (224,231,34), font_size = 50, x = 0, y = 65)
            egg1 = play.new_circle(color = (224,231,34), radius = 50, x = 0, y = 0)

            await play.timer(1)
            quit()

play.start_program()


'''

frames = 48  

# GLOBAL VARIABLES
score = 0 # the game score
finish = False # end game flag
old_time = 0 # time counter for starting a new egg

hello_txt = play.new_text(words='Catch them all!', x=0, y=play.screen.height/2-30)
hello_txt.color = (120, 120, 120) # gray, similar to the official Python
score_txt = play.new_text(words='0', x=play.screen.width/2-80, y=play.screen.height/2-30, color='gold') # points on the screen
help_txt = play.new_text(words="Use 'q', 'a', 'e', 'd' keys", x=0, y=-play.screen.height/2+30)

bunny = play.new_image(image='easter-bunny-1.png', x=0, y=20) # bunny
bowl = play.new_image(image='bowl.png', x=100,  y=80, size=40) #bowl

# in total there are 4 possible locations for a new egg
egg_x = [400, -380] 
egg_y = [200, 50]
eggs = [] # list of available eggs

def add_shelf(x, y, a): # creating shelves
    shelf = play.new_box(x=x, y=y, width=300, height=10, angle=a)
    shelf.color = (48, 105, 152)
    shelf.start_physics(can_move=False, mass=10, friction=1.0)

def new_egg():
    # a function that creates one egg and adds it to the eggs list
    pass

@play.when_program_starts
def start():
    global old_time
    old_time = time.time()

    add_shelf(300, 150, 20)
    add_shelf(300, 0, 20)
    add_shelf(-300, 150, -20)
    add_shelf(-300, 0, -20)
    new_egg()

@play.repeat_forever
def game():
    pass

play.start_program()

'''
