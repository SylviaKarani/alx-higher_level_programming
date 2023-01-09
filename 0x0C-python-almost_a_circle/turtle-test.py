#!/usr/bin/python3
import turtle

size = 200

turt = turtle.Turtle()
turt.screen.bgcolor("#000")
turt.pensize(1)
turt.shape("turtle")

turt.color("#fff")

turt.showturtle()
turt.up()
turt.goto(-50, 300)
turt.down()
turt.write("Rectangles")
turt.up()
turt.goto(10, 10)
turt.down()


turt.goto(size, 10)
turt.goto(size, size / 2)
turt.goto(10, size / 2)
turt.goto(10, 10)
turt.up()
turt.home()

turt.hideturtle()

turt.showturtle()
turt.up()
turt.goto(-(20 + size), 10)
turt.down()

turt.forward(size)
turt.left(90)
turt.forward(size / 2)
turt.left(90)
turt.forward(size)
turt.left(90)
turt.forward(size / 2)


turt.hideturtle()

turtle.exitonclick()
