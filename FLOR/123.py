from turtle import *

def tallo():
    speed(40)
    bgcolor("black")
    penup()
    goto(0, -100)
    pendown()
    color("green")
    begin_fill()
    rt(90)
    fd(400)
    lt(90)
    fd(20)
    lt(90)
    fd(400)
    lt(90)
    fd(20)
    end_fill

def dibujar_hojas():
    m = 0
    penup()
    goto(0, 0)
    pendown()
    for i in range(16):
        for j in range(18):
            color("yellow")
            m += 0.005
            rt(90)
            circle(150 - j * 6, 90)
            lt(90)
            circle(150 - j * 6, 90)
            rt(180)
        circle(40, 24)

def dibujar_centro():
    penup()
    goto(-20, 0)
    pendown()
    color("#8B4513")
    begin_fill()
    circle(44)
    color("red")
    write("PARA EL AMOR DE MI VIDA", align="center", font=("Brush Script MT",45, "normal"))
    end_fill

tallo()
dibujar_hojas()
dibujar_centro()

done()
    
            

    
    