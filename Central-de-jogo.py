
print("====================")
print("  Central de jogo   ")
print("====================")

print("1-Cadastrar jogador")
print("2- Listar jogador ")
print("3- Consultar jogador")
print("4- Alterar jogador")
print("5 - Remover jogador")
print("6 - Mostrar estatísticas")
print("7 - Sair")
print("\n")



jogadores = []

def Cadastrar_jogador():
  
  cadastro_lista = {
    "nome": str(input("Digite o nome do seu personagem: ")) ,
    "idade" : int(input("Digite a idade do seu personagem: ")) , 
    "nivel" : int(input("digite o nivel em que o seu personagem estar (tem que ser entre 0 a 100): "))
  }

  if cadastro_lista["nivel"] >= 0 and cadastro_lista["nivel"] < 101:
     print("nivel cadastrado com sucesso!")
     jogadores.append(cadastro_lista) 
  else:
    print("recomeçe o seu cadastro novamente!. nivel não foi aceito!!")
    return 
    


def listar_jogador():

     if len(jogadores) == 0:
      print("Nenhum jogador cadastrado!")
      return

     for jogador in jogadores:
       print("===================================")
       print(f"Nome do jogador: " , jogador["nome"])
       print(f"idade: " ,  jogador["idade"])
       print(f"nivel: " ,  jogador["nivel"])
       print("===================================")
       print("\n")

     



def Consultar_jogador():
    pesquisar = str(input("Digite o nome do jogador que vc quer consultar: "))
    encontrado = False
    for jogador in jogadores:
     if pesquisar == jogador["nome"]:
        print("===================================")
        print(f"Nome do jogador: " , jogador["nome"])
        print(f"idade: " ,  jogador["idade"])
        print(f"nivel: " ,  jogador["nivel"])
        print("===================================")

        encontrado = True
        break

    if encontrado == False:
        print("Jogador não encontrado!")


        

def Alterar_jogador():
    alterar = str(input("Digite o nome do jogador que vc quer alterar: "))

    encontrado = False

    for jogador in jogadores:

        if alterar == jogador["nome"]:
            novo_nome = str(input("Digite o novo nome do jogador: "))
            nova_idade = int(input("Digite o nova idade do jogador: "))
            novo_nivel = int(input("Digite o novo nivel do jogador: "))
            
            if novo_nivel >= 0 and novo_nivel <= 100:    
              jogador["nome"] = novo_nome
              jogador["idade"] = nova_idade
              jogador["nivel"] = novo_nivel

            encontrado = True
            print("Jogador alterado com sucesso!")

        else:
            print("Nível inválido! O jogador não foi alterado.")
            break

    if encontrado == False:
        print("Jogador não encontrado!")

            


def Remover_jogador():
    remover = str(input("Digite o nome do jogador que vc quer remover:  "))
    encontrado = False

    for jogador in jogadores:
      if remover == jogador["nome"]:
        jogadores.remove(jogador)
        encontrado = True
        print("Jogador removido com sucesso!")
        break  
    
    if encontrado == False:
        print("Jogador não encontrado!")
   







def Mostrar_estatisticas():

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado!")
        return

    total_jogadores = len(jogadores)

    soma_niveis = 0
    soma_idades = 0

    maior_nivel = jogadores[0]
    menor_nivel = jogadores[0]

    for jogador in jogadores:

        soma_niveis += jogador["nivel"]
        soma_idades += jogador["idade"]

        if jogador["nivel"] > maior_nivel["nivel"]:
            maior_nivel = jogador

        if jogador["nivel"] < menor_nivel["nivel"]:
            menor_nivel = jogador

    media_nivel = soma_niveis / total_jogadores
    media_idade = soma_idades / total_jogadores

    print("===================================")
    print("          ESTATÍSTICAS")
    print("===================================")
    print(f"Total de jogadores: {total_jogadores}")
    print(f"Nível médio: {media_nivel:.1f}")
    print(f"Idade média: {media_idade:.1f}")
    print(f"Maior nível: {maior_nivel['nome']} ({maior_nivel['nivel']})")
    print(f"Menor nível: {menor_nivel['nome']} ({menor_nivel['nivel']})")
    print("===================================")





while True:
    opcoes = int(input("Escolha qual opcao vc quer(Digite apenas os numeros das opcoes): "))
    print("\n")
    if opcoes == 1:
      Cadastrar_jogador()
    elif opcoes == 2:
      listar_jogador()
    elif opcoes == 3:
      Consultar_jogador()
    elif opcoes == 4:
      Alterar_jogador()
    elif opcoes == 5:
       Remover_jogador()
    elif opcoes == 6:
      Mostrar_estatísticas()
    elif opcoes == 7:
        break
    else:
        print("Opção inválida!")



