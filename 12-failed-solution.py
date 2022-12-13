from functions import *
from copy import deepcopy

def bfs(heights, visited, x, y, start=False):
    print(visited)
    print((x, y))
    if heights[y][x] == 'E' and heights[visited[-1][1]][visited[-1][0]] >= 24:
        return visited

    if heights[y][x] - heights[visited[-1][1]][visited[-1][0]] > 1:
        return None

    visited.append((x, y))
    #if heights[y][x] == 'E':
    #    return visited

    child_results = []
    #  Test right
    if x + 1 < len(heights[0]):
        if (x + 1, y) not in visited:
            res = bfs(heights, visited, x + 1, y)
            if res is not None:
                child_results.append(res)

    #  Test left
    if x - 1 > 0:
        if (x - 1, y) not in visited:
            res = bfs(heights, visited, x - 1, y)
            if res is not None:
                child_results.append(res)

    #  Test up
    if y - 1 > 0:
        if (x, y - 1) not in visited:
            res = bfs(heights, visited, x, y - 1)
            if res is not None:
                child_results.append(res)

    #  Test down
    if y + 1 < len(heights):
        if (x, y + 1) not in visited:
            res = bfs(heights, visited, x, y + 1)
            if res is not None:
                child_results.append(res)

    if len(child_results) > 0:
        print("Child" + str(child_results))
        return child_results
    else:
        return None

def bfs2(heights, visitedC, x, y, goal):
    #print("\n")
    #print("I'm currently in" + str((x, y)))
    visited = deepcopy(visitedC)
    if goal[0] == x and goal[1] == y:
        #print("I have won")
        visited.append("WON")
        return visited

    #if heights[y][x] - heights[visited[-1][1]][visited[-1][0]] > 1:
    #    return None

    visited.append((x, y))
    #print("I have already visited" + str(visited))
    #if heights[y][x] == 'E':
    #    return visited

    child_results = deepcopy([])
    #  Test right
    if x + 1 < len(heights[0]):
        if (x + 1, y) not in visited:
            if heights[y][x + 1] - 1 <= heights[y][x]:
                #print("I can go right")
                res = bfs2(heights, visited, x + 1, y, goal)
                if res is not None:
                    child_results.append(res)
    #print("I'm currently in" + str((x, y)))
    #  Test left
    if x - 1 >= 0:
        if (x - 1, y) not in visited:
            if heights[y][x - 1] - 1 <= heights[y][x]:
                #print("I can go left")
                res = bfs2(heights, visited, x - 1, y, goal)
                if res is not None:
                    child_results.append(res)
    #print("I'm currently in" + str((x, y)))
    #  Test up
    if y - 1 >= 0:
        if (x, y - 1) not in visited:
            if heights[y - 1][x] - 1 <= heights[y][x]:
                #print("I can go up")
                res = bfs2(heights, visited, x, y - 1, goal)
                if res is not None:
                    child_results.append(res)
    #print("I'm currently in" + str((x, y)))
    #  Test down
    if y + 1 < len(heights):
        if (x, y + 1) not in visited:
            if heights[y + 1][x] - 1 <= heights[y][x]:
                #print("I can go down")
                res = bfs2(heights, visited, x, y + 1, goal)
                if res is not None:
                    child_results.append(res)
    #print((x, y))
    if len(child_results) > 0:
        #print("Child" + str(child_results))
        return [item for sublist in child_results for item in sublist]
    else:
        #print("Can't go here")
        return None

def task1():
    heights = [map(lambda x: ord(x) - ord('a') if x != 'S' and x != 'E' else 0 if x == 'S' else 'E', list(a)) for a in readlines("12.txt")]
    goal = (0, 0)
    for y in range(len(heights)):
        for x in range(len(heights[0])):
            if heights[y][x] == 'E':
                goal = (x, y)
    heights[goal[1]][goal[0]] = 25

    res = bfs2(heights, [(0, 20)], 0, 0, goal)
    ans = []
    temp = []
    for i in res:
        if i == "WON":
            ans.append(len(temp))
            temp = []
        else:
            temp.append(i)
    print(min(ans)-1)



task1()

#  Dict = {"(0,0)": [(0, 1), (0, 2)] }
