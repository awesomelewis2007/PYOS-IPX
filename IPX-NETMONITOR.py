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
win.title("IPX")
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
textadd.write("Low",align="center")
textadd.goto(20,-60)
textadd.pencolor("red")
textadd.write("High",align="center")
textadd.hideturtle()
def main():
   old_value = 0    

   while True:
      new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
      if old_value:
         send_stat(new_value - old_value)

      old_value = new_value

      


    

def send_stat(value):
   persentvalue = value /200
   mainval = "B: "+str(value)

   negativepes = abs(-persentvalue)
   win.tracer(0)
   win.update()
   text.clear()
   if persentvalue >= 100.0:
      text.pencolor("red")

   if persentvalue <= 100.0:
      text.pencolor("green")

   

 
   text.write(mainval,font=(20),align="center")
   win.update()
   win.tracer(1)
   arrow.showturtle()
   if persentvalue >= 100.0:
      arrow.pencolor("red")

   if persentvalue <= 100.0:
      arrow.pencolor("green")  
   
   if persentvalue >= 200.0:
      arrow.setheading(180)

   if persentvalue <= 200.0:
      arrow.setheading(-negativepes)

   
   

main()
