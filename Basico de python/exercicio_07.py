# Faça um programa que receba uma string e responda se ela tem alguma vogal,
# se sim, quais são? E também diga se ela é uma frase ou não.

string = input("Palavra: ")

vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# vogais = "aeiou"
frase = " " in string

# for(int i; i > string; i++)
for letra in string:
    if (letra in vogais):
        print(f" Vogal: {letra}\n")
    else:
        print("Suco de caju\n")


if(frase == 1):
    print("é uma frase")
else:
    print("é uma palavra")
