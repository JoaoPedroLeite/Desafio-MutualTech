def tamanho_titas(tamanhoTita):
    
    listaTita = []
    for i in tamanhoTita:
        listaTita.append(i)

    print(listaTita)
    return listaTita

def converte_array(tamanhoTita,titaP,titaM,titaG):

    tamanho = len(tamanhoTita)
    posicao = 0

    for i in tamanhoTita:
        if i == "P":
            tamanhoTita[posicao] = titaP
        elif i == "M":
            tamanhoTita[posicao] = titaM
        elif i == "G":
            tamanhoTita[posicao] = titaG
        posicao +=1

        if posicao == tamanho:
            break

    print(tamanhoTita)
    return tamanhoTita


def quantidade_muralha(listaTita,tamanhoMuralha):

    tamanho = len(listaTita)
    print(tamanho)
    posicao = 0
    muralhaDerrubada = 0

    print(listaTita)

    for tita in listaTita:
        if tita <= tamanhoMuralha:
            tamanhoMuralha -= tita
            # del(listaTita[listaTita.index(tita)])
            
            print(f"A{listaTita[posicao]}")
            print(f"B{tita}")
            print(f"C{tamanhoMuralha}")
            del(listaTita[posicao])
            posicao -=1
            
        
        posicao +=1
        if posicao == tamanho:
            muralhaDerrubada += 1
            break
    
    print(listaTita)
    print(tamanhoMuralha)
    # posicao = 0

    # for tita in listaTita:
    #     # if tita == "Morto":
    #     #     # del(listaTita[posicao]) #print(lista.index('maçã'))
    #     #     print(listaTita.index(tita))
    #     #     # del(listaTita[listaTita.index(tita)])
    #     #     posicao -= 2

    #     print(f"{listaTita.index(tita)}{tita}")
    #     posicao += 1


    # print(listaTita)
   






quantidadeTita,tamanhoMuralha =  (map(int, input("informe a quantidade de titas e o tamanho da muralha: ").split(" ")))

tamanhoTita =  input("informe o tamanho dos Titas: ")

titaP,titaM,titaG =  (map(int, input("informe o tamanho dos Titas P, M e G: ").split(" ")))

tamanhoTita = tamanho_titas(tamanhoTita)
listaTita = converte_array(tamanhoTita,titaP,titaM,titaG)
quantidade_muralha(listaTita,tamanhoMuralha)

# print(quantidadeTita,tamanhoMuralha)
# print(tamanhoTita)
# print(titaP, titaM, titaG)