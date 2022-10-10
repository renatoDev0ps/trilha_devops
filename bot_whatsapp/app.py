import pyautogui
from time import sleep

contato = 'Sai que e sua Taffarel'
vezes = 1

pyautogui.click(87,442, duration=2)
pyautogui.write(contato)
pyautogui.click(106,567,duration=2)
pyautogui.click(540,1048,duration=2)

while(True):
  for i in range(vezes):
    pyautogui.write('Bolsonaro Presidente 2022. Aceita que doi menos!')
    pyautogui.click(1329,1047,duration=1)
    
    pyautogui.write('https://lulaflix.com.br/')
    pyautogui.click(1329,1047,duration=1)
    
  sleep(5)
  
# campo mensagem contato '_22Msk'