def light_logic():
    if rope == 5:
        for i in range(4):
            red.set_pixel_color(i, neopixel.colors(NeoPixelColors.RED))
            red.show()
        j = 6
        while j < 11:
            blue.set_pixel_color(j, neopixel.colors(NeoPixelColors.BLUE))
            blue.show()
            j += 1

def on_pin_pressed_p2():
    global rope
    rope += -0.1
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global a_line, b_line
    a_line += 0.1
    b_line += -0.1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_pin_pressed_p1():
    global rope
    rope += 0.1
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

b_line = 0
a_line = 0
rope = 0
blue: neopixel.Strip = None
red: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P16, 11, NeoPixelMode.RGB)
ropelight = strip.range(0, 11)
red = strip.range(0, 11)
blue = strip.range(0, 11)
rope = 5
ropelight.set_pixel_color(5, neopixel.colors(NeoPixelColors.WHITE))
red.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
blue.set_pixel_color(6, neopixel.colors(NeoPixelColors.BLUE))
ropelight.show()
blue.show()
red.show()

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    light_logic()
loops.every_interval(5000, on_every_interval)
