import pandas as pd
import numpy as np

# NIVEL 1
print("NIVEL 1")
# =========================
# Carregar dataset
# =========================
df = pd.read_csv("livros.csv", sep=";")

print("Primeiras 5 linhas:")
print(df.head())

print("======================================================")
# =========================
# Informações gerais
# =========================
print("\nInfo:")
print(df.info())

print("\nEstatísticas:")
print(df.describe())

print("======================================================")
# =========================
# Valores nulos
# =========================
print("\nValores nulos por coluna:")
nulos = df.isnull().sum()
print(nulos)

print("======================================================")
# =========================
# Livros com 0 páginas
# =========================
livros_zero_paginas = df[df["paginas"] == 0]

print("\nLivros com 0 páginas:")
print(livros_zero_paginas)

print("\nQuantidade de livros com 0 páginas:", livros_zero_paginas.shape[0])

print("======================================================")
# =========================
# Livros por ano
# =========================
print("\nQuantidade de livros por ano:")
livros_por_ano = df["ano"].value_counts().sort_index()
print(livros_por_ano)


print("\n\n===============================================================================================================")



# NIVEL 2
print("NIVEL 2")

# =========================
# Faixa de páginas
# =========================
df["faixa_paginas"] = df["paginas"].apply(
    lambda x: "Curto" if x < 150 else "Médio" if x <= 350 else "Longo"
)

print("\nColuna faixa_paginas criada:")
print(df[["paginas", "faixa_paginas"]].head())

print("======================================================")
# =========================
# Remover páginas = 0
# =========================
qtd_antes = df.shape[0]

df_limpo = df[df["paginas"] > 0].copy()

qtd_depois = df_limpo.shape[0]
removidos = qtd_antes - qtd_depois

print(f"\nRegistros removidos (paginas == 0): {removidos}")

print("======================================================")
# =========================
# Tratar coluna ano
# =========================
mediana_ano = df_limpo["ano"].median()

df_limpo["ano"] = df_limpo["ano"].fillna(mediana_ano).astype(int)

print("\nColuna 'ano' tratada:")
print(df_limpo["ano"].head())

print("======================================================")
# =========================
# Criar coluna década
# =========================
df_limpo["decada"] = (df_limpo["ano"] // 10) * 10

print("\nColuna 'decada' criada:")
print(df_limpo[["ano", "decada"]].head())

print("======================================================")
# =========================
# Resultado final
# =========================
print("\nDataFrame final:")
print(df_limpo.head())


print("\n\n===============================================================================================================")

# NIVEL 3
print("NIVEL 3")
# =========================
# Média de páginas por década
# =========================
media_paginas_decada = df_limpo.groupby("decada")["paginas"].mean().sort_index()

print("\nMédia de páginas por década:")
print(media_paginas_decada)

print("======================================================")
# =========================
# Top 10 autores com mais livros
# =========================
top_autores = df_limpo["autor"].value_counts().head(10)

print("\nTop 10 autores com mais livros:")
print(top_autores)

print("======================================================")
# =========================
# Distribuição faixa_paginas após 2010
# =========================
dist_faixa_pos_2010 = df_limpo[df_limpo["ano"] > 2010]["faixa_paginas"].value_counts()

print("\nDistribuição de faixa_paginas (após 2010):")
print(dist_faixa_pos_2010)

print("======================================================")
# =========================
# Exportar para Excel
# =========================
df_limpo.to_excel("livros_analisados.xlsx", index=False)

print("\nArquivo 'livros_analisados.xlsx' exportado com sucesso!")