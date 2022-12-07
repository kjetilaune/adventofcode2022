from functions import *


class Folder:

    def explore_folder(self, commands):
        counter = 0

        for cmd in commands:
            cmd_parts = cmd.split(" ")
            if cmd_parts[0] == "dir":
                self.sub_folders[cmd_parts[1]] = Folder(cmd_parts[1], self)
            elif cmd_parts[0].isdigit():
                self.files.append(int(cmd_parts[0]))
            elif cmd_parts[0] == "$":
                return commands[counter:]
            counter += 1

    def next_command(self, commands):
        new_commands = []

        if commands[0] == "$ ls":
            new_commands = self.explore_folder(commands[1:])
        else:
            new_commands = commands

        if new_commands is None or len(new_commands) == 0:
            return

        if new_commands[0] == "$ cd ..":
            self.parent.next_command(new_commands[1:])
        elif new_commands[0] == "$ ls":
            self.explore_folder(new_commands[1:])
        elif len(new_commands[0].split(" ")) == 3:
            self.sub_folders.get(new_commands[0].split(" ")[2]).next_command(new_commands[1:])

    def print_me(self, level):
        print("     " * level + " - Name: " + self.name + ", Size: " + str(self.size))
        for file in self.files:
            print("     " * (level + 1) + " - " + str(file))
        for _, v in self.sub_folders.items():
            v.print_me(level + 1)

    def set_size(self):
        self.size = sum(self.files)

        for _, v in self.sub_folders.items():
            self.size += v.set_size()

        return self.size

    def get_small_directories(self):
        small_size = 0
        if self.size < 100000:
            small_size += self.size

        for _, v in self.sub_folders.items():
            small_size += v.get_small_directories()

        return small_size

    def smallest_deletable_directory(self, limit):
        if self.size < limit:
            return self.size

        best_so_far = self.size

        for _, v in self.sub_folders.items():
            if limit < v.smallest_deletable_directory(limit) < best_so_far:
                best_so_far = v.smallest_deletable_directory(limit)
        return best_so_far

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.sub_folders = {}
        self.files = []
        self.size = 0


def day7():
    commands = readlines("7.txt")
    topFolder = Folder("/", None)
    topFolder.next_command(commands[1:])
    used_space = topFolder.set_size()
    print("Task 1: " + str(topFolder.get_small_directories()))
    need_to_clear_up = 30000000 - (70000000 - used_space)
    print("Need to clear up at least: " + str(need_to_clear_up))
    print("Task 2: " + str(topFolder.smallest_deletable_directory(need_to_clear_up)))


day7()
