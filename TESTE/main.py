from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import string as s
from secrets import SystemRandom as Sr

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'chromedriver.exe'
SENHAS = ROOT_FOLDER / 'senhas.txt'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

options = ('--headless',)
browser = make_chrome_browser(*options)

browser.get('https://testedesenha.com.br/')

senhas_seleciondas = [] 

c = 0
while c < 500:
    search_input = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(
                (By.ID, 'passwordPwd')
            )
        )

    senha = []

    search_input.send_keys(senha)
    search_input.send_keys(Keys.ENTER)


    senha = ''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=16))
    # senha = ''.join(Sr().choices(s.ascii_letters + s.digits, k=16))

    search_input.send_keys(senha)
    search_input.send_keys(Keys.ENTER)

    result = browser.find_element(By.ID, 'score')

    if result.text == '100%' and not result.text in senhas_seleciondas:
        senhas_seleciondas.append(senha)
        c += 1

with open(SENHAS, 'w', encoding='utf-8') as file:
    for i,senha_unica in enumerate(senhas_seleciondas):
        file.write(f'{i};{senha_unica}\n')
