from functions import *


class Monkey:

    def unpack_items(self, items):
        return [int(x.strip()) for x in items[18:].split(",")]

    def calculate_new(self, old):
        operator = self.operation_string[1]
        if self.operation_string[2] == "old":
            right_side = old
        else:
            right_side = int(self.operation_string[2])

        if operator == "*":
            return old * right_side
        else:
            return old + right_side

    def inspect_item_task_1(self):
        if len(self.items) == 0:
            return None

        self.inspected_items += 1

        item = self.items[0]
        self.items = self.items[1:]

        item = self.calculate_new(item)
        item = int(item / 3)
        if item % self.test == 0:
            return {"item": item, "to_monkey": self.true_monkey}
        else:
            return {"item": item, "to_monkey": self.false_monkey}

    def inspect_item_task_2(self, prod):
        if len(self.items) == 0:
            return None

        self.inspected_items += 1
        item = self.items[0]
        self.items = self.items[1:]

        item = self.calculate_new(item)

        if item % self.test == 0:
            return {"item": item % prod, "to_monkey": self.true_monkey}
        else:
            return {"item": item % prod, "to_monkey": self.false_monkey}

    def receive_item(self, item):
        self.items.append(item)

    def __init__(self, number, items_string, operation_string, test_string, test_true_string, test_false_string):
        self.number = number
        self.items = self.unpack_items(items_string)
        self.operation_string = operation_string.split(" ")[-3:]
        self.test = int(test_string.split(" ")[-1])
        self.true_monkey = int(test_true_string.split(" ")[-1])
        self.false_monkey = int(test_false_string.split(" ")[-1])
        self.inspected_items = 0

    def __str__(self):
        ret = ""
        ret += "Monkey " + str(self.number) + "\n "
        ret += str(self.items) + "\n "
        ret += str(self.operation_string) + "\n "
        ret += str(self.test) + "\n  "
        ret += str(self.true_monkey) + "\n  "
        ret += str(self.false_monkey) + "\n "
        ret += str(self.inspected_items) + "\n"
        return ret


def task1():
    my_list = readlines("11.txt")
    monkeys = []

    for monkey in range(int(len(my_list) / 7) + 1):
        index = monkey * 7
        monkeys.append(Monkey(monkey, my_list[index + 1], my_list[index + 2], my_list[index + 3], my_list[index + 4],
                              my_list[index + 5]))

    for i in range(20):
        for monkey in monkeys:
            for idx in range(len(monkey.items)):
                res = monkey.inspect_item_task_1()
                if res is not None:
                    monkeys[res.get("to_monkey")].receive_item(res.get("item"))

    res = [int(m.inspected_items) for m in monkeys]
    res.sort()
    print(res[-2] * res[-1])


def task2():
    my_list = readlines("11.txt")
    monkeys = []
    prod = 1
    for monkey in range(int(len(my_list) / 7) + 1):
        index = monkey * 7
        monkeys.append(Monkey(monkey, my_list[index + 1], my_list[index + 2], my_list[index + 3], my_list[index + 4],
                              my_list[index + 5]))
        prod *= int(my_list[index + 3].split(" ")[-1])

    for i in range(10000):
        if i % 100 == 0:
            print(i)
        for monkey in monkeys:
            for idx in range(len(monkey.items)):
                res = monkey.inspect_item_task_2(prod)
                if res is not None:
                    monkeys[res.get("to_monkey")].receive_item(res.get("item"))

    res = [int(m.inspected_items) for m in monkeys]
    res.sort()
    print(res[-2] * res[-1])


task2()
