def jogar():
    print("*********************************")
    print("*** Estipulando tentativas e erros ***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index=0

            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você venceu")
    else:
        print("Você perdeu")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
