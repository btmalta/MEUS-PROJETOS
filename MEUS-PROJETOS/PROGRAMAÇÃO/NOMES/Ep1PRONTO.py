with open("nomes.txt", "r") as arquivo:
 lista_de_nomes = []
 for linha in arquivo:
     lista_de_nomes.append(linha)
L = lista_de_nomes
lista_resultado = []

for nome_completo in L:
    L_nome = nome_completo.split()
    for i in range(len(L_nome)):
        L_nome[i] = L_nome[i].lower()
    for n in range(len(L_nome)):
        L_nome[n] = L_nome[n].capitalize()
    for e in range(len(L_nome)):
        while True:
            if L_nome[e] == "De":
                L_nome[e] = "de"
            if L_nome[e] == "Da":
                L_nome[e] = "da"
            if L_nome[e] == "Do":
                L_nome[e] = "do"
            if L_nome[e] == "Dos":
                L_nome[e] = "dos"
            break
    L2 = []
    for i in L_nome:
        if not i in L2:
            L2.append(i)
    lista_de_nomes = " ".join(L2)

    if lista_de_nomes not in lista_resultado:
        x = lista_resultado.append(lista_de_nomes)
    w = "\n".join(lista_resultado)
        
print(w)
        



    
            
   
        

    
    

    
    
