import pyautogui as posicaoAbreArquivos

posicaoAbreArquivos.hotkey('win', 'r')
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.typewrite('notepad')
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.press("Enter")
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.hotkey('ctrl', 'a')
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.press('delete')
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.typewrite('Abrir o bloco de notas com o python')
posicaoAbreArquivos.sleep(60)

fecharBlocoDeNotas = posicaoAbreArquivos.getActiveWindow()

posicaoAbreArquivos.sleep(2)

fecharBlocoDeNotas.close()



