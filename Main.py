import sys
import pessoas
import evento

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if not pessoas.verificar_permissao(nome, idade):
    print("Acesso Bloqueado")
    sys.exit()
else:
    print(f"Bem-vindo à organização do {evento.role_nome}!\n")

while True:
    print("\n--- MENU INTERATIVO ---")
    print("1 - Ver Lista")
    print("2 - Adicionar Amigo")
    print("3 - Remover Amigo")
    print("4 - Calcular Vaquinha")
    print("5 - Logística de Carros")
    print("0 - Encerrar")
    
    escolha = input("Digite a opção desejada: ")
    print("-" * 30)

    if escolha == "1":
        pessoas.exibir_lista()

    elif escolha == "2":
        novo_nome = input("Digite o nome do novo amigo: ")
        carro = input("Ele tem carro? (s/n): ")
        pessoas.adicionar_amigo(novo_nome, carro)

    elif escolha == "3":
        nome_remover = input("Digite o nome de quem cancelou: ")
        pessoas.remover_amigo(nome_remover)

    elif escolha == "4":
        evento.calcular_vaquinha()

    elif escolha == "5":
        evento.verificar_logistica()

    elif escolha == "0":
        evento.exibir_relatorio_final()
        break

    else:
        print("Opção Inválida")