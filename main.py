theFlag = True

def on_button_pressed_a():
    global theFlag
    basic.show_icon(IconNames.SQUARE)
    basic.pause(8000)
    if theFlag:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global theFlag
    theFlag = not theFlag
    basic.show_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)
