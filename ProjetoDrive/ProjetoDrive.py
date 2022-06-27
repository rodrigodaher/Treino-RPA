import pyautogui
import time

# abrir o google drive no meu computador

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(0.25)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# entrar na área de trabalho
pyautogui.hotkey('win', 'd')

# clicar no arquivo, arrastar e jogar no drive
pyautogui.moveTo(1307, 54)
pyautogui.mouseDown()
pyautogui.moveTo(-641, 513)
pyautogui.hotkey('alt', 'tab')
time.sleep(1.5)
pyautogui.mouseUp()
