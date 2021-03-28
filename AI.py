from Model import *
import random
from consts import *
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
        self.turn: int = -1
        self.vision = []

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
        base_x = self.game.baseX
        base_y = self.game.baseX
        self.turn = self.turn + 1

        if not self.vision:
            for i in range(self.game.mapHeight):
                new_line = []
                for j in range(self.game.mapWidth):
                    if base_x == j and base_y == i:
                        new_line.append((BASE, self.turn))
                    else:
                        cell = self.game.ant.getMapCell(j, i)
                        if not cell:
                            new_line.append((UNKNOWN, self.turn))
                        elif cell.type == CellType.WALL.value:
                            new_line.append((WALL, self.turn))
                        elif cell.type == CellType.BASE.value:
                            new_line.append((ENEMY_BASE, self.turn))
                        elif cell.resource_value != 0:
                            if cell.resource_type == ResourceType.BREAD.value:
                                new_line.append((BREAD, self.turn))
                            else:
                                new_line.append((GRASS, self.turn))
                        elif not cell.ants:
                            new_line.append((EMPTY, self.turn))
                        else:
                            maximum = TEAM_KARGAR
                            for a in cell.ants:
                                if a.antType == AntType.KARGAR and a.antTeam == AntTeam.ALLIED:
                                    this = TEAM_KARGAR
                                elif a.antType == AntType.SARBAAZ and a.antTeam == AntTeam.ALLIED:
                                    this = TEAM_SARBAZ
                                elif a.antType == AntType.KARGAR and a.antTeam == AntTeam.ENEMY:
                                    this = ENEMY_KARGAR
                                else:
                                    this = ENEMY_SARBAZ

                                if this > maximum:
                                    maximum = this

                            new_line.append((maximum, self.turn))

                self.vision.append(new_line)

        if ant.antType == AntType.SARBAAZ.value:
            direction = random.randint(0, 4)
        elif ant.antType == AntType.KARGAR.value:
            pass

        return message, message_value, direction
