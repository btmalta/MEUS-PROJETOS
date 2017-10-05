import time
import json
import random 




with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)


  
def passeio():

    numero_insperdex = random.choice(range(len(insperdex)))
  
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    
    #NÍVEL 1
    N1 = [2,3,4,6,8,11,11]
    #NÍVEL 2
    N2 = [0,5,15,18]
    #NÍVEL 3
    N3 = [9,12,14]
    #NÍVEL 4
    N4 = [7,16]
    #NÍVEL 5/#NÍVEL 6
    N5_6 = [1,10,17,19]

    
    n = random.choice(range(49))
    if n < 50: #NÍVEL 1
        numero_inspermons = random.choice(N1)
  
    if n < 75 and n >= 50: #NÍVEL 2
        numero_inspermons = random.choice(N2)

    if n < 85 and n >= 75: #NÍVEL 3
        numero_inspermons = random.choice(N3)

    if n < 95 and n >= 85: #NÍVEL 4
        numero_inspermons = random.choice(N4)
  
    if n < 100 and n >= 95: #NÍVEL 5/NÍVEL 6
        numero_inspermons = random.choice(N5_6)

         


    print("Você encontrou um {0}! Seu Inspermon é {1} (nível {2}).".format(inspermons[numero_inspermons]["nome"],insperdex[numero_insperdex]["nome"],insperdex[numero_insperdex]["nivel"]))
    luta = int(input("""Você deseja batalhar ou fugir?
    Digite 1 para batalhar,
    Digite 2 para fugir.
    : """))
    if luta == 2:
        if int((inspermons[numero_inspermons]['nivel'])) < 3: #CASO O POKEMON SEJA NÍVEL 1 OU NÍVEL 2
            y = random.choice(range(2))
            if y == 0 or y == 1:
                time.sleep(0.5)
                print("Você conseguiu fugir!")
            else:
                time.sleep(0.5)
                print("Você não conseguiu fugir e vai ter que batalhar! O nível desse inspermon é {0}".format(inspermons[numero_inspermons]['nivel']))
                #CHAMA A FUNÇÃO BATALHA
                batalha(numero_inspermons, numero_insperdex)
        if int((inspermons[numero_inspermons]['nivel'])) < 5 and int((inspermons[numero_inspermons]['nivel'])) >= 3: #CASO O POKEMON SEJA NÍVEL 3 OU NÍVEL 4
            y = random.choice(range(4))
            if y == 0 or y == 1:
                time.sleep(0.5)
                print("Você conseguiu fugir!")
            else:
                time.sleep(0.5)
                print("Você não conseguiu fugir e vai ter que batalhar! O nivel desse inspermon é {0}".format(inspermons[numero_inspermons]['nivel']))
                #CHAMA A FUNÇÃO BATALHA
                batalha(numero_inspermons, numero_insperdex)
        if int((inspermons[numero_inspermons]['nivel'])) < 7 and int((inspermons[numero_inspermons]['nivel'])) >= 5: #CASO O POKEMON SEJA NÍVEL 5 OU NÍVEL 6
            y = random.choice(range(6))
            if y == 0 or y == 1:
                time.sleep(0.5)
                print("Você conseguiu fugir!")
            else:
                time.sleep(0.5)
                print("Você não conseguiu fugir e vai ter que batalhar! O nível desse inspermon é {0}".format(inspermons[numero_inspermons]['nivel']))
                 #CHAMA A FUNÇÃO BATALHA
                batalha(numero_inspermons, numero_insperdex)
    if luta == 1:
        time.sleep(0.5)
        print("Você escolheu batalhar, boa sorte!")
        #CHAMA FUNÇÃO BATALHA
        batalha(numero_inspermons, numero_insperdex)


#FUNÇÃO BATALHA



