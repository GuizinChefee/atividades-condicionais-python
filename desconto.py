import os

#limpando a tela 
os.system("cls")

def calcular_total_com_desconto(nome_produto, quantidade, preco_unitario):
    
    total_sem_desconto = quantidade * preco_unitario
    
    if quantidade <= 5:
        desconto = total_sem_desconto * 0.02 
    elif 5 < quantidade <= 10:
        desconto = total_sem_desconto * 0.03 
    else:
        desconto = total_sem_desconto * 0.05  

    total_com_desconto = total_sem_desconto - desconto
    
    print(f"Produto: {nome_produto}")
    print(f"Quantidade adquirida: {quantidade}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Total sem desconto: R$ {total_sem_desconto:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")

# Solicita os dados ao usuário
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

calcular_total_com_desconto(nome_produto, quantidade, preco_unitario)