import math

#cell types
import tools

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
BUILDINGS = {WALL, ENEMY_BASE}
RESOURCES = {BREAD, GRASS}
EMPTIES = {EMPTY, NO_ANTS}

#const values
INF = 1e10
COST = {
    'ant': {
        UNKNOWN: (10, 0),
        WALL: (INF, 0),
        EMPTY: (10, 0),
        NO_ANTS: (10, 0),
        ENEMY_BASE: (INF, 0),
        BREAD: (0, 0),
        GRASS: (0, 0),
        TEAM_KARGAR: (10, -1.5),
        TEAM_SARBAZ: (0, 0),
        ENEMY_KARGAR: (0, 0),
        ENEMY_SARBAZ: (1000, -1.5)
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
        ENEMY_SARBAZ: (1000, -1.5)
    }
}

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
        ENEMY_SARBAZ: lambda t: -1000 * math.exp(-t),
    },
    'scorpion': {
        UNKNOWN: lambda t: 20,
        WALL: lambda t: -INF,
        EMPTY: lambda t: 0,
        NO_ANTS: lambda t: 0,
        ENEMY_BASE: lambda t: -500 + int(tools.turn_number / 70) * 1000,
        BREAD: lambda t: 0,
        GRASS: lambda t: 0,
        TEAM_KARGAR: lambda t: 50,
        TEAM_SARBAZ: lambda t: 0,
        ENEMY_KARGAR: lambda t: 100,
        ENEMY_SARBAZ: lambda t: -200
    }
}

AVOIDABLE = {
    'ant': {
        ENEMY_SARBAZ: 4,
        ENEMY_BASE: 6
    },
    'scorpion': {
        ENEMY_SARBAZ: 4,
        ENEMY_BASE: 6
    }
}