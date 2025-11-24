# Jogo da Velha usando matriz 3x3

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tab):
    print("\n  0   1   2")
    for i, linha in enumerate(tab):
        print(i, " | ".join(linha))
        if i < 2:
            print("  ---------")

def verificar_vitoria(tab):
    # Linhas
    for linha in tab:
        if linha[0] == linha[1] == linha[2] != " ":
            return True

    # Colunas
    for c in range(3):
        if tab[0][c] == tab[1][c] == tab[2][c] != " ":
            return True

    # Diagonais
    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return True

    return False

def jogo_da_velha():
    tab = criar_tabuleiro()
    jogador = "X"
    jogadas = 0

    while True:
        mostrar_tabuleiro(tab)
        print(f"\nVez do jogador {jogador}")

        linha = int(input("Escolha a linha (0, 1 ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

        if tab[linha][coluna] != " ":
            print("Posição ocupada! Tente novamente.")
            continue

        tab[linha][coluna] = jogador
        jogadas += 1

        if verificar_vitoria(tab):
            mostrar_tabuleiro(tab)
            print(f"\n🎉 Jogador {jogador} venceu!")
            break

        if jogadas == 9:
            mostrar_tabuleiro(tab)
            print("\n⚠️ Empate!")
            break

        # Troca de jogador
        jogador = "O" if jogador == "X" else "X"


jogo_da_velha()
