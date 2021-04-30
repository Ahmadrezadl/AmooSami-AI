import math

#cell types
import tools

TRAP = -2
SWAMP = -3
BAD_TRAP = -4

UNKNOWN = -1
WALL = 0
EMPTY = 1
NO_ANTS = 2
ENEMY_BASE = 3
BREAD = 4
GRASS = 5
TEAM_KARGAR = 6
TEAM_SARBAZ = 7

ENEMY_KARGAR = 8
ENEMY_SARBAZ = 9


#types sets
ENTITIES = {TEAM_KARGAR, TEAM_SARBAZ, ENEMY_KARGAR, ENEMY_SARBAZ}
BUILDINGS = {WALL, ENEMY_BASE, TRAP , SWAMP}
RESOURCES = {BREAD, GRASS}
EMPTIES = {EMPTY, NO_ANTS}

#const values
INF = 1e10
MAX_CHARS = 32

def trap_for_ant(t):
    from tools import has_resource
    # print("salam" , has_resource)
    return 2000 if has_resource else 10

def bad_trap_for_ant(t):
    from tools import has_resource
    # print("salam" , has_resource)
    return 10 if has_resource else 2000

COST = {
    'ant': {
        UNKNOWN: lambda t: 20,
        WALL: lambda t: INF,
        EMPTY: lambda t: 10,
        NO_ANTS: lambda t: 10,
        ENEMY_BASE: lambda t: INF,
        BREAD: lambda t: 0,
        GRASS: lambda t: 0,
        TEAM_KARGAR: lambda t: 20 * math.exp(-1*t),
        TEAM_SARBAZ: lambda t: 10,
        ENEMY_KARGAR: lambda t: 10,
        ENEMY_SARBAZ: lambda t: 2000 * math.exp(-1.5*t),
        SWAMP: lambda t: 50,
        TRAP: trap_for_ant,
        BAD_TRAP: bad_trap_for_ant
    },
    'scorpion': {
        UNKNOWN: lambda t: 10,
        WALL: lambda t: INF,
        EMPTY: lambda t: 10,
        NO_ANTS: lambda t: 10,
        ENEMY_BASE: lambda t: 50,
        BREAD: lambda t: 5,
        GRASS: lambda t: 5,
        TEAM_KARGAR: lambda t: 0,
        TEAM_SARBAZ: lambda t: 0,
        ENEMY_KARGAR: lambda t: 0,
        ENEMY_SARBAZ: lambda t: 1000 * math.exp(-1.5 * t),
        SWAMP: lambda t: 50,
        TRAP: lambda t: 10,
        BAD_TRAP: lambda t: 10
    }
}

def f(t):
    return (tools.allied_in_range - tools.enemy_in_range) * 100 * math.exp(-2*t)

GOAL_COST = {
    'ant': {
        UNKNOWN: lambda t: 10,
        WALL: lambda t: -INF,
        EMPTY: lambda t: 10 + -100 * math.exp(-0.2*t),
        NO_ANTS: lambda t: 0,
        ENEMY_BASE: lambda t: -INF,
        BREAD: lambda t: 2000 * math.exp(-0.2*t),
        GRASS: lambda t: 3000 * math.exp(-0.2*t),
        TEAM_KARGAR: lambda t: -10 * math.exp(-t),
        TEAM_SARBAZ: lambda t: 0,
        ENEMY_KARGAR: lambda t: 0,
        ENEMY_SARBAZ: lambda t: -2000 * math.exp(-t),
        SWAMP: lambda t: -1000,
        TRAP: lambda t: -100000,
        BAD_TRAP: lambda t: -100000
    },
    'scorpion': {
        UNKNOWN: lambda t: 20,
        WALL: lambda t: -INF,
        EMPTY: lambda t: 0,
        NO_ANTS: lambda t: 0,
        ENEMY_BASE: lambda t: -500 + int(tools.turn_number / 1150) * 550,
        BREAD: lambda t: 0,
        GRASS: lambda t: 0,
        TEAM_KARGAR: lambda t: 50 * math.exp(-t),
        TEAM_SARBAZ: lambda t: 0,
        ENEMY_KARGAR: lambda t: 200 * math.exp(-0.5*t),
        ENEMY_SARBAZ: f,
        SWAMP: lambda t: 0,
        TRAP: lambda t: 0,
        BAD_TRAP: lambda t: 0
    }
}

SCALABLE = {
    'ant': {
        ENEMY_SARBAZ: 4,
        ENEMY_BASE: 6
    },
    'scorpion': {
        ENEMY_KARGAR: 4,
        ENEMY_BASE: 6
    }
}
