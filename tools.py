import math
from consts import BAD_TRAP, BUILDINGS, ENEMY_BASE, ENTITIES, EMPTY, COST, GOAL_COST, INF, EMPTIES, NO_ANTS, RESOURCES, SWAMP, UNKNOWN , TRAP, WALL

turn_number = 0
allied_in_range=0
enemy_in_range=0
has_resource = 0
last_resource = (-1,-1)

def set_turn_number(tn):
    global turn_number
    turn_number = tn

def beat(new_object, old_object):
    if old_object == ENEMY_BASE:
        return True
    if old_object == UNKNOWN:
        return True
    if old_object == WALL:
        return False
    if new_object == old_object:
        return True
    if old_object in EMPTIES and new_object in EMPTIES:
        return True
    if old_object in BUILDINGS and new_object in BUILDINGS:
        return True
    if (new_object == NO_ANTS or new_object in ENTITIES) and (old_object == NO_ANTS or old_object in ENTITIES):
        return True
    if (new_object == EMPTY or new_object in RESOURCES) and (old_object == EMPTY or old_object in RESOURCES):
        return True

    return False


def prune(ls):
    ls.sort(key=lambda x: -x[1])
    ret = []
    for ind in range(len(ls)):
        f = True
        for pre in range(ind):
            if beat(ls[pre][0], ls[ind][0]) and ls[pre][1] > ls[ind][1]:
                f = False
                break
        if f:
            ret.append(ls[ind])
    return ret

def calc(w, alpha, t):
    return w * math.exp(alpha * t)

def get_cost(ls, role, offset):
    # offset = 0
    return 1 + sum([cost(*it, role, offset) for it in ls])

def cost(obj, tm, role, offset):
    return COST[role][obj](offset + turn_number - tm)

def get_goal_cost(ls, role):
    return sum([goal_cost(*it, role) for it in ls])

def goal_cost(obj, tm, role):
    return GOAL_COST[role][obj](turn_number - tm)

def has_obj(fobj, ls):
    for obj, tm in ls:
        if obj == fobj:
            return True
    return False

def decode(i, j, obj):
    s = chr(j)
    offset = 0
    if obj == TRAP:
        offset = 50
    if obj == SWAMP:
        offset = 100
    if obj == BAD_TRAP:
        offset = 150
    f = chr(i + offset)
    return f+s

def encode(msg):
    j = ord(msg[1])
    i = ord(msg[0])%50
    obj = WALL
    if ord(msg[0])//50 == 1:
        obj = TRAP
    if ord(msg[0])//50 == 2:
        obj = SWAMP
    if ord(msg[0])//50 == 3:
        obj = BAD_TRAP
    return i, j, obj