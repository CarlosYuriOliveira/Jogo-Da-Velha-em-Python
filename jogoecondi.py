import mtrizO
import mtrizX
def jogo():
    m = [[" "," "," "],[" "," "," "],[" "," "," "]]
    cont = 1
    escolha = str(input("Qual ira começar ( X ou O )? ")).lower()
    if escolha == "o":
        while cont <= 5:
            mtrizO.matrizo(m)
            if (m[0][0] == 'o' and m[0][1] == 'o' and m[0][2] == 'o') \
                    or (m[1][0] == 'o' and m[1][1] == 'o' and m[1][2] == 'o') \
                    or (m[2][0] == 'o' and m[2][1] == 'o' and m[2][2] == 'o') \
                    or (m[0][0] == 'o' and m[1][0] == 'o' and m[2][0] == 'o') \
                    or (m[0][1] == 'o' and m[1][1] == 'o' and m[2][1] == 'o') \
                    or (m[0][2] == 'o' and m[1][2] == 'o' and m[2][2] == 'o') \
                    or (m[0][0] == 'o' and m[1][1] == 'o' and m[2][2] == 'o') \
                    or (m[0][2] == 'o' and m[1][1] == 'o' and m[2][0] == 'o'):
                print("Jogador do X ganhou\n!!")
                break
            if cont == 5:
                break
            mtrizX.matrizx(m)
            if (m[0][0] == 'x' and m[0][1] == 'x' and m[0][2] == 'x') \
                    or (m[1][0] == 'x' and m[1][1] == 'x' and m[1][2] == 'x') \
                    or (m[2][0] == 'x' and m[2][1] == 'x' and m[2][2] == 'x') \
                    or (m[0][0] == 'x' and m[1][0] == 'x' and m[2][0] == 'x') \
                    or (m[0][1] == 'x' and m[1][1] == 'x' and m[2][1] == 'x') \
                    or (m[0][2] == 'x' and m[1][2] == 'x' and m[2][2] == 'x') \
                    or (m[0][0] == 'x' and m[1][1] == 'x' and m[2][2] == 'x') \
                    or (m[0][2] == 'x' and m[1][1] == 'x' and m[2][0] == 'x'):
                print("Jogador do O ganhou\n!!")
                break
            cont+=1
    if escolha == "x":
        while cont <= 5:
            mtrizX.matrizx(m)
            if (m[0][0] == 'x' and m[0][1] == 'x' and m[0][2] == 'x') \
                    or (m[1][0] == 'x' and m[1][1] == 'x' and m[1][2] == 'x') \
                    or (m[2][0] == 'x' and m[2][1] == 'x' and m[2][2] == 'x') \
                    or (m[0][0] == 'x' and m[1][0] == 'x' and m[2][0] == 'x') \
                    or (m[0][1] == 'x' and m[1][1] == 'x' and m[2][1] == 'x') \
                    or (m[0][2] == 'x' and m[1][2] == 'x' and m[2][2] == 'x') \
                    or (m[0][0] == 'x' and m[1][1] == 'x' and m[2][2] == 'x') \
                    or (m[0][2] == 'x' and m[1][1] == 'x' and m[2][0] == 'x'):
                print("Jogador do O ganhou\n!!")
                break
            if cont == 5:
                break
            mtrizO.matrizo(m)
            if (m[0][0] == 'o' and m[0][1] == 'o' and m[0][2] == 'o') \
                    or (m[1][0] == 'o' and m[1][1] == 'o' and m[1][2] == 'o') \
                    or (m[2][0] == 'o' and m[2][1] == 'o' and m[2][2] == 'o') \
                    or (m[0][0] == 'o' and m[1][0] == 'o' and m[2][0] == 'o') \
                    or (m[0][1] == 'o' and m[1][1] == 'o' and m[2][1] == 'o') \
                    or (m[0][2] == 'o' and m[1][2] == 'o' and m[2][2] == 'o') \
                    or (m[0][0] == 'o' and m[1][1] == 'o' and m[2][2] == 'o') \
                    or (m[0][2] == 'o' and m[1][1] == 'o' and m[2][0] == 'o'):
                print("Jogador do X ganhou\n!!")
                break
            cont+=1

