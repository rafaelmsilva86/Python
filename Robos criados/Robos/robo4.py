from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('C:\\Users\\Rafael Moraes\\Desktop\\Robos\\chromedriver')
driver.get("https://www.trt6.jus.br")



dominio = ["proad", "pje", "sans"]
for dominio in dominio:
	pesquisa = driver.find_element_by_id("edit-search-block-form--2")
	pesquisa.clear() #Limpar a barra de pesquisa
	pesquisa.send_keys(dominio)
	pesquisa.send_keys(Keys.RETURN)
	time.sleep(3)
	resultados = driver.find_elements_by_tag_name("strong") #procura palavra em negrito
	print("Encontramos %s %s" % (dominio, resultados[2].text)) #exibe a palavra do campo específico

#time.sleep(8)
driver.close()
