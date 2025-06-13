import pandas as pd

def carregar_dados(pasta_dados):
    cabecalho = pd.read_csv(f"{pasta_dados}/202401_NFs_Cabecalho.csv")
    itens = pd.read_csv(f"{pasta_dados}/202401_NFs_Itens.csv")
    return cabecalho, itens

def fornecedor_maior_montante(cabecalho):
    # Coluna correta para o fornecedor: 'RAZÃO SOCIAL EMITENTE'
    # Coluna correta para valor: 'VALOR NOTA FISCAL'
    resultado = cabecalho.groupby("RAZÃO SOCIAL EMITENTE")["VALOR NOTA FISCAL"].sum().sort_values(ascending=False)
    return resultado.head(1)

def item_maior_quantidade(itens):
    # Vamos verificar o nome real da coluna depois, mas por enquanto deixamos assim
    resultado = itens.groupby("DESCRIÇÃO DO PRODUTO/SERVIÇO")["QUANTIDADE"].sum().sort_values(ascending=False)
    return resultado.head(1)

def media_valor_notas(cabecalho):
    return cabecalho["VALOR NOTA FISCAL"].mean()

def nota_com_mais_itens(itens):
    # Verifique se a coluna correta em itens é 'CHAVE DE ACESSO' (igual ao cabeçalho)
    return itens["CHAVE DE ACESSO"].value_counts().head(1)

