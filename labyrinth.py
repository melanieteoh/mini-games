import play

player = play.new_circle(color = "medium slate blue", x = 0, y = -270, radius = 20, border_color = "black")

wall1 = play.new_box(color = "dark green", x = 0, y = 0, width = 10, height = 100)
wall2 = play.new_box(color = "dark green", x = -50, y = 20, width = 100, height = 10)
wall3 = play.new_box(color = "dark green", x = 250, y = 30, width = 100, height = 10)
wall4 = play.new_box(color = "dark green", x = 50, y = 50, width = 10, height = 100)
wall5 = play.new_box(color = "dark green", x = 300, y = 200, width = 10, height = 100)

finish = play.new_text(words = "FINISH", font = None, font_size = 50, color = "black", x = 0, y = 270)

@play.when_program_starts
def start():
    player.start_physics(bounciness = 2)
    wall1.start_physics(can_move=False)
    wall2.start_physics(can_move=False)
    wall3.start_physics(can_move=False)
    wall4.start_physics(can_move=False)

@play.repeat_forever
def do():
    player.physics.x_speed = 0
    player.physics.y_speed = -10

    if play.key_is_pressed("up"):
        player.physics.y_speed = 20
    if play.key_is_pressed("down"):
        player.physics.y_speed = -20
    if play.key_is_pressed("right"):
        player.physics.x_speed = 20
    if play.key_is_pressed("left"):
        player.physics.x_speed = -20

    if player.is_touching(finish):
        wall1.hide()
        wall2.hide()
        wall3.hide()
        wall4.hide()
        wall5.hide()
        finish.hide()
        play.new_text(words = "VICTORY!", font = None, font_size = 50, color = "black", x = 0, y = 0)

play.start_program()
