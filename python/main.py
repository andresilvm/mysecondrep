import turtle
import math

bob = turtle.Turtle()
print(bob)


def square(length, t):
    for i in range(4):
        t.fd(length)
        t.rt(90)


def house_symple(t):
    square(100, t)
    t.lt(60)
    t.fd(100)
    t.rt(120)
    t.fd(100)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(length, n, t, angle):
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)

# house_symple(bob)

circle(bob, 50)
arc(bob, 50, 120)
bob.rt(45)
bob.fd(30)
bob.lt(120)
bob.fd(27.999)
bob.rt(45)
arc(bob, 50, 70)
bob.rt(45)
bob.fd(30)
bob.lt(120)
bob.fd(40)
bob.lt(30)
bob.pu()
bob.fd(25)
bob.pd()
circle(bob, 5)

turtle.mainloop()