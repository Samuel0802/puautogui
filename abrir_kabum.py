#FAZER UM PEDIDO NA KABUM

#2 PASSO ENTRAR NO SITE https://www.kabum.com.br
#3 PASSO ESCOLHER O PRODUTO
#4 PASSO FINALIZAR A COMPRA

import pyautogui
import time

pyautogui.PAUSE = 0.3

#1 PASSO ENTRAR NO GOOGLE
pyautogui.press("win")

pyautogui.write("opera")

pyautogui.press("enter")

#1 PASSO ENTRAR NO SITE DA KABUM
pyautogui.write("https://www.kabum.com.br")
pyautogui.press("enter")

time.sleep(3) #intervalo de 3 segundos

pyautogui.click(x=1063, y=424)
time.sleep(3)

pyautogui.click(x=437, y=151)
time.sleep(3)

pyautogui.write("RTX 3060")

pyautogui.click(x=861, y=143)
time.sleep(3)

pyautogui.scroll(-160)
time.sleep(3)

pyautogui.click(x=494, y=662)
time.sleep(3)


pyautogui.click(x=859, y=568)
time.sleep(3)


pyautogui.click(x=862, y=570)



