from functions import *

def overlaps(a, b):
    if int(a.split("-")[0]) <= int(b.split("-")[0]) <= int(a.split("-")[1]) or int(a.split("-")[0]) <= int(b.split("-")[1]) <= int(a.split("-")[1]):
        return 1
    elif int(b.split("-")[0]) <= int(a.split("-")[0]) <= int(b.split("-")[1]) or int(b.split("-")[0]) <= int(a.split("-")[1]) <= int(b.split("-")[1]):
        return 1
    return 0

def contains(a, b):
    if int(a.split("-")[0]) <= int(b.split("-")[0]) <= int(a.split("-")[1]) and int(a.split("-")[0]) <= int(b.split("-")[1]) <= int(a.split("-")[1]):
        return 1
    elif int(b.split("-")[0]) <= int(a.split("-")[0]) <= int(b.split("-")[1]) and int(b.split("-")[0]) <= int(a.split("-")[1]) <= int(b.split("-")[1]):
        return 1
    return 0


def task1():
    mylist = [line.rstrip().split(",") for line in open("4.txt")]
    sum = 0
    for item in mylist:
        sum += contains(item[0], item[1])
    print(sum)


task1()

def task2():
    mylist = [line.rstrip().split(",") for line in open("4.txt")]
    sum = 0
    for item in mylist:
        sum += overlaps(item[0], item[1])
    print(sum)

task2()