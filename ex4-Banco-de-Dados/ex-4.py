import os
import time


# Estrutura do 'Banco'.
banco_usuario = {} # Dicionario criado para atuar como se fosse um banco de dados.
unique_id = 1 # Variavel declarada para atuar com se fosse um uniqueid, garatindo a order do 'banco'.

# Constantes.
# Opcoes de resposta do usuario dentro dos menus.
OPTION_1 = '1'
OPTION_2 = '2'
OPTION_3 = '3'
OPTION_4 = '4'
OPTION_5 = '5'

MENU_A = 'a' # menu Principal
MENU_B = 'b' # menu para cadastra mais campos
MENU_C = 'c' # menu para os filtros do imprimir_usuarios
MENU_D = 'd' # menu para os filtros do imprimir_usuarios_campos

# Funcoes.
def menu(param = 'a'):
    """
     -- Funcao responsavel apenas para exibir o meu menu dentro do programa.
     -- Sem parametros. 
    """
    if param == MENU_A:
        print('='*20)
        print('[1].Cadastrar Usuario')
        print('[2].Imprimir Usuario')
        print('[3].Encerrar')
        print('='*20)
    
    elif param == MENU_B:
        print('[1].Adicionar Campo')
        print('[2].Sair')
        print('='*20)
    
    elif param == MENU_C:
        print('[1].Imprimir Todos')
        print('[2].Filtrar por Nomes')
        print('[3].Filtrar por Campos')
        print('[4].Filtrar por Nomes e Campos')
        print('[5].Sair')
        print('='*20)


def verifica_campo(campo, campos_cadastrados):
    """
     -- Funcao responsavel por verificar os campos que ja estao cadastrados a fim de aceitar somentes campos novos.
     -- campo: Campo que esta sendo adicionado.
     -- campos_cadastrados: Lista dos campos que ja foram cadastrados para esse usuario.
    """
    if campo in campos_cadastrados:
        print('::ERRO:: CAMPO JA CADASTRADO!')
        return False
    return True

def seta_campos():
    """
     -- Funcao responsavel por setar os campos obrigatorios a partir do input do usuario.
     -- Sem parametros. 
    """
    campos = input('Digite os campos Obrigatorios (separados por virgula): ').split(',')
    campos_obrigatorios = tuple([x.strip().lower() for x in campos])
    print(campos_obrigatorios)
    return campos_obrigatorios


def transicao(tempo = 1):
    """
     -- Funcao responsavel por fazer a transicao entre os menus e as visualicoes de dados no terminal
     -- Sem parametros.
    """
    time.sleep(tempo)
    os.system('cls')



def cadastra_usuario(campos):
    """
     -- Funcao resposavel por popular os campos obrigatorios passados pelo usuario, e cadastra-lo no banco de usuarios.
     -- campos: Tupla contendo os campos Obrigatorios
    """
    campos_cadastrados = list(campos)
    user = {}


    for campo in campos_cadastrados:
        print(f'{campo} (obrigatorio): ', end='')  
        valor = input('').lower()
        if(valor == ''):
            valor = None
        user[campo] = valor
        print(f':: SUCESSO :: {campo.upper()}: {valor.capitalize()} CADASTRADO.')

    transicao()
    
    while(True):
        print('-'*30)
        print(f'CASTRANDO USUARIO: {user["nome"]}')
        print('-'*30)
        menu(MENU_B)
        resp = input('Opcao: ')
        if resp == OPTION_1:
            campo_novo = input('Digite um Campo: ').lower()
            if (verifica_campo(campo_novo, campos_cadastrados)):
                print(f'{campo_novo.upper()}: ', end='')  
                valor_novo = input('').lower()
                if (valor_novo == ''):
                    valor_novo = None
                user[campo_novo] = valor_novo
                print(f':: SUCESSO :: {campo_novo.upper()}: {valor_novo.capitalize()} CADASTRADO.')
                transicao()
        

        elif resp == OPTION_2:
            print('VOLTANDO AO MENU!')
    
            break

        else:
            print('DIGITE UMA OPCAO VALIDA!')  
    
    return user


def imprimir_usuario_todos():
    for user in banco_usuario.values():
        for k,v in user.items():
            print(f'{k} ==> {v}')
        print('-'*20)
    time.sleep(3)


