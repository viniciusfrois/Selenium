from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage: 
    
    URL = "https://www.saucedemo.com/"
    
    def __init__(self, driver, wait): 
        self.driver = driver 
        self.wait = wait

    #Elementos
    USERNAME = (By.CSS_SELECTOR, "[data-test='username']")
    PASSWORD = (By.CSS_SELECTOR, "[data-test='password']")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    #Ações
    def abrir(self):
        self.driver.get(self.URL)

    def preencher_usuario(self, usuario):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(*self.PASSWORD).send_keys(senha)

    def submeter(self):
        self.driver.find_element(*self.PASSWORD).submit()

    def fazer_login(self, usuario, senha):
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.submeter()

    def obter_mensagem_erro(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
