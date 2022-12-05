def getinput():
    stacks = ["",
              "BSVZGPW",
              "JVBCZF",
              "VLMHNZDC",
              "LDMZPFJB",
              "VFCGJBQH",
              "GFQTSLB",
              "LGCZV",
              "NLG",
              "JFHC"]
    mylist = [line.rstrip().split(" ") for line in open("5.txt")]
    return stacks, mylist


def print_stacks(stacks):
    s = ""
    for i in stacks:
        if len(i) > 0:
            s += i[-1]
    print(s)


def task1():
    stacks, mylist = getinput()

    for command in mylist:
        num, from_stack, to_stack = int(command[1]), int(command[3]), int(command[5])

        for i in range(num):
            container = stacks[from_stack][-1]
            stacks[to_stack] = stacks[to_stack] + container
            stacks[from_stack] = stacks[from_stack][:-1]

    print_stacks(stacks)


def task2():
    stacks, mylist = getinput()

    for command in mylist:
        num, from_stack, to_stack = int(command[1]), int(command[3]), int(command[5])
        containers = stacks[from_stack][-num:]
        stacks[to_stack] = stacks[to_stack] + containers
        stacks[from_stack] = stacks[from_stack][:-num]

    print_stacks(stacks)


task1()
task2()
