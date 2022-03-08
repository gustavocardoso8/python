import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 2

# para abrir o navegador

pyautogui.press("winleft")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.alert("Vai começar, aperte OK e não mexa em mais nada!")
pyautogui.hotkey('ctrl', 't')
pyperclip.copy("https://www.linkedin.com/in/gustavo-cardoso08/")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")
time.sleep(3)
pyautogui.alert("Seja bem vindo ao meu LinkedIn!")