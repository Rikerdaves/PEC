from turtle import *
import random

def desenhar_estrela():
    penup()
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    goto(x, y)
    dot(random.randint(1, 5), "white")

def desenhar_ceu_estrelado(num_estrelas):
    bgcolor("black")  # Define a cor de fundo como preto

    for _ in range(num_estrelas):
        desenhar_estrela()

    done()

def main():
    speed(0)  # Define a velocidade da tartaruga (0 é a velocidade máxima)

    num_estrelas = int(input("Digite o número de estrelas desejado: "))
    
    desenhar_ceu_estrelado(num_estrelas)

if __name__ == "__main__":
    main()
