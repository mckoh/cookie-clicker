"""
Cookie Clicker Main
Author: Michael KOHLEGGER
Date: October 2024
"""

import turtle

cookie_count = 0
cps = 1
TICK_TIME = 1000

canvas = turtle.Screen()
canvas.title("Cookie Clicker by Mike Kohlegger")
canvas.bgcolor("black")

canvas.register_shape("cookie.gif")
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"cookie_count: {cookie_count}", align="center", font=("Courier New", 32, "normal"))

def clicked(x=0, y=0):
    global cookie_count
    cookie_count += 1

def tick(x=0, y=0):
    global cookie_count
    global cps

    cookie.onclick(clicked)

    cookie_count += cps
    pen.clear()
    pen.write(f"cookie_count: {cookie_count}", align="center", font=("Courier New", 32, "normal"))

turtle.ontimer(tick, TICK_TIME)

canvas.mainloop()
