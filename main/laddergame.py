from time import sleep
from gpiozero import LED, Button
from config import LED_PINS, BUTTON_PIN

class Laddergame:
    def __init__(self, led_pins=LED_PINS, button_pin=BUTTON_PIN):
        self._current_led_index = 0
        self._leds = [LED(pin) for pin in led_pins]
        self._button = Button(button_pin)
        self.__debounce_ms = 200
        self._blink_time_s = 1

    def __current_led(self):
        return self._leds[self._current_led_index]

    def _next_level(self):
        self._current_led_index += 1

    def _current_led_is_on(self):
        return self.__current_led().value

    def _flip_current_led(self):
        if self._current_led_is_on():
            self.__current_led().off()
        else:
            self.__current_led().on()

    def start(self):
        for led in range(len(self._leds)):
            self._current_led_index = led
            # Мигание дважды: ON-OFF-ON-OFF с паузой между
            for blink in range(3):
                self.__current_led().on()
                sleep(0.1)
                self.__current_led().off()
                sleep(0.2)

                if blink == 0:
                    sleep(0.5)
            
            self.__current_led().on()


if __name__ == "__main__":
    game = Laddergame()
    game.start()