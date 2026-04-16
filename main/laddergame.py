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

    # def start(self):
    #     for led in range(len(self._leds)):
    #         if not self._button.is_pressed:
    #             self._current_led_index = led
    #             pressed_the_button = False
    #             pressed_in_time = False

                
    #             while not pressed_the_button:
    #                 self.__current_led().on()
    #                 sleep(0.6)
                    
    #                 if self._button.is_pressed and pressed_in_time:
    #                     pressed_the_button = True
    #                     pressed_in_time = True
                        
                    
    #                 self.__current_led().off()
    #                 sleep(0.3)

    #                 if self._button.is_pressed:
    #                     pass

#NEED TO MAKE A METHOD TO CHECK IF THE BUTTON WAS PRESSED IN TIME, AND IF NOT, THEN THE GAME IS OVER
        

if __name__ == "__main__":
    game = Laddergame()
    #game.start()
    
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass  # Ctrl+C to exit