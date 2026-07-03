import math
import pessoas

role_nome = "2.0 aniversario dos cria"
custo_total = 200.00

def calcular_vaquinha():
    total_pessoas = len(pessoas.lista_vip)
    if total_pessoas > 0:
        vaquinha_individual = custo_total / total_pessoas
        print(f"O valor atual é R$ {vaquinha_individual:.2f} para cada um.")
    else:
        print("A lista está vazia.")

def verificar_logistica():
    carros_disponiveis = 0
    for amigo in pessoas.lista_vip:
        if amigo["tem_carro"]:
            carros_disponiveis += 1
            
    total_pessoas = len(pessoas.lista_vip)
    carros_necessarios = math.ceil(total_pessoas / 5)
    
    print(f"Pessoas confirmadas: {total_pessoas}")
    print(f"Carros disponíveis: {carros_disponiveis}")
    
    if carros_disponiveis < carros_necessarios:
        print("ALERTA: Vai faltar carro para o rolê!")
    else:
        print("Logística perfeita! Todos têm carona.")

def exibir_relatorio_final():
    total_pessoas = len(pessoas.lista_vip)
    carros_disponiveis = 0
    for amigo in pessoas.lista_vip:
        if amigo["tem_carro"]:
            carros_disponiveis += 1
            
    if total_pessoas > 0:
        custo_por_pessoa = custo_total / total_pessoas
    else:
        custo_por_pessoa = 0
        
    print(f"\nRolê Fechado! Total de pessoas: {total_pessoas}. Custo por pessoa: R$ {custo_por_pessoa:.2f}. Carros confirmados: {carros_disponiveis}.")