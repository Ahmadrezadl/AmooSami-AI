from Model import *
import random
from consts import *
import json
from typing import *
from tools import prune

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

    @classmethod
    def get_instance(cls):
        try:
            return cls.instance
        except:
            cls.instance = AI()
            return cls.instance
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
                    new_line.append([(UNKNOWN, -1)])
                self.vision.append(new_line)

        for i in range(self.game.mapHeight):
            for j in range(self.game.mapWidth):
                cell = self.game.ant.getMapCell(j, i)
                if not cell:
                    continue
                elif cell.type == CellType.WALL.value:
                    self.vision[i][j].append((WALL, self.turn_number))
                elif cell.type == CellType.BASE.value and (base_x != j or base_y != i):
                    self.vision[i][j].append((ENEMY_BASE, self.turn_number))
                elif cell.resource_type == ResourceType.BREAD.value:
                    self.vision[i][j].append((BREAD, self.turn_number))
                elif cell.resource_type == ResourceType.GRASS.value:
                    self.vision[i][j].append((GRASS, self.turn_number))
                elif cell.ants:
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
                    self.vision[i][j].append((maximum, self.turn_number))
                else:
                    self.vision[i][j].append((EMPTY, self.turn_number))

                prune(self.vision[i][j])


        print("turn: ", self.turn_number)
        for row in self.vision:
            for cell in row:
                print(cell[0][0], end=' ')
            print()
        if ant.antType == AntType.SARBAAZ.value:
            direction = random.randint(0, 4)
        elif ant.antType == AntType.KARGAR.value:
            direction = random.randint(0, 4)

        # for i in self.vision:
            # print(i)
        # print(message, message_value, direction)
        return message, message_value, direction
