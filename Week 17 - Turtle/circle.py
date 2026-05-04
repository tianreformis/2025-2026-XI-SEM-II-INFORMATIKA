import turtle 

t =  turtle.Turtle()
screen = turtle.Screen()
#setup the turtle
height = 800
width = 800
screen.setup(width, height) #set the screen size to 800x800
t.speed(1) #set the turtle speed to 1 (slowest)

t.penup() #lift the pen up to move without drawing
t.goto(-100, -100) #move the turtle to the starting position
t.pendown() #put the pen down to start drawing

t.color("red") #set the pen color to blue
t.begin_fill() #start filling the shape
t.fillcolor("red") #set the fill color to cyan
t.circle(50)
t.end_fill() #end filling the shape

t.penup() #lift the pen up to move without drawing
t.goto(10, -100) #move the turtle to the starting position
t.pendown() #put the pen down to start drawing
t.color("black") #set the pen color to blue
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
turtle.done()