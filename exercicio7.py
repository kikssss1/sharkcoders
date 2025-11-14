numero1=int(input("escolha um numero inicial: "))
numero2=int(input("escolha um numero final: "))
soma= 0
variavel1= int(input("quer uma sequência de pares ou ímpares?: "))
if variavel1 == "par":
    print("você escoheu par confirme a sequência abaixo")
elif variavel1 == "impar":
    print("voce escolheu impar confirme a sequencia abaixo")
for i in range (numero1, numero2):
    if numero1 == "par" :
      if i!= 0:
          print(i)
          soma+=i
    elif numero1 == "impar" :
        if i != 0 :
          print(i)
if i %2==0:
    print(i)