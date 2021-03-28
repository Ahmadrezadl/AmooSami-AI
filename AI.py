from Model import *
import random
import json
from typing import *


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
        ant = self.game.ant
        x = ant.currentX
        y = ant.currentY

        if ant.antType == AntType.SARBAAZ:
            self.message = "Sarbazam =)"
        elif ant.antType == AntType.KARGAR:
            self.message = "kargaram =)"

        # Move where
        rand = random.randint(1, 4)
        if rand == 1:
            self.direction = Direction.UP.value
        if rand == 2:
            self.direction = Direction.DOWN.value
        if rand == 3:
            self.direction = Direction.LEFT.value
        if rand == 4:
            self.direction = Direction.RIGHT.value

        return self.message, self.value, self.direction
