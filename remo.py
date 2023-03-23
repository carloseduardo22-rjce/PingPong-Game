from turtle import Turtle


class Remo(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def suba(self):
        new_y = self.ycor() + 20
        # A função aumenta a posição da minha raquete então a atualiza usando o método goto, isso faz com que
        # a raquete se mova para cima da tela
        self.goto(self.xcor(), new_y)

    def desca(self):
        new_y = self.ycor() - 20
        # A função diminui a posição da minha raquete então a atualiza usando o método goto, isso faz com que
        # a raquete se mova para baixo da tela
        self.goto(self.xcor(), new_y)