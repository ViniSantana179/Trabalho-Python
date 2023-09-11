import random

jogo = [
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-'],
    ['-', '-', '-', '-']
]

def desenha_jogo(jogo):
    cont_lin = 0
    cont_col = 0

    for i in range(len(jogo)):
        print(f'   {cont_col}', end = '')
        cont_col += 1
    print()
    for linha in jogo:
        print(f'{cont_lin}', end='')
        print('| ', end='')
        for ele in linha:
            print(f'{ele}', end=' | ')
        print()
        cont_lin += 1

def preenche_jogo(jogo, jogada, jogador):
    if jogo[jogada[0]][jogada[1]] == '-':
        jogo[jogada[0]][jogada[1]] = jogador
        return True
    else:
        print("Essa célula já está preenchida. Escolha outra.")
        return False

def verifica_ganhador(jogo, param):
    # Verificação de vitória precisa ser implementada para um tabuleiro 4x4
    for linha in jogo:
        if all([celula == param for celula in linha]):
            return True
    
    for coluna in range(4):
        if all([jogo[linha][coluna] == param for linha in range(4)]):
            return True

    # Verificar diagonais
    if all([jogo[i][i] == param for i in range(4)]) or all([jogo[i][3 - i] == param for i in range(4)]):
        return True

    return False

# Inicialização das variáveis
jogadores = ['X', 'O']
num_jogadas = 0
quem_comeca = random.choice([0, 1])
jogador = jogadores[quem_comeca]

while num_jogadas < 16:
    desenha_jogo(jogo)
    print(f'JOGADOR: {jogador}')
    jogada = [int(x.strip()) for x in input('Posicao (lin, col): ').split(',')]

    if 0 <= jogada[0] < 4 and 0 <= jogada[1] < 4:
        if preenche_jogo(jogo, jogada, jogador):
            num_jogadas += 1
            if verifica_ganhador(jogo, jogador):
                print(f'Jogador {jogador} venceu!')
                break
            else:
                jogador = 'X' if jogador == 'O' else 'O'
        else:
            print('Jogada inválida. Tente novamente.')
    else:
        print('Posição fora do tabuleiro. Tente novamente.')

if num_jogadas == 16:
    print('Empate! O jogo terminou sem vencedores.')

print('Fim do jogo.')