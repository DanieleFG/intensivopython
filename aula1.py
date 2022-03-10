import pyautogui
import pyperclip
import time

# pyautogui.PAUSE = 1
# # Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.hotkey("Shift", "Ctrl", "N")
# pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
# pyautogui.hotkey("shift", "ctrl", "v")
# pyautogui.press("enter")
#time.sleep(5)
#https://www.vivaolinux.com.br/dica/Comandos-rapidos-para-Mozilla-Firefox-1  atalhos
#https://pyautogui-readthedocs-io.translate.goog/en/latest/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc  comandos pyauto


pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
# pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("CTRL", "V")
pyautogui.press("enter")

time.sleep(5)

