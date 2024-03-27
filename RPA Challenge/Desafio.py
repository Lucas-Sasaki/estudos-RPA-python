from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera
from openpyxl import load_workbook
import os
import glob

#Abrir site formulário
navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/?lang=EN")
tempoEspera.sleep(5)

#Download planilha excel
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()
tempoEspera.sleep(15)

#Recuperar caminho arquivo
caminho_pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
arquivo_excel = glob.glob(os.path.join(caminho_pasta_download, "*.xlsx"))
caminho_arquivo_excel = max(arquivo_excel, key=os.path.getctime)

#Abrir aqrquivo Excel
planilhaDados = load_workbook(caminho_arquivo_excel)
sheetSelecionada = planilhaDados["Sheet1"]

#Ler linha a linha do excel
for linha in range(2, len(sheetSelecionada["A"]) + 1):
    firstName = sheetSelecionada['A%s' % linha].value
    lastName = sheetSelecionada['B%s' % linha].value
    companyName = sheetSelecionada['C%s' % linha].value
    roleInCompany = sheetSelecionada['D%s' % linha].value
    adress = sheetSelecionada['E%s' % linha].value
    email = sheetSelecionada['F%s' % linha].value
    phoneNumber = sheetSelecionada['G%s' % linha].value

    #Verifica se a célula está vazia
    if firstName is None:
        break

    #Preencher formulário
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(firstName)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(lastName)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(companyName)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(roleInCompany)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(adress)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(email)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(phoneNumber)
    tempoEspera.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()

print("Processo finalizado")