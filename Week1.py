import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [1,7,3,5])
pylab.show()

for x in range(5):
	print x

def isAlphabeticalWord(word, wordList = None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList


### L1 Problem 3
import pylab
import numpy as np

PATH_TO_FILE = '/Users/yzy1986/Eugene\'s/Coursera/Computational Thinking and Data Science/julyTemps.txt'

def loadFile():
	inFile = open(PATH_TO_FILE, 'r', 0)
	high = []
	low = []
	for line in inFile:
	    fields = line.split()
	    if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
	        continue
	    else:
	        high.append(int(fields[1]))
	        low.append(int(fields[2]))
	return (low, high)

def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
        
(low, high) = loadFile()    
producePlot(low, high)

# L2 Problem 2
def getEven():
	return random.randrange(0, 101, 2)

# L2 Problem 3A
import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0)
    return random.randrange(10, 21, 2)









