import time
import psutil
import turtle

win = turtle.Screen()
text = turtle.Turtle()
textadd = turtle.Turtle()
arrow  = turtle.Turtle()
semi_circle = turtle.Turtle()

win.setup(height=200,width=200)
win.bgcolor("black")
win.title("CVXR")
win.tracer(1)

text.pencolor("green")
text.hideturtle()
text.goto(0,20)
arrow.goto(0,-30)

semi_circle.pendown()
semi_circle.pencolor("white")
arrow.shapesize(stretch_len=-2)


textadd.pencolor("white")

semi_circle.speed(10000000)

semi_circle.penup()
semi_circle.goto(0,-60)
semi_circle.pendown()
semi_circle.circle(25)
semi_circle.penup()
semi_circle.pencolor("black")
semi_circle.fillcolor("black")
semi_circle.pendown()
semi_circle.goto(-20,-50)
semi_circle.pensize(25)
semi_circle.goto(20,-50)
semi_circle.hideturtle()


textadd.hideturtle()
textadd.penup()
textadd.goto(-20,-60)
textadd.pencolor("green")
textadd.write("Low",align="center",font=(r"Perfect DOS VGA 437 Win",8))
textadd.goto(20,-60)
textadd.pencolor("red")
textadd.write("High",align="center",font=(r"Perfect DOS VGA 437 Win",8))
textadd.hideturtle()


      


    

while True:
   value = psutil.virtual_memory().percent


   value = value
   persentvalue = -value * 2
   mainval = "RAM  %"+str(value)

   win.tracer(0)
   win.update()
   text.clear()
   if persentvalue <= -180.0:
      text.pencolor("red")

   if persentvalue >= -180.0:
      text.pencolor("green")

   

 
   text.write(mainval,font=(r"Perfect DOS VGA 437 Win",20),align="center")
   win.update()
   win.tracer(1)
   arrow.showturtle()
   if persentvalue <= -180.0:
      arrow.pencolor("red")

   if persentvalue >= -180.0:
      arrow.pencolor("green")  
   


   
   arrow.setheading(persentvalue)
   
   
   


