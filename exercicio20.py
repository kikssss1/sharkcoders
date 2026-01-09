from datetime import date
anos=int(input("Em que ano nasceu?"))
idade = date.today().year-anos
if idade <9:
    print("Voce é da categoria benjamin")
elif idade <=14:
    print("Você é da categoria infantil")
elif idade <=19:
    print("voce é da categoria junior")
elif idade <=25:
    print("voce está na categoria sénior")
else:
    print("Voce é da categoria master")