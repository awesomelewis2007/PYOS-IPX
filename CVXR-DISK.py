from os import replace
import time
import psutil
import turtle

win = turtle.Screen()
text = turtle.Turtle()


win.setup(height=200,width=200)
win.bgcolor("black")
win.title("CVXR")
win.tracer(1)

text.pencolor("green")
text.hideturtle()
text.goto(0,-20)



while True:
    value = psutil.disk_usage("C:/")
    value = str(value)
    value = value.replace(",","\n").replace("sdiskusage("," ").replace(")","")

    win.tracer(0)
    win.update()
    text.clear()
    text.write(value,align="center",font=(r"Perfect DOS VGA 437 Win",12))
    win.update()



    
 
 
    

    
   
   


