import os
import zipfile
import re
import pandas as pd

from censo_escolar import colunas


# Caminho do diretório onde estão os arquivos .zip
caminho_diretorio = 'dataset/'
padrao_csv = r'microdados_ed_basica_\d{4}.csv'

# Lista para armazenar os DataFrames carregados
dataframes = []

# Loop para percorrer todos os arquivos no diretório
for arquivo in os.listdir(caminho_diretorio):
    # Verifica se o arquivo é um .zip
    if arquivo.endswith(".zip"):
        caminho_arquivo_zip = os.path.join(caminho_diretorio, arquivo)
        # Abre o arquivo zipado
        with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
            # Lista todos os arquivos no zip
            lista_arquivos = [f for f in zip_ref.namelist()]

            if lista_arquivos:
                for arquivo_csv in lista_arquivos:
                    if re.findall(padrao_csv, arquivo_csv) or arquivo_csv.endswith('.CSV'):
                        print(caminho_arquivo_zip)
                        print(arquivo_csv)
                        with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_file:
                            with zip_file.open(arquivo_csv) as file:
                                df = pd.read_csv(file,
                                                 encoding='iso-8859-1',
                                                 on_bad_lines='skip',
                                                 sep=';',
                                                 low_memory=False,
                                                 usecols=colunas)
                                dataframes.append(df)

# concatenação de todos os DataFrames lidos
print("Concatenando DataFrames...")
df_final = pd.concat(dataframes, ignore_index=True)

# Salva o DataFrame final em um arquivo CSV
print("Salvando DataFrame final em um arquivo CSV...")
df_final.to_csv('microdados_ed_basica_2007_2023_10.csv', index=False)