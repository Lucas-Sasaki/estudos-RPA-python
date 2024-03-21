from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
import pyautogui as funcoesTeclado
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Criar Lista
dataFrameLista = []

#Acessa site
navegador.get("https://www.magazineluiza.com.br/")

#Digita o nome do produto em procurar
navegador.find_element(By.ID, 'input-search').send_keys("geladeira")

#Aguarda um tempo para o computador processar as informações
tempoEspera.sleep(5)

#Apertando a tecla "Enter" para pesquisar o produto
funcoesTeclado.press("Enter")

#Aguardar carregamento
tempoEspera.sleep(10)

#Recuperar os itens que aparecem na página
listaProdutos = navegador.find_elements(By.CLASS_NAME, 'ciMFyT')

for item in listaProdutos:

    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "fbccdO")
        except Exception:
            pass

    elif nomeProduto == "":

        try:
            nomeProduto = item.find_element(By.CLASS_NAME, "sc-fvwjDU")
        except Exception:
            pass

#------------------------------------------------------------------------------------------

    if precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "eCPtRw")
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "sc-bOhtcR")
        except Exception:
            pass

    elif precoProduto == "":

        try:
            precoProduto = item.find_element(By.CLASS_NAME, "dOwMgM")
        except Exception:
            pass

    else:

        precoProduto = "0"

#------------------------------------------------------------------------------------------

    if urlProduto == "":

        try:
            urlProduto = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except Exception:
            pass

    else:

        urlProduto = "-"

    print(nomeProduto.text, "-", precoProduto.text)
    print(urlProduto)

    #Adicionar informações a lista
    dataFrameLista.append(nomeProduto.text + " - " + precoProduto.text)
    dataFrameLista.append(urlProduto)

#Preencher dados no Excel
arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
dataFrame = pd.DataFrame(dataFrameLista, columns=['Coluna_Dados'])
dataFrame.to_excel(arquivoExcel, sheet_name='Sheet 1', index=False)
arquivoExcel._save()