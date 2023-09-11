from unidecode import unidecode
import random

arquivo = "lista_palavras.txt"

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """
    with open(arq, encoding='utf-8') as f:
        return [linha.strip() for linha in f] 

lista_aux = le_arquivo(arquivo)
lista = [x for x in lista_aux if len(x) == 5]

palavra_secreta = lista[random.randint(0, len(lista) - 1)]
palavra_secreta = unidecode(palavra_secreta)

print(palavra_secreta)
palavra_montada = ['-', '-', '-', '-', '-']
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letras_removidas = []
letras_corretas = []
num_tentativas = 3

def verifica_palavra(palavra, palavra_secreta):
    if palavra == palavra_secreta:
        print(f'Parabens a palavra sorteada era {palavra}')
        return True
    else:
        for i in range(len(palavra)):
            if palavra[i] not in palavra_secreta:
                print(palavra[i].upper())
                if palavra[i] not in letras_removidas:
                    alfabeto.remove(palavra[i].upper())
                    letras_removidas.append(palavra[i])
            else:
                if palavra [i] not in letras_corretas:
                    letras_corretas.append(palavra[i])
                    if palavra[i] == palavra_secreta[i]:
                        print(f'A letra \033[0;30;44m[{palavra[i].upper()}]\033[m esta na posicao correta.')
                        palavra_montada[i] = palavra[i]
                    else:
                        print(f'A letra \033[0;30;43m[{palavra[i].upper()}]\033[m existe na palavra mas nao esta na posicao correta.')
        return False

                
                
while(True):
        print(f'PALAVRA: {palavra_montada}')
        print(f'Letras Disponiveis: {alfabeto}')
        print(f'Letras Corretas: {letras_corretas}')
        palavra = input('Digite uma palavra: ')
        if len(palavra) == 5:
            if(verifica_palavra(palavra, palavra_secreta)):
                break
        else:
            print('Digite uma palavra com 5 letras.')
        if(len(letras_corretas) == 5 or num_tentativas == 0):
            print('GAME OVER!')
            print('A palavra sorteada era {palavra_sorteada}.')
            break
        num_tentativas -= 1