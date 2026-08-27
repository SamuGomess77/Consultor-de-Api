import httpx

def menu():
 print("================================")
 print("       CENTRAL DE APIs          ")
 print("================================")

 print("1 - Consultar usuário")
 print("2 - Listar usuários")
 print("3 - Consultar postagem")
 print("4 - Sair")

 print("\n")

 opcoes = input("Escolha uma opcao: ")

 return opcoes




def pedir_id():

  while True:

    id_usuario = input("Digite o numero de id do usuario: ")
  
    if id_usuario.isdigit():
      return id_usuario
    print("Digite apenas numeros!")




def consultar_usuario(id_usuario):
    resposta = httpx.get(

      f"https://jsonplaceholder.typicode.com/users/{id_usuario}",
        timeout=5
    )

    return resposta

  
def listar_usuarios():
     resposta = httpx.get(

      f"https://jsonplaceholder.typicode.com/users/",
        timeout=5
    )

     resposta.raise_for_status() 

     dados = resposta.json()

     for usuario in dados:
      print(usuario["name"])
      print(usuario["username"])
      print(usuario["email"])




def consultar_postagem(id_postagem):

    resposta = httpx.get(

      f"https://jsonplaceholder.typicode.com/posts/{id_postagem}",
        timeout=5
    )

    return resposta

    



while True:

    opcao = menu()

    if opcao == "1":

        id_usuario = pedir_id()

        try:
            resposta = consultar_usuario(id_usuario)

            print("Status:", resposta.status_code)

            if resposta.status_code == 200:

                dados = resposta.json()

                print("\nNome:", dados["name"])
                print("Email:", dados["email"])
                print("Usuário:", dados["username"])
                print("Cidade:", dados["address"]["city"])
                print("Empresa:", dados["company"]["name"])

            else:
                print("Usuário não encontrado.")

        except httpx.RequestError:
            print("Erro ao conectar com a API.")


    elif opcao == "2":

        try:
            listar_usuarios()

        except httpx.RequestError:
            print("Erro ao conectar com a API.")


    elif opcao == "3":

        id_postagem = pedir_id()

        try:
            resposta = consultar_postagem(id_postagem)

            print("Status:", resposta.status_code)

            if resposta.status_code == 200:

                dados = resposta.json()

                print("\nID:", dados["id"])
                print("ID do usuário:", dados["userId"])
                print("Título:", dados["title"])
                print("Texto:", dados["body"])

            else:
                print("Postagem não encontrada.")

        except httpx.RequestError:
            print("Erro ao conectar com a API.")


    elif opcao == "4":

        break


    else:

        print("Opção inválida!")


print("\nPrograma encerrado.")