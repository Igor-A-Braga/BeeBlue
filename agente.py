from utils import descompactar_zip
from perguntas import carregar_dados, fornecedor_maior_montante, item_maior_quantidade, media_valor_notas, nota_com_mais_itens

def menu():
    print("\n--- AGENTE CSV ---")
    print("1 - Fornecedor com maior montante recebido")
    print("2 - Item com maior quantidade entregue")
    print("3 - Média do valor das notas fiscais")
    print("4 - Nota fiscal com mais itens")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def rodar_agente():
    caminho_zip = "202401_NFs.zip"
    pasta_dados = "dados"

    descompactar_zip(caminho_zip, pasta_dados)
    cabecalho, itens = carregar_dados(pasta_dados)

    while True:
        escolha = menu()
        if escolha == "1":
            print(fornecedor_maior_montante(cabecalho))
        elif escolha == "2":
            print(item_maior_quantidade(itens))
        elif escolha == "3":
            print("Média do valor das notas:", media_valor_notas(cabecalho))
        elif escolha == "4":
            print("Nota com mais itens:", nota_com_mais_itens(itens))
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
