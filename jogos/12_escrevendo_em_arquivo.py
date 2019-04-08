print("*********************************")
print("*** Lendo, escrevendo e só adicionando em arquivos ***")
print("*********************************")

# O modo w abre o arquivo para escrita, mas apaga o arquivo se existir!!
# O modo l abre o arquivo para leitura
# O modo a abre o arquivo para adicionar, sem apagar o arquivo
arquivo = open('palavras.txt', "w" , encoding='utf8')

print(arquivo)

arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.close()

arquivo = open("palavras.txt", 'a')
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()