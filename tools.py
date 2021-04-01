from consts import BUILDINGS, ENTITIES, EMPTY, RESOURCES


def beat(ob_f, ob_s):
    if ob_s in BUILDINGS:
        return False
    if ob_f in ENTITIES and ob_s in ENTITIES:
        return True
    if ob_f == EMPTY and ob_s in RESOURCES:
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
