# Task 1

def task1():
	myList = [line.rstrip() for line in open('1.txt')]
	calList = []
	counter = 0
	for item in myList:
		if item == '':
			calList += [counter]
			counter = 0
			continue
		counter += int(item)

	print max(calList)


#Task 2

def task2():
	myList = [line.rstrip() for line in open('1.txt')]
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