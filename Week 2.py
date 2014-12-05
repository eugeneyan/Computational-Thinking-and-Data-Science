# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:58:07 2014

@author: yzy1986
"""
### Week 2 Exercises

# L4 Problem 3

import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) < 1:
        return float('NaN')
        
    total_len = float(0)
    no_of_i = len(L)
    
    # find total length of all items
    for i in L:
        total_len += len(i)
      
    # calculate mean of all items  
    mean = total_len/no_of_i
    
    # init sum_of_diff
    sumsq_of_diff= 0
    
    # calculate variance
    for i in L:
        sumsq_of_diff += ((len(i) - mean)**2)
        
    # calculate sd
    sd = math.sqrt(sumsq_of_diff/no_of_i)
    
    return sd


    
L1 = ['a', 'z', 'p']
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
L3 = [10, 4, 12, 15, 20, 5]

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    