from functions import *

def print_cave_section(cave, min_x, max_x, min_y, max_y):
    for line in cave[min_y-1:max_y+1]:
        print(line[min_x-1:max_x+1])


def draw_line(cave, start, end):
    x = min(start[0], end[0])
    y = min(start[1], end[1])

    if start[0] == end[0]:
        for i in range(abs(end[1] - start[1]) + 1):
            cave[y + i][x] = "#"
    else:
        for i in range(abs(end[0] - start[0]) + 1):
            cave[y][x + i] = "#"

    return cave

def drop_sand_unit(cave, sand_start, max_y):
    new_sand_pos = (sand_start[0], sand_start[1] + 1)

    if cave[new_sand_pos[1]][new_sand_pos[0]] == ".":
        return drop_sand_unit(cave, new_sand_pos, max_y)
    elif cave[new_sand_pos[1]][new_sand_pos[0]] == "#" or cave[new_sand_pos[1]][new_sand_pos[0]] == "+":
        if cave[new_sand_pos[1]][new_sand_pos[0] - 1] == ".":
            return drop_sand_unit(cave, (new_sand_pos[0] - 1, new_sand_pos[1]), max_y)
        elif cave[new_sand_pos[1]][new_sand_pos[0] + 1] == ".":
            return drop_sand_unit(cave, (new_sand_pos[0] + 1, new_sand_pos[1]), max_y)
        cave[sand_start[1]][sand_start[0]] = "+"
        return cave



def task1():
    my_list = [line.rstrip().split(" -> ") for line in open("14.txt")]
    rock_lines = [list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), l)) for l in my_list]

    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 1000
    for y in rock_lines:
        max_x_temp = max(x[0] for x in y)
        max_y_temp = max(x[1] for x in y)
        max_x = max_x_temp if max_x_temp > max_x else max_x
        max_y = max_y_temp if max_y_temp > max_y else max_y

        min_x_temp = min(x[0] for x in y)
        min_y_temp = min(x[1] for x in y)
        min_x = min_x_temp if min_x_temp < min_x else min_x
        min_y = min_y_temp if min_y_temp < min_y else min_y

    print(max_x, max_y, min_x, min_y)

    sand_start = (500, 0)

    cave = [["." for x in range(max_x + 1)] for y in range(max_y + 2)]
    print(rock_lines)
    for line in rock_lines:
        for i in range(len(line) - 1):
            cave = draw_line(cave, line[i], line[i + 1])

    print_cave_section(cave, min_x, max_x, min_y, max_y)

    while True:

        try:
            cave = drop_sand_unit(cave, sand_start, max_y)
        except:
            num_units = 0
            for line in cave:
                for cell in line:
                    if cell == "+":
                        num_units += 1
            print(num_units)
            return

def task2():
    my_list = [line.rstrip().split(" -> ") for line in open("14.txt")]
    rock_lines = [list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), l)) for l in my_list]

    max_x = 0
    max_y = 0
    min_x = 1000
    min_y = 1000
    for y in rock_lines:
        max_x_temp = max(x[0] for x in y)
        max_y_temp = max(x[1] for x in y)
        max_x = max_x_temp if max_x_temp > max_x else max_x
        max_y = max_y_temp if max_y_temp > max_y else max_y

        min_x_temp = min(x[0] for x in y)
        min_y_temp = min(x[1] for x in y)
        min_x = min_x_temp if min_x_temp < min_x else min_x
        min_y = min_y_temp if min_y_temp < min_y else min_y

    print(max_x, max_y, min_x, min_y)

    sand_start = (500, 0)

    cave = [["." for x in range(max_x * 2)] for y in range(max_y + 3)]
    print(rock_lines)
    for line in rock_lines:
        for i in range(len(line) - 1):
            cave = draw_line(cave, line[i], line[i + 1])

    cave[-1] = ["#" for x in range(max_x * 2)]

    while True:
        if cave[sand_start[1]][sand_start[0]] == "+":
            print_cave_section(cave, min_x, max_x, min_y, max_y)
            break
        try:
            cave = drop_sand_unit(cave, sand_start, max_y)
        except:
            continue

    num_units = 0
    for line in cave:
        for cell in line:
            if cell == "+":
                num_units += 1
    print(num_units)



task2()
