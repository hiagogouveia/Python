def jogar():
    print("********************************")
    print("Bem vindo ao jogo da froca")
    print("********************************")

    palava_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palava_secreta:
            if(chute.upper() == letra.upper()):
                print("Econtrei a letra {} na posição {}".format(chute, index))
            index = index + 1
        print("continue jogando")


if(__name__ == "__main__"):
    jogar()
