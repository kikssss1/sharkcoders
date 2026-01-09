import math
def escolher_funcao():
    global escolhe
    print()
    escolhe= int(input("escolhe a conta: "))
    print ()

def soma (x,y):
    r=x+y
    print("O resultado da soma é", r)

def subtracao (x,y):
    r=x-y
    print("resultado da subtraçao é", r)

def multiplicacao (x,y):
    r=x*y
    print("Resultado da multiçao", r)

def divisao (x,y):
    r=x/y
    print("resultado da divisão é", r)

def raiz_quadrada (x):
    r = math.sqrt(x)
    print("resultado da raiz quadrado", r)

def potencia (x, y):
    r=x**y
    print("resultado potencia", r)

def volume_prisma (x, y, z):
    r=x*y*z
    print("resultado do volume prisma", r)

def volume_cilindro (x, y, z):
    r=(math.pi*y**2*z)
    print("resultado do volume cilindro", r)

def volume_cone (x, y, z):
    r=math.pi*y*z
    print("resultado do volume cone", r)

def volume_esfera (y):
    r= 4*( math.pi*y**3)/3
    print("resultado do volume esfera", r)

while True:
    escolher_funcao()
    if escolhe == 0:
        break
    elif escolhe == 1:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        soma(x,y)
    elif escolhe == 2:
        x = int(input("entre com o valor A: "))
        y = int(input("entre com o valor B: "))
        subtracao(x,y)
    elif escolhe == 3:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        multiplicacao(x, y)
    elif escolhe == 4:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        divisao(x, y)
    elif escolhe == 5:
        x = int(input("entro com o valor A: "))
        raiz_quadrada(x)
    elif escolhe == 6:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        potencia(x, y)
    elif escolhe == 7:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        z = int(input("entro com o valor C: "))
        volume_prisma(x, y, z)
    elif escolhe == 8:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        z = int(input("entro com o valor C: "))
        volume_cilindro(x, y, z)
    elif escolhe == 9:
        x = int(input("entro com o valor A: "))
        y = int(input("entro com o valor B: "))
        z = int(input("entro com o valor C: "))
        volume_cone(x, y, z)
    elif escolhe == 10:
        x = int(input("entro com o valor A: "))
        volume_esfera(x)



