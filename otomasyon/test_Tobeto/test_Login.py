import openpyxl
import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import random
from Constants import globalConstants as gc

class Test_Tobeto:
    def setup_method(self): #Her test başlangıcında çalışacak method
        self.driver = webdriver . Chrome ()
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window()

    def tearDown_method(self):
        self.driver.quit()

    def loginButton(self):
        self.driver.get("https://tobeto.com/")
        LogInButton = self.driver.find_element(By.CSS_SELECTOR, "a.btn.border-light.text-light.mx-4")
        LogInButton.click()

    def test_SuccessLogin(self):
        self.loginButton()

        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/giris"

        eMail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "email")))
        eMail.send_keys("htugcetaskin@gmail.com")
        password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "password")))
        password.send_keys("Tunc1189035.")
        Login = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-primary w-100 mt-6']")
        Login.click()

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Giriş başarılı."
        sleep(3)
        Tobeto = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class = 'mw-5xl mx-auto'] /h3/span[1]")))
        ya = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class = 'mw-5xl mx-auto'] /h3/span[2]")))
        welcome = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class = 'mw-5xl mx-auto'] /h3/span[3]")))
        userName = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class = 'mw-5xl mx-auto'] /h4")))
        welcomeText = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class = 'mw-5xl mx-auto'] /p")))
        sleep(2)
        assert Tobeto.text == "TOBETO"
        assert ya.text == "'ya"
        assert welcome.text == "hoş geldin"
        assert userName.text == "Tuğçe"
        assert welcomeText.text == "Yeni nesil öğrenme deneyimi ile Tobeto kariyer yolculuğunda senin yanında!"
        sleep(2)

    def test_BlankAreaLogin(self):
        self.loginButton()

        Login = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class = 'btn btn-primary w-100 mt-6']")))
        Login.click()

        email = self.driver.find_element(By.XPATH, "//input[@name = 'email']/following-sibling::p[1]")
        assert email.text =="Doldurulması zorunlu alan*"

        password = self.driver.find_element(By.XPATH, "//input[@name = 'email']/following-sibling::p[2]")
        assert password.text =="Doldurulması zorunlu alan*"

    @pytest.mark.parametrize("email, ePassword", [("htuggcetaskin@gmail.com", "Ebrar1189035d."),("htugcetaskin@gmail.com", "Ebrarra1189035d."),("htugceettaskin@gmail.com", "Ebrarra1189035d."),("htuggcetaskin", "Ebrar1189035d.")])
    def test_WrongEmailOrPassword(self, email, ePassword):
        self.loginButton()

        eMail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "email")))
        eMail.send_keys(email)
        password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME, "password")))
        password.send_keys(ePassword)
        Login = self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-primary w-100 mt-6']")
        Login.click()

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Geçersiz e-posta veya şifre."
        sleep(5)

    def test_ForgotPassword(self):
        self.loginButton()

        forgotPassword = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='py-4 px-sm-0 px-md-12 text-center ']/form/label/small")))
        forgotPassword.click()
        sleep(3)
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/sifremi-unuttum"

        resetPassword = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//h3[@class = 'mt-6 mb-8']")))
        assert resetPassword.text == "Şifre Sıfırlama"

    def test_Register(self):
        self.loginButton()

        register = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a[@class = 'text-decoration-none text-muted fw-bold']")))
        register.click()

        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/kayit-ol"

        registerNow = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//h3[@class = 'mt-6 mb-8']")))
        assert registerNow.text == "Hemen Kayıt Ol"