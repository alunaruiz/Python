from turtle import *
def Dibujar_Cuadrado (parametro):
    color('red','yellow')
    begin_fill()
    for _ in range(4):
        fd(parametro)
        rt(90)
    end_fill()
    done()
Dibujar_Cuadrado(200)