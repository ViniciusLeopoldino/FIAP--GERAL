#Challenge 2024 - Sprint 1 - DSC - 20h37 - 12/04/2024

import re
import os
os.system('cls')

#Local onde as variáveis de condição do programa se encontram.
cadastro_pessoal = 1
abrir_chamado = 3
consultar_chamado = 4
login = 2
fechar = 5
cadastro_veicular = 6
confirmar = 1 or 2
correcao = 0

home = print ("Olá, seja bem vindo a plataforma Porto Seguro.")
confirmacao = int (input ("\nPara cadastrar-se, digite 1. \nPara logar na plataforma, digite 2. \n"))
if confirmacao > 2:
    while confirmacao > 2:
        print ("\nRESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        confirmacao = int (input ("\nPara cadastrar-se, digite 1. \nPara logar na plataforma, digite 2. \n"))
if confirmacao == cadastro_pessoal:
    #solicitação do nome do cliente.
    nome = input ("\nDigite seu nome completo. \n")

    #validação do dado confirmar em nome
    print (f"\nO seu nome está correto? {nome}?")
    confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))

    if confirmar == 1:
        print ("Ok.")
    else:
        if confirmar > 2:
            while confirmar > 2:
                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                print (f"\nO seu nome está correto? {nome}?")
                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
        if confirmar == 2:
            while confirmar == 2:
                nome = input ("\nDigite seu nome completo. \n")
                print (f"\nO seu nome está correto? {nome}?")
                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                if confirmar == 1:
                    print ("Ok!")

    #solicitação da data de nascimento do cliente
    nascimento = input ("\nDigite sua data de nascimento, conforme o exemplo: xx/xx/xxxx. \n")

    #validação do dado confirmar em nascimento
    print (f"\nSua data de nascimento está correta? {nascimento}?")
    confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))

    if confirmar == 1:
        print ("Ok.")
    else:
        if confirmar > 2:
            while confirmar > 2:
                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                print (f"\nSua data de nascimento está correta? {nascimento}?")
                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
        if confirmar == 2:
            while confirmar == 2:
                nascimento = input ("\nDigite sua data de nascimento, conforme o exemplo: xx/xx/xxxx. \n")
                print (f"\nSua data de nascimento está correta? {nascimento}?")
                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                if confirmar == 1:
                    print ("Ok!")

    #solicitação do gênero do cliente - loop e if
    print ("Defina seu gênero digitando os números respectivos da categoria.")
    genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))

    while genero > 4:
        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))

    #validação do dado genero
    if genero == 1:
        genero = 'Masculino'
        print ("O gênero masculino está correto para você?")
        confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
    elif genero == 2:
        genero = 'Feminino'
        print ("O gênero feminino está correto para você?")
        confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
    elif genero == 3:
        genero = 'Não-binário'
        print ("O gênero não-binário está correto para você?")
        confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
    elif genero == 4:
        genero = 'Preferiu não informar o gênero'
        print ("Não informar o gênero está correto para você?")
        confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))

    #validação do dado confirmar em genero
    if confirmar == 1:
        print ("Ok.")
    elif confirmar == 2:
        while confirmar == 2:
            genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))
            if genero == 1:
                genero = 'Masculino'
                print ("O gênero masculino está correto para você?")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            elif genero == 2:
                genero = 'Feminino'
                print ("O gênero feminino está correto para você?")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            elif genero == 3:
                genero = 'Não-binário'
                print ("O gênero não-binário está correto para você?")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            elif genero == 4:
                genero = 'Preferiu não informar o gênero'
                print ("Não informar o gênero está correto para você?")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
    elif confirmar > 2:
        while confirmar > 2:
            print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
            print (f"A opção de gênero selecionada como {genero}, está correta?")
            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")

    #solicitação de contato - celular/telefone
    numero_telefone1 = input ("\nPara termos uma informação de contato, precisaremos do seu telefone. \nDigite-o conforme a formatação a seguir: \n(XX)XXXXX-XXXX ou XXXX-XXXX se usas telefone convencional \n")
            
    #validação do numero_telefone
    print (f"O seu número de contato está correto? {numero_telefone1}? \n")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            
    if confirmar == 1:
        print ("Ok.")
    else:
        while confirmar == 2:
            numero_telefone1 = input ("Digite novamente o seu número de telefone. \nCaso seja celular: (XX)XXXXX-XXXX \nEm caso de telefone residencial: \nXXXX-XXXX \n")
            print (f"O seu número de contato está correto? {numero_telefone1}? \n")
            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
        while confirmar > 2:
                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                print (f"O seu número de contato está correto? {numero_telefone1}? \n")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                if confirmar == 1:
                    print ("Ok.")

    ##solicitação de documento - cpf
    ponto = '.'
    traco = '-'
    contador = 10
    posicao = 0
    acumulo = 0
    resto = 0
    cont = 11
    pos = 0
    res = 0
    acu = 0
    cpf = str(input('Digite seu CPF, sem traços e pontos: ')).strip()

    #validador de cpf
    if len(cpf) == 11 and cpf.isnumeric():
        cpf_formatado = cpf[0:3] + ponto + cpf[3:6] + ponto + cpf[6:9] + traco + cpf[9:]
        print(f"\nO CPF informado foi: {cpf_formatado}")

        for i in range(len(cpf[0:9])):
            primeiro = int(cpf[posicao]) * contador
            posicao += 1
            contador -= 1  
            acumulo = acumulo + primeiro

            if contador < 2 and posicao > 8:
                resto = acumulo % 11
                primeiro_verificador = 11 - resto
                if primeiro_verificador >= 10:
                    primeiro_verificador = 0

        
        for x in range(len(cpf[0:10])):
            segundo = int(cpf[pos]) * cont
            pos += 1
            cont -= 1  
            acu = acu + segundo

            if cont < 2 and pos > 9:
                res = acu % 11
                segundo_verificador = 11 - res
                if segundo_verificador >= 10:
                    segundo_verificador = 0

        primeiro_verificador = str(primeiro_verificador)
        segundo_verificador = str(segundo_verificador)

        if primeiro_verificador == cpf[9] and segundo_verificador == cpf[10]:
            print('O CPF foi analisado e aprovado. CPF válido!')

        else:
            print('CPF inválido!')

    elif len(cpf) == 14 and '.' == cpf[3] and '.' == cpf[7] and '-' == cpf[11]:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        for i in range(len(cpf[0:9])):
            primeiro = int(cpf[posicao]) * contador
            posicao += 1
            contador -= 1  
            acumulo = acumulo + primeiro

            if contador < 2 and posicao > 8:
                resto = acumulo % 11
                primeiro_verificador = 11 - resto
                if primeiro_verificador >= 10:
                    primeiro_verificador = 0

        
        for x in range(len(cpf[0:10])):
            segundo = int(cpf[pos]) * cont
            pos += 1
            cont -= 1  
            acu = acu + segundo

            if cont < 2 and pos > 9:
                res = acu % 11
                segundo_verificador = 11 - res
                if segundo_verificador >= 10:
                    segundo_verificador = 0

        primeiro_verificador = str(primeiro_verificador)
        segundo_verificador = str(segundo_verificador)

        if primeiro_verificador == cpf[9] and segundo_verificador == cpf[10]:
            print('O CPF foi analisado e aprovado. CPF válido!')

        else:
            print('CPF inválido!')
                                
    else:
        print('CPF inválido!')

    ##criação da senha do cliente
    senha = input ("\nCrie uma senha: \n")
    senha1 = input ("\nRepita a senha: \n")
    if senha1 == senha:
        print ("\nOk. Suas senhas conferem.")
    else:
        while senha1 != senha:
            print ("As senhas não conferem. ")
            senha1 = input ("\nRepita a senha: \n")
            if senha1 != senha:
                print ("\nOk. Suas senhas conferem.")

                
    #tela final - confirmação dos dados
    print ("\nEstes são os seus dados?")
    print (f"{nome};\n{nascimento};\n{genero};\n{numero_telefone1};\n{cpf_formatado}?")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
    if confirmar == 1:
        if confirmar == 1 and genero == 'Masculino':
            print (f"\nCadastro finalizado senhor {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))

        elif confirmar == 1 and genero == 'Feminino':
            print (f"\nCadastro finalizado senhora {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))

        elif confirmar == 1 and genero == 'Não-binário':
            print (f"\nCadastro finalizado senhore {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))

        elif confirmar == 1 and genero == 'Preferiu não informar o gênero':
            print (f"\nCadastro finalizado {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))

    else:
                while confirmar > 2:
                    print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2.")
                    print ("Estes são os seus dados?")
                    print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}?")
                    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                if confirmar == 2:
                            correcao = int ( input ("Para corrigir seu nome, digite 1. \nPara corrigir sua data de nascimento, digite 2. \nPara selecionar novamente o gênero, digite 3. \nPara corrigir seu CPF, digite 4. \nPara corrigir seu telefone, digite 5. \n"))
                if correcao == 1:
                    
                    #re-solicitação do nome do cliente
                    nome = input ("\nDigite seu nome completo. \n")

                    print (f"\nO seu nome está correto? {nome}?")
                    confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))

                                #re-validação do dado confirmar em nome
                    if confirmar == 1:
                                    print (f"\nOk! Dado corrigido {nome}.")
                                    print ("\nEstes são seus dados:")
                                    print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                    confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                    else:
                        while confirmar > 2:
                            print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                            print (f"\nO seu nome está correto? {nome}?")
                            confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                        while confirmar == 2:
                            print (f"\nO seu nome está correto? {nome}?")
                            confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                        if confirmar == 1:
                            print (f"\nOk! Dado corrigido {nome}.")
                            print ("\nEstes são seus dados:")
                            print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                else:
                    if correcao == 2:

                        #solicitação da data de nascimento do cliente
                        nascimento = input ("\nDigite sua data de nascimento, conforme o exemplo: xx/xx/xxxx. \n")

                        #validação do dado confirmar em nascimento
                        print (f"\nSua data de nascimento está correta? {nascimento}?")
                        confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))

                        if confirmar == 1:
                            print (f"\nOk! Data corrigida. Você nasceu em {nascimento}.")
                            print ("\nEstes são seus dados:")
                            print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                        else:
                            while confirmar > 2:
                                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                                print (f"\nSua data de nascimento está correta? {nascimento}?")
                                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                            while confirmar == 2:
                                print (f"\nSua data de nascimento está correta? {nascimento}?")
                                confirmar = int ( input ("Se sim, digite 1, se não, digite 2. \n"))
                                if confirmar == 1:
                                    print (f"\nOk! Data corrigida. Você nasceu em {nascimento}.")
                                    print ("\nEstes são seus dados:")
                                    print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                    confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                    elif correcao == 3:

                        #solicitação do gênero do cliente - loop e if
                        print ("Defina seu gênero digitando os números respectivos da categoria.")
                        genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))

                        while genero > 4:
                            print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                            genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))

                        #validação do dado genero
                        if genero == 1:
                            genero = 'Masculino'
                            print ("O gênero masculino está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 2:
                            genero = 'Feminino'
                            print ("O gênero feminino está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 3:
                            genero = 'Não-binário'
                            print ("O gênero não-binário está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 4:
                            genero = 'Preferiu não informar o gênero'
                            print ("Não informar o gênero está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))

                        #validação do dado confirmar em genero
                        if confirmar == 1:
                            print ("Ok.")
                            print ("\nEstes são seus dados:")
                            print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                            confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                        elif confirmar == 2:
                            while confirmar == 2:
                                genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))
                                if genero == 1:
                                    genero = 'Masculino'
                                    print ("O gênero masculino está correto para você?")
                                    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 2:
                            genero = 'Feminino'
                            print ("O gênero feminino está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 3:
                            genero = 'Não-binário'
                            print ("O gênero não-binário está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                        elif genero == 4:
                            genero = 'Preferiu não informar o gênero'
                            print ("Não informar o gênero está correto para você?")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                            if confirmar == 1:
                                print ("\nOk. Dado gênero alterado com sucesso.")
                                print ("\nEstes são seus dados:")
                                print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                        elif confirmar > 2:
                            while confirmar > 2:
                                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                                print (f"A opção de gênero selecionada como {genero}, está correta?")
                                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                                if confirmar == 1:
                                    print ("\nOk. Dado gênero alterado com sucesso.")
                                    print ("\nEstes são seus dados:")
                                    print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                    confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                        elif correcao == 4:

                        #validação do numero_telefone
                            numero_telefone1 = input ("Digite novamente o seu número de telefone. \nCaso seja celular: (XX)XXXXX-XXXX \nEm caso de telefone residencial: \nXXXX-XXXX \n")
                            print (f"O seu número de contato está correto? {numero_telefone1}? \n")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                                        
                            if confirmar == 1:
                                print (f"\nOk. Dado alterado. Se precisarmos, faremos contato através do número {numero_telefone1}.")
                                print ("\nEstes são seus dados:")
                                print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                        else:
                            while confirmar == 2:
                                numero_telefone1 = input ("Digite novamente o seu número de telefone. \nCaso seja celular: (XX)XXXXX-XXXX \nEm caso de telefone residencial: \nXXXX-XXXX \n")
                                print (f"O seu número de contato está correto? {numero_telefone1}? \n")
                                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                                if confirmar == 1:
                                    print (f"\nOk. Dado alterado. Se precisarmos, faremos contato através do número {numero_telefone1}.")
                                    print ("\nEstes são seus dados:")
                                    print (f"{nome}; \n{nascimento}; \n{genero}; \n{numero_telefone1}.")
                                    confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
                            while confirmar > 2:
                                print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                                numero_telefone1 = input ("Digite novamente o seu número de telefone. \nCaso seja celular: (XX)XXXXX-XXXX \nEm caso de telefone residencial: \nXXXX-XXXX \n")
                                print (f"O seu número de contato está correto? {numero_telefone1}? \n")
                                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                                if confirmar == 1:
                                    print (f"\nOk. Dado alterado. Se precisarmos, faremos contato através do número {numero_telefone1}.")
                                    print ("\nEstes são seus dados:")
                                    print (f"{nome}; \n{nascimento}; \n{genero};\n{cpf}; \n{numero_telefone1}.") 
                                    confirmacao = int (input ("\nPara fazermos o cadastro de seu veículo, digite 6. \n"))
if confirmacao == login:
    #solicitação do telefone para login
    print ("Login...")
    numero_telefone = input("\nTelefone: \n")
    senha2 = input ("\nSenha: \n")
    #if numero_telefone == numero_telefone1 and senha2 == senha1:
    print ("\nSeja bem vindo ao portal do cliente Porto Seguro.") 
    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4.  \n"))
    #else:
        #while numero_telefone != numero_telefone1 or senha2 != senha1:
            #print ("\nTelefone está incorreto.")
            #if numero_telefone != numero_telefone1:
                    #numero_telefone = str ( input("\nTelefone: \n"))
            #elif numero_telefone == numero_telefone1:
                #print ("\nSeja bem vindo ao portal do cliente Porto Seguro.")
            #elif senha2 != senha1:
                #print ("\nSenha está incorreta.")
            #elif senha2 == senha1:
                #print ("\nSeja bem vindo ao portal do cliente Porto Seguro.")
if confirmacao == fechar:
    print ("\nPrograma finalizado.")
if confirmacao == cadastro_veicular:
    ##solicitação da placa do veículo
    print ("\nAgora cadastraremos seu veículo para que você possa usufruir da nossa plataforma.")

    placa_veiculo = input ("Digite a placa, de forma fidedigna, de seu automóvel. \n")
    print (f"A placa do seu veículo está correta? {placa_veiculo}")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))

    if confirmar == 1:
        print ("Ok.")
    elif confirmar == 2:
        while confirmar == 2:
            placa_veiculo = input ("Digite, novamente, de forma fidedigna a placa de seu carro. \n")
            print (f"A placa do seu veículo está correta? {placa_veiculo}")
            confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
    elif confirmar > 2:
        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        print (f"A placa do seu veículo está correta? {placa_veiculo}")
        confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
        if confirmar == 1:
            print ("Ok.")
        elif confirmar == 2:
            while confirmar == 2:
                placa_veiculo = input ("Digite, novamente, de forma fidedigna a placa de seu carro. \n")
                print (f"A placa do seu veículo está correta? {placa_veiculo}")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                if confirmar == 1:
                    print ("Ok.")

    ##solicitar ano do veículo
    print ("\nAgora, precisaremos do ano do seu automóvel.")

    ano_veicular = int ( input ("Digite o ano em que seu carro foi fabricado. \n"))
    confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
    if confirmar == 1:
        print ("Ok.")
    elif confirmar == 2:
        while confirmar == 2:
            ano_veicular = int ( input ("Digite, novamente, o ano em que seu carro foi fabricado. \n"))
            confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
    elif confirmar > 2:
        while confirmar > 2:
            print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
            confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
            elif confirmar == 2:
                while confirmar == 2:
                    ano_veicular = int ( input ("Digite, novamente, o ano em que seu carro foi fabricado. \n"))
                    confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                    if confirmar == 1:
                        print ("Ok.")

    ##solicitação do modelo do carro
    print ("\nPara finalizarmos o seu cadastro veicular,")
    modelo_veicular = input ("Informe-nos o modelo de seu veículo. Ex: Toyota, Corolla. \n")
    confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
    if confirmar == 1:
        print ("Ok.")
    elif confirmar == 2:
        while confirmar == 2:
            modelo_veicular = input ("Informe-nos, novamente, o modelo de seu veículo. Ex: Toyota, Corolla. \n")
            confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
    elif confirmar > 2:
        while confirmar > 2:
            print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
            confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
            if confirmar == 1:
                print ("Ok.")
            elif confirmar == 2:
                while confirmar == 2:
                    modelo_veicular = input ("Informe-nos, novamente, o modelo de seu veículo. Ex: Toyota, Corolla. \n")
                    confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                    if confirmar == 1:
                        print ("Ok.")

    ##tela final - confirmação
    print ("\nEstes são seus dados?")
    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
    if confirmar == 1:
        print (f"O seu veículo, {modelo_veicular}, foi cadastrado com sucesso em nosso sistema.")
        confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
    elif confirmar == 2:
        while confirmar == 2:
            ##corrigir os dados do cliente
            correcao = int ( input ("Para corrigir a placa de seu veículo, digite 1. \nPara corrigir o ano de seu veículo, digite 2. \nPara corrigir o modelo de seu veículo, digite 3. \n"))

            if correcao == 1:
                ##re-solicitação da placa do veículo
                print ("\nAgora cadastraremos seu veículo para que você possa usufruir da nossa plataforma.")

                placa_veiculo = input ("Digite de forma fidedigna a placa de seu carro. \n")
                print (f"A placa do seu veículo está correta? {placa_veiculo}")
                confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))

                if confirmar == 1:
                    print ("Ok. \nEstes são seus dados.")
                    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))

                elif confirmar == 2:
                    while confirmar == 2:
                        placa_veiculo = input ("Digite, novamente, de forma fidedigna a placa de seu carro. \n")
                        print (f"A placa do seu veículo está correta? {placa_veiculo}")
                        confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
                        if confirmar == 1:
                            print ("Ok. \nEstes são seus dados.")
                            print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                            confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))

                elif confirmar > 2:
                    print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                    print (f"A placa do seu veículo está correta? {placa_veiculo}")
                    confirmar = int ( input ("Se sim, digite 1, senão, digite 2. \n"))
                    if confirmar == 1:
                        print ("Ok. \nEstes são seus dados.")
                        print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                        confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))

                    elif confirmar == 2:
                        while confirmar == 2:
                            placa_veiculo = input ("Digite, novamente, de forma fidedigna a placa de seu carro. \n")
                            print (f"A placa do seu veículo está correta? {placa_veiculo}")
                            confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
                            if confirmar == 1:
                                print ("Ok. \nEstes são seus dados.")
                                print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                                confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))


            if correcao == 2:
                ##re-solicitar ano do veículo
                print ("Agora, precisaremos do ano do seu automóvel.")

                ano_veicular = int ( input ("Digite o ano em que seu carro foi fabricado. \n"))
                confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))

                if confirmar == 1:
                    print ("Ok. \nEstes são seus dados.")
                    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
                elif confirmar == 2:
                    while confirmar == 2:
                        ano_veicular = int ( input ("Digite, novamente, o ano em que seu carro foi fabricado. \n"))
                        confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                        if confirmar == 1:
                            print ("Ok. \nEstes são seus dados.")
                            print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                            confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
                elif confirmar > 2:
                    while confirmar > 2:
                        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                        confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                        if confirmar == 1:
                            print ("Ok. \nEstes são seus dados.")
                            print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                        elif confirmar == 2:
                            while confirmar == 2:
                                ano_veicular = int ( input ("Digite, novamente, o ano em que seu carro foi fabricado. \n"))
                                confirmar = int ( input (f"O ano está correto? {ano_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                                if confirmar == 1:
                                    print ("Ok. \nEstes são seus dados.")
                                    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")

            if correcao == 3:
                ##re-solicitação do modelo do carro
                print ("Para finalizarmos o seu cadastro veicular,")
                modelo_veicular = input ("Informe-nos o modelo de seu veículo. Ex: Toyota, Corolla. \n")
                confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                
                if confirmar == 1:
                    print ("Ok. \nEstes são seus dados.")
                    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
                elif confirmar == 2:
                    while confirmar == 2:
                        modelo_veicular = input ("Informe-nos, novamente, o modelo de seu veículo. Ex: Toyota, Corolla. \n")
                        confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                        if confirmar == 1:
                            print ("Ok. \nEstes são seus dados.")
                            print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                            confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
                elif confirmar > 2:
                    while confirmar > 2:
                        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
                        confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                        if confirmar == 1:
                            print ("Ok. \nEstes são seus dados.")
                            print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                            confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
                        elif confirmar == 2:
                            while confirmar == 2:
                                modelo_veicular = input ("Informe-nos, novamente, o modelo de seu veículo. Ex: Toyota, Corolla. \n")
                                confirmar = int ( input (f"O modelo de seu automóvel está correto? {modelo_veicular} \nSe sim, digite 1, senão, digite 2. \n"))
                                if confirmar == 1:
                                    print ("Ok. \nEstes são seus dados.")
                                    print (f"{placa_veiculo};\n{ano_veicular};\n{modelo_veicular}.")
                                    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara fechar a aplicação, digite 5"))
if confirmacao == abrir_chamado:
    ##abertura de ticket para resolução de problema do cliente
    ##solicitação da placa do veículo do cliente
    placa = input ("\nPara abrir o seu ticket, precisaremos da placa de seu veículo. \n")
    print (f"Esta é a placa do seu automóvel? {placa}.")
    confirmar = int ( input ("Sim sim, digite 1, senão, digite 2. \n"))

    if confirmar == 1:
        print ("\nOk. O seu problema se enquadra em algum dos 5 problemas mais comuns dos automóveis?")
        print ("1. Superaquecimento. \n2. Pane elétrica. \n3. Problemas no câmbio. \n4. Bateria ruim. \n5. Falta de combustível.")
        problema = int ( input("Digite o número da categoria de seu problema. Se não se encaixar em nenhuma das opções acima, digite 6. \n"))
        if problema == 1:
            print ("\n- Verifique o ponteiro que marca a temperatura. \nSe ele chegar no vermelho, levo o veículo direto para uma oficina.")
            print ("\n- Complete o nível de água do motor. \nPorém, caso tenha que fazer isso diversas vezes em um curto período de tempo, \npode ser um aviso de que há algo errado.")
            print ("\n- Fique atento às mangueiras internas. Caso alguma esteja estufada, \npode haver uma má circulação da água.")
        elif problema == 2:
            print ("\n- Verificar se há sinais de dificuldade para ligar o automóvel.")
            print ("- Certificar-se de que não está acontecendo nenhum vazamento de ácido.")
            print ("Observar se acontece alguma redução das luzes ao dar a partida no carro.")
            print ("Conferir se a correia do alternador não está esbranquiçada ou desfiando.")
        elif problema == 3:
            print ("\n- Não apoie a mão no câmbio. Use a alavanca apenas na troca de marchas.")
            print ("Evite deixar o pé sobre a embreagem enquanto estiver dirigindo.")
            print ("Evite arrancar em segunda marcha. O motor suporta, mas isso causa um desgaste demasiado.")
        elif problema == 4:
            print ("\n- Um sensor de temperatura da bateria, o alternador danificado ou outros componentes do sistema de carregamento, \npodem acelerar esse problema.")
            print ("O ideal, portanto, é substituir a bateria do seu veículo no período indicado pelo fabricante, mesmo que não \nesteja apresentando sinais de dano")
        elif problema == 5:
            print ("\n- Certifique-se de que o marcador do automóvel está funcionando bem.")
            print ("Caso o ponto demore para descer, ou se está descendo rápido demais, talvez haja um problema na bomba.")
            print ("\n- A marcação de ¼ de combustível deve ser sempre considerada como indicativo para abastecer no próximo posto.")
            print ("\n- Evite postos com procedência duvidosa, afinal de contas, o produto fornecido pode estar alterado.")
        elif problema == 6:
            print ("Você deverá levar o seu carro em alguma mecânica filiada da Porto Seguro, para melhor resolução do problema.")

    if confirmar == 2:
        while confirmar == 2:
            placa = input ("Precisaremos da placa de seu veículo, novamente. \n")
            print (f"Esta é a placa do seu automóvel? {placa}.")
            confirmar = int ( input ("Sim sim, digite 1, senão, digite 2. \n"))

            if confirmar == 1:
                print ("\nOk. O seu problema se enquadra em algum dos 5 problemas mais comuns dos automóveis?")
                print ("1. Superaquecimento. \n2. Pane elétrica. \n3. Problemas no câmbio. \n4. Bateria ruim. \nFalta de combustível.")
                problema = int ( input("Digite o número da categoria de seu problema. Se não se encaixar em nenhuma das opções acima, digite 6. \n"))
                if problema == 1:
                    print ("\n- Verifique o ponteiro que marca a temperatura. \nSe ele chegar no vermelho, levo o veículo direto para uma oficina.")
                    print ("\n- Complete o nível de água do motor. \nPorém, caso tenha que fazer isso diversas vezes em um curto período de tempo, \npode ser um aviso de que há algo errado.")
                    print ("\n- Fique atento às mangueiras internas. Caso alguma esteja estufada, \npode haver uma má circulação da água.")
                elif problema == 2:
                    print ("\n- Verificar se há sinais de dificuldade para ligar o automóvel.")
                    print ("- Certificar-se de que não está acontecendo nenhum vazamento de ácido.")
                    print ("Observar se acontece alguma redução das luzes ao dar a partida no carro.")
                    print ("Conferir se a correia do alternador não está esbranquiçada ou desfiando.")
                elif problema == 3:
                    print ("\n- Não apoie a mão no câmbio. Use a alavanca apenas na troca de marchas.")
                    print ("Evite deixar o pé sobre a embreagem enquanto estiver dirigindo.")
                    print ("Evite arrancar em segunda marcha. O motor suporta, mas isso causa um desgaste demasiado.")
                elif problema == 4:
                    print ("\n- Um sensor de temperatura da bateria, o alternador danificado ou outros componentes do sistema de carregamento, \npodem acelerar esse problema.")
                    print ("O ideal, portanto, é substituir a bateria do seu veículo no período indicado pelo fabricante, mesmo que não \nesteja apresentando sinais de dano")
                elif problema == 5:
                    print ("\n- Certifique-se de que o marcador do automóvel está funcionando bem.")
                    print ("Caso o ponto demore para descer, ou se está descendo rápido demais, talvez haja um problema na bomba.")
                    print ("\n- A marcação de ¼ de combustível deve ser sempre considerada como indicativo para abastecer no próximo posto.")
                    print ("\n- Evite postos com procedência duvidosa, afinal de contas, o produto fornecido pode estar alterado.")
                elif problema == 6:
                    print ("Você deverá levar o seu carro em alguma mecânica filiada da Porto Seguro, para melhor resolução do problema.")
if confirmacao == consultar_chamado:
    placa = input ("Digite a placa, de forma fidedigna, de seu automóvel. \n")
    print (f"A placa do seu veículo está correta? {placa}")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
    if confirmar == 1:
        print ("O conserto de seu automóvel está em andamento.")

    elif confirmar == 2:
        while confirmar == 2:
            placa = input ("Digite a placa, novamente, de forma fidedigna, de seu automóvel. \n")
            print (f"A placa do seu veículo está correta? {placa}")
            confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
            if confirmar == 1:
                print ("O conserto de seu automóvel está em andamento.")

    elif confirmar > 2:
        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        print (f"A placa do seu veículo está correta? {placa}")
    confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
    if confirmar == 1:
        print ("O conserto de seu automóvel está em andamento.")
    elif confirmar == 2:
        while confirmar == 2:
            placa = input ("Digite a placa, novamente, de forma fidedigna, de seu automóvel. \n")
            print (f"A placa do seu veículo está correta? {placa}")
            confirmar = int ( input ("Se sim, digite 1, senão, digite 2."))
            if confirmar == 1:
                print ("O conserto de seu automóvel está em andamento.")
