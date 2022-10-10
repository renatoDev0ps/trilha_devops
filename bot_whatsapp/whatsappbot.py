# importar as bibbliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# Navegar até o whatsapp
service = Service()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# Definir contatos e grupos e mensagens a serem envidas
contatos = ['Familia supapo']
mensagem = ['Bolsonaro Presidente 2022, aceita que dói menos!', 'https://lulaflix.com.br/']
# Buscar cintatos/grupos
def buscar_contato(contato):
  campo_pesquisa = driver.find_element('//div[contains(@class,"copyable-text selectable-text")]')
  time.sleep(3)
  campo_pesquisa.click()
  campo_pesquisa.send_keys(contato)
  campo_pesquisa.send_keys(Keys.ENTER)
  print(campo_pesquisa)

# for contato in contatos:
#   buscar_contato(contato)
#   print(contato)
  # enviar_mensagem(mensagem)
# Campo de pesquisa 'copyable-text selectable-text'
# Campo de mensagem 'selectable-text copyable-text'
# Enviar mensagens para o contato/grupo