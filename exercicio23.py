from random import randint
valor = randint (1,100)
while True:
    numero = int(input("Digite um numero: "))
    if numero > valor:
        print("menor")
    elif numero < valor:
        print("maior")
    else:
        print("igual")
        break