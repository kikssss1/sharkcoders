from random import randint
from time import sleep
vidaA= 15
vidaB= 15
while True:
    forcaA= randint(1,vidaA)
    forcaB= randint(1,vidaB)
    vidaB = vidaB - forcaA
    vidaA = vidaA - forcaB
    print(f"O lutador A deu um murro de força {forcaA} e a vida do lutador B foi para {vidaB}")
    print(f"O lutador B deu um murro de força {forcaB} e a vida do lutador A foi para {vidaA}")
    sleep(1)
    if vidaA <= 0:
        print("Jogador B ganha")
        break
    elif vidaB <= 0:
        print("Jogador A ganha")
        break