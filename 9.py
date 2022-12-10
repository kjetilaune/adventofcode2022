from functions import *


class Knot:

    def calculate_new_head_position(self, dir):
        if dir == 'R':
            self.x += 1
        elif dir == 'L':
            self.x -= 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1
        self.visited.append((self.x, self.y))

    def should_move(self, parent):
        if abs(parent.x - self.x) == 2:
            return True
        if abs(parent.y - self.y) == 2:
            return True
        return False

    def move_to(self, prevKnot):
        new_pos = prevKnot.get_last_position()
        if self.x != prevKnot.x and self.y != prevKnot.y:
            # Move diagonally
            if prevKnot.x > self.x:
                if prevKnot.y > self.y:
                    self.x += 1
                    self.y += 1
                else:
                    self.x += 1
                    self.y -= 1
            if prevKnot.x < self.x:
                if prevKnot.y > self.y:
                    self.x -= 1
                    self.y += 1
                else:
                    self.x -= 1
                    self.y -= 1
        elif self.x == prevKnot.x:
            if self.y > prevKnot.y:
                self.y -= 1
            else:
                self.y += 1
        elif self.y == prevKnot.y:
            if self.x > prevKnot.x:
                self.x -= 1
            else:
                self.x += 1
            # self.x = new_pos[0]
            # self.y = new_pos[1]
        self.visited.append((self.x, self.y))

    def get_last_position(self):
        return self.visited[-2]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prevX = 0
        self.prevY = 0
        self.visited = [(0, 0)]


def should_move_tail(H, T):
    if abs(H[0] - T[0]) == 2:
        return True
    if abs(H[1] - T[1]) == 2:
        return True
    return False


def print_snake(knots):
    list = [['0' for x in range(20)] for y in range(20)]
    for knot in knots:
        for i in range(len(knots)):
            x = knots[i].x
            y = knots[i].y
            if i == 0:
                list[y][x] = 'H'
            elif i == 9:
                list[y][x] = 'T'
            else:
                list[y][x] = str(i)
    for row in list:
        print(row)
    print("\n")


def task1():
    my_list = [x.split(" ") for x in readlines("9.txt")]
    visited = {}
    H = (0, 0)
    T = (0, 0)
    prev_H = (0, 0)
    visited[T] = "visited"

    for dir, num in my_list:
        for i in range(int(num)):
            prev_H = H
            if dir == 'R':
                H = (H[0] + 1, H[1])
            elif dir == 'L':
                H = (H[0] - 1, H[1])
            elif dir == 'U':
                H = (H[0], H[1] + 1)
            elif dir == 'D':
                H = (H[0], H[1] - 1)

            if should_move_tail(H, T):
                T = prev_H
            visited[T] = "visited"

    print(len(visited))


def task2():
    my_list = [x.split(" ") for x in readlines("9.txt")]
    knots = [Knot(0, 0) for x in range(10)]
    for dir, num in my_list:
        for i in range(int(num)):
            knots[0].calculate_new_head_position(dir)
            prevKnot = knots[0]

            for knot in knots[1:]:
                if knot.should_move(prevKnot):
                    knot.move_to(prevKnot)
                prevKnot = knot

    print(len(set(knots[-1].visited)))


task2()
