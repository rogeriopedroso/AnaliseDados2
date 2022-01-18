import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://drive.google.com/drive/folders/1RQuhaHty3JO3upp8DdDlTZzY1c8918nF'

navegador = webdriver.Chrome()

navegador.get(url)
time.sleep(1)

navegador.find_element(
    By.XPATH, '//*[@id=":0"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[3]/div/div/div/div[1]/div[2]').click()
time.sleep(3)

navegador.quit()

imp_base_dados = '/home/rogerio/Downloads'

listar_arquivos = os.listdir(imp_base_dados)

listar_datas = []

for arquivo in listar_arquivos:
    data = os.path.getatime(f'{imp_base_dados}/{arquivo}')
    listar_datas.append((data, arquivo))

listar_datas.sort(reverse=True)
ultimo_arquivo = listar_datas[0]
print(ultimo_arquivo)
