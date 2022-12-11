from functools import reduce


# -- INPUT --
def read_tuples(filename):
    return [tuple(map(str, line.rstrip().split(" "))) for line in open(filename)]


def readlines(filename):
    return [line.rstrip() for line in open(filename)]


# -- ARRAYS --

def create_2d_array(width, height, value=0):
    return [[value for i in range(width)] for j in range(height)]


def lmap(func, *iterables):
    return list(map(func, *iterables))
