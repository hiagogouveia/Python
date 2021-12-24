import adivinhacao
import forca
def escolhe_jogo():
    print("********************************")
    print("Bem vindo ao jogos")
    print("********************************")

    print("Escolha seu jogo:")
    print("Adivinhacao: 1")
    print("Forca: 2")
    jogo = int(input("Qual jogo: "))

    if(jogo == 1):
        print("Jogando Adivinhacao")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()