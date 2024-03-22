from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pandas as pd

navegador = opcoesSelenium.Chrome()

# Criar Lista
dataFrameLista = []

#Acessar site Busca CEP
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

tempoEspera.sleep(5)

#Dicionário
dicionarioCEPS = {
    "CEP 1" : "05892387",
    "CEP 2" : "23548057",
    "CEP 3" : "01153000"
}

for contador in dicionarioCEPS.values():
    #Digitar CEP no site Buscca CEP
    navegador.find_element(By.NAME, 'endereco').send_keys(contador)

    tempoEspera.sleep(3)

    #Clicar em buscar
    navegador.find_element(By.NAME, 'btn_pesquisar').click()

    tempoEspera.sleep(10)

    # Recuperar informações da tabela
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody')

    endereco = ""

    for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, 'tr'):

        for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, 'td'):
            endereco = endereco + ";" + colunaTabela.text

    print(endereco)

    dataFrameLista.append(endereco)

    tempoEspera.sleep(3)

    navegador.find_element(By.ID, 'btn_nbusca').click()

    tempoEspera.sleep(7)

# Preencher dados no Excel
arquivoExcel = pd.ExcelWriter('enderecosBuscaCEP.xlsx', engine='xlsxwriter')
dataFrame = pd.DataFrame(dataFrameLista, columns=['Coluna_Dados'])
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet 1', index=False)
arquivoExcel._save()