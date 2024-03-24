from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")

tempoEspera.sleep(10)

#Nome
navegador.find_element(By.ID, '72542598').send_keys("João Pedro Silva")

tempoEspera.sleep(2)

#E-mail
navegador.find_element(By.ID,'72542821').send_keys("joaopedro.silva@hotmail.com")

tempoEspera.sleep(2)

#Qual sexo
sexo = "Feminino"

if sexo == "Masculino":
    navegador.find_element(By.XPATH, '//*[@id="72542994_583517054_label"]/span[1]').click()

else:
    navegador.find_element(By.XPATH, '//*[@id="72542994_583517055_label"]/span[1]').click()

tempoEspera.sleep(2)

#Cor favorita
pegaDropDown = navegador.find_element(By.ID, '72543178')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(3)