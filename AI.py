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
        self.turn_number: int = -1
        self.vision = []

    """
    Return a tuple with this form:
        (message: str, message_value: int, message_dirction: int)
    check example
    """

    def turn(self) -> (str, int, int):
        print(self.game.mapWidth)
        print(self.game.mapHeight)
        print(self.game.ant.currentX)
        print(self.game.ant.currentY)
        # Fill these fields to return
        message: str = None
        message_value: int = 0
        direction: int = Direction.CENTER.value

        ant = self.game.ant
        x = ant.currentX
        y = ant.currentY
        base_x = self.game.baseX
        base_y = self.game.baseX
        self.turn_number = self.turn_number + 1

        if not self.vision:
            for i in range(self.game.mapHeight):
                new_line = []
                for j in range(self.game.mapWidth):
                    if base_x == j and base_y == i:
                        new_line.append((BASE, self.turn_number))
                    else:
                        cell = self.game.ant.visibleMap.cells[i][j]
                        if not cell:
                            new_line.append((UNKNOWN, self.turn_number))
                        elif cell.type == CellType.WALL.value:
                            new_line.append((WALL, self.turn_number))
                        elif cell.type == CellType.BASE.value:
                            new_line.append((ENEMY_BASE, self.turn_number))
                        elif cell.resource_type != 0:
                            if cell.resource_type == ResourceType.BREAD.value:
                                new_line.append((BREAD, self.turn_number))
                            else:
                                new_line.append((GRASS, self.turn_number))
                        elif not cell.ants:
                            new_line.append((EMPTY, self.turn_number))
                        else:
                            maximum = TEAM_KARGAR
                            for a in cell.ants:
                                if a.antType == AntType.KARGAR.value and a.antTeam == AntTeam.ALLIED.value:
                                    this = TEAM_KARGAR
                                elif a.antType == AntType.SARBAAZ.value and a.antTeam == AntTeam.ALLIED.value:
                                    this = TEAM_SARBAZ
                                elif a.antType == AntType.KARGAR.value and a.antTeam == AntTeam.ENEMY.value:
                                    this = ENEMY_KARGAR
                                else:
                                    this = ENEMY_SARBAZ

                                if this > maximum:
                                    maximum = this

                            new_line.append((maximum, self.turn_number))

                self.vision.append(new_line)

        if ant.antType == AntType.SARBAAZ.value:
            direction = random.randint(0, 4)
        elif ant.antType == AntType.KARGAR.value:
            pass

        print(self.vision)
        return message, message_value, direction
