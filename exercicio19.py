from datetime import date
ano= int(input("digite a sua data de nascimento: "))
idade= date.today().year-ano
if idade<18:
    print("você não tem idade para ir para o exército")
elif idade>18 and idade<65:
    print("você pode ir para o exército")
else:
    print("Não pode ir para o exército")
