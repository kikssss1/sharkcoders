from random import randint
from time import sleep

def fairy ():
    fairyhealth = randint(1,20)
    fairystrenght = randint(1,20)

    fairy = [fairyhealth, fairystrenght]
    return fairy

def dice ():
    return int (randint(1, 20))

def gooblins ():
    gooblinsHealth = randint(1,20)
    gooblinsStrenght = randint(1,20)


    gooblins = [gooblinsHealth, gooblinsStrenght]
    return gooblins

def status ():
    playerhealth = (randint(15,25))
    print("health",playerhealth)
    playerstrenght = (randint(15,25))
    print("strenght",playerstrenght)

    player = [playerhealth, playerstrenght]
    return player
    #a ordem começa no zeroooo ZEROO

player = status()
fairy = fairy()
gooblins = gooblins()
dice = dice()

print("⚔️𝖂𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖙𝖍𝖊 𝕯𝖚𝖓𝖌𝖊𝖔𝖓𝖘 𝖇𝖗𝖆𝖛𝖊 𝖙𝖗𝖆𝖛𝖊𝖑𝖑𝖊𝖗⚔️\n"
      "𝕾𝖊𝖑𝖊𝖈𝖙 𝖞𝖔𝖚𝖗 𝖈𝖍𝖆𝖗𝖆𝖈𝖙𝖊𝖗, 𝖏𝖚𝖘𝖙 𝖗𝖊𝖒𝖊𝖒𝖇𝖊𝖗 𝖞𝖔𝖚 𝖈𝖆𝖓𝖙 𝖌𝖔 𝖇𝖆𝖈𝖐!!")
personagem = input("𝖜𝖎𝖑𝖑 𝖙𝖍𝖊 𝖜𝖎𝖟𝖆𝖗𝖉 (A)\n" "𝕷𝖚𝖈𝖆𝖘 𝖙𝖍𝖊 𝖆𝖗𝖈𝖍𝖊𝖗 (B)\n" "𝕸𝖎𝖐𝖊 𝖙𝖍𝖊 𝖐𝖓𝖎𝖌𝖍𝖙 (C)\n" "𝕯𝖚𝖘𝖙𝖎𝖓 𝖙𝖍𝖊 𝖜𝖎𝖘𝖊 (D)\n")
sleep(1)
if personagem.upper() == "A":
    print("𝖂𝖎𝖑𝖑 𝖙𝖍𝖊 𝖜𝖎𝖟𝖆𝖗𝖉 𝖘𝖊𝖑𝖊𝖈𝖙𝖊𝖉 🧙‍♂️")
    print("𝖂𝖎𝖑𝖑 𝖙𝖍𝖊 𝖜𝖎𝖟𝖆𝖗𝖉 𝖎𝖘 𝖆 𝖆𝖕𝖕𝖗𝖊𝖓𝖙𝖎𝖈𝖊 𝖋𝖗𝖔𝖒 𝖌𝖆𝖓𝖉𝖆𝖑𝖋 𝖙𝖍𝖊 𝖜𝖍𝖎𝖙𝖊, 𝖇𝖔𝖗𝖓 𝖎𝖓 𝕲𝖔𝖓𝖉𝖔𝖗 𝖗𝖆𝖎𝖘𝖊𝖉 𝖇𝖞 𝖗𝖔𝖞𝖆𝖑𝖙𝖞.")
    print(status())
elif personagem.upper() == "B":
    print("𝕷𝖚𝖈𝖆𝖘 𝖙𝖍𝖊 𝖆𝖗𝖈𝖍𝖊𝖗 𝖘𝖊𝖑𝖊𝖈𝖙𝖊𝖉 🧝🏻‍♀️🏹")
    print("𝕷𝖚𝖈𝖆𝖘 𝖎𝖘 𝖇𝖗𝖆𝖛𝖊 𝖆𝖗𝖈𝖍𝖔𝖗 𝖊𝖑𝖋 𝖙𝖗𝖆𝖎𝖓𝖊𝖉 𝖆𝖓𝖉 𝖗𝖆𝖎𝖘𝖊𝖉 𝖇𝖞 𝖙𝖍𝖊 𝖊𝖑𝖋𝖘 𝖔𝖋 𝕷𝖔𝖙𝖍𝖑ó𝖗𝖎𝖊𝖓")
    print(status())
