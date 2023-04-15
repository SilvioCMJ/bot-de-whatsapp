import pyautogui
import time

# aq vai preencher os dados essenciais

contato = "nome do contato"
msg = "mensagem"
navegador = "teu navegador"

# executando bot

pyautogui.press("win")
time.sleep(2)
pyautogui.write(navegador)
pyautogui.press("enter")
time.sleep(10)
pyautogui.write('https://web.whatsapp.com')
pyautogui.press("enter")
time.sleep(35)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(contato)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write(msg)
pyautogui.press('enter')
