import pyautogui as posicaoMouse
import pyautogui as tempoEspera

# Tempo de espera para que o computador possa processar as informações
tempoEspera.sleep(1)

# Movendo o mouse até botão iniciar
posicaoMouse.moveTo(x=273, y=750)

# Tempo de espera para que o computador possa processar as informações
tempoEspera.sleep(1)

# Clicando na posição
posicaoMouse.click(x=273, y=750)

# Tempo de espera para que o computador possa processar as informações
tempoEspera.sleep(1)

# Digitando a palavra calculadora
posicaoMouse.typewrite('calculadora')

# Tempo de espera para que o computador possa processar as informações
tempoEspera.sleep(2)

# Movendo o mouse calculadora
posicaoMouse.moveTo(x=355, y=241)

# Tempo de espera para que o computador possa processar as informações
tempoEspera.sleep(1)

#Abrir calculadora
posicaoMouse.click(x=355, y=241)
