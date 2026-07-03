lista_vip = [
    {"nome": "Gugu", "tem_carro": True},
    {"nome": "Gaga", "tem_carro": False},
    {"nome": "Gégé", "tem_carro": True}
]

def verificar_permissao(nome, idade):
    if idade < 18:
        return False
    for convidado in lista_vip:
        if convidado["nome"].lower() == nome.lower():
            return True
    return False

def exibir_lista():
    print("--- Lista de Confirmados ---")
    for amigo in lista_vip:
        if amigo["tem_carro"]:
            status_carro = "Tem carro"
        else:
            status_carro = "Não tem carro"
        print(f"• {amigo['nome']} ({status_carro})")

def adicionar_amigo(nome, tem_carro_input):
    if tem_carro_input.strip().lower() == "s":
        tem_carro_bool = True
    else:
        tem_carro_bool = False
        
    novo_amigo = {"nome": nome, "tem_carro": tem_carro_bool}
    lista_vip.append(novo_amigo)
    print(f"{nome} foi adicionado com sucesso!")

def remover_amigo(nome_remover):
    for amigo in lista_vip:
        if amigo["nome"].lower() == nome_remover.lower():
            lista_vip.remove(amigo)
            print(f"{nome_remover} foi removido da lista.")
            return
    print("Nome não encontrado na lista.")