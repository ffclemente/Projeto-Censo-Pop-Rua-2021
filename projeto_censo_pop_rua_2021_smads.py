# -*- coding: utf-8 -*-
"""PROJETO CENSO POP RUA 2021 SMADS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yUiEKppCRYuMKYVQJdr7LuX43IDrLv7S
"""

#PROJETO CENSO POPULAÇÃO DE RUA 2021 - FONTE: DADOS PREFEITURA DE SÃO PAULO / SMADS, FEV.2024.
#OBSERVAÇÃO! ATENÇÃO! O arquivo baixado diretamente do site da Prefeitura está corrompido. É necessário copiar os dados para uma outra planilha nova, antes de carregar os dados.
# link para download da base de dados: https://www.prefeitura.sp.gov.br/cidade/secretarias/assistencia_social/censo_2021/index.php?p=2007

# link projeto e da base de dados no Github: https://github.com/ffclemente/Projeto-Censo-Pop-Rua-2021

# Faça o upload do arquivo
from google.colab import files
uploaded = files.upload()

# Carregar pacotes
import pandas as pd

# Carregar e visualizar os dados
nome_do_arquivo = 'censo pop rua (novo).xlsx'
dados = pd.read_excel(nome_do_arquivo)
dados.head(30)

# Verificar a frequência da variável 'Situação de rua'
situacao_da_pessoa = dados['Situação de rua'].value_counts()

print("\nFrequência da variável 'Situação da Pessoa':")
print(situacao_da_pessoa)
print("\nTotal de registros:", len(dados['Situação de rua']))

# carregar pacotes
import matplotlib.pyplot as plt

# Verificar a frequência da variável 'Situação de rua'
situacao_da_pessoa = dados['Situação de rua'].value_counts()

# Calcular o valor total
total_pessoas = len(dados['Situação de rua'])

# Configurações para a plotagem
plt.figure(figsize=(8, 6))

# Texto personalizado com frequências
texto = f'TOTAL DE PESSOAS EM SITUAÇÃO DE RUA: {total_pessoas}\n\n'
for situacao, frequencia in situacao_da_pessoa.items():
    texto += f'{situacao}: {frequencia} pessoa(s)\n'

