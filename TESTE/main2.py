from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

def get_random_string(length=16):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

c = 0
teste1 = False

driver.get('https://testedesenha.com.br/')
# mask = driver.find_element(By.ID, 'mask')
# mask.click()

while True:
    camposenha = driver.find_element(By.ID, 'passwordPwd')


    senha = ''
    camposenha.send_keys(senha)


    senha = get_random_string()
    camposenha.send_keys(senha)

    criteriosa = []
    criteriosd = []

    # Adições
    criteriosa.append(driver.find_element(By.ID, 'div_nLength'))
    criteriosa.append(driver.find_element(By.ID, 'div_nAlphaUC'))
    criteriosa.append(driver.find_element(By.ID, 'div_nAlphaLC'))
    criteriosa.append(driver.find_element(By.ID, 'div_nNumber'))
    criteriosa.append(driver.find_element(By.ID, 'div_nSymbol'))
    criteriosa.append(driver.find_element(By.ID, 'div_nMidChar'))
    criteriosa.append(driver.find_element(By.ID, 'div_nRequirements'))

    # Deduções
    criteriosd.append(driver.find_element(By.ID, 'div_nAlphasOnly'))
    criteriosd.append(driver.find_element(By.ID, 'div_nNumbersOnly'))
    criteriosd.append(driver.find_element(By.ID, 'div_nRepChar'))
    criteriosd.append(driver.find_element(By.ID, 'div_nConsecAlphaUC'))
    criteriosd.append(driver.find_element(By.ID, 'div_nConsecAlphaLC'))
    criteriosd.append(driver.find_element(By.ID, 'div_nConsecNumber'))
    criteriosd.append(driver.find_element(By.ID, 'div_nSeqAlpha'))
    criteriosd.append(driver.find_element(By.ID, 'div_nSeqNumber'))

    # Teste 1
    for criterio in criteriosa:
        print(criterio.get_attribute('class'))
        if criterio.get_attribute('class') == 'exceed':
            teste1 = True
        else:
            teste1 = False
            break
        
    c = 0
    # Teste 2
    for criterio in criteriosa:
        print(criterio.get_attribute('class'))
        if criterio.get_attribute('class') == 'pass':
            print(c)
            c += 1
        else:
            print(c)
    
    if teste1 == True and c >= 4:
        break

# R7gAEz=[VX4_^QOY
print('c fora',c)
print(f'Senha: {senha}') # type: ignore
