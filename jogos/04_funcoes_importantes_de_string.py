def jogar():
    print("*********************************")
    print("***Funções importantes da String***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        index=0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {} ".format(chute, index))

            index =index +1

        print("Tente outra vez...")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