elif personagem.upper() == "C":
    print("𝕸𝖎𝖐𝖊 𝖙𝖍𝖊 𝖐𝖓𝖎𝖌𝖍𝖙 𝖘𝖊𝖑𝖊𝖈𝖙𝖊𝖉🗡️")
    print("𝕸𝖎𝖐𝖊 𝖆 𝖆𝖕𝖕𝖗𝖊𝖓𝖙𝖎𝖈𝖊 𝖋𝖗𝖔𝖒 𝕾𝖆𝖗𝖚𝖒𝖆𝖓, 𝖇𝖔𝖗𝖓 𝖆𝖓𝖉 𝖗𝖆𝖎𝖘𝖊𝖉 𝖎𝖓 𝕽𝖔𝖍𝖆𝖓")
    print(status())
elif personagem.upper() == "D":
    print("𝕯𝖚𝖘𝖙𝖎𝖓 𝖙𝖍𝖊 𝖜𝖎𝖘𝖊 𝖘𝖊𝖑𝖊𝖈𝖙𝖊𝖉 🕵️‍♂️")
    print("𝕯𝖚𝖘𝖙𝖎𝖓 𝖎𝖘 𝖆 𝖍𝖔𝖇𝖇𝖎𝖙, 𝖕𝖆𝖗𝖙 𝖔𝖋 𝖆 𝖘𝖔𝖈𝖎𝖊𝖆𝖙𝖞 𝖔𝖋 𝖙𝖎𝖓𝖞 𝖆𝖓𝖉 𝖈𝖚𝖙𝖊 𝖈𝖗𝖊𝖆𝖙𝖚𝖗𝖊𝖘 𝖋𝖗𝖔𝖒 𝖆 𝖘𝖎𝖒𝖕𝖑𝖊 𝖆𝖓𝖉 𝖘𝖒𝖆𝖑𝖑 𝖐𝖎𝖓𝖌𝖉𝖔𝖔𝖒 𝕳𝖔𝖇𝖇𝖎𝖙𝖔𝖓")
    print(status())
print("𝕬𝖗𝖊 𝖞𝖔𝖚 𝖗𝖊𝖆𝖉𝖞? 𝕷𝖊𝖙𝖘 𝕲𝕺𝕺𝕺")
sleep(1)
while True:
    escolha = int(input("𝖄𝖔𝖚 𝖋𝖔𝖚𝖓𝖉 𝖘𝖔𝖒𝖊 𝖌𝖔𝖔𝖇𝖑𝖎𝖓𝖘 𝖜𝖍𝖆𝖙 𝖉𝖔 𝖞𝖔𝖚 𝖉𝖔?"
                    "\n 𝕬𝖙𝖙𝖆𝖈𝖐 - 1    \n 𝕽𝖚𝖓 - 2  "))
    print(gooblins)
    if escolha ==1:
        print("𝕽𝖔𝖑𝖑 𝖞𝖔𝖚𝖗 𝖉𝖎𝖈𝖊!!🎲")
        sleep(1)
        break
    elif escolha ==2:
        print("𝖄𝖔𝖚 𝖙𝖗𝖎𝖊𝖉 𝖙𝖔 𝖕𝖆𝖘𝖘 𝖙𝖗𝖔𝖚𝖌𝖍𝖙 𝖙𝖍𝖊𝖒 𝖇𝖚𝖙 𝖞𝖔𝖚 𝖋𝖆𝖎𝖑𝖊𝖉")
