from functions import *


def task1():
    my_list = readlines("10.txt")
    commands = []
    for cmd in my_list:
        if cmd != "noop":
            commands.append("noop")
        commands.append(cmd)

    signal = 1
    signal_strengths = 0
    for cycle in range(1, len(commands) + 1):
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            signal_strengths += signal * cycle
        if commands[cycle - 1] == "noop":
            continue
        signal += int(commands[cycle - 1].split(" ")[1])
    print(signal_strengths)


def task2():
    my_list = readlines("10.txt")
    commands = []
    for cmd in my_list:
        if cmd != "noop":
            commands.append("noop")
        commands.append(cmd)

    sprite_pos = 1
    screen = [["." for x in range(40)] for y in range(6)]
    for cycle in range(len(commands)):
        y = int(cycle / 40)
        x = cycle % 40
        if sprite_pos - 1 <= x <= sprite_pos + 1:
            screen[y][x] = "#"
        if commands[cycle] == "noop":
            continue
        sprite_pos += int(commands[cycle].split(" ")[1])

    for l in screen:
        print(l)


task2()
