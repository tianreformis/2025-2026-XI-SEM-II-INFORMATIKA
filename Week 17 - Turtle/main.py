import turtle

#refactoring function
t = turtle.Turtle()
screen = turtle.Screen()

#setup the turtle
height = 800
width = 800
screen.setup(width, height) #set the screen size to 800x800
t.speed(10000) #set the turtle speed to 1 (slowest)
t.color("blue") #set the pen color to blue
t.pensize(5) #set the pen size to 5
screen.bgcolor("black") #set the background color to black

#posisi
t.penup() #lift the pen up to move without drawing
t.goto(0, 0) #move the turtle to the starting position
t.pendown() #put the pen down to start drawing

t.begin_fill() #start filling the shape
t.fillcolor("red") #set the fill color to cyan
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)

t.end_fill() #end filling the shape
turtle.done()