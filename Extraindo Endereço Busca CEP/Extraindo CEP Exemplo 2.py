from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()

#Acessar site Busca CEP
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

tempoEspera.sleep(5)

#Digitar CEP
navegador.find_element(By.ID, 'endereco').send_keys('01310930')

tempoEspera.sleep(3)

#Clicar em Buscar
navegador.find_element(By.ID, 'btn_pesquisar').click()

tempoEspera.sleep(10)

#Recuperar informações da tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody')

endereco = ""

for linhaTabela in elementoTabela.find_elements(By.TAG_NAME, 'tr'):

    for colunaTabela in linhaTabela.find_elements(By.TAG_NAME, 'td'):

        endereco = endereco + ";" + colunaTabela.text

print(endereco)