from random import randint
from time import sleep
ponto= 0
while True:
   numero1=randint (1,6)
   numero2=randint(1,6)
   if numero1==numero2:
       print("os valores sao iguais com os numeros", numero1)
       break
   else:
       ponto=ponto+1
       print("o primeiro valor foi", numero1)
       print("o segundo valor foi", numero2)
   sleep(1)
print(ponto) 