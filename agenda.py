"""
    Sobre o desafio

    Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. 
    O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo Introdução ao Python.

    
    Regras da aplicação

    - A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
    - Deve ser possível adicionar um contato
        ° O contato pode ter os dados:
        ° Nome
        ° Telefone
        ° Email
        ° Favorito (está opção é para poder marcar um contato como favorito)
    - Deve ser possível editar um contato
    - Deve ser possível visualizar a lista de contatos cadastrados
    - Deve ser possível marcar/desmarcar um contato como favorito
    - Deve ser possível ver uma lista de contatos favoritos
    - Deve ser possível apagar um contato
"""

# Arquivo principal

from cadastro import adicionar_contato, editar_cadastro, excluir_contato
import visualizacao

contatos = []

while True:
    print("\nAgenda de Contatos Rocket\n")

    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Ver Contatos")
    print("4. Editar Favoritos")
    print("5. Ver Favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("\nDigite a opção desejada: \n")

    if escolha == "1":
        adicionar_contato(contatos)
    
    if escolha == "2":
        editar_cadastro(contatos)
        print("\nContato alterado!")
    
    if escolha == "3":
        print("\nLista de Contatos - Geral\n")
        visualizacao.visualizar_contatos(contatos, "geral")

    if escolha == "4":
        visualizacao.marcar_desmarcar_favorito(contatos, visualizacao.visualizar_contatos)
        print("\nFavorito alterado!")

    if escolha == "5":
        print("\nLista de Contatos - Favoritos\n")
        visualizacao.visualizar_contatos(contatos, "favoritos")

    if escolha == "6":
        excluir_contato(contatos, visualizacao.visualizar_contatos)
        print("\nContato Excluido!")

    if escolha == "7":
        break
