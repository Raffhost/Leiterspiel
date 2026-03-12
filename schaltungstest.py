from gpiozero import Button, LED
from signal import pause
from time import sleep

# LEDs
led_pins = [17, 27, 22, 23, 24, 25, 5, 6]
leds = [LED(pin) for pin in led_pins]

# Button
button = Button(26)

def all_leds_on():
    print("Button pressed!")
    for led in leds:
        led.on()
    sleep(1)
    for led in leds:
        led.off()

button.when_pressed = all_leds_on

pause()