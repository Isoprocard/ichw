
# coding: utf-8

# In[ ]:


"""planets.py: Simulation of the Solar System.

__author__ = "Sun Siyuan"
__pkuid__  = "1600012120"
__email__  = sunsiyuan@pku.edu.cn"
"""

import sys
sys.setExecutionLimit(50000)

import turtle
wn=turtle.Screen()
Sun=turtle.Turtle()
Sun.shape("circle")
Sun.color("yellow")
Sun.stamp()

def ellipse(t,stdis,stangle,forw,stepdis,stepangle):
    t.shape("circle")
    t.speed(0)
    t.up()
    t.forward(forw)
    t.down()
    t.left(90)
    sumangle=0
    while sumangle<=90:
        t.forward(stdis)
        t.left(stangle)
        sumangle=sumangle+stangle
        stangle=stangle+stepangle
        stdis=stdis+stepdis
    while sumangle<=180:
        t.forward(stdis)
        t.left(stangle)
        sumangle=sumangle+stangle
        stangle=stangle-stepangle
        stdis=stdis-stepdis
    while sumangle<=270:
        t.forward(stdis)
        t.left(stangle)
        sumangle=sumangle+stangle
        stangle=stangle+stepangle
        stdis=stdis+stepdis
    while sumangle<=360:
        t.forward(stdis)
        t.left(stangle)
        sumangle=sumangle+stangle
        stangle=stangle-stepangle
        stdis=stdis-stepdis
    t.stamp() 
    t.right(90)


def main():
    planet=turtle.Turtle()
    planet.color("gray")
    ellipse(planet,0.01,0.4,20,0.03,0.08)
    planet.color("orange")
    ellipse(planet,0.04,0.4,20,0.04,0.05)
    planet.color("blue")
    ellipse(planet,0.06,0.4,20,0.06,0.05)
    planet.color("red")
    ellipse(planet,0.08,0.4,40,0.1,0.05)
    planet.color("brown")
    ellipse(planet,0.12,0.4,20,0.13,0.05)
    planet.color("orangered")
    ellipse(planet,0.14,0.4,20,0.16,0.05)


if __name__ == '__main__':
    main()

