from functions import *
from functools import cmp_to_key


def check_signals(left, right):
    #  If both are lists of ints
    if all(isinstance(i, int) for i in left) and all(isinstance(i, int) for i in right):
        zipped = zip(left, right)
        for i in zipped:
            if i[0] < i[1]:
                return True
            elif i[0] > i[1]:
                return False
        if len(left) < len(right):
            return True
        if len(left) > len(right):
            return False
        if len(left) == len(right):
            return None

    for idx in range(min(len(left), len(right))):
        #  If both values are lists
        if type(left[idx]) == list and type(right[idx]) == list:
            ret = check_signals(left[idx], right[idx])
            if ret is not None:
                return ret
            else:
                continue

        #  If exactly one value is integer
        ret = None
        if isinstance(left[idx], int) and isinstance(right[idx], int):
            ret = check_signals([left[idx]], [right[idx]])
        elif isinstance(left[idx], int):
            ret = check_signals([left[idx]], right[idx])
        elif isinstance(right[idx], int):
            ret = check_signals(left[idx], [right[idx]])
        if ret is not None:
            return ret
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    return None


def task1():
    my_list = readlines("13.txt")
    signals = []
    for i in range(0, len(my_list), 3):
        signals.append((eval(my_list[i]), eval(my_list[i + 1])))

    right_order = []
    for i in range(len(signals)):
        if check_signals(signals[i][0], signals[i][1]):
            right_order.append(i + 1)

    print(reduce(lambda x, y: x + y, right_order))


def task2():
    my_list = readlines("13.txt")
    signals = []
    for i in range(0, len(my_list), 3):
        signals.append((eval(my_list[i])))
        signals.append((eval(my_list[i + 1])))

    signals.append([[2]])
    signals.append([[6]])

    signals.sort(key=cmp_to_key(lambda x, y: i if check_signals(x, y) else -1), reverse=True)

    print((signals.index([[2]]) + 1) * (signals.index([[6]]) + 1))

task1()
task2()
