__author__ = 'yzy1986'

import random
random.gauss( 50,10) + random.gauss( 70, 10 )

import pylab
a = 1.0
b = 2.0
c = 4.0
yVals = []
xVals = range(-20, 20)
for x in xVals:
    yVals.append(a*x**2 + b*x + c)
yVals = 2*pylab.array(yVals)
xVals = pylab.array(xVals)
try:
    a, b, c, d = pylab.polyfit(xVals, yVals, 3)
    print a, b, c, d
except:
    print 'fell to here'

import statistics
a = [0,1,2,3,4,5,6,7,8]
b = [5,10,10,10,15]
c = [0,1,2,4,6,8]
d = [6,7,11,12,13,15]
e = [9,0,0,3,3,3,6,6]

statistics.mean(a)
statistics.pvariance(a)
statistics.mean(b)
statistics.pvariance(b)
statistics.mean(c)
statistics.pvariance(c)
statistics.mean(d)
statistics.pvariance(d)
statistics.mean(e)
statistics.pvariance(e)

def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

possible_variance(a)
possible_variance(b)
possible_variance(c)
possible_variance(d)
possible_variance(e)

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    if CURRENTRABBITPOP < 10 : return None
    if CURRENTRABBITPOP < MAXRABBITPOP:
        temp = 0
        prob_rabb_reprod = 1.0 - CURRENTRABBITPOP*1.0/MAXRABBITPOP
        for i in range(CURRENTRABBITPOP):
            if random.random() < prob_rabb_reprod:
                temp+=1
        CURRENTRABBITPOP+=temp
        if CURRENTRABBITPOP > MAXRABBITPOP:
            CURRENTRABBITPOP = MAXRABBITPOP

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    if CURRENTFOXPOP < 10 : return None

    for i in range (CURRENTFOXPOP):
        prob_fox_eats_rabb = CURRENTRABBITPOP *1.0/ MAXRABBITPOP
        # print "prob_fox_eats_rabb", prob_fox_eats_rabb
        if random.random() < prob_fox_eats_rabb and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP-=1
            # print CURRENTFOXPOP, "win"
            if random.random() < 1.0/3.0 and CURRENTFOXPOP < CURRENTRABBITPOP:
                # print CURRENTFOXPOP,CURRENTRABBITPOP
                CURRENTFOXPOP+=1

        elif random.random() < 0.9 and CURRENTFOXPOP > 10:
            CURRENTFOXPOP-=1
            # print CURRENTFOXPOP, "lose"




def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO

    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations

CURRENTRABBITPOP = 500
MAXRABBITPOP = 1000
CURRENTFOXPOP = 30
y = runSimulation(200)
x = range(200)

pylab.plot(x, y[0])
pylab.plot(x, y[1])
pylab.show()

coeff = pylab.polyfit(x, y[0], 2)
pylab.plot(pylab.polyval(coeff, x))
pylab.show()

coeff = pylab.polyfit(x, y[1], 2)
pylab.plot(pylab.polyval(coeff, x))
pylab.show()
##----