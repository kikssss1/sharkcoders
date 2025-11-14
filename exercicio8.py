paises = ["portugal", "espanha", "frança", "itália", "luxemburgo","alemanha", "reino unido", "irlanda","suiça","malta"\
    ,""]
for i in range (3):
    escolhas = input("escolha um país da europa: ")
    if escolhas in paises:
        print("conseguiste")
        break
