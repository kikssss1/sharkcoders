import random
def resultados (jogador, computador):
    if jogador==computador:
        return "empate"
    elif (jogador=="pedra" and computador=="tesoura")or \
        (jogador=="papel" and computador=="pedra")or \
        (jogador=="tesoura" and computador=="papel"):
        return "ganhou"
    else:
        return "perdeu"

opçoes = ["pedra", "papel", "tesoura"]

while True:
    computador = random.choice(opçoes)
    jogador = (input("escolha pedra pappel ou tesoura "))


    print(f"computador jogou {computador} e jogador {jogador}")
    resultado = resultados(jogador, computador)
    print(resultado)