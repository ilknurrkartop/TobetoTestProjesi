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
from test_Login import Test_Tobeto

class Test_TopMenu:
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

    def test_MyProfileControl(self):
        Test_Tobeto.test_SuccessLogin(self)
        myProfile = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Profilim']")
        myProfile.click()
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/profilim"
        profilShare= self.driver.find_element(By.ID,"dropdown-basic").click()
        sleep(3)
        profile_link = self.driver.find_element(By.XPATH,"//label[@class='input-label-text']")
        assert profile_link.text == "Profil Linki"
        
    def test_Reviews(self):
        Test_Tobeto.test_SuccessLogin(self)
        reviews = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Değerlendirmeler']")
        reviews.click()
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/degerlendirmeler"
        
    def test_Catalog(self):
        Test_Tobeto.test_SuccessLogin(self)
        catalog = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Katalog']")
        catalog.click()
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/platform-katalog"
       
    def test_Calender(self):
        Test_Tobeto.test_SuccessLogin(self)
        calender = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Takvim']")
        calender.click()
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/takvim"
        
    def test_ReturnHomePsge(self):
        Test_Tobeto.test_SuccessLogin(self)
        calender = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Takvim']")
        calender.click()
        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/takvim"
        homepage = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='Ana Sayfa']")
        homepage.click()
        url = self.driver.current_url
        assert url == "https://tobeto.com/platform"
        
    def test_TopMenuWindowControl(self):
        Test_Tobeto.test_SuccessLogin(self)
        topMenuWindow = self.driver.find_element(By.XPATH, "//button[@class='btn p-0 fw-normal b-r-35 text-end d-flex align-items-center']")
        topMenuWindow.click()
        profileInformation = self.driver.find_element(By.XPATH,"//a[@class='dropdown-item profil-dropdown'and text()='Profil Bilgileri']")
        assert profileInformation.text == "Profil Bilgileri"
        topMenuWindowClose= self.driver.find_element(By.XPATH,"//button[@class='btn p-0 fw-normal b-r-35 text-end d-flex align-items-center show']").click()
        profileInformation = self.driver.find_element(By.XPATH,"//a[@class='dropdown-item profil-dropdown'and text()='Profil Bilgileri']")
        assert not profileInformation.is_displayed()
        
    
    def test_IstanbulCodingPage(self):
        Test_Tobeto.test_SuccessLogin(self)
        istanbulCoding = self.driver.find_element(By.XPATH, "//a[@class='nav-link c-gray-3' and text()='İstanbul Kodluyor']")
        istanbulCoding.click()
        _url = self.driver.current_url
        assert _url == "https://tobeto.com/istanbul-kodluyor"
    
        
        