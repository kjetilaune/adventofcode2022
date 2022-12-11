from functools import reduce
import time


def map_test():
    a = [1, 2, 3, 4, 5]
    a = map(lambda x: x * x, a)
    print(a)
    # Output: [1, 4, 9, 16, 25]


def eval_test():
    a = [1, 2, 3, 4, 5]
    op = "Operation: new = old * 19"
    print(map(eval("lambda old:" + op.split("=")[1]), a))
    # Output: [19, 38, 57, 76, 95]


def lambda_test():
    square = lambda x: x * x
    print(square(8))
    # Output: 64


def zip_test():
    x_coords = [1, 4, 2, 5, 4, 2, 3]
    y_coords = [9, 6, 5, 7, 8, 5, 4]
    print(zip(x_coords, y_coords))
    # Output: [(1, 9), (4, 6), (2, 5), (5, 7), (4, 8), (2, 5), (3, 4)]


class Monkey:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "I am Monkey number " + str(self.id)


def create_monkey(id):
    return Monkey(id)


def task1():
    # input_array = [i for i in range(10)]

    # List
    input_array = list("0123456789")

    # Native
    monkeys1 = []
    for i in input_array:
        monkeys1.append(Monkey(i))

    # Map and function
    monkeys2 = map(create_monkey, input_array)

    # Map and lambda
    monkeys3 = map(lambda m: Monkey(m), input_array)

    # Map and lambda and eval
    monkeys4 = map(eval("lambda m: Monkey(m)"), input_array)

    for index, monkey in enumerate(monkeys4):
        print(str(monkeys1[index]) + "\t" + str(monkeys2[index]) + "\t" + str(monkeys3[index]) + "\t" + str(
            monkeys4[index]))


# task1()

#  Tasks from https://www.w3resource.com/python-exercises/python-functions-exercises.php solved in not the default way

def e1():  # Max of list
    a = 1
    b = 2
    c = 3
    listen = [Monkey(1), Monkey(2), Monkey(3)]
    # print(max(a, b, c))
    print(reduce(lambda x, y: x if x.id > y.id else y, listen))


def e2():  # Sum numbers in list
    numbers = [8, 2, 3, 0, 7]
    # print(sum(numbers))
    print(eval(str(numbers).replace(",", " +")[1:-1]))


def e3():  # Multiply numbers in list
    numbers = [8, 2, 3, -1, 7]
    print(reduce(lambda x, y: x * y, numbers))


def e4():  # Reverse string
    input_string = "1234abcd"
    reversed_string = input_string[::-2]
    print(reversed_string)


def e5(n):  # Factorial
    print(reduce(lambda x, y: x * y, [x for x in range(n, 0, -1)]))


def e6(x, n, m):  # Number falls in given range
    print(map(lambda x, n, m: True if m >= x >= n else False, [x], [n], [m])[0])
    return x in range(n, m + 1)


def e7(s):  # Count number of upper and lower case letters
    count = map(lambda x: 1 if 'A' <= x <= 'Z' else 0, list(s))
    return {"upper": reduce(lambda x, y: x + y, count),
            "lower": reduce(lambda x, y: x + y, map(lambda x: 1 if x is 0 else 0, count))}


def e8():  # Unique values
    my_list = [1, 2, 3, 3, 3, 3, 4, 5]
    my_dict = {}
    for item in my_list:
        my_dict[item] = 0
    print(my_dict.keys())


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def e9(n):  # is prime
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


t1 = int(time.time() * 1000)
print(e9(27182))
t2 = int(time.time() * 1000)
print(t2 - t1)
print(e9(27182))
t3 = int(time.time() * 1000)
print(t3 - t2)
print(e9(27182))
t4 = int(time.time() * 1000)
print(t4 - t3)
