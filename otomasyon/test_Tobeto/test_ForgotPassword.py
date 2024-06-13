import openpyxl
import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Tobeto:
    

    def setup_method(self): #Her test başlangıcında çalışacak method
        self.driver = webdriver . Chrome ()
        self.driver.get("https://tobeto.com/sifremi-unuttum")
        self.driver.maximize_window()

    def tearDown_method(self):
        self.driver.quit()

    def test_Success_Change_Password(self):
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/sifremi-unuttum"

        eMail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@class='form-control mt-6']")))
        eMail.send_keys("tobetotestmail@gmail.com")

        sendButton = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")
        sendButton.click()

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin."
        
    def test_Unsuccess_Change_Password(self):
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/sifremi-unuttum"

        eMail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@class='form-control mt-6']")))
        eMail.send_keys("taskinttugce@gmail.com")

        sendButton = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")
        sendButton.click()

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Kullanıcı bulunamadı."

    @pytest.mark.parametrize("email", [("htuggcetaskin")])
    def test_Changing_Password_With_Invalid_Email(self, email):

        eMail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@class='form-control mt-6']")))
        eMail.send_keys(email)

        sendButton = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")
        sendButton.click()

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Girdiğiniz e-posta geçersizdir."