from screen import Screen
import sys
import random
from ship import Ship

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        ship_x = random.randint(self.__screen_min_x, self.__screen_max_x)
        ship_y = random.randint(self.__screen_min_y, self.__screen_max_y)
        self.__ship = Ship(ship_x, ship_y, 0, 0, 0)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        # TODO: Your code goes here
        ship = self.__ship
        Screen.draw_ship(ship.get_x_place(), ship.get_y_place(),
                         ship.get_angle())


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
