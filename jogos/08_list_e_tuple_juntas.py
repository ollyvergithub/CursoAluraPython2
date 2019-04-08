
print("*********************************")
print("*** List e Tuple juntos ***")
print("*********************************")

print("Tuple é uma lista imutável e deve ser declarada com () e não com []")

p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
line = [p1, p2, p3]

print(line)

pessoa1 = ("Nico", 39)
pessoa2 = ("Ollyver", 47)
instrutores = [pessoa1, pessoa2]

print(instrutores)

print("O nome do primeiro instrutor é: ", instrutores[0])
print("A idade do primeiro instrutor é: ", instrutores[0][1])

print("**************** Convertendo tuple em list ****************")
palavra = []
palavra.append("banana")
palavra.append("abacaxi")
print(palavra)
converter_lista_em_tuple = tuple(palavra)
print(converter_lista_em_tuple)

print("**************** Convertendo list em tuple ****************")
converter_tuple_em_lista = list(converter_lista_em_tuple)
print(converter_tuple_em_lista)