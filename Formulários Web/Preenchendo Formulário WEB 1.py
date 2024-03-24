from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

from selenium.webdriver.support.select import Select

navegador = opcoesSelenium.Chrome()

navegador.get("https://form.jotform.com/221436066464051")

navegador.fullscreen_window()

tempoEspera.sleep(5)

#Nome
navegador.find_element(By.NAME, 'q3_nome[first]').send_keys("Pedro")

tempoEspera.sleep(2)

#Sobrenome
navegador.find_element(By.NAME, 'q3_nome[last]').send_keys("Silva")

tempoEspera.sleep(2)

#E-mail
navegador.find_element(By.NAME, 'q4_email').send_keys("pedro.silva@email.com.br")

tempoEspera.sleep(2)

#Estado Civil
pegaDropDown = navegador.find_element(By.NAME, 'q5_estadoCivil')
itemSelecionado = Select(pegaDropDown)
itemSelecionado.select_by_index(1)

tempoEspera.sleep(2)

#Rolar página para baixo
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#Tem Filhos
filho = "Não"

if filho == "Não":
    navegador.find_element(By.ID, 'label_input_6_1').click()

else:
    navegador.find_element(By.ID, 'label_input_6_0').click()

tempoEspera.sleep(2)

#Cores Favoritas
navegador.find_element(By.ID, 'label_input_7_0').click()

tempoEspera.sleep(2)

#Avaliação
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[3]').click()

tempoEspera.sleep(2)

#Qualidade do Serviço
navegador.find_element(By.ID, 'input_9_0_3').click()

tempoEspera.sleep(2)

#Grau de Dificuldade
navegador.find_element(By.ID, 'input_9_1_0').click()