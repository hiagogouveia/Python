def jogar():
    print("********************************")
    print("Bem vindo ao jogo da forca")
    print("********************************")

    palava_secreta = "mamao".upper()
    letras_acertadas = ["_" for palavra in palava_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palava_secreta):
            index = 0
            for letra in palava_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            print(letras_acertadas)
            letras_faltando = str(letras_acertadas.count('_'))
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()

