#importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#navagar até o whatsapp web
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(10)
#definir contatos e grupos e mensagem a ser enviada
contatos = ['JÉSSICA']
mensagem = ('''E aí, pessoal, sou um bot criado por Thiago para mandar mensagem automatizada no whatsapp web. 

Fui desenvolvido utilizando-se de uma biblioteca Python chamada Selenium.  ''')
#buscar contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(0.5)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    time.sleep(0.5)
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(0.5)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(0.5)
    campo_mensagem[1].send_keys(Keys.ENTER)
    time.sleep(0.5)

buscar_contato(contatos)
enviar_mensagem(mensagem)

#campo de pesquisa 'copyable-text selectable-text'
#campo de mensagem privada '_1awRl copyable-text selectable-text'
#Enviar mensagens para o contato/grupo

