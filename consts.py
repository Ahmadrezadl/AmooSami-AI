import math

#cell types
import tools

TRAP = -2
SWAMP = -3

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
COST = {
    'ant': {
        UNKNOWN: (20, 0),
        WALL: (INF, 0),
        EMPTY: (10, 0),
        NO_ANTS: (10, 0),
        ENEMY_BASE: (INF, 0),
        BREAD: (0, 0),
        GRASS: (0, 0),
        TEAM_KARGAR: (20, -1),
        TEAM_SARBAZ: (10, 0),
        ENEMY_KARGAR: (10, 0),
        ENEMY_SARBAZ: (2000, -1.5),
        SWAMP: (50, 0),
        -100: (1000,0),
        -101: (0,0)
    },
    'scorpion': {
        UNKNOWN: (10, 0),
        WALL: (INF, 0),
        EMPTY: (10, 0),
        NO_ANTS: (10, 0),
        ENEMY_BASE: (50, 0),
        BREAD: (5, 0),
        GRASS: (5, 0),
        TEAM_KARGAR: (0, -1.5),
        TEAM_SARBAZ: (0, 0),
        ENEMY_KARGAR: (0, 0),
        ENEMY_SARBAZ: (1000, -1.5),
        SWAMP: (50, 0),
        TRAP: (10, 0)
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
        SWAMP: -1000,
        TRAP: -1000
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
        SWAMP: 0,
        TRAP: 0
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
