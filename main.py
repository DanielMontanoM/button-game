def bluewinreverse():
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.BLUE))
    strip.show()
def redwinreverse():
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.RED))
def redwin():
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.WHITE))

def on_button_pressed_a():
    global rope
    rope += 1
    strip.rotate(1)
    strip.show()
    red.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    red.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global rope
    rope += -1
    strip.rotate(1)
    strip.show()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global a_line, b_line
    a_line += 0.1
    b_line += -0.1
    strip.rotate(1)
    strip.rotate(-1)
    strip.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def bluewin():
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(10, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.WHITE))
    strip.set_pixel_color(9, neopixel.colors(NeoPixelColors.WHITE))
    strip.show()

def on_button_pressed_b():
    global rope
    rope += -1
    strip.rotate(-1)
    strip.show()
    blue.set_pixel_color(4, neopixel.colors(NeoPixelColors.BLUE))
    blue.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global rope
    rope += 1
    strip.rotate(-1)
    strip.show()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def ONSTART():
    global strip, ropelight, red, blue, rope
    strip = neopixel.create(DigitalPin.P16, 11, NeoPixelMode.RGB)
    ropelight = strip.range(5, 1)
    red = strip.range(0, 5)
    blue = strip.range(6, 5)
    rope = 5
    red.set_brightness(10)
    blue.set_brightness(10)
    strip.set_brightness(10)
    ropelight.set_brightness(10)
    red.show_color(neopixel.colors(NeoPixelColors.RED))
    ropelight.show_color(neopixel.colors(NeoPixelColors.WHITE))
    blue.show_color(neopixel.colors(NeoPixelColors.BLUE))
    strip.show()
ropelight: neopixel.Strip = None
blue: neopixel.Strip = None
b_line = 0
a_line = 0
red: neopixel.Strip = None
rope = 0
strip: neopixel.Strip = None
ONSTART()

def on_forever():
    basic.show_number(rope)
    if rope <= 0:
        for index in range(4):
            bluewin()
            basic.pause(100)
            bluewinreverse()
            basic.pause(100)
    elif rope >= 10:
        for index2 in range(4):
            bluewin()
            basic.pause(100)
            bluewinreverse()
            basic.pause(100)
basic.forever(on_forever)
