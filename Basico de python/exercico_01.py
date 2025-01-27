
def login():
    global nome, idade
    nome = input("Digite seu nome por gentileza: ")
    print("Opa muito bom pai tu sabe demais\n")
    idade = input("Digite sua idade por gentileza: ")
    print("Muito bom\n")


login()
print(f"Seu nome é {nome} e sua idade é {idade}?\n")
escolha = input("S ou N: ").strip().lower()


while (escolha == 'n'):
    print("Vamos tentar denovo")
    login()
    print(f"Seu nome é {nome} e sua idade é {idade}?\n")
    escolha = input("S ou N: ").strip().lower()

print("PArabnes login concluido")
