import pyautogui as posicaoMouse
import pyautogui as tempoEspera

tempoEspera.sleep(1)
posicaoMouse.moveTo(x=273, y=750)
tempoEspera.sleep(1)
posicaoMouse.click(x=273, y=750)
tempoEspera.sleep(1)
posicaoMouse.typewrite('google chrome')
tempoEspera.sleep(2)
posicaoMouse.click(x=763, y=443)
tempoEspera.sleep(10)
posicaoMouse.typewrite('Dolar Hoje')
tempoEspera.sleep(2)
posicaoMouse.press("Enter")
