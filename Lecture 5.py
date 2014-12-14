__author__ = 'yzy1986'

### L5 Problem 1

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    num_trials = numTrials
    same_colour_count = 0

    # for i in num of trials:
    for trial in range(num_trials):

        # initialize three red balls and three green balls in a list
        balls = ['red', 'red', 'red', 'green', 'green', 'green']

        # randomly remove one ball and initialize to ball 1
        ball_1 = balls.pop(random.randrange(len(balls)))

        # randomly remove one ball and initialize to ball 2
        ball_2 = balls.pop(random.randrange(len(balls)))

        # randomly remove one ball and initialize to ball 3
        ball_3 = balls.pop(random.randrange(len(balls)))

        # if ball 1, 2, and 3 are same colour, add 1 to same_colour count
        if ball_1 == ball_2 == ball_3:
            same_colour_count += 1

    # return float(same_colour_count) / num_trials
    return float(same_colour_count) / num_trials

x = ['red', 'red', 'red', 'green', 'green', 'green']
x.pop(random.randrange(len(x))); print x
