import random

cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
naipes = ["Espadas","Paus","Ouros","Copas"]
escolhapc = ["S","N"]

def maojogador():
    carta1j = random.choice(cartas)
    carta2j = random.choice(cartas)
    naipe1j = random.choice(naipes)
    naipe2j = random.choice(naipes)
    
    print("Jogador", nome, "você tem", carta1j,"de",naipe1j, "e", carta2j, "de", naipe2j)


def maopc():
    carta1pc = random.choice(cartas)
    carta2pc = random.choice(cartas)
    naipe1pc = random.choice(naipes)
    naipe2pc = random.choice(naipes)

def mesa():
    cartamesa = random.choice(cartas)
    naipemesa = random.choice(naipes)
    print("A",i,"ª carta da mesa é: ", cartamesa,"de",naipemesa)
        
    
def csa():
    r = str(input("\nQuer continuar essa mão, sair dessa mão ou aumentar sua aposta? "))
    return r    


r = 0
nome = str(input("Digite seu nome: "))
maojogador()
i = 0
escolhapcc = 0
while i <= 5:
    i = i + 1
    if i <= 5 and escolhapcc != "N":
        r = csa()
        if r == "s":
            print("Você saiu dessa mão!")
            
        elif r == "c":
            mesa()
            
        elif r == "a":
            qnt = int(input("Pra quanto você quer aumentar a aposta? R$"))
            escolhapcc = random.choice(escolhapc)
            if escolhapcc == "S":
                print("\nO computador aceitou sua aposta de R$",qnt)
                mesa()
            elif escolhapcc == "N":
                print("\nO computador não aceitou sua aposta.")
                print("Você saiu dessa mão!")
        
    else:
        print("Encerrou!")  
        
