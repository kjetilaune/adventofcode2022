from functions import readlines


def find_start(num):
    signal = readlines("6.txt")[0]
    for i in range(len(signal) - num):
        subsignal = signal[i:i + num]

        if len(set(subsignal)) == num:
            return i + num


# Task 1
print(find_start(4))

# Task 2
print(find_start(14))
