from tools import get_cost, get_goal_cost, goal_cost, prune, set_turn_number
from Model import *
from consts import *
from typing import *
import random
import heapq

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
            for i in range(self.game.mapWidth):
                new_line = []
                for j in range(self.game.mapHeight):
                    new_line.append([(UNKNOWN, -1)])
                self.vision.append(new_line)

        for i in range(self.game.mapWidth):
            for j in range(self.game.mapHeight):
                cell = self.game.ant.visibleMap.cells[i][j]
                if not cell:
                    continue
                if cell.type == CellType.WALL.value:
                    self.vision[i][j].append((WALL, self.turn_number))
                elif cell.type != CellType.EMPTY.value and (base_x != i or base_y != j): # what
                    self.vision[i][j].append((ENEMY_BASE, self.turn_number))
                if cell.resource_type == ResourceType.BREAD.value:
                    self.vision[i][j].append((BREAD, self.turn_number))
                elif cell.resource_type == ResourceType.GRASS.value:
                    self.vision[i][j].append((GRASS, self.turn_number))
                else:
                    self.vision[i][j].append((EMPTY, self.turn_number))
                if cell.ants:
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
                    self.vision[i][j].append((NO_ANTS, self.turn_number))

                self.vision[i][j] = prune(self.vision[i][j])

        print("turn: ", self.turn_number)
        set_turn_number(self.turn_number)
        if ant.antType == AntType.SARBAAZ.value:
            direction = random.randint(0, 4)
        elif ant.antType == AntType.KARGAR.value:
            direction = self.do_ant()

        return message, message_value, direction
    
    def do_ant(self):
        # TODO apply sarbaz and enemy's base range
        ant = self.game.ant
        x, y = ant.currentX, ant.currentY
        par = {}
        dis = {}
        dirs = {
            (1, 0): RIGHT,
            (-1, 0): LEFT,
            (0, 1): DOWN,
            (0, -1): UP
        }
        N = self.game.mapWidth
        M = self.game.mapHeight
        dir_funcs = []
        for (dx, dy) in dirs:
            def g(dx, dy):
                def f(p):
                    return ((p[0] + dx + N)%N, (p[1] + dy + M)%M)
                return f
            dir_funcs.append(g(dx, dy))
        for i in range(N):
            for j in range(M):
                if i == x and j == y:
                    print("#", end=' ')
                print(self.vision[i][j][0][0], end=' ')
            print()

        def dij():
            seen = {}
            ls = []
            root = (x, y)
            dis[root] = get_cost(self.vision[x][y])
            par[root] = (-1, -1)
            heapq.heappush(ls, (dis[root], root))
            while ls:
                cdis, cur = heapq.heappop(ls)
                if cur in seen:
                    continue
                seen[cur] = True

                for df in dir_funcs:
                    npos = df(cur)
                    nx, ny = npos
                    ccst = get_cost(self.vision[nx][ny])
                    if npos not in dis or dis[npos] > cdis + ccst:
                        dis[npos] = min(INF, cdis + ccst)
                        par[npos] = cur
                        heapq.heappush(ls, (dis[npos], npos))
        dij()

        def get_goal():
            if ant.currentResource and ant.currentResource.value > 0:
                return self.game.baseX, self.game.baseY
            ret = (-1, -1)
            mx = -INF
            for i in range(N):
                for j in range(M):
                    ccst = get_goal_cost(self.vision[i][j])
                    if mx < ccst:
                        mx = ccst
                        ret = (i, j)
            return ret
        
        gx, gy = get_goal()
        print("goal is: ", gx, gy)
        print("goal vision: ", self.vision[gx][gy])
        print("goal cost:", get_goal_cost(self.vision[gx][gy]))
        if (x, y) == (gx, gy):
            return None
        
        print(gx, gy)
        it = (gx, gy)
        while par[it] != (x, y):
            print(it)
            it = par[it]
        
        return dirs[(it[0] - x, it[1] - y)]