# -- INPUT --
def readTuples(filename):
	return [tuple(map(str, line.rstrip().split(" "))) for line in open(filename)]

def readLines(filename):
	return [line.rstrip() for line in open(filename)]



# -- ARRAYS --

def created2dArray(width, height, value=0):
	return [[value for i in range(width)] for j in range(height)]