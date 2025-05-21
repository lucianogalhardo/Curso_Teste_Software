from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.utils import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def setup_teardown():
    # Setup: Configurar conexão com o driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://wcaquino.me/cypress/componentes.html")
    driver.set_window_size(2000, 0)  # Definir tamanho da janela
    #driver.implicitly_wait(10)  # Espera implícita de 2 segundos
    time.sleep(2)

    # Teardown: Fechar o driver após os testes
    yield driver
    driver.quit()

def test_botao_muda_texto(setup_teardown):
    driver = setup_teardown
    
    # Escrever em um elemento utilizando o By.ID
    time.sleep(5)
    campo_nome = driver.find_element(By.ID, "formNome")
    campo_nome.send_keys("David")
    
    # Escrever em um elemento utilizando o By.CSS_SELECTOR
    driver.find_element(By.CSS_SELECTOR, "#formSobrenome").send_keys("Brandão")
    
    # Clicar em um botão - radio button - checkbox
    btn_click_me = driver.find_element(By.ID, "buttonSimple")
    print(recupera_texto(btn_click_me))
    
    btn_click_me.click()
    print(recupera_texto(btn_click_me))
    
    btn_click_me = driver.find_element(By.ID, "buttonCount")
    for i in range(5):
        btn_click_me.click()
        print(recupera_texto(btn_click_me))
