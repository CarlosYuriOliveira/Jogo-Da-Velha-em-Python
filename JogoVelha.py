import praver
import jogoecondi
op = ""
print(8*"--"+"Jogo Da Velha"+"--"*8)
print(11*"----")
praver.sopraver()
while op != "n":
    jogoecondi.jogo()
    op = str(input("Novo Jogo? (s / n) "))
    if op == 's':
        praver.sopraver()
