import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

def imprime_mensagem_abertura():
    print("*********************************")
    print("*** Organizando o codigo em funções ***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    print(palavras)
    numero_index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_index].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    lista = ["_" for letra in palavra_secreta]
    return lista

if (__name__ == "__main__"):
    jogar()