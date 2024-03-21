from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Acessar site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#Identificar tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#Identificar colunas e linhas
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

#Criar lista
dataFrameLista = []

#Imprimir linha a linha e adicionar-las na lista
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)

#Preencher dados no Excel
arquivoExcel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
dataFrame = pd.DataFrame(dataFrameLista, columns=['Coluna_Dados'])
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet 1', index=False)
arquivoExcel._save()