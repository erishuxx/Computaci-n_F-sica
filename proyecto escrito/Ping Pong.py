#Importamos la libreria turtle que nos permite crear gráficos
import turtle

#Creamos la ventana donde veremos el juego
wn = turtle.Screen()
#Configruamos la ventana
wn.title("Ping-Pong - Equipo 6")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#creamos el marcador
marcadorA = 0
marcadorB = 0

#Creamos los objetos del juego
#Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=3.5, stretch_len=0.7)

#Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=3.5, stretch_len=0.7)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.17
pelota.dy = 0.17

#Linea divisora
linea = turtle.Turtle()
linea.color("white")
linea.goto(0, 400)
linea.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A: 0          Jugador B: 0", align="center", font=("Courier", 12, "normal"))

#Creamos las funciones para el movimiento de los objetos del juego
#Para el jugado A
def jugadorA_up(): 
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down(): 
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

#Para el jugado B
def jugadorB_up(): 
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down(): 
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#Conectar las funciones al teclado
#Para el jugador A
wn.listen()
wn.onkeypress(jugadorA_up, "w")

wn.listen()
wn.onkeypress(jugadorA_down, "s")

#Para el jugador B
wn.listen()
wn.onkeypress(jugadorB_up, "i")

wn.listen()
wn.onkeypress(jugadorB_down, "k")


#Creamos nuestro bucle principal para actualizar la ventana
while True: 
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Creamos los bordes de la pelota, es decir, que rebote cuando toque un borde
    if pelota.ycor() > 290:
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}          Jugador B: {}".format(marcadorA,marcadorB), align="center", font=("Courier", 12, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador A: {}          Jugador B: {}".format(marcadorA,marcadorB), align="center", font=("Courier", 12, "normal"))

    #Creamos las colisiones de la pelota
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < jugadorB.ycor() + 50
        and pelota.ycor() > jugadorB.ycor() -50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
        and (pelota.ycor() < jugadorA.ycor() + 50
        and pelota.ycor() > jugadorA.ycor() -50)):
        pelota.dx *= -1