def imprimir_usuario_nomes(*nomes, ret = False):
    """
     -- Funcao resposavel por apresentar os usuarios na tela, filtrando pelos nomes
     -- nomes: Parametro onde estao os nomes que deverao ser listados
     -- ret: Parametro que retorna uma lista com os nomes do usuarios filtrados
    """
    lista_nomes = nomes
    retorno = []
    if (lista_nomes):
        for user in banco_usuario.values():
            if user['nome'] in lista_nomes[0]:
                retorno.append(user)
                if (not ret):
                    for k,v in user.items():
                        print(f'{k} ==> {v}')
                    print('-='*20)

    if (ret):
        return retorno

    time.sleep(3)


def imprimir_usuario_campos(lista_nomes='', **campos):
    """
     -- Funcao resposavel por apresentar os usuarios na tela, filtrando pelos campos.
     -- lista_nomes: Parametro onde estarao os nomes pelo qual a busca por campos devera filtrar, caso vazio, ela filtrara pelo banco de usuarios.
     -- campos: Parametro onde estarao os campos de filtragem setados pelo usuario.
    """
    arr = []
    retorno = []
    banco = {}
    if(lista_nomes):
        for i in range(len(lista_nomes)):
            banco[i] = lista_nomes[i]
        dicio_tmp = banco
    else:
        dicio_tmp = banco_usuario
    for c, v in campos.items():
        arr.append((c, v))
    
    for ele in arr:
        retorno.clear()
        for value in dicio_tmp.values():
            for k, v in value.items():
                if ele[0] == k and ele[1] == v:
                    retorno.append(value)
        
        dicio_tmp = {}
        for i in range(len(retorno)):
            dicio_tmp[i] = retorno[i]
    if(retorno):
        for user in retorno:
            for k, v in user.items():
                print(f'{k} ==> {v}')
            print('-='*20)
    else:
        print('::ERRO:: NENHUM USUARIO ENCONTRADO!')

def imprimir_usuario():
    """
     -- Funcao resposavel por todas as acoes que envolvem a apresentacao de usuarios na tela
    """
    menu('c')
    opcao = input('Opcao: ')
    if opcao == OPTION_1:
        imprimir_usuario_todos()
    elif opcao == OPTION_2:
        nomes = [x.strip().lower() for x in input('Digite os nomes (separados por virgula): ').split(',')]
        imprimir_usuario_nomes(nomes)
    elif opcao == OPTION_3:
        filtro = {}
        while(True):
            campo = (input('Digite o campo de Busca: ').strip().lower())
            valor = (input(f'Digite o {campo.capitalize()}: ').strip().lower())
            filtro[campo] = valor
            resp = input('Mais algum campo [s/n]: ').strip().lower()
            if resp == 'n':
                break
        imprimir_usuario_campos(**filtro)
    elif opcao == OPTION_4:
        nomes = [x.strip().lower() for x in input('Digite os nomes (separados por virgula): ').split(',')]
        retorno = imprimir_usuario_nomes(nomes, ret = True)
        filtro = {}
        while(True):
            campo = (input('Digite o campo de Busca: ').strip().lower())
            valor = (input(f'Digite o {campo.capitalize()}: ').strip().lower())
            filtro[campo] = valor
            resp = input('Mais algum campo [s/n]: ').strip().lower()
            if resp == 'n':
                break
        imprimir_usuario_campos(lista_nomes=retorno, **filtro)
    elif opcao == OPTION_5:
        print('VOLTANDO AO MENU!')




# Run.

# Setando campos obrigatorios para todos os cadastros.
campos_obrigatorios = seta_campos()
transicao(1)
while(True):
    menu()
    resp = input('Opcao: ')
    if resp == OPTION_1:
        banco_usuario[unique_id] = cadastra_usuario(campos_obrigatorios)
        unique_id += 1
        transicao()
    elif(resp == OPTION_2):
        imprimir_usuario()
        transicao(3)
    elif resp == OPTION_3:
        print('::SUCESSO::  ENCERRANDO PROGRAMA!') 
        break
    else:
        print('DIGITE UMA OPCAO VALIDA!')
