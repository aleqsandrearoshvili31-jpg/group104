from turtle import *

# we want to make a house

#step1: draw a square
speed(15)
width(5)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)

#step2: draw a door

left(90)

forward(75)

color("black")
left(90)

forward(100)

right(90)

forward(50)

right(90)

forward(100)
#step3:draw a roof
color("brown")

right(90)

forward(75)

left(180)

forward(150)

left(90)

forward(200)

left(30)

forward(100)
left(60)
forward(100)
left(60)
forward(100)
left(30)
forward(30)
left(90)
#step4: draw a windows
penup()
goto(20, 170)
pendown()
color("black")
forward (40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)
right(90)
forward(20)
right(90)
penup()
goto(180, 170)
pendown()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)
penup()
goto(0, 0)
pendown()
right(90)
color("green")
width(20)
forward(100)
left(90)
forward(10)
left(90)
forward(400)
left(90)
forward(10)
left(90)
forward(100)
right(180)
forward(100)
right(90)
forward(20)
right(90)
forward(800)
right(90)
forward(20)
right(90)
forward(400)
left(180)
forward(150)
right(90)
#step5:maiking a tree
width(30)
color("brown")
forward(70)
right(90)
width(20)
color("green")
forward(70)
left(180)
forward(140)
right(109)
forward(200)
right(138)
forward(200)

exitonclick()
