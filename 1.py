from functions import *

# Task 1

def task1():
	myList = readlines('1.txt')
	calList = []
	counter = 0
	for item in myList:
		if item == '':
			calList += [counter]
			counter = 0
			continue
		counter += int(item)

	print max(calList)

task1()

#Task 2

def task2():
	myList = readlines('1.txt')
	calList = []
	counter = 0
	for item in myList:
		if item == '':
			calList += [counter]
			counter = 0
			continue
		counter += int(item)

	calList.sort()	
	print calList[-1] + calList[-2] + calList[-3]

task2()