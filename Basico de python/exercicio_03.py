#Faça um programa que peça 2 números inteiros e um número float. Calcule e
#mostre:
#● O produto do dobro do primeiro com metade do segundo .
#● A soma do triplo do primeiro com o terceiro.
#● O terceiro elevado ao cubo.
import math

n1 = int(input())
n2 = int(input())
n3 = float(input())

print( (n1* 2) * (n2 / 2) )
print( (n1* 3) + (n3) )
print( n3 ** 3)