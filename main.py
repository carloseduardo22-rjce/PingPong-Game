from turtle import Screen
from remo import Remo
from bola import bola
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong game")
# O tracer é responsável pela a minha animação e colocando o valor 0 eu desligo ela
screen.tracer(0)

# raquete direita
r_remo = Remo((350, 0))
# raquete esquerda
l_remo = Remo((-350, 0))
bola = bola()
scoreboard = Scoreboard()

screen.listen()
# método responsável por ouvir meu teclado
screen.onkey(r_remo.suba, "Up")
screen.onkey(r_remo.desca, "Down")
screen.onkey(l_remo.suba, "w")
screen.onkey(l_remo.desca, "s")


game_comecou = True
while game_comecou:
    time.sleep(bola.move_speed)
    screen.update()
    bola.move()

    # Detectar colisão com a parede
    if bola.ycor() > 300 or bola.ycor() < - 300:
        bola.saltar_y()

    # Detectar colisão com as duas raquetes
    if bola.distance(r_remo) < 50 and bola.xcor() > 320 or bola.distance(l_remo) < 50 and bola.xcor() < - 320:
        bola.saltar_x()

    # Detectar quando a raquete direita falhar
    if bola.xcor() > 350:
        bola.reset_posicao_x()
        scoreboard.l_point()


    # Detectar quando a raquete esquerda falhar
    if bola.xcor() < - 350:
        bola.reset_posicao_x()
        scoreboard.r_point()




# dimensões raquete
# width = 20
#height = 100
#x_pos = 350
#y_pos = 0

# método de rastreio que controla minha animação e para desliga-lá só precisamos por um 0







screen.exitonclick()