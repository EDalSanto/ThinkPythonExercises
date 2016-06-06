from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.redraw()
bob.delay = 0.01

def koch(t,n):
    if n<3:
        fd(t,n)
        return
    m = n/3.0
    koch(t,m)
    lt(t,60)
    koch(t,m)
    rt(t,120)
    koch(t,m)
    lt(t,60)
    koch(t,m)

def snowflake(t,n):
    for i in range(3):
        koch(t,n)
        rt(t,120)

# snowflake(bob,300)

def quadratic(t,n):
    for i in range(4):
        koch(t,n)
        rt(t,90)

quadratic(bob,200)
