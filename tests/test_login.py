import os
from pages.login import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def criar_driver():
    options = Options()
    options.add_argument("--disable-notifications")
    
    # só ativa headless se variável estiver definida
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    return driver, wait


def test_login_invalido():
   
    try:
        # Arrange
        driver, wait = criar_driver()
        login = LoginPage(driver, wait)
        login.abrir()

        # Act
        login.fazer_login("email@invalido.com", "asdf123")
        mensagem = login.obter_mensagem_erro()

        # Assert
        assert "Username and password do not match any user in this service" in mensagem

    finally:
        driver.quit()

def test_login_valido():

    try:
        # Arrange
        driver, wait = criar_driver()
        login = LoginPage(driver, wait)
        login.abrir()
        
        # Act
        login.fazer_login("standard_user", "secret_sauce")

        # Assert
        assert "/inventory.html" in driver.current_url

    finally:
        driver.quit()