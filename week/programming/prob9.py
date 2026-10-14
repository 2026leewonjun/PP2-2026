#거북이 그래픽 문제

import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape("turtle")
t2.shape("turtle")

t1.forward(100)
t1.right(90)
t1.forward(100)

t2.left(90)
t2.forward(100)
t2.right(90)
t2.forward(100)

turtle.done()