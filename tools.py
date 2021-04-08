import math
from consts import BUILDINGS, ENEMY_BASE, ENTITIES, EMPTY, COST, GOAL_COST, INF, EMPTIES, NO_ANTS, RESOURCES, UNKNOWN

turn_number = 0

def set_turn_number(tn):
    global turn_number
    turn_number = tn

def beat(new_object, old_object):
    if old_object == UNKNOWN:
        return True
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

def get_cost(ls):
    return 1 + sum([cost(*it) for it in ls])

def cost(obj, tm):
    w, alpha = COST[obj]
    return calc(w, alpha, turn_number - tm)

def get_goal_cost(ls):
    return sum([goal_cost(*it) for it in ls])

def goal_cost(obj, tm):
    return GOAL_COST[obj](turn_number - tm)