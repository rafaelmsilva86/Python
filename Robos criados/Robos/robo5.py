from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
print("Iniciando nosso robô...\n")

dominios = []
#Lendo excel
workbook = xlrd.open_workbook('dominio.xlsx')
sheet = workbook.sheet_by_index(0)

for linha in range(0, 10):
	dominios.append(sheet.cell_value(linha,0))

driver = webdriver.Chrome('C:\\Users\\Rafael Moraes\\Desktop\\Robos\\chromedriver')
driver.get("https://www.registro.br")



dominio = ["www.liveconexao.com.br", "www.pjetrt6.com.br", "www.globlo.com"]
for dominio in dominios:
	pesquisa = driver.find_element_by_id("is-avail-field")
	pesquisa.clear() #Limpar a barra de pesquisa
	pesquisa.send_keys(dominio)
	pesquisa.send_keys(Keys.RETURN)
	time.sleep(3)
	resultados = driver.find_elements_by_tag_name("strong") #procura palavra em negrito
	print("Dominio: %s %s" % (dominio, resultados[2].text)) #exibe a palavra do campo específico

#time.sleep(8)
driver.close()
