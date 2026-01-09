def acharLetra ():
    frase=input('Digite uma frase: ')
    letra=input('Digite uma letra: ')
    computador = 0
    if letra in frase:
      for e in frase:
        if e == letra:
            computador = computador + 1
        print(computador)
    else:
        print("valor incorreto")

acharLetra()