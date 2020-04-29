from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('C:\\Users\\Rafael Moraes\\Desktop\\Robos\\chromedriver')
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear() #Limpar a barra de pesquisa
pesquisa.send_keys("www.globo.com.br")
pesquisa.send_keys(Keys.RETURN)
time.sleep(3)

resultados = driver.find_elements_by_tag_name("strong")
import pdb; pdb.set_trace()

time.sleep(8)
driver.close()
