"""
    Funções para Criação de Contatos
"""
def adicionar_contato(lista_contatos):
    """
        - Função para salvar contatos
            A função tem alguns incrementos:
            ° Nome é obrigatório e precisa ter mais de 3 letras, não é permitido caracteres especiais 
            ou números.
            ° Para salvar um contato será obrigatório inserir pelo menos 1 informação de contato,
            ou um e-mail ou um número de telefone ou ambos.
            ° No campo de telefone tem uma validação que só permitirá o cadastro se todos os caracteres 
            forem numéricos e o número de telefone tenha 8 ou mais caracteres. 
            ° No campo de e-mail tem uma validação que só permitirá o cadastro caso o e-mail tenha 
            um @ e mais de 5 letras. 
    """
    def validador_contato(contato, opcao_menu):
        if opcao_menu == "1":
            telefone = input("\nInsira o telefone (Apenas números)\n--> ").strip()
            while True:
                try:
                    comprimento_string = len(telefone)
                except Exception as e:
                    comprimento_string = 0
                if telefone.isdigit() and comprimento_string >= 8:
                    break
                telefone = input("\nInsira um telefone válido (Apenas números)\n--> ").strip()
            contato.update({"telefone": telefone})
            return
        if opcao_menu == "2":
            email = input("\nInsira o E-mail\n--> ").strip()
            while True:
                try:
                    comprimento_string = len(email)
                except Exception as e:
                    comprimento_string = 0
                if "@" in email and comprimento_string >= 5:
                    break
                email = input("\nInsira um e-mail válido (Apenas números)\n--> ").strip()  
            contato.update({"email": email})
            return
        
    contato = {}

    nome = input("\nNome do Contato\n--> ").strip()
    while True:
        try:
            comprimento_campo_nome = len(nome)
        except Exception as e:
            comprimento_campo_nome = 0
        if nome.isalpha() and comprimento_campo_nome >= 3:
            break
        nome = input("\nInsira um nome válido:\n--> ").strip()
    
    contato.update({"nome": nome})

    telefone = input("\nInsira o telefone (Apenas números)\n--> ").strip()
    try:
        comprimento_string_telefone = len(telefone)
    except Exception as e:
        comprimento_string_telefone = 0
    status_telefone = True if telefone.isdigit() and comprimento_string_telefone >= 8 else False

    email = input("\nInsira o E-mail\n--> ").strip()
    try:
        comprimento_string_email = len(email)
    except Exception as e:
        comprimento_string_email = 0
    status_email = True if "@" in email and comprimento_string_email >= 5 else False
    
    if not status_telefone and not status_email:
        print("\nTelefone e E-mail inválidos.\nInsira pelo menos 1 contato para continuar")
        opcao_escolhida = input("\nQuais informações de contato deseja salvar:\n1. Telefone\n2. E-mail\n3. Telefone e E-mail\n--> ").strip()
        while True:
            if opcao_escolhida == "1" or opcao_escolhida == "2" or opcao_escolhida == "3":
                break
            opcao_escolhida = input("\nEscolha uma das opções para salvar:\n1. Telefone\n2. E-mail\n3. Telefone e E-mail\n--> ").strip()
        
        if opcao_escolhida == "1":
            validador_contato(contato, "1")
        if opcao_escolhida == "2":
            validador_contato(contato, "2")
        if opcao_escolhida == "3":
            validador_contato(contato, "1")
            validador_contato(contato, "2")
    elif not status_telefone or not status_email:
        if not status_telefone and comprimento_string_telefone > 0:
            opcao_escolhida = input("\nTelefone Inválido, deseja ajustar?\n1. Sim\n2. Não\n--> ").strip()
            while True:
                if opcao_escolhida == "1" or opcao_escolhida == "2":
                    break
                opcao_escolhida = input("\nTelefone Inválido, escolha uma opção?\n1. Sim\n2. Não\n--> ").strip()
            if opcao_escolhida == "1":
                validador_contato(contato, "1")
            else:
                contato.update({"telefone": "--"})
        else:
            contato.update({"telefone": telefone})

        if not status_email and comprimento_string_email > 0:
            opcao_escolhida = input("\nE-mail Inválido, deseja ajustar?\n1. Sim\n2. Não\n--> ").strip()
            while True:
                if opcao_escolhida == "1" or opcao_escolhida == "2":
                    break
                opcao_escolhida = input("\nE-mail Inválido, escolha uma opção?\n1. Sim\n2. Não\n--> ").strip()
            if opcao_escolhida == "1":
                validador_contato(contato, "2")
            else:
                contato.update({"email": "--"})
        else:
            contato.update({"email": email})
    else:
        print("Aqui")
        contato.update({"telefone": telefone})
        contato.update({"email": email})

    opcao_favorito = input("\nDeseja salvar o contato como favorito?\n1. Sim\n2. Não\n--> ").strip()
    favoritar = "Não"
    while True:
        if opcao_favorito == "1" or opcao_favorito == "2":
            break
        opcao_favorito = input("\nEscolha uma das opções.\nDeseja salvar o contato como favorito ?\n1. Sim\n2. Não\n--> ").strip()
    if opcao_favorito == "1":
        favoritar = "Sim"

    contato.update({"favorito":favoritar})
    lista_contatos.append(contato)
    print("\nContato Salvo!\n")

    return


