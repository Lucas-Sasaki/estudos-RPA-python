from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()

#Acessar site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#Identificar tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#Identificar colunas e linhas
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

#Imprimir linha a linha
for linhaAtual in linhas:

    print(linhaAtual.text)