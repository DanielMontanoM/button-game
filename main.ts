function light_logic () {
    let j: number;
if (rope == 5) {
        for (let i = 0; i <= 3; i++) {
            red.setPixelColor(i, neopixel.colors(NeoPixelColors.Red))
            red.show()
        }
        j = 6
        while (j < 11) {
            blue.setPixelColor(j, neopixel.colors(NeoPixelColors.Blue))
            blue.show()
            j += 1
        }
    }
}
input.onPinPressed(TouchPin.P2, function () {
    rope += -0.1
})
input.onButtonPressed(Button.AB, function () {
    a_line += 0.1
    b_line += -0.1
})
input.onPinPressed(TouchPin.P1, function () {
    rope += 0.1
})
let b_line = 0
let a_line = 0
let rope = 0
let blue: neopixel.Strip = null
let red: neopixel.Strip = null
let strip = neopixel.create(DigitalPin.P16, 11, NeoPixelMode.RGB)
let ropelight = strip.range(0, 11)
red = strip.range(0, 11)
blue = strip.range(0, 11)
rope = 5
ropelight.setPixelColor(5, neopixel.colors(NeoPixelColors.White))
red.setPixelColor(4, neopixel.colors(NeoPixelColors.Red))
blue.setPixelColor(6, neopixel.colors(NeoPixelColors.Blue))
ropelight.show()
blue.show()
red.show()
basic.forever(function () {
    light_logic()
})
loops.everyInterval(5000, function () {
	
})
