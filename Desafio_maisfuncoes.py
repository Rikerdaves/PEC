from turtle import *

def desenhar_poligono(lados, comprimento, cor_contorno, cor_preenchimento):
    color(cor_contorno)
    fillcolor(cor_preenchimento)
    
    pendown()
    begin_fill()

    for _ in range(lados):
        forward(comprimento)
        left(360 / lados)

    end_fill()
    penup()

def main():
    speed(2)  # Ajusta a velocidade da tartaruga

    # Desenha um triângulo
    desenhar_poligono(3, 100, "blue", "yellow")

    # Move a tartaruga para uma nova posição
    goto(200, 0)

    # Desenha um quadrado
    desenhar_poligono(4, 100, "red", "green")

    done()

if __name__ == "__main__":
    main()
