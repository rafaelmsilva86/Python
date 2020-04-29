from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('C:\\Users\\Rafael Moraes\\Desktop\\Robos\\chromedriver')
driver.get("https://www.trt6.jus.br")

pesquisa = driver.find_element_by_id("edit-search-block-form--2")
pesquisa.clear() #Limpar a barra de pesquisa
pesquisa.send_keys("PROAD")
pesquisa.send_keys(Keys.RETURN)

time.sleep(8)
driver.close()
