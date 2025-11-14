maior= 0
menor= 0
for i in range(5):
    pesos= int(input("digite o seu peso no últimos 5 meses: "))
    if i==0:
        maior = menor = pesos
    if pesos>maior:
        maior = pesos
    if pesos < menor:
        menor = pesos