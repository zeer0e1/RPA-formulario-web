from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as tempo_espera

"""
    email = 164664499
    telefone = 164664560
    texto = 164665180
    masculino = 164665110_1204416430_label
    feminino = 164665110_1204416431_label]
    button submit = //*[@id="patas"]/main/article/section/form/div[2]/button
"""

navegadorForm = opcoes_selenium.Chrome()
navegadorForm.get("https://pt.surveymonkey.com/r/2LXVCXJ")

navegadorForm.find_element(By.NAME, "164664468").send_keys('Lucas de Freitas Gonçalves Ribeiro')
navegadorForm.find_element(By.NAME, "164664499").send_keys('lucasfreitasr@outlook.com')
navegadorForm.find_element(By.NAME, "164664560").send_keys('(15) 99170-0089')
navegadorForm.find_element(By.ID, "164665110_1204416430_label").click()
navegadorForm.find_element(By.NAME, "164665180").send_keys('Eu amo Python')
navegadorForm.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()
navegadorForm.get("https://pt.surveymonkey.com/r/2LXVCXJ")



tempo_espera.sleep(40)