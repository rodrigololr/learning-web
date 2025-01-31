# tamanho em metros²da area ser pintada
# 1L para cada 3 metros quadrados
# tinta de 18L = 80 conto
# quantas tintas devem ser compradas e o total a ser pago

import math

area = int(input("Quantos metros quadrados vão ser pintados? "))

litros = math.ceil(area / 3)
latas = math.ceil(litros / 18)
preco = latas * 80

print(f"Total de latas: {latas}")
print(f"Preço total: R$ {preco:.2f}")
