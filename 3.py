from functions import *


def convert_to_value(char):
    if str.islower(char):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 1 + 26


# ------------# TASK 1 #----------------#

def find_priority(string):
    s1 = string[:len(string) / 2]
    s2 = string[len(string) / 2:]
    hash = dict.fromkeys(s1, 1)
    for char in s2:
        if hash.get(char) == 1:
            return convert_to_value(char)


def task1():
    my_list = readlines("3.txt")
    sum = 0
    for item in my_list:
        sum += find_priority(item)

    print(sum)


task1()


# ------------# TASK 2 #----------------#

def find_group(s1, s2, s3):
    hash1 = dict.fromkeys(s1, 1)
    hash2 = dict.fromkeys(s2, 1)
    hash3 = dict.fromkeys(s3, 1)
    result = {i: hash1.get(i, 0) + hash2.get(i, 0) for i in set(hash1).union(hash2)}
    result = {i: result.get(i, 0) + hash3.get(i, 0) for i in set(result).union(hash3)}

    for key, value in result.items():
        if value == 3:
            return convert_to_value(key)


def task2():
    my_list = readlines("3.txt")
    sum = 0
    for i in range((int(len(my_list) / 3))):
        sum += find_group(my_list[i * 3], my_list[i * 3 + 1], my_list[i * 3 + 2])
    print(sum)


task2()
