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
            pass
        elif ant.antType == AntType.KARGAR:
            pass

        # Move where
        self.direction = Direction.UP.value

        # Send Message
        self.message = "Daram Mimiram =)"
        self.value = 1

        return self.message, self.value, self.direction
