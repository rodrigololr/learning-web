#Faça um programa que itera em uma string e toda vez que uma vogal aparecer
#na sua string print o seu nome entre as letras

palavra = input()
vogais = "aeiouAEIOU"
palavra_nova = ""

print("\n")
for letra in palavra:
    if(letra in vogais):
        palavra_nova += " eduardo "
    else:
        palavra_nova += letra


print(palavra_nova)