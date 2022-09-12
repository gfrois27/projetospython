#logica de programação
#passso 0 entender o desafio que voce quer resolver
#passo 1 percorrer todas os arquivos da pasta base de dados(pasta vendas)
import os
import pandas as pd
lista_arquivos = os.listdir('Balanço')

tabela_total = pd.DataFrame()

#passo 2  importar as bases de dados de vendas
for arquivo in lista_arquivos:
    #se tem 'vendas'no nome do arquivo, entao
    if 'Vendas' in arquivo:
        #importar arquivo
        tabela = pd.read_csv(f'Balanço/{arquivo}')
        tabela_total = tabela_total.append(tabela)

#passo 3  tratar/ compilar as bases de dados
print(tabela_total)

#passo 4  calcular o produto mais vendido(em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida','Preco Unitario']].sort_values(by='Quantidade Vendida',ascending=False)
print(tabela_produtos)

#passo 5  calcular o ponto que mais faturou(em faturamento)

tabela_total['Faturamento']=tabela_total['Quantidade Vendida']* tabela_total['Preco Unitario']
tabela_total = tabela_total.groupby('p'
                                    '')
#passo 6  calcular a loja/cidade que mais vendeu(em faturamneto) - criar um grafico/dashbord

