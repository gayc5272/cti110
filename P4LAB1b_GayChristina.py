import turtle

t= turtle.Turtle()
t.pensize(15)
t.pencolor("Red")

t.penup()
t.goto(-30,50)
t.pendown()
t.right(180)
t.circle(100,189)

t.penup()
t.goto(-30,50)
t.forward(180)
t.right(90)
t.pendown()
t.setheading(140)
t.circle(100,270)
t.setheading(90)
t.forward(50)
t.left(90)
t.forward(50)

turtle.done()
