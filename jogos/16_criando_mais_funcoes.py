import random


def imprime_mensagem_vencedor(acertou):
    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")


def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    imprime_mensagem_vencedor(acertou)



def imprime_mensagem_abertura():
    print("*********************************")
    print("*** Criando mais funções ***")
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

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

if (__name__ == "__main__"):
    jogar()