import random
import time
import turtle
from turtle import Turtle
import math
import numpy as np



class Customer(Turtle):

    def __init__(self, name, reputation, xloc, yloc):
        super().__init__()
        self.name = name
        self.reputation = reputation
        self.xloc = xloc
        self.yloc = yloc

    def getxloc(self):
        return self.xloc

    def getyloc(self):
        return self.yloc

# window setup
w = turtle.Screen()
w.setup(500, 500)
turtle.penup()
w.title('Distance influence')
turtle.setpos(-100, 160)
turtle.bgcolor('coral1')
turtle.write('Distance influences', font=('Arial', 20, 'bold' ))
turtle.color('coral1')
turtle.speed(0)
turtle.penup()

# set the location
# color, loop to produce each object
list = []
distanceList = []
colorlist = ['red', 'blue', 'purple', 'black', 'orange']
namelist = ['Peter', 'Karen', 'Jimmy', 'Lisa', 'Giuliet']

def distance(a, a2, b, b2):
    d = math.hypot(a2 - a, b2 - b)
    return d

for i in range(5):

    x = random.randint(-100, 50)
    y = random.randint(-50, 100)

    a = Customer(namelist[i], random.randint(1,10), x, y )
    a.speed(0)
    print(a.name, ' is created with reputation ', a.reputation)
    a.color(colorlist[i])
    a.shape('circle')
    a.penup()
    a.setpos(x, y)
    distanceList.append((x, y))
    a.pendown()
    list.append(a)
    time.sleep(3)
#
print('------------------------------------------------------------------------')
for j in list:
    print('The location of ', j.name, ' is ', '(', j.xloc, ', ', j.yloc, ')')


list_array = np.array(distanceList)
n = len(list_array)
for r in range(len(list)):

    x1 = list_array[r][0] # 0,0
    y1 = list_array[r][1]  # 0,1
    print(x1, y1)

    for col in range(5-1):

        if col < 4:
            x2 = list_array[col+1][0]
            y2 = list_array[col+1][1]
            print('x2, y2 = ', x2, y2)
        else:
            x2 = list_array[col][0]
            y2 = list_array[col][1]


        D = distance(x1, x2, y1, y2)
        print(list[r].name, '&', list[col+1].name, ' = ', D)

        if D > 50 or 0:
            continue
        else:
            if list[r].reputation > list[col+1].reputation and list[r].reputation > 6:
                list[col+1].color = list[r].color
                turtle.setpos(list[col+1].getxloc(), list[col+1].getyloc())

                turtle.penup()
                turtle.shape('circle')
                turtle.color(colorlist[r])
                turtle.stamp()
                # turtle.pendown()
                print(list[col+1].name, ' will change preference according to ', list[r].name)
                print(turtle.color(colorlist[r]))

                # list.[col+1].color = list[r].color()

                time.sleep(2)









