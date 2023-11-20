from turtle import *

def drawPlanet(size, color):
    pensize(2)  # Define a largura da caneta
    pencolor("black")  # Define a cor do contorno

    # Desenha o planeta
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()

def main():
    speed(2)  # Define a velocidade da tartaruga

    # Desenha um planeta azul
    drawPlanet(100, "blue")

    # Move a tartaruga para uma nova posição
    penup()
    goto(200, 0)

    # Desenha um planeta vermelho
    drawPlanet(80, "red")

    done()

if __name__ == "__main__":
    main()
