# questão da data de nascimento
# o usuario manda a data de nascimento e vc tem que tirar as barras dela

data = input()
# 10/11/2000

dia, mes, ano = data.split('/')

print(f"você nasceu no dia: {dia} do mes {mes} do ano {ano}")
