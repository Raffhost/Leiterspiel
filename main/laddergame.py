from time import sleep, time
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
        print("Starte Leiterspiel")
        time_last_change = time()
        running = True

        while running == True:
            if self._button.is_pressed:
                if self._current_led_is_on():
                    self._next_level
                    if self._current_led_index == len(self._leds):
                        print("Gewonnen")
                        running = False
                    sleep(self.__debounce_ms/1000) # Debounce
                    print("Next level:", self._current_led_index)
                else:
                    print("Verloren")
                    running = False

            if time() - time_last_change > self._blink_time_s:
                self._flip_current_led()
                time_last_change = time()

        print("Spiel beendet.")




if __name__ == "__main__":
    game = Laddergame()
    game.start()
    
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass  # Ctrl+C to exit