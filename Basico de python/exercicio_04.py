# Sistema de Avaliação com Critérios Especiais

# 1. O programa deve ler quatro notas de um aluno.

# 2. Cálculo da média:
#    - Se a maior nota for menor que 8, a média deve ser aritmética.
#    - Se a maior nota for 8 ou mais, a média deve ser ponderada (pesos: 1, 2, 3, 4).

# 3. Critério de Aprovação:
#    - "Aprovado" se a média for 7 ou mais.
#    - "Recuperação" se a média estiver entre 5 e 6.9.
#    - "Reprovado" se a média for menor que 5.
#    - "Aprovado com Distinção" se todas as notas forem 10.

# 4. Reprovação Automática:
#    - Se o aluno tiver mais de uma nota abaixo de 4, ele é reprovado automaticamente.

# 5. Prova Extra:
#    - Se o aluno estiver em recuperação, ele poderá fazer uma prova extra.
#    - A nova média será a média aritmética entre a média antiga e a nota da prova extra.
#    - Se essa nova média for maior ou igual a 6, o aluno é aprovado. Caso contrário, reprovado.

import sys


def extra(media):
    print("digite a nota do pontos extra")
    n_extra = float(input())
    nova_media = (media + n_extra) / 2

    if (nova_media >= 6):
        print("aprovado")
    else:
        print("reprovado")


def comparacao(media):
    if (media == 10):
        print("Aprovado com Distinção")
    elif (media >= 7):
        print("aprovado")
    elif (media < 7 and media >= 5):
        print("recuperação")
        extra(media)
    elif (media < 5):
        print("Reprovado")


print("digite as quatro notas")
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

cont = 0

if (n1 < 4):
    cont = cont + 1

if (n2 < 4):
    cont = cont + 1
if (n3 < 4):
    cont = cont + 1

if (n4 < 4):
    cont = cont + 1


if (cont >= 2):
    print("você foi reprovado automaticamente")
    sys.exit()

media_arit = (n1+n2+n3+n4) / 4
media_pon = ((n1*1)+(n2*2)+(n3*3)+(n4*4)) / 10
# ESsse max significa vai pegar o maior e comparar se é maior q igual a 8
if max(n1, n2, n3, n4) >= 8:
    comparacao(media_pon)
    print("here")
else:
    comparacao(media_arit)
    print("or")
