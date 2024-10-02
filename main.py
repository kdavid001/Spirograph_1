import turtle as t
import random

tim = t.Turtle()
tony = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tony.speed("fastest")

def draw(size):
    heading = 0
    for _ in range(int(360/ size)):
        color = random_color()
        tony.color(color)
        tony.circle(100)
        tony.setheading(tim.heading()+ heading )
        heading += 1

draw(1)
  
