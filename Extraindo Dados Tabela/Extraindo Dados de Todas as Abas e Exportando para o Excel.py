from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd

navegador = opcoesSelenium.Chrome()

# Acessar site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

# Criar Lista
dataFrameLista = []

# Recuperar dados de todas as tabelas
i = 1

while i < 4:
    # Identificar tabela
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # Identificar colunas e linhas
    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)
        # Adicionar linhas a lista
        dataFrameLista.append(linhaAtual.text)

    i += 1
    # Para dar tempo do computador processar as informações
    tempoEspera.sleep(5)

    # Clicar em "next" para seguir para a próxima tabela
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # Para dar tempo do computador processar as informações
    tempoEspera.sleep(5)

else:
    print("Dados extraidos com sucesso!")

#Preencher dados no Excel
arquivoExcel = pd.ExcelWriter('dadosAbaSite.xlsx', engine='xlsxwriter')
dataFrame = pd.DataFrame(dataFrameLista, columns=['Coluna_Dados'])
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet 1', index=False)
arquivoExcel._save()