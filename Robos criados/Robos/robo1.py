from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso robô...\n")

driver = webdriver.Chrome('C:\\Users\\Rafael Moraes\\Desktop\\Robos\\chromedriver')
driver.get("https://www.trt6.jus.br")

time.sleep(3)
driver.close()
