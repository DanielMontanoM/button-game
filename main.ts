function bluewinreverse () {
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(4, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(6, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(8, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(10, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Blue))
    strip.show()
}
function redwin () {
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(6, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(10, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(3, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(5, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(7, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(9, neopixel.colors(NeoPixelColors.White))
    strip.show()
}
input.onButtonPressed(Button.A, function () {
    ONSTART()
})
function redwinreverse () {
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(4, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(6, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(8, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(10, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(3, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(5, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(7, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(9, neopixel.colors(NeoPixelColors.Red))
    strip.show()
}
input.onPinPressed(TouchPin.P2, function () {
    rope += -1
    strip.rotate(-1)
    strip.show()
    blue.setPixelColor(4, neopixel.colors(NeoPixelColors.Blue))
    blue.show()
})
input.onButtonPressed(Button.AB, function () {
    ONSTART()
})
function bluewin () {
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(6, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(10, neopixel.colors(NeoPixelColors.Blue))
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(3, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(5, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(7, neopixel.colors(NeoPixelColors.White))
    strip.setPixelColor(9, neopixel.colors(NeoPixelColors.White))
    strip.show()
}
input.onButtonPressed(Button.B, function () {
    rope += -1
    strip.rotate(-1)
    strip.show()
    blue.setPixelColor(4, neopixel.colors(NeoPixelColors.Blue))
    blue.show()
})
input.onPinPressed(TouchPin.P1, function () {
    rope += 1
    strip.rotate(1)
    red.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    strip.show()
    red.show()
})
function ONSTART () {
    strip = neopixel.create(DigitalPin.P16, 11, NeoPixelMode.RGB)
    ropelight = strip.range(5, 1)
    red = strip.range(0, 5)
    blue = strip.range(6, 5)
    rope = 5
    red.setBrightness(255)
    blue.setBrightness(255)
    strip.setBrightness(255)
    ropelight.setBrightness(255)
    red.showColor(neopixel.colors(NeoPixelColors.Red))
    ropelight.showColor(neopixel.colors(NeoPixelColors.White))
    blue.showColor(neopixel.colors(NeoPixelColors.Blue))
    strip.show()
}
let ropelight: neopixel.Strip = null
let red: neopixel.Strip = null
let blue: neopixel.Strip = null
let rope = 0
let strip: neopixel.Strip = null
ONSTART()
basic.forever(function () {
    if (rope <= 0) {
        for (let index = 0; index < 4; index++) {
            bluewin()
            basic.pause(100)
            bluewinreverse()
            basic.pause(100)
        }
    } else if (rope >= 10) {
        for (let index = 0; index < 4; index++) {
            redwin()
            basic.pause(100)
            redwinreverse()
            basic.pause(100)
        }
    }
})