# Adicionar uma caixa de texto para visualização
plt.text(0.5, 0.5, texto, ha='center', va='center', fontsize=14, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Exibir a plotagem sem eixo
plt.axis('off')

# Exibir a plotagem
plt.show()

# Frequência da variável 'Situação de rua'
situacao_da_pessoa = dados['Situação de rua'].value_counts()

# Criar um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(situacao_da_pessoa, labels=situacao_da_pessoa.index, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(situacao_da_pessoa) / 100), startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])

# Adicionar título
plt.title('Situação da Pessoa')

# Exibindo o gráfico
plt.show()

# Frequência da variável 'Identifica com o sexo nasceu'
sexo_identifica = dados['Identifica com o sexo nasceu'].value_counts()

print("\nFrequência sexo se identifica':")
print(sexo_identifica)
print("\nTotal de registros:", len(dados['Identifica com o sexo nasceu']))

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = sexo_identifica.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(sexo_identifica):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Sexo se identifica')
plt.xlabel('Sexo se identifica')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

# Suponha que 'dados' seja o DataFrame que você carregou anteriormente
sexo_pessoa = dados['Sexo'].value_counts()

# Criar um gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(sexo_pessoa, labels=sexo_pessoa.index, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(sexo_pessoa) / 100), startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen'])

# Adicionar título
plt.title('Sexo')

# Exibindo o gráfico
plt.show()

faixa_idade = dados['Faixa de idade'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = faixa_idade.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(faixa_idade):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Faixa de idade')
plt.xlabel('Faixa de idade')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns  # Certifique-se de ter a biblioteca seaborn instalada

# Suponha que 'dados' seja o DataFrame que você carregou anteriormente
classificacao_idade = dados['Classificação de idade'].value_counts()

# Escolha uma paleta de cores do seaborn
cores_personalizadas = sns.color_palette('pastel')

# Criar um gráfico de pizza
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(classificacao_idade, labels=classificacao_idade.index, autopct=lambda p: '{:.1f}%'.format(p), startangle=90, colors=cores_personalizadas, textprops=dict(color="w"))

# Ajustar a localização da legenda
plt.legend(wedges, classificacao_idade.index, title='Classificação de idade', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adicionar título
plt.title('Classificação de idade')

# Exibindo o gráfico
plt.show()

cor_raca = dados['Cor_Raça_Etnia'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = cor_raca.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(cor_raca):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Cor Raça')
plt.xlabel('Cor Raça')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

import matplotlib.pyplot as plt

tempo_situacao = dados['Tempo na situação'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = tempo_situacao.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(tempo_situacao):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Tempo em situação de rua')
plt.xlabel('Tempo de situação')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

import matplotlib.pyplot as plt

onde_dormiu = dados['Onde dormiu ontem'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = onde_dormiu.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(onde_dormiu):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Onde a pessoa dormiu ontem (a pesquisa é realizada nos Centros de Acolhida)')
plt.xlabel('Onde dormiu ontem')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

import matplotlib.pyplot as plt

tempo_permanencia = dados['Tempo de permanência'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = tempo_permanencia.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(tempo_permanencia):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Tempo de permanência nesse Centro de Acolhida')
plt.xlabel('Tempo de permanência')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

# Frequência da variável 'Distrito'
distrito = dados['Distrito'].value_counts()

print("\nFrequência da variável 'Distrito':")
print(distrito)

import matplotlib.pyplot as plt

distrito = dados['Distrito'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = distrito.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(distrito):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Distrito')
plt.xlabel('Distrito')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

import matplotlib.pyplot as plt

# Suponha que 'dados' seja o DataFrame que você carregou anteriormente
distrito = dados['Distrito'].value_counts()

# Filtrar apenas os valores com frequência maior ou igual a 500
distrito_filtrado = distrito[distrito >= 500]

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = distrito_filtrado.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(distrito_filtrado):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Distrito (Frequência >= 500)')
plt.xlabel('Distritos')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

# Frequência da variável 'Distrito'
distrito = dados['Subprefeitura'].value_counts()

print("\nFrequência da variável 'Subprefeitura':")
print(distrito)

import matplotlib.pyplot as plt

# Suponha que 'dados' seja o DataFrame que você carregou anteriormente
subprefeitura = dados['Subprefeitura'].value_counts()

# Filtrar apenas os valores com frequência maior ou igual a 500
subprefeitura_filtrado = subprefeitura[subprefeitura >= 500]

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = subprefeitura_filtrado.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(subprefeitura_filtrado):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Subprefeitura (Frequência >= 500)')
plt.xlabel('Subprefeitura')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

# Frequência da variável 'Criança_acomp_Adulto' e 'Criança_Sozinha'
crianca_adulto = dados['Criança_acomp_Adulto'].value_counts()

print("\nFrequência Criança com Adulto':")
print(crianca_adulto)

crianca_sozinha = dados['Criança_acomp_Adulto'].value_counts()

print("\nFrequência Criança Sozinha':")
print(crianca_sozinha)

crianca_adulto = dados['Criança_acomp_Adulto'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = crianca_adulto.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(crianca_adulto):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Criança acompanhada de Adulto')
plt.xlabel('Criança acompanhada de Adulto')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

crianca_sozinha = dados['Criança_Sozinha'].value_counts()

# Criar um gráfico de barras
plt.figure(figsize=(10, 6))
ax = crianca_sozinha.plot(kind='bar', color='skyblue')

# Adicionar rótulos nas barras
for i, v in enumerate(crianca_sozinha):
    ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

plt.title('Criança Sozinha')
plt.xlabel('Criança Sozinha')
plt.ylabel('Contagem')
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

3145+2640

import matplotlib.pyplot as plt

# Supondo que 'dados' seja o DataFrame que você já carregou

# Criar contagem de crianças sozinhas
crianca_sozinha = dados['Criança_Sozinha'].value_counts()

# Criar contagem de crianças acompanhadas por adulto
crianca_acomp_adulto = dados['Criança_acomp_Adulto'].value_counts()

# Criar um gráfico de barras empilhadas
plt.figure(figsize=(10, 6))
bottom_bar = plt.bar(crianca_sozinha.index, crianca_sozinha, color='skyblue', label='Criança Sozinha')
top_bar = plt.bar(crianca_acomp_adulto.index, crianca_acomp_adulto, color='orange', label='Criança Acompanhada por Adulto', bottom=crianca_sozinha)

# Adicionar rótulos nas barras
for bars in [bottom_bar, top_bar]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_y() + bar.get_height()/2, round(yval, 1), ha='center', va='center')

plt.title('Contagem de Crianças Sozinhas e Acompanhadas por Adulto')
plt.xlabel('Criança Acompanhada por Adulto')
plt.ylabel('Contagem')
plt.legend()
plt.xticks(rotation=45, ha='right')  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.show()

from rich.console import Console
from rich.table import Table
from rich import print

# Calcular o valor total
total_pessoas = 5785

# Configuração da tabela
table = Table(show_header=False, expand=True)
table.add_column(justify="center")

# Adicionar linhas à tabela
table.add_row("[bold]TOTAL DE PESSOAS EM SITUAÇÃO DE RUA[/bold]")
table.add_row("[bold]QUE RESPONDERAM ESTAR ACOMPANHADAS DE CRIANÇAS[/bold]", str(total_pessoas))

# Configurar a caixa de texto com tamanho da fonte dobrado
console = Console()
console.print(table, style="bold white on black")

import matplotlib.pyplot as plt

# Criar valores manualmente
sim_respondeu_com_crianca = 5785
total_pessoas_situacao_rua = 31884

# Configurações para a plotagem
plt.figure(figsize=(8, 6))

# Texto personalizado
texto = f'TOTAL DE PESSOAS EM SITUAÇÃO DE RUA: {total_pessoas_situacao_rua}\n'
texto += f'Pessoas em situação de rua que responderam estar acompanhada de criança: {sim_respondeu_com_crianca}\n'

# Adicionar uma caixa de texto sofisticada
plt.text(0.5, 0.5, texto, ha='center', va='center', fontsize=14, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

# Exibir a plotagem sem eixo
plt.axis('off')

# Exibir a plotagem
plt.show()