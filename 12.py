from functions import *
from Queue import PriorityQueue


def dijkstra(nodes, start_id, end_id):
    dist = [float("inf") for _ in range(len(nodes))]
    dist[start_id] = 0
    Q = PriorityQueue()

    Q.put((0, nodes[start_id]))

    while not Q.empty():
        u = Q.get()[1]
        u.visited = True
        if u.id == end_id:
            return dist

        for neighbour in u.neighbours:
            if not nodes[neighbour].visited:
                nodes[neighbour].visited = True
                alt = dist[u.id] + 1
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    Q.put((alt, nodes[neighbour]))

    return dist


class Node:

    def __init__(self, id, x, y, height):
        self.id = id
        self.x = x
        self.y = y
        self.height = height
        self.neighbours = []
        self.visited = False

    def __str__(self):
        return str(self.neighbours)


def get_id(x, y, heights):
    return y * len(heights[0]) + x


def set_neighbours(node, heights):
    x, y = node.x, node.y

    #  Test right
    if x + 1 < len(heights[0]):
        if heights[y][x + 1] <= node.height + 1:
            node.neighbours.append(get_id(x + 1, y, heights))
    #  Test left
    if x - 1 >= 0:
        if heights[y][x - 1] <= node.height + 1:
            node.neighbours.append(get_id(x - 1, y, heights))
    #  Test up
    if y - 1 >= 0:
        if heights[y - 1][x] <= node.height + 1:
            node.neighbours.append(get_id(x, y - 1, heights))
    #  Test down
    if y + 1 < len(heights):
        if heights[y + 1][x] <= node.height + 1:
            node.neighbours.append(get_id(x, y + 1, heights))


def task1():
    heights = [map(lambda x: ord(x) - ord('a') if x != 'S' and x != 'E' else x, list(a)) for a in
               readlines("12.txt")]
    start_id = 0
    end_id = 0
    nodes = []
    for y in range(len(heights)):
        for x in range(len(heights[0])):
            node = Node(y * len(heights[0]) + x, x, y, heights[y][x])
            if heights[y][x] == 'S':
                start_id = y * len(heights[0]) + x
                heights[y][x] = 0
                node.height = 0
            elif heights[y][x] == 'E':
                end_id = y * len(heights[0]) + x
                heights[y][x] = 25
                node.height = 25
            nodes.append(node)
    for n in nodes:
        set_neighbours(n, heights)

    dist = dijkstra(nodes, start_id, end_id)
    print(dist[end_id])


def task2():
    heights = [map(lambda x: ord(x) - ord('a') if x != 'S' and x != 'E' else x, list(a)) for a in
               readlines("12.txt")]
    start_id = 0
    end_id = 0

    nodes = []
    for y in range(len(heights)):
        for x in range(len(heights[0])):
            node = Node(y * len(heights[0]) + x, x, y, heights[y][x])
            if heights[y][x] == 'S':
                start_id = y * len(heights[0]) + x
                heights[y][x] = 0
                node.height = 0
            elif heights[y][x] == 'E':
                end_id = y * len(heights[0]) + x
                heights[y][x] = 25
                node.height = 25
            nodes.append(node)
    for n in nodes:
        set_neighbours(n, heights)


    paths = []
    for i in range(len(nodes)):
        for node in nodes:
            node.visited = False
        if nodes[i].height == 0:
            paths.append(dijkstra(nodes, nodes[i].id, end_id)[end_id])

    print(min(paths))


task2()
