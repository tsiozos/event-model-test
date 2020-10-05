let theFlag = true
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showIcon(IconNames.Square)
    basic.pause(8000)
    if (theFlag) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    theFlag = !theFlag
    basic.showNumber(0)
})
