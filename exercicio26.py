def blackjack():
    print("bem vindo ao Black Jack\n")
    from random import randint
    saldo = randint (150, 200)
    cartas = randint(2,10)
    print("O seu saldo é igual a", saldo)
    aposta = int(input("Quanto quer apostar?"))
    if saldo >= aposta:
        while True:
            print(f'\nIniciou com {cartas} pontos\n')
            opc = int(input("Deseja comprar mais cartas?\n1 - SIM\n2 - NÃO\nOpção:"))
            if opc == 1:
                cartas += randint (2,10)
                if cartas > 21:
                    saldo -= aposta
                    print(f"parabens perdeste á banca! perdeste mais {aposta} pontos")
                    print(f"seu saldo atual é de {saldo} euros\n")
                    break
            elif opc == 2:
                print(cartas)
                banca = randint(15,21)
                print(f'\n A banca somou", banca "pontos')
                if cartas >= banca:
                    print()
                    ganhos = aposta * 2
                    saldo += ganhos
                    print(f"parabens ganhaste a banca! Somou mais {ganhos} pontos")
                    print(f"seu saldo atual é de {saldo} euros\n")
                    break
                else:
                    print()
                    saldo -= aposta
                    print(f"parabens perdeste á banca! perdeste mais {aposta} pontos")
                    print(f"seu saldo atual é de {saldo} euros\n")
                    break






blackjack()