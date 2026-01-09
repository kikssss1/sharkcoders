from random import randint
numero1= 0
while True:
    numero1=randint(1,5)
    jogador=int(input("adivinhe o numero de um a cinco"))
        if jogador==numero1:
            print("voce acertou")
        else:
            print("voce errou")