lista = []
x = 0
A = int (input ("Digite o tamanho do seu conjunto. \n"))
while x < A:
    conj = int (input ("Digite um número. \n"))
    x = x + 1
    lista.append(conj)
 
lista.sort()
print (lista)

