# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:13:57 2014

@author: yzy1986
"""

class Point:
    pass

blank = Point()
blank.x = 3.0
blank.y = 4.0

print '(' + str(blank.x) + ', ' + str(blank.y) + ')' 
distanceSquared = blank.x * blank.x + blank.y * blank.y 
print distanceSquared

def printPoint(p): 
  print '(' + str(p.x) + ', ' + str(p.y) + ')' 
  
printPoint(blank)

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point() 
box.corner.x = 0.0 
box.corner.y = 0.0 

def findCenter(box): 
  p = Point() 
  p.x = box.corner.x + box.width/2.0 
  p.y = box.corner.y - box.height/2.0 
  return p 

center = findCenter(box)

printPoint(center)

box.width = box.width + 50
box.height += 100

def growRect(box, dwidth, dheight):
    import copy
    newBox = copy.deepcopy(box)
    box.width += dwidth
    box.height += dheight
    return newBox

bob = Rectangle()
bob.width = 100.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0
growRect(bob, 50, 100)

class Time: 
  def __init__(self, hours=0, minutes=0, seconds=0): 
    self.hours = hours 
    self.minutes = minutes 
    self.seconds = seconds

  def printTime(time): 
    print str(time.hours) + ":" + \
    str(time.minutes) + ":" + \
    str(time.seconds)

currentTime = Time(9, 14, 30)
currentTime.printTime()

class Point: 
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y 

    def __str__(self): 
        return '(' + str(self.x) + ', ' + str(self.y) + ')' 

    def __add__(self, other): 
        return Point(self.x + other.x, self.y + other.y) 
        
    def __mul__(self, other): 
        return self.x * other.x + self.y * other.y 

    def __rmul__(self, other): 
        return Point(other * self.x,  other * self.y)
        
        
p1 = Point(3,4)
p2 = Point(5, 7)
p3 = p1 + p2
print p3

print p1*p2
print 2*p2

