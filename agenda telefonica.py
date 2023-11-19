import copy
atual=[]
lista=[]
agenda= { }


##Criando a estrutura dos dados

def adicionar_novo_contato():
    print('Inserindo novos numeros')
    while True:
        print(' Adicione um novo contato ? ')
        agenda['nome'] = input('Escolha um nome ')
        agenda['Telefone1'] = (input('Adicione o numero de celular chip1 '))
        agenda['Telefone2'] = (input('Adicione o numero de celular chip2 '))
        lista.append(agenda.copy())

        print('Contato adicionado')
        print(lista)

        continuar = input('Deseja continuar a inserir os contatos ? ')
        if continuar == 'sim':
            continue
        else:
            print('Finalizando adição de contatos')
            print(lista)
            break
#adicionar_novo_contato()


def adicionar_novo_numero():
    inserir = input('Deseja inserir a um numero a um contato existente ou inserir tudo do 0 ? ')
    if inserir == ' do 0':
        adicionar_novo_contato()
    elif inserir == 'existente':
        qualc = str(input('Qual seria o nome dessa pessoa ? '))
        if qualc in agenda['nome']:
            agenda['Telefone1'] = input('Insira o numero se for no chip1 ')
            agenda['Telefone2'] = input('Insira o numero se for no chip2 ')
            print(agenda)
        else:
            print('Nenhuma opção coicide, fim do programa')
# adicionar_novo_numero()

def excluir_contato_completo():
    ctz = input('Tem certeza que deseja utilizar essa função de deletar contatos ?')
    if ctz == 'sim':
        apagar = input('Qual nome do contato que deseja apagar')
        if apagar in agenda['nome']:
            agenda.clear()
            for n in lista:
                if n['nome'] == apagar:
                    alvo = (lista.index(n))
                    lista.pop(alvo)
                    print('Listas com os contatos atuais')
                    print(lista)


# excluir_contato_completo()

def encontrar_numero():
    numero = input('Digite o numero que voce procura na lista')
    if numero in agenda['Telefone1'] or agenda['Telefone2']:
        print(agenda['nome'])


# encontrar_numero()

def excluir_numero():
    print('=-=' * 20)
    print(lista)
    excluir = input('Qual numero de celular voce quer excluir? ')
    if excluir in agenda['Telefone1'] or agenda['Telefone2']:
        print(agenda)
        exe = agenda['nome']
        print(exe)
        if agenda['Telefone1'] == excluir:
            agenda['Telefone1'] = ' '
            print(agenda)
            if agenda['Telefone1'] or agenda['Telefone2'] == ' ':
                print('Esse contato sera apagado')
                for n in lista:
                    if n['nome'] == exe:
                        alvo = (lista.index(n))
                        lista.pop(alvo)
                        print('Listas com os contatos atuais')
                        print(lista)

        elif agenda['Telefone2'] == excluir:
            agenda['Telefone2'] = ' '
            print(agenda)
            if agenda['Telefone1'] or agenda['Telefone2'] == ' ':
                print('Esse contato sera exlcluido da agenda')
                for n in lista:
                    if n['nome'] == exe:
                        alvo = (lista.index(n))
                        lista.pop(alvo)
                        print('Listas com os contatos atuais')
                        print(lista)

        else:
            print('Inserção numero invalida')

# excluir_numero()

"""Excluir telefone"""

print('Agenda telefonica')
print('Ola Selecione conforme melhor opção te atender')
opcoes=[
    'Escolha 1 = Adicionar novo contato',
    'Escolha 2 = Adcionar novo numero',
    'Escolha 3 = Encontrar numero ',
    'Escolha 4 = Excluir numero ',
    'Escolha 5 = Excluir contato completo'
]
for n in opcoes:
    print(n)

while True:
    escolha=input('Qual das opções voce deseja. lembrando que a agenda esta vazia ainda, não existem contatos \n'
                  'para serem exlcuidos, caso quiser terminar so digitar nao ' )
    if escolha =='1':
        adicionar_novo_contato()
    elif escolha=='2':
        adicionar_novo_numero()
    elif escolha=='3':
        encontrar_numero()
    elif  escolha=='4':
        excluir_numero()
    elif escolha =='5':
        excluir_contato_completo()
    elif escolha=='nao':
        print('Fim do codigo')
        break
    else:
        print('Opção invaliada')



