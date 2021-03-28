from Model import *
import random
import json
from typing import *

CENTER = Direction.CENTER.value
LEFT = Direction.LEFT.value
RIGHT = Direction.RIGHT.value
UP = Direction.UP.value
DOWN = Direction.DOWN.value


class AI:
    def __init__(self):
        # Current Game State
        self.game: Game = None

        # Answer
        self.message: str = None
        self.direction: int = None
        self.value: int = None

    """
    Return a tuple with this form:
        (message: str, message_value: int, message_dirction: int)
    check example
    """

    def turn(self) -> (str, int, int):
        # Fill these fields to return
        message: str = None
        message_value: int = 0
        direction: int = Direction.CENTER.value

        ant = self.game.ant
        x = ant.currentX
        y = ant.currentY
        baseX = self.game.baseX
        baseY = self.game.baseX

        # Sarbaaz
        if ant.antType == 0:
            direction = random.randint(0, 4)
        # Karegar
        elif ant.antType == 1:
            pass

        # Just for test:
        # Move random
        # direction = random.randint(0, 4)

        return message, message_value, direction
