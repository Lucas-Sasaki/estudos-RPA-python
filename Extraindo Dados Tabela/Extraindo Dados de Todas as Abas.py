from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()

# Acessar site
navegador.get("https://rpachallengeocr.azurewebsites.net/")

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

    i += 1

    # Para dar tempo do computador processar as informações
    tempoEspera.sleep(5)

    # Clicar em "next" para seguir para a próxima tabela
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # Para dar tempo do computador processar as informações
    tempoEspera.sleep(6)

else:

    print("Dados extraidos com sucesso!")