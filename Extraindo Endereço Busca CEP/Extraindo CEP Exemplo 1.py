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

#Recuperar Logradouro
logradouro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text

#Recuperar Bairro
bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text

#Recuperar Localidade
localidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

#Recuperar CEP
cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text

tempoEspera.sleep(2)

#Imprimir resultado
print("Logradouro: " + logradouro)
print("Bairro: " + bairro)
print("Localidade: " + localidade)
print("CEP: " + cep)