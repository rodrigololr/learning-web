#Faça uma programa que dada a entrada de uma lista ele faça o cálculo
#acumulativo da mesma:
#Exemplo de entrada: [1, 2, 3, 4]
#Exemplo de saída: [1, 3, 6, 10]

lista = []

n = int(input())
lista.append(n)

while n != -1:
    n = int(input())
    lista.append(n)

lista.pop()

soma = 0
for i in lista:
    soma += i

print(soma)