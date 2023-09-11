import random

def inicializa_tabuleiro(n):
    tabuleiro = [[' ' for _ in range(n)] for _ in range(n)]
    return tabuleiro

def imprime_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * (n * 2 - 1))

def preenche_jogo(tabuleiro, jogada, jogador):
    if tabuleiro[jogada[0]][jogada[1]] == ' ':
        tabuleiro[jogada[0]][jogada[1]] = jogador
        return True
    else:
        print("Essa célula já está preenchida. Escolha outra.")
        return False

def verifica_ganhador(tabuleiro, jogador):
    n = len(tabuleiro)
    
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    
    for coluna in range(n):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(n)]):
            return True

    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(n)]) or all([tabuleiro[i][n - i - 1] == jogador for i in range(n)]):
        return True

    return False

def jogo_da_velha_nxn(n):
    tabuleiro = inicializa_tabuleiro(n)
    jogadores = ['X', 'O']
    jogador_atual = random.choice(jogadores)
    num_jogadas = 0

    print(f"Bem-vindo ao Jogo da Velha {n}x{n}!")

    while True:
        imprime_tabuleiro(tabuleiro)
        print(f'JOGADOR: {jogador_atual}')
        jogada = [int(x.strip()) for x in input(f'Posicao (linha, coluna) - Digite números de 0 a {n-1}, separados por vírgula: ').split(',')]

        if 0 <= jogada[0] < n and 0 <= jogada[1] < n:
            if preenche_jogo(tabuleiro, jogada, jogador_atual):
                num_jogadas += 1
                if verifica_ganhador(tabuleiro, jogador_atual):
                    imprime_tabuleiro(tabuleiro)
                    print(f'Jogador {jogador_atual} venceu!')
                    break
                elif num_jogadas == n * n:
                    imprime_tabuleiro(tabuleiro)
                    print('O jogo terminou em empate!')
                    break
                else:
                    jogador_atual = 'X' if jogador_atual == 'O' else 'O'
            else:
                print('Jogada inválida. Tente novamente.')
        else:
            print(f'Posição fora do tabuleiro. Digite números de 0 a {n-1}.')

    print('Fim do jogo.')

# Tamanho do tabuleiro (por exemplo, 3 para um jogo da velha 3x3)
n = int(input("Digite o tamanho do tabuleiro (n x n): "))
jogo_da_velha_nxn(n)