from functions import *

#Task 1

def playMatch(opponent, me):
	plays = ['A', 'B', 'C']
	
	meShifted = chr(ord(me) - 23)

	if opponent == meShifted:
		return "D"
	elif plays[plays.index(meShifted) - 1] == opponent:
		return "W"
	else:
		return "L"

def main1():
	myList = readTuples('2.txt')

	score = {'X': 1, 'Y': 2, 'Z': 3, 'L': 0, 'D': 3, 'W': 6}

	totalScore = 0

	for match in myList:
		opponent, me = match[0], match[1]

		totalScore += score[me] + score[playMatch(opponent, me)]
		
	print totalScore

main1()




#Task 2

def findPlay(opponent, result):
	plays = ['A', 'B', 'C']
	
	if result == "X":
		return plays[plays.index(opponent) - 1]
	elif result == "Y":
		return opponent
	else:
		return plays[plays.index(opponent) -2]

def main2():
	myList = readTuples('2.txt')

	score = {'X': 0, 'Y': 3, 'Z': 6, 'A': 1, 'B': 2, 'C': 3}
	totalScore = 0

	for match in myList:
		opponent, result = match[0], match[1]

		totalScore += score[result] + score[findPlay(opponent, result)]

	print totalScore

	

main2()