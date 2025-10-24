tipo = (input("Qual o seu tipo de residencia? "))
kwh = int(input("Quantos kwh gastou? "))
if tipo== "residencial" :
    if kwh<=500:
        print("vai ter de pagar", 0.4*kwh ,"£")
    else :
        print("vai ter de pagar", 0.65*kwh ,"£")
elif tipo== "comercial" :
    if kwh<=1000:
         print("vai ter de pagar", 0.55*kwh ,"£")
    else:
         print("vai ter de pagar", 0.6*kwh ,"£")
elif tipo== "industrial" :
    if kwh<=5000:
        print("vai ter de pagar", 0.55*kwh ,"£")
    else :
        print("vai ter de pagar" ,0.6*kwh ,"£")
else:
    print("Valores incorretos")