"""
    Função para Edição de Contatos
"""
def editar_cadastro(lista_contatos):
    print("\nQual contato deseja editar?\n")

    print("N°   Favorito   Nome           Telefone / E-mail")
    print(".... .........  .............. ..........................................")
    for indice, contato in enumerate(lista_contatos, start=1):
        status_favorito = "✓" if contato["favorito"] == "Sim" else " "
        print(f"{indice}ª.  [ {status_favorito} ]      {contato["nome"]}      {contato["telefone"]} - {contato["email"]}")

    escolha_contato = input("\n--> ").strip()
    while True:
        if int(escolha_contato) > 0 and int(escolha_contato) <= len(lista_contatos):
            break
        escolha_contato = input("\nEscolha uma opção válida\n--> ").strip()
    
    telefone_preenchido = True if lista_contatos[int(escolha_contato) - 1]["telefone"] != "--" else False
    email_preenchido = True if lista_contatos[int(escolha_contato) - 1]["email"] != "--" else False

    print("\nQual campo deseja editar?")
    escolha_campo = input("1. Nome\n2. Telefone\n3. E-mail\n--> ")
    while True:
        if escolha_campo == "1" or escolha_campo == "2" or escolha_campo == "3":
            break
        escolha_campo = input("\nEscolha uma das opções abaixo\n1. Nome\n2. Telefone\n3. E-mail\n--> ")
    if escolha_campo == "1":
        nome = input("\nNome do Contato\n--> ").strip()
        while True:
            try:
                comprimento_campo_nome = len(nome)
            except:
                comprimento_campo_nome = 0
            if nome.isalpha() and comprimento_campo_nome >= 3:
                break
            nome = input("\nInsira um nome válido:\n--> ").strip()
        lista_contatos[int(escolha_contato) - 1]["nome"] = nome

    if escolha_campo == "2":
        telefone = input("\nNúmero do Telefone\n--> ").strip()
        try:
            comprimento_string_telefone = len(telefone)
        except:
            comprimento_string_telefone = 0
        if email_preenchido and comprimento_string_telefone == 0:
            telefone = "--"
            lista_contatos[int(escolha_contato) - 1]["telefone"] = telefone
        else:
            while True:
                if telefone.isdigit() and comprimento_string_telefone >= 8:
                    break
                telefone = input("\nDigite o Telefone\n--> ").strip()
            lista_contatos[int(escolha_contato) - 1]["telefone"] = telefone
    
    if escolha_campo == "3":
        email = input("\nInsira o E-mail\n--> ").strip()
        try:
            comprimento_string_email = len(email)
        except:
            comprimento_string_email = 0
        if telefone_preenchido and comprimento_string_email == 0:
            email = "--"
            lista_contatos[int(escolha_contato) - 1]["email"] = email
        else:
            while True:
                if "@" in email and comprimento_string_email >= 5:
                    break
                email = input("\nDigite o E-mail\n--> ").strip()
            lista_contatos[int(escolha_contato) - 1]["email"] = email
    return


"""
    Função para Exclusão de contatos
"""
def excluir_contato(lista_contatos, f_visualizar):
    print("\nQual contato deseja excluir?\n")

    f_visualizar(lista_contatos, "geral")

    escolha_contato = input("\n--> ").strip()
    while True:
        if int(escolha_contato) > 0 and int(escolha_contato) <= len(lista_contatos):
            break
        escolha_contato = input("\nEscolha uma opção válida\n--> ").strip()
    lista_contatos.remove(lista_contatos[int(escolha_contato)-1])
    return
    
