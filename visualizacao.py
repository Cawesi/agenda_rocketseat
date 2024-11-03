"""
    Função para visualização dos contatos
"""
def visualizar_contatos(lista_contatos, visualizacao):
    print("N°   Favorito   Nome           Telefone / E-mail")
    print(".... .........  .............. ..........................................")

    for indice, contato in enumerate(lista_contatos, start=1):
        status_favorito = "✓" if contato["favorito"] == "Sim" else " "
        favorito = True if contato["favorito"] == "Sim" else False
        if visualizacao == "geral":
            print(f"{indice}ª.  [ {status_favorito} ]      {contato["nome"]}      {contato["telefone"]} - {contato["email"]}")
        if visualizacao == "favoritos" and favorito:
            print(f"{indice}ª.  [ {status_favorito} ]      {contato["nome"]}      {contato["telefone"]} - {contato["email"]}")
    return

def marcar_desmarcar_favorito(lista_contatos, f_visualizar):
    print("\nQual contato deseja adicionar ou remover da lista de favoritos\n")

    f_visualizar(lista_contatos, "geral")

    escolha_contato = input("\n--> ").strip()
    while True:
        if int(escolha_contato) > 0 and int(escolha_contato) <= len(lista_contatos):
            break
        escolha_contato = input("\nEscolha uma opção válida\n--> ").strip()

    troca_favorito = "Sim" if lista_contatos[int(escolha_contato) - 1]["favorito"] == "Não" else "Sim"
    lista_contatos[int(escolha_contato)-1]["favorito"] = troca_favorito
    return
    