def matrizx(m):
    print("Vez do X\n")
    i = int(input("Linha: "))
    j = int(input("Coluna: "))
    if m[i][j] == 'x' or m[i][j] == 'o':
        while m[i][j] == 'x' or m[i][j] == 'o':
            print("Espaço ocupado!!")
            print("Digite outra posição")
            i = int(input("Linha: "))
            j = int(input("Coluna: "))
    m[i][j] = 'x'
    print("     0     1     2")
    print(f' 0  {m[0][0]}   |  {m[0][1]}  |  {m[0][2]} ')
    print(f"    -------------")
    print(f" 1  {m[1][0]}   |  {m[1][1]}  |  {m[1][2]} ")
    print(f"    -------------")
    print(f" 2  {m[2][0]}   |  {m[2][1]}  |  {m[2][2]} ")
