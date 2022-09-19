import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
nomes_arquivo = "Pasta14.xlsx"
url ="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__i1AOI1UNTI2SkRWTjlTTE4yME9TNVFRUjlWRllUMC4u"
arquivo = pd.read_excel(nomes_arquivo)


for index,row in arquivo.iterrows():
    print("Index: "+str(index)+"E o nome do fulano é "+row["NOME"])
    edg = webdriver.Edge()
    edg.get(url)
    edg.quit

    time.sleep(3)

    elemento_texto_nome = edg.find_element(By.XPATH,'//*[@id="desktop-scroller"]/div[1]/div[2]/div[1]/div[1]/div/div/button/div/div[2]/div/div')
    elemento_texto_telefone = edg.find_element(By.XPATH,'//*[@id="desktop-scroller"]/div[1]/div[2]/div[2]/div[1]/div/div/button/div/div[2]/div/div')
    elemento_estrela_nota = edg.find_element(By.XPATH,'//*[@id="desktop-scroller"]/div[1]/div[2]/div[3]/div[1]/div/div/button/div/div[2]/div/div/div['+str(row['Nota'])+']/div/span/svg')

    elemento_texto_nome.send_keys(row['NOME'])
    elemento_texto_telefone.send_keys(row["TELEFONE"])
    elemento_estrela_nota.click()
    edg.find_element(By.XPATH,'//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div').click()
    edg.quit