while True :
    if player[0] >= 1:
        dice = randint(1, 20)
        print("𝕿𝖍𝖊 𝖉𝖎𝖈𝖊 𝖗𝖔𝖑𝖑𝖊𝖉🎲", dice)
        if dice >= 10:
            print("𝖄𝖔𝖚 𝖉𝖊𝖆𝖑𝖑𝖊𝖉", player[1]/2)
            gooblins[0] = player[1]/2-player[0]
            if gooblins[0] - player[1] == 0:
                print("𝕮𝖔𝖓𝖌𝖗𝖆𝖙𝖘 𝖞𝖔𝖚 𝖐𝖎𝖑𝖑𝖊𝖉 𝖙𝖍𝖊𝖒")
            elif gooblins[0] == 10:
                print("𝕲𝖔𝖔𝖇𝖑𝖎𝖓'𝖘 𝖙𝖚𝖗𝖓")
                sleep(1)
                damagegooblin = print("𝕲𝖔𝖔𝖇𝖑𝖎𝖓 𝖉𝖊𝖆𝖑𝖊𝖉", randint(1, gooblins[1]))
                print("𝖄𝖔𝖚'𝖗𝖊", gooblins[1] - player[0] ,"ℋ𝒫")
                print("𝖄𝖔𝖚 𝖈𝖆𝖓 𝖉𝖔 𝖎𝖙! 𝕽𝖔𝖑𝖑 𝖙𝖍𝖊 𝖉𝖎𝖈𝖊 𝖆𝖌𝖆𝖎𝖓🎲")
        elif dice <= 10:
                print("𝖞𝖔𝖚 𝖑𝖔𝖔𝖘𝖊..")
                player[0] = 0
                break
        else:
                print("𝖞𝖔𝖚 𝖐𝖎𝖑𝖑𝖊𝖉 𝖙𝖍𝖊𝖒!")
                sleep(1)
    print("𝕷𝖊𝖙'𝖘 𝖈𝖔𝖓𝖙𝖎𝖓𝖚𝖊, \n"
          "𝖆𝖋𝖙𝖊𝖗 𝖆 𝖑𝖔𝖓𝖌 𝖏𝖔𝖗𝖓𝖊𝖞 𝖎𝖓 𝖙𝖍𝖊 𝖉𝖚𝖓𝖌𝖊𝖔𝖓𝖘 𝖞𝖔𝖚 𝖋𝖔𝖚𝖓𝖉 𝖆 𝖑𝖎𝖙𝖙𝖑𝖊 𝖋𝖆𝖎𝖗𝖞..\n"
          "𝖜𝖍𝖊𝖓 𝖞𝖔𝖚 𝖌𝖔𝖙 𝖈𝖑𝖔𝖘𝖊 𝖙𝖔 𝖎𝖙, 𝕴𝕿 𝕭𝕴𝕿𝕰𝕯 𝖄𝕺𝖀🧚🏼‍♂️")
    sleep(1)
    print(fairy)
    fairybite = player[0]-(randint (1,5))
    break
while player[0] > 0 and  fairy[0] > 0:
        choise = input("𝕽𝖔𝖑𝖑 𝖙𝖍𝖊 𝖉𝖎𝖈𝖊!!🎲\n"
                      "𝖞𝖊𝖘\n"
                      "𝖓𝖔 "  )
        if choise == "yes":
                    dice = int(randint(1, 20))
                    print("𝕿𝖍𝖊 𝖉𝖎𝖈𝖊 𝖎𝖘 𝖗𝖔𝖑𝖑𝖎𝖓𝖌...🎲")
                    sleep(1)
                    print ("𝕿𝖍𝖊 𝖉𝖎𝖈𝖊 𝖗𝖔𝖑𝖑𝖊𝖉🎲", dice)
                    fairy[0] = fairy[0] - player[1]
                    if dice >= 15 and fairy[0] <= 0 :
                        print("🎊𝓨𝓞𝓤 𝓦𝓞𝓝𝓝!!🎉")
                        break
                    else:
                        fairy[0] = fairy[0] - player[1]/2
                        print("𝖕𝖑𝖆𝖞𝖊𝖗 𝖉𝖊𝖆𝖑𝖑𝖊𝖉", player[1])

#força do player é 1, força da fada é 1, vida dos dois é 0
        else:
            print("𝖞𝖔𝖚 𝖗𝖆𝖓 𝖆𝖜𝖆𝖞 \n 𝖄𝖔𝖚 𝖑𝖔𝖘𝖙\n")
            break

        if fairy[0] >= 1:
            print("𝕱𝖆𝖎𝖗𝖞 𝖆𝖙𝖙𝖆𝖈𝖐𝖊𝖉 𝖞𝖔𝖚 𝖆𝖓𝖉 𝖉𝖊𝖆𝖑𝖑𝖊𝖉🧚🏼‍♂️", fairy[1] - player[0])
            player[0] = player[0] - fairy[1]
        elif fairy[1] - player[0] >= 0:
            print("𝖄𝖔𝖚 𝖑𝖔𝖔𝖘𝖊...")

        else:
            print("🎊𝖄𝖔𝖚 𝖜𝖎𝖓!!🎉")
            break
while True:
    print(" ")
    break

