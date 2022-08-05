'''
Make a class Circle that can be initialized with a single parameter. So
far super easy, right? How about we make a requirement that Circle can
initialize using any type related to a description of a circle--radius, 
list of two points representing the center and a point on the circumference, 
or the circumference length. I'll make some of the types to get you started. 

We will use @dataclass to make various types that hold data--Radius, Circle, Point
PointSet, Circumference etc. @dataclass decorates class definitions and 
reduces the boilerplate code--allowing you to simply list the attributes holding
data. 

Make an circle.area attribute that returns the area. 

>>> r = Radius(1)

>>> print(r)
Radius(length=1)

>>> p = Point(0,0)

>>> print(p)
Point(x=0, y=0)

>>> circ = Circumference(pi)

>>> round(circ.length, 2)
3.14

>>> type(circ)
<class '__main__.Circumference'>

>>> c3 = Circle(circ)

>>> assert c3.area == pi * (1/2)**2

>>> c1 = Circle(Radius(1))

>>> assert c1.area == pi * 1**2

>>> c2 = Circle(PointSet(Point(0,0), Point(0,1)))

>>> assert c2.area == pi * 1**2

>>> c4 = Circle(PointSet(Point(0,0), Point(sqrt(1/2),sqrt(1/2)) ))

>>> assert c4.area == pi * 1**2

>>> assert Circle(Radius(1)).area == Circle(PointSet(Point(1,1), Point(2,1))).area
'''

# Write your code here:
from math import pi, sqrt
from dataclasses import dataclass

@dataclass
class Radius:
    length: float

@dataclass
class Point:
    x: float
    y: float

from functools import singledispatchmethod
class Circle:
    @singledispatchmethod
    def __init__(self, unrecognized_type):
        raise ValueError(f"unsupported data: {unrecognized_type}")

    @__init__.register(Radius)
    def _from_radius(self, radius):
        self.radius = radius.length

        
# Do not edit any code below this line!
if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nWOOT! You know how to singledispatch initialize')

# Part of Powerful Python. Copyright MigrateUp LLC. All rights reserved.

