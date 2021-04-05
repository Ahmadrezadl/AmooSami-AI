from consts import BUILDINGS, ENTITIES, EMPTY, RESOURCES, EMPTIES


def beat(new_object, old_object):
    if old_object in EMPTIES and new_object in EMPTIES:
        return True
    if old_object in BUILDINGS and new_object in BUILDINGS:
        return True
    if new_object in ENTITIES and old_object in ENTITIES:
        return True
    if (new_object == EMPTY or new_object == RESOURCES) and old_object in RESOURCES:
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
