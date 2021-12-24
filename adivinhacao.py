import random
def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    pontuacao = 1000
    numero_de_tentaivas = 0

    nivel = int(input("escolha um nivel: 1-Easy, 2-Medium, 3-Hard: "))
    print("Você escolheu o nivel", nivel)

    if (nivel == 1):
        numero_de_tentaivas = 10
    elif (nivel == 2):
        numero_de_tentaivas = 5
    else:
        numero_de_tentaivas = 3

    for rodada in range(1, numero_de_tentaivas + 1):
        print("tentativa {} de {}".format(rodada, numero_de_tentaivas))
        print("Números válidos entre 1 e 100")
        chute_str = input("Digitite seu numero: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100")
            continue

        if (acertou):
            print("você acertou ")
            break
        else:
            if (maior):
                print("você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("você errou! seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

    print("Você fez:{} pontos".format(pontuacao))
    print("O número secreto era:{} ".format(numero_secreto))
    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()