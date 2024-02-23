import functions

lista_contato = []

while True:
    print("\nMinha lista de contatos")
    print("\n1. Adicionar um contato")
    print("2. Visualizar os contatos")
    print("3. Editar um contato")
    print("4. Marcar/desmarcar um contato com favorito")
    print("5. Visualizar os contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")
    
    try:
        option = int(input("\nDigite o numero da opção que deseja prosseguir: "))
    except ValueError as e:
        print(f"Erro de value error: {e}")
        print("Opção inválida, escolha entre 1 e 7!")
    else:

        if option > 7 or option <= 0:
            print("Opção inválida, digite um numero entre 1 e 7!")
        elif option == 1:
            nome_contato = input("Digite o nome do contato: ")
            telefone_contato = input("Digite o telefone do contato: ")
            email_contato = input("Digite o email do contato: ")

            functions.adicionar_contato(lista_contato,nome_contato,telefone_contato,email_contato)

        elif option == 2:
            functions.visualizar_contato(lista_contato)

        elif option == 3:
            functions.visualizar_contato(lista_contato)

            try:
                contato_editado = int(input("Digite o numero do contato a ser editado: "))
            except ValueError as e:
                print(f"Erro de value error: {e}")
                print(f"Opção inválida, digite um numero entre 1 e {len(lista_contato)}")
            else:
                if contato_editado <= 0 or contato_editado > len(lista_contato):
                    print(f"Digite um número válido entre 1 e {len(lista_contato)}")
                else:
                    nome_contato_editado = input("Digite o nome do contato: ")
                    email_contato_editado = input("Digite o telefone do contato: ")
                    telefone_contato_editado = input("Digite o email do contato: ")

                    functions.editar_contato(lista_contato,nome_contato_editado,email_contato_editado,telefone_contato_editado,contato_editado)
        elif option == 4:
            functions.visualizar_contato(lista_contato)
            try:
                contato_favorito = int(input("\nDigite o numero do contato para marca-lo como favorito: "))
            except ValueError as e:
                print(f"Erro de value error: {e}")
                print(f"Opção inválida, digite um numero entre 1 e {len(lista_contato)}")
            else:
                if contato_favorito <= 0 or contato_favorito > len(lista_contato):
                    print(f"Digite um número válido entre 1 e {len(lista_contato)}")
                else:
                    functions.marcar_desmacar_favorito(lista_contato,contato_favorito)

        elif option == 5:
            functions.visualizar_contatos_favorito(lista_contato)

        elif option == 6:
            functions.visualizar_contato(lista_contato)
            try:
                contato_excluido = int(input("\nDigite o numero do contato a ser excluido: "))
            except ValueError as e:
                print(f"Erro de value error: {e}")
                print(f"Opção inválida, digite um numero entre 1 e {len(lista_contato)}")
            else:
                if contato_excluido <= 0 or contato_excluido > len(lista_contato):
                    print(f"Digite um número válido entre 1 e {len(lista_contato)}")
                else:
                    functions.apagar_contato(lista_contato,contato_excluido)

        elif option == 7:
            print("Programa finalizado!")
            break;