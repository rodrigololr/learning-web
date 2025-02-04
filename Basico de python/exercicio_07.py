# Faça um programa que receba uma string e responda se ela tem alguma vogal,
# se sim, quais são? E também diga se ela é uma frase ou não.

string = input("Palavra: ")

vogais = ["a", "e", "i", "o", "u"]
# vogais = "aeiou"


# for(int i; i > string; i++)
for letra in string:
    if (letra in vogais):
        print("Rodrigo")
    else:
        print("Suco de caju")