def batalha (numero_inspermons, numero_insperdex):
    
    #meu inspermon
    x = int(insperdex[numero_insperdex]["vida"])
    c = int(insperdex[numero_insperdex]["poder"])
    z = int(int(insperdex[numero_insperdex]["defesa"])/2)

    #inimigo
    y = int(inspermons[numero_inspermons]["poder"])
    b = int(inspermons[numero_inspermons]["vida"])
    d = int(int(inspermons[numero_inspermons]["defesa"])/2)
   

    while True:
        ataque = int(input("""Você deseja atacar ou fugir?
    Digite 1 para atacar
    Digite 2 para fugir
    : """))
        if ataque == 1:
            pass
        if ataque == 2:
            y = random.choice(range(4))
            if y == 0 or y == 1:
                time.sleep(0.5)
                print("Você conseguiu fugir!")
                break
            else:
                time.sleep(0.5)
                print("Você não conseguiu fugir e vai ter que batalhar!")
                pass
        time.sleep(1)
        n1 = random.choice(range(99))
        n2 = random.choice(range(99))
        n3 = random.choice(range(99))


        atk = int(input("""Você quer utilizar seu ataque comum ou o ataque forte
    Lembrando: O ataque forte tem 2,5x do poder, porém,
    precisa de uma rodada de carregamento.
    Digite 1 para o ataque comum,
    Digite 2 para o ataque forte.
    : """))

        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)

        
        if atk == 1:
            if n2<74:
                if (c-d) < 0:
                    b = b
                else:
                    b = b - (c-d)
            else:
                print("Seu Inspermon errou o ataque!")
                pass
            
            if n1<74:
                if (y-z) < 0:
                    x = x
                else:
                    x = x - (y - z)
            else:
                print("O Inspermon inimigo errou o ataque!")
                pass
            
        elif atk == 2:
            if n1<74:
                if (y-z) < 0:
                    x = x
                else:
                    x = x - (y - z)
                print("A vida do seu Inspermon é {0}.".format(int(x)))
                
            else:
                print("O Inspermon inimigo errou o ataque!")
                pass
            
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)

            if n3<74:
                if (y-z) < 0:
                    x = x
                else:
                    x = x - (y - z)
                
            else:
                print("O Inspermon inimigo errou o ataque!")
                pass

            if n2<85:
                if (c-d) < 0:
                    b = b
                else:
                    b = b - (c*2.5 - d)
            else:
                print("Seu Inspermon errou o ataque!")
            


        if x <= 0:
            print("O seu inspermon morreu.........")
            print("Você perdeu a batalha!")
            break
        else:
            print("Continue se defendendo!")
            print("A vida do seu Inspermon é {0}.".format(int(x)))
            pass

        time.sleep(0.5)
            
        if b <= 0:
            print("\nVocê venceu a batalha! Parabéns!")
            time.sleep(0.5)
            #DAR APPEND EM UM POKEMON! PRECISA IR PARA A INSPERDEX
            if inspermons[numero_inspermons] not in insperdex:
                print("\nPor isso agora o Inspermon {0} é seu!".format((inspermons[numero_inspermons]['nome'])))
                insperdex.append(inspermons[numero_inspermons])
            
            (insperdex[numero_insperdex]['xp'])=(int(inspermons[numero_inspermons]['vida']))+int((insperdex[numero_insperdex]['xp']))

            time.sleep(0.5)
            
            print("Depois de vencer essa batalha o xp do {0} aumentou, agora é {1}.".format(insperdex[numero_insperdex]['nome'],insperdex[numero_insperdex]['xp']))
            insperdex[numero_insperdex]['nivel'] = int(insperdex[numero_insperdex]['nivel']) + 1

            if insperdex[numero_insperdex]['xp'] >= int(insperdex[numero_insperdex]['exp. para nivel']):
                time.sleep(0.5)                
                print("O seu Inspermon passou de nivel!")
                while (int(insperdex[numero_insperdex]['xp'])) > (int(insperdex[numero_insperdex]['exp. para nivel'])):
                    insperdex[numero_insperdex]["vida"] = int(insperdex[numero_insperdex]["vida"]) + 5
                    insperdex[numero_insperdex]["poder"] = int(insperdex[numero_insperdex]["poder"]) + 5
                    insperdex[numero_insperdex]["defesa"] = int(insperdex[numero_insperdex]["defesa"]) + 5
                    insperdex[numero_insperdex]['xp'] = insperdex[numero_insperdex]['xp']- int(insperdex[numero_insperdex]['exp. para nivel'])
                    insperdex[numero_insperdex]['exp. para nivel'] = int(insperdex[numero_insperdex]['exp. para nivel']) + 200
                    
            break
        else:
            print("A vida do Inspermon inimigo é {0}.".format(int(b)))
            continue


##CODIGO


    
while True:
     
    s = int(input("""Seja muito bem-vindo ao Inspermon! Essa é sua primeira vez aqui?
    Digite 1 para Sim
    Digite 2 para Não
    : """))
    
    if s == 1:
        
        with open('insperdex.json','w') as insperdex:
            pass

        insperdex = []
     
        pokemon = int(input("""Escolha um inspermon para iniciar sua jornada:
    Nome: Ratricate
    Poder: 12
    Vida: 80
    Defesa: 15
    Nível: 1
    Digite 1
                        
    Nome: Catergripe
    Poder: 8
    Vida: 60
    Defesa: 10
    Nível: 1
    Digite 2

    Nome: Spearro
    Poder: 15
    Pontos de vida: 100
    Defesa: 8
    Nível: 1
    Digite 3

    Sua escolha: """))

        
        if pokemon == 1:
                insperdex.append(inspermons[2])
        if pokemon == 2:
                insperdex.append(inspermons[3])
        if pokemon == 3:
                insperdex.append(inspermons[4])
            

    if s == 2:
        l = int(input("""Deseja carregar o seu último jogo?
    1 para Sim
    2 para Não
    : """))
        if l == 1:
                with open ('insperdex.json') as insperdex:
                    insperdex = json.load(insperdex)
            
        if l == 2:
            
            with open("Insperdex.json","w") as insperdex:
                pass
            insperdex = []
            
            pokemon = int(input("""Escolha um inspermon para iniciar sua jornada:
    Nome: Ratricate
    Poder: 12
    Vida: 80
    Defesa: 15
    Nível: 1
    Digite 1

    Nome: Catergripe
    Poder: 8
    Vida: 60
    Defesa: 10
    Nível: 1
    Digite 2

    Nome: Spearro
    Poder: 15
    Pontos de vida: 100
    Defesa: 8
    Nível: 1
    Digite 3

    : """))
                
            if pokemon == 1:
                insperdex.append(inspermons[2])
            if pokemon == 2:
                insperdex.append(inspermons[3])
            if pokemon == 3:
                insperdex.append(inspermons[4])

    while True:
        pergunta = int(input("""Bem vindo! O que você deseja fazer?
    1 para passear,
    2 para dormir,
    3 para Insperdex.
    : """))

        

        if pergunta == 1:       #passear
            passeio()
            continue
        
        
        if pergunta == 3:       #insperdex
            print("\nINSPERDEX:\n")
            for h in range(len(insperdex)):
                print("Nome:{0}\nXP:{1} / {2}\nNível: {3}\n".format(insperdex[h]['nome'],insperdex[h]['xp'],insperdex[h]['exp. para nivel'], insperdex[h]['nivel']))
                
            sair = input("Digite qualquer tecla para voltar ao menu.")
            if sair == True:
                continue


        if pergunta < 1:
            continue
        if pergunta > 3:
            continue


        if pergunta == 2:
            with open('insperdex.json','a') as dex:
                json.dump(insperdex,dex)
            print("Bom descanso! Até a próxima!")
            break
    break




