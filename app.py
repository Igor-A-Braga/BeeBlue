import streamlit as st
from utils import descompactar_zip
from perguntas import (
    carregar_dados,
    fornecedor_maior_montante,
    item_maior_quantidade,
    media_valor_notas,
    nota_com_mais_itens,
)

import matplotlib.pyplot as plt

# LOGO (adicione seu arquivo em 'img/logo.png')
st.set_page_config(page_title="Agente de Notas Fiscais", layout="wide")
st.image('./logo_beeblue.png', width=150)

st.title("📊 Agente de Notas Fiscais")
st.write("Escolha uma pergunta abaixo para consultar os dados:")

# Processamento
with st.spinner("Descompactando e carregando os dados..."):
    descompactar_zip("202401_NFs.zip", "dados")
    cabecalho, itens = carregar_dados("dados")
st.success("Dados prontos!")

# Pergunta
opcao = st.selectbox("Pergunta:", [
    "Fornecedor com maior montante recebido",
    "Item com maior quantidade entregue",
    "Média do valor das notas fiscais",
    "Nota fiscal com mais itens"
])

# Resposta
if opcao == "Fornecedor com maior montante recebido":
    resultado = fornecedor_maior_montante(cabecalho)
    fornecedor = resultado.index[0]
    valor = resultado.values[0]
    st.metric(label="Fornecedor com maior montante", value=f"R$ {valor:,.2f}")
    st.write(f"Fornecedor: **{fornecedor}**")

    if st.checkbox("Ver top 5 fornecedores"):
        st.bar_chart(cabecalho.groupby("RAZÃO SOCIAL EMITENTE")["VALOR NOTA FISCAL"].sum().sort_values(ascending=False).head(5))

elif opcao == "Item com maior quantidade entregue":
    resultado = item_maior_quantidade(itens)
    item = resultado.index[0]
    qtd = resultado.values[0]
    st.metric(label="Item mais entregue", value=f"{qtd:,.0f} unidades")
    st.write(f"Produto: **{item}**")

    if st.checkbox("Ver top 5 itens"):
        top5 = itens.groupby("DESCRIÇÃO DO PRODUTO/SERVIÇO")["QUANTIDADE"].sum().sort_values(ascending=False).head(5)
        fig, ax = plt.subplots()
        top5.plot(kind="barh", ax=ax)
        st.pyplot(fig)

elif opcao == "Média do valor das notas fiscais":
    media = media_valor_notas(cabecalho)
    st.metric(label="Média das notas fiscais", value=f"R$ {media:,.2f}")

elif opcao == "Nota fiscal com mais itens":
    nota = nota_com_mais_itens(itens)
    chave = nota.index[0]
    qtd = nota.values[0]
    st.metric(label="Nota com mais itens", value=f"{qtd} itens")
    st.write(f"Chave de acesso: `{chave}`")

# Rodapé
st.markdown("---")
st.caption("Desenvolvido pelo grupo para atividade de agentes autônomos · Especialização I2A2")

