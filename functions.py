def adicionar_contato(lista,nome_contato,telefone_contato,email_contato):
    novo_contato = {"Nome": nome_contato, "Telefone": telefone_contato, "email_contato": email_contato, "Favorito": False}
    lista.append(novo_contato)
    print("\nContato adicionado com sucesso")
    return

def visualizar_contato(lista):
    for indice,contato in enumerate(lista,start=1):

        nome_contato = contato["Nome"]
        telefone_contato = contato["Telefone"]
        email_contato = contato["email_contato"]

        if contato["Favorito"] == True:
            favorito_contato = "[♥️]"
        else:
            favorito_contato = "[ ]"

        print(f"{indice}. {favorito_contato} Nome: {nome_contato} | Telefone: {telefone_contato} | Email: {email_contato}")
    
    return

def editar_contato(lista,nome_contato,telefone_contato,email_contato,indice_contato):

    indice_contato_ajustado = indice_contato - 1

    lista[indice_contato_ajustado]["Nome"] = nome_contato
    lista[indice_contato_ajustado]["Telefone"] = telefone_contato
    lista[indice_contato_ajustado]["email_contato"] = email_contato


    print("\nContato atualizado com sucesso!")

    return
def marcar_desmacar_favorito(lista,indice_contato):
    indice_contato_ajustado = indice_contato - 1

    lista[indice_contato_ajustado]["Favorito"] = True
    print("\nContato marcado com sucesso!")
    return


def visualizar_contatos_favorito(lista):
    for indice,contato in enumerate(lista,start=1):

        if contato["Favorito"] == True:
            nome_contato = contato["Nome"]
            telefone_contato = contato["Telefone"]
            email_contato = contato["email_contato"]
            favorito_contato = "[♥️]"

            print(f"{indice}. {favorito_contato} Nome: {nome_contato} | Telefone: {telefone_contato} | Email: {email_contato}")

    return

def apagar_contato(lista,indice_contato):

    indice_contato_ajustado = indice_contato - 1

    contato_excluido = lista[indice_contato_ajustado]

    lista.remove(contato_excluido)

    print("\nContato excluído com sucesso!")

    return