from random import randint
from time import sleep

saldo = randint(100, 200)

while True:
    li = []
    for x in range(3):
         n = randint(1,6)
         li.append(n)

    print("Bem vindo ao Slot\n")
    print("3 numeros iguais =  Aposta x 50\n2 numeros iguais =  Aposta x 3\n 3 numeros diferentes = perde valor apostado")
    print(f"Seu saldo atual é de {saldo} euros")
    print ()
    aposta = int(input("Qual a quantidade que deseja paostar aposta?"))
    if saldo >= aposta:
        input("Aperte ENTER para iniciar")
        print("Girando. . . ")
        sleep (2)
        for x in li:
            print([x], end="  ")
            sleep (2)
        if li[0] == li[1] or li[0] == li[2] or li[1] == li[2]:
            ganhos = aposta*3
            saldo += ganhos
            print ()
            print(f"Parabens! fez uma dupla e ganhou {ganhos} euros")
            print(f"Saldo atual é {saldo} euros")
        elif li[0] == li[1] == li[2]:
            ganhos = aposta*50
            saldo += ganhos
            print(f"Parabens! Ganhou {ganhos} euros")
            print(f"Parabens! O seu saldo agora é de {saldo} euros")
        else :
            saldo -= aposta
            print(f"Nao ganhou nada")
            print(f"O saldo agora é de {saldo} euros")
