#Challenge 2024 - Sprint 1 - DSC - 19h26 - 20/05/2024

import re
import os
os.system('cls')

def menu_c(confirmacao):
    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara cadastro veicular, digite 5. \n"))
    return confirmacao

def menu(confirmacao):
    confirmacao = int ( input ("\nPara abrir um ticket, digite 3. \nPara consultar seus tickets digite 4. \nPara cadastro veicular, digite 5. \nPara fechar a aplicação, digite 6. \n"))
    return confirmacao

#Local onde as variáveis de condição do programa se encontram.
#welcome!
cadastro = 1
cadastro_pessoal = 'PF'
cadastro_juridico = 'PJ'
login = 2
#menus
abrir_chamado = 3
consultar_chamado = 4
cadastro_veicular = 5
fechar = 6
#validações
confirmar = 1 or 2
correcao = 0

home = print ("Olá, seja bem vindo a plataforma Porto Seguro.")
confirmacao = int (input ("\nPara cadastrar-se, digite 1. \nPara logar na plataforma, digite 2. \n"))
if confirmacao > 2 or confirmacao < 1:
    while confirmacao > 2 or confirmacao < 1:
        print ("\nRESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        confirmacao = int (input ("\nPara cadastrar-se, digite 1. \nPara logar na plataforma, digite 2. \n"))

if confirmacao == 1:
    confirmacao = str ( input ("\nPessoa Jurídica (PJ) \nPessoa física (PF) \n"))

if confirmacao == cadastro_juridico:
    print ("\nEsta é a tela de cadastro. Seja bem vindo!")
    ##lista PJ
    pj = []
    ##tela de cadastro juridico - pj
    ##solicitação do cnpj
    cnpj = input ("Digite o CNPJ da empresa. \n")

    pj.append(cnpj)

    ##solicitação da razão social da empresa
    nomePJ = input ("Digite a razão social da empresa. \n")

    pj.append(nomePJ)

    ##solicitação de email para contato
    emailPJ = input ("Informe um email para contato. \n")


    pj.append(emailPJ)

    ##criação de senha
    senha_pj = input ("\nCrie uma senha: \n")
    senha_pj1 = input ("\nRepita a senha: \n")
    if senha_pj1 == senha_pj:
        print ("\nOk. Suas senhas conferem, anote-a para não esquecer.")
    else:
        while senha_pj1 != senha_pj:
            print ("As senhas não conferem. ")
            senha1 = input ("\nRepita a senha: \n")
            if senha_pj1 != senha_pj:
                print ("\nOk. Suas senhas conferem, anote-a para não esquecer.")
    
    pj.append(senha_pj1)

    ##tela final - mostrar dados cadastrados

    print ("Estes são seus dados:")
    print (pj[0])
    print (pj[1])
    print (pj[2])
    print (pj[3])
    print ("Anote sua senha para não esquece-lá.")
    
    confirmacao = menu(confirmacao)

if confirmacao == cadastro_pessoal:
    print ("\nEsta é a tela de cadastro. Seja bem vindo!")
    #criação de lista
    dadosPessoais = []

    #solicitação do nome do cliente.
    nome = input ("\nDigite seu nome completo. \n")

    dadosPessoais.insert(1, nome)

    #solicitação da data de nascimento do cliente
    nascimento = input ("\nDigite sua data de nascimento, conforme o exemplo: xx/xx/xxxx. \n")

    dadosPessoais.insert(2, nascimento)

    #solicitação do gênero do cliente - loop e if
    print ("Defina seu gênero digitando os números respectivos da categoria.")
    genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))


    while genero > 4:
        print ("RESPOSTA INVÁLIDA! DIGITE APENAS 1 OU 2!")
        genero = int ( input ("1 - Masculino. \n2 - Feminino. \n3 - Não binário. \n4 - Prefiro não informar. \n"))

    #mostra o gênero selecionado ao usuário
    if genero == 1:
        genero = 'Masculino'
        print ("Gênero masculino.")
        dadosPessoais.insert(3, genero)

    elif genero == 2:
        genero = 'Feminino'
        print ("Gênero feminino.")
        dadosPessoais.insert(3, genero)

    elif genero == 3:
        genero = 'Não-binário'
        print ("Gênero não-binário.")
        dadosPessoais.insert(3, genero)

    elif genero == 4:
        genero = 'Preferiu não informar o gênero'
        print ("Não informar o gênero.")
        dadosPessoais.insert(3, genero)
 
    #solicitação de contato - celular/telefone
    numero_telefone1 = input ("\nPara termos uma informação de contato, precisaremos do seu telefone. \nDigite-o conforme a formatação a seguir: \n(XX)XXXXX-XXXX ou XXXX-XXXX se usas telefone convencional \n")
         
    dadosPessoais.insert(4, numero_telefone1)

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
    cpf = str(input("\nDigite seu CPF, sem traços e pontos: ")).strip()

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

    dadosPessoais.insert(5, cpf_formatado)

    ##criação da senha do cliente
    senha = input ("\nCrie uma senha: \n")
    senha1 = input ("\nRepita a senha: \n")
    if senha1 == senha:
        print ("\nOk. Suas senhas conferem, anote-a para não esquecer.")
    else:
        while senha1 != senha:
            print ("As senhas não conferem. ")
            senha1 = input ("\nRepita a senha: \n")
            if senha1 != senha:
                print ("\nOk. Suas senhas conferem, anote-a para não esquecer.")

    dadosPessoais.insert(6, senha1)
                
    #tela final - confirmação dos dados
    print ("\nEstes são os seus dados.")
    print (dadosPessoais[0])
    print (dadosPessoais[1])
    print (dadosPessoais[2])
    print (dadosPessoais[3])
    print (dadosPessoais[4])
    print (dadosPessoais[5])
    print ("Anote sua senha para não esquece-la.")
    
    confirmar = int ( input ("Gostaria de prosseguir? Se sim, digite 1. Para fechar o programa, digite 2. \n"))
    if confirmar == 1:
        if confirmar == 1 and genero == 'Masculino':
            print (f"\nCadastro finalizado senhor {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = menu_c(confirmacao)

        elif confirmar == 1 and genero == 'Feminino':
            print (f"\nCadastro finalizado senhora {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = menu_c(confirmacao)

        elif confirmar == 1 and genero == 'Não-binário':
            print (f"\nCadastro finalizado senhore {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = menu_c(confirmacao)

        elif confirmar == 1 and genero == 'Preferiu não informar o gênero':
            print (f"\nCadastro finalizado {nome}. \nAgora você pode usufruir de toda nossa plataforma. \nObrigado pela escolha.")
            confirmacao = menu_c(confirmacao)

    else:
        print ("Ok. Programa finalizado.")

if confirmacao == login:
    print ("\nEsta é a tela de login. Seja bem vindo, novamente!")
    numero_telefone = input("\nTelefone: \n")
    senha2 = input ("\nSenha: \n")
    
    print ("\nSeja bem vindo ao portal do cliente Porto Seguro.") 
    confirmacao = menu(confirmacao)

#--------------------------------------------------------------------#
##qualquer outra funcao do menu deve ser colocada dentro do laço
##caso esteja fora, sendo IF, nao funcionara
##unica opcao do menu fora do while deve ser a que fecha o programa!
#--------------------------------------------------------------------#

while confirmacao == 3 or confirmacao == 4 or confirmacao == 5:
    if confirmacao == abrir_chamado:
        ##abertura de ticket para resolução de problema do cliente
        ##solicitação da placa do veículo do cliente
        placa = input ("\nPara abrir o seu ticket, precisaremos da placa de seu veículo. \n")   
        print ("\nOk. O seu problema se enquadra em algum dos 5 problemas mais comuns dos automóveis?")
        print ("1. Superaquecimento. \n2. Pane elétrica. \n3. Problemas no câmbio. \n4. Bateria ruim. \n5. Falta de combustível.")
        problema = int ( input("Digite o número da categoria de seu problema. Se não se encaixar em nenhuma das opções acima, digite 6. \n"))
        if problema == 1:
            print ("\n- Verifique o ponteiro que marca a temperatura. \nSe ele chegar no vermelho, levo o veículo direto para uma oficina.")
            print ("\n- Complete o nível de água do motor. \nPorém, caso tenha que fazer isso diversas vezes em um curto período de tempo, \npode ser um aviso de que há algo errado.")
            print ("\n- Fique atento às mangueiras internas. Caso alguma esteja estufada, \npode haver uma má circulação da água.")
            confirmacao = menu(confirmacao)
        elif problema == 2:
            print ("\n- Verificar se há sinais de dificuldade para ligar o automóvel.")
            print ("- Certificar-se de que não está acontecendo nenhum vazamento de ácido.")
            print ("Observar se acontece alguma redução das luzes ao dar a partida no carro.")
            print ("Conferir se a correia do alternador não está esbranquiçada ou desfiando.")
            confirmacao = menu(confirmacao)
        elif problema == 3:
            print ("\n- Não apoie a mão no câmbio. Use a alavanca apenas na troca de marchas.")
            print ("Evite deixar o pé sobre a embreagem enquanto estiver dirigindo.")
            print ("Evite arrancar em segunda marcha. O motor suporta, mas isso causa um desgaste demasiado.")
            confirmacao = menu(confirmacao)
        elif problema == 4:
            print ("\n- Um sensor de temperatura da bateria, o alternador danificado ou outros componentes do sistema de carregamento, \npodem acelerar esse problema.")
            print ("O ideal, portanto, é substituir a bateria do seu veículo no período indicado pelo fabricante, mesmo que não \nesteja apresentando sinais de dano")
            confirmacao = menu(confirmacao)
        elif problema == 5:
            print ("\n- Certifique-se de que o marcador do automóvel está funcionando bem.")
            print ("Caso o ponto demore para descer, ou se está descendo rápido demais, talvez haja um problema na bomba.")
            print ("\n- A marcação de ¼ de combustível deve ser sempre considerada como indicativo para abastecer no próximo posto.")
            print ("\n- Evite postos com procedência duvidosa, afinal de contas, o produto fornecido pode estar alterado.")
            confirmacao = menu(confirmacao)
        elif problema == 6:
            print ("Você deverá levar o seu carro em alguma mecânica filiada da Porto Seguro, para melhor resolução do problema.")
            confirmacao = menu(confirmacao)

    elif confirmacao == consultar_chamado:
        #exemplo fictício

        #assim que um database for implementado em nosso projeto, havera um validacao do dado
        #iremos conferir a existencia da placa dentro de nosso banco e puxar qual a situação atual referente a manutencao do veiculo

        placa = input ("Digite a placa, de forma fidedigna, de seu automóvel. \n")
        print ("O conserto de seu automóvel está em andamento.")
        confirmacao = menu(confirmacao)
    
    elif confirmacao == cadastro_veicular:
            #criação lista cadastro veicular 
            dadosVeiculares = []

            ##solicitação da placa do veículo
            print ("\nAgora cadastraremos seu veículo para que você possa usufruir da nossa plataforma.")

            placa_veiculo = input ("Digite a placa, de forma fidedigna, de seu automóvel. \n")
            
            dadosVeiculares.insert(0, placa_veiculo)

            ##solicitar ano do veículo
            print ("\nAgora, precisaremos do ano do seu automóvel.")

            ano_veicular = int ( input ("Digite o ano em que seu carro foi fabricado. \n"))
            
            dadosVeiculares.insert(1, ano_veicular)

            ##solicitação do modelo do carro
            print ("\nPara finalizarmos o seu cadastro veicular,")
            modelo_veicular = input ("Informe-nos o modelo de seu veículo. Ex: Toyota, Corolla. \n")
            
            dadosVeiculares.insert(2, modelo_veicular)

            ##tela final - confirmação
            print ("\nEstes são seus dados.")
            print (dadosVeiculares[0])
            print (dadosVeiculares[1])
            print (dadosVeiculares[2])
        
            print (f"O seu veículo, {modelo_veicular}, foi cadastrado com sucesso em nosso sistema.")
            confirmacao = menu(confirmacao)

if confirmacao == fechar:
        print ("\nPrograma finalizado.")
