import openpyxl
import pytest
from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains





class Test_Calender:
    def setup_method(self): #Her test başlangıcında çalışacak method
        self.driver = webdriver . Chrome ()
        self.driver.get("https://tobeto.com/")
        self.driver.maximize_window()
        
        

    def tearDown_method(self):
        self.driver.quit()
        
    def test_Calender_control(self):
        calendericon = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='calendar-btn'] ")))
        calendericon.click()
        message = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Eğitim ve Etkinlik Takvimi']")))
        assert message.text =="Eğitim ve Etkinlik Takvimi"
        sleep(3)
        lessonButton = self.driver.find_element(By.XPATH,"//input[@value = 'eventNotStarted']")
        lessonButton.click()
        calenderFilter =self.driver.find_element(By.XPATH,"//button[@title='Ay']")
        calenderFilter.click()
        assert calenderFilter.text == "Ay"
        cross =self.driver.find_element(By.XPATH,"//button[@class='btn-close btn-close-white']").click()
        metin= self.driver.find_element(By.XPATH,"//button[@class='ik-btn']")
        assert metin.text == "Başvur"
       
        sleep(3)
        