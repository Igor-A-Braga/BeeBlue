import zipfile
import os

def descompactar_zip(caminho_zip, destino):
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(destino)
    print("Arquivos descompactados com sucesso.")

# Caminhos absolutos
caminho_zip = r'C:\Users\rosej\OneDrive\Documentos\I2A2\202401_NFs.zip'
destino = r'C:\Users\rosej\OneDrive\Documentos\I2A2\dados'

# Executa a função
descompactar_zip(caminho_zip, destino)
