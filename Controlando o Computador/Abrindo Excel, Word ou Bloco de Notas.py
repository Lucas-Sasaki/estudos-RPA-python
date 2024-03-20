import pyautogui as escolha_opcao


opcao = escolha_opcao.confirm('Clique no botão desejado',
            buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":

    escolha_opcao.hotkey('win', 'r')

    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('Excel')

    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')

    escolha_opcao.sleep(20)

    escolha_opcao.typewrite("Você escolheu abrir o Excel")

    print("Você escolheu abrir o Excel")

elif opcao == "Word":

    escolha_opcao.hotkey('win', 'r')

    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('winword')

    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')

    escolha_opcao.sleep(20)

    escolha_opcao.click(x=370, y=299)

    escolha_opcao.sleep(3)

    escolha_opcao.typewrite("Você escolheu abrir o Word")

    print("Você escolheu abrir o Word")

else:

    escolha_opcao.hotkey('win', 'r')

    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('notepad')

    escolha_opcao.sleep(2)

    escolha_opcao.press('Enter')

    escolha_opcao.sleep(20)

    escolha_opcao.typewrite("Você escolheu abrir o Bloco de Notas")

    print("Você escolheu abrir o Bloco de Notas")