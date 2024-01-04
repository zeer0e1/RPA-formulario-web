from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.by import By
import pyautogui as tempo_espera
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



caminho_arquivo = 'dados-form.xlsx'
planilha_aberta = load_workbook(filename=caminho_arquivo)
sheet_selecionada = planilha_aberta['Dados']
navegadorForm = opcoes_selenium.Edge()

for linha in range(2, len(sheet_selecionada['A']) + 1):

    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value

    if nome is None and email is None and telefone is None and sexo is None and sobre is None:
        print(f"Fim dos dados na linha {linha}. Terminando a execução.")
        break

    navegadorForm.get("https://pt.surveymonkey.com/r/2LXVCXJ")

    espera = WebDriverWait(navegadorForm, 10)

    campo_nome = espera.until(
        ec.presence_of_element_located((By.ID, "164664468")))
    campo_nome.send_keys(nome)

    campo_email = espera.until(
        ec.presence_of_element_located((By.ID, "164664499")))
    campo_email.send_keys(email)

    campo_telefone = espera.until(
        ec.presence_of_element_located((By.ID, "164664560")))
    campo_telefone.send_keys(telefone)

    campo_sbore = espera.until(
        ec.presence_of_element_located((By.ID, "164665180")))
    campo_sbore.send_keys(sobre)

    if sexo == 'Masculino':
        botao_masculino = espera.until(ec.element_to_be_clickable(
            (By.ID, "164665110_1204416430_label")))
        botao_masculino.click()
    else:
        botao_feminino = espera.until(ec.element_to_be_clickable(
            (By.ID, "164665110_1204416431_label")))
        botao_feminino.click()

    botao_enviar = espera.until(ec.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="patas"]/main/article/section/form/div[2]/button')))
    botao_enviar.click()

    navegadorForm.refresh()

navegadorForm.quit()
