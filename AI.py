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
            print("Creating vision")
            for i in range(self.game.mapHeight):
                new_line = []
                for j in range(self.game.mapWidth):
                    new_line.append((UNKNOWN, -1))
                self.vision.append(new_line)

        for i in range(self.game.mapHeight):
            for j in range(self.game.mapWidth):
                cell = self.game.ant.getMapCell(j, i)
                if not cell:
                    continue
                elif cell.type == CellType.WALL.value:
                    self.vision[i][j] = (WALL, self.turn_number)
                elif cell.type == CellType.BASE.value:
                    self.vision[i][j] = (ENEMY_BASE, self.turn_number)
                elif cell.resource_type is not None:
                    if cell.resource_type == ResourceType.BREAD.value:
                        self.vision[i][j] = (BREAD, self.turn_number)
                    else:
                        self.vision[i][j] = (GRASS, self.turn_number)
                elif not cell.ants:
                    self.vision[i][j] = (EMPTY, self.turn_number)
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

                    self.vision[i][j] = (maximum, self.turn_number)


        if ant.antType == AntType.SARBAAZ.value:
            direction = random.randint(0, 4)
        elif ant.antType == AntType.KARGAR.value:
            pass

        for i in self.vision:
            print(i)
        return message, message_value, direction
