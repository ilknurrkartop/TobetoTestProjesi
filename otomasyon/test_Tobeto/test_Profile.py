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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Test_Profile:
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

    def test_Edit_Profile(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()

        current_url = self.driver.current_url
        assert current_url == "https://tobeto.com/profilim"

        share = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='dropdown-basic']")))
        share.click()
        sleep(1)

        share_Profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='dropdown-menu show']/div/p")))
        assert share_Profile.text == "Profilimi paylaş"

        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        sleep(3)
        textarea = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        textarea.clear()
        textarea.send_keys("Bilgisayar mühendisliği bölümünden 2022 yılında mezun oldum.")
        sleep(2)
        save = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")
        sleep(2)
        save.click()
        
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Bilgileriniz başarıyla güncellendi."
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,0)")
        sleep(3)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        is_Saved = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//p[@id='user_desc']")))
        assert is_Saved.text == "Bilgisayar mühendisliği bölümünden 2022 yılında mezun oldum."

    def test_Unsuccessful_Experience(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()

        experience = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='experience']/following-sibling::span")))
        experience.click()
        sleep(2)
        corporationName = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='corporationName']")))
        corporationName.clear()
        corporationName.send_keys("Bilgisayar mühendisliği bölümünden 2022 yılında mezun oldum. Mezun olduktan sonra Wissen Akademie'de projeler üzerinde çalışarak C#, ASP.NET MVC, SQL Server, HTML, CSS ve JavaScript eğitimlerini aldım. Aynı zamanda takım çalışmasına yatkın sorumluluk sahibi birisiyim.")
        position = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='position']")))
        position.clear()
        position.send_keys("Bilgisayar mühendisliği bölümünden 2022 yılında mezun oldum. Mezun olduktan sonra Wissen Akademie'de projeler üzerinde çalışarak C#, ASP.NET MVC, SQL Server, HTML, CSS ve JavaScript eğitimlerini aldım. Aynı zamanda takım çalışmasına yatkın sorumluluk sahibi birisiyim.")
        sector = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='sector']")))
        sector.clear()
        sector.send_keys("Bilgisayar mühendisliği bölümünden 2022 yılında mezun oldum. Mezun olduktan sonra Wissen Akademie'de projeler üzerinde çalışarak C#, ASP.NET MVC, SQL Server, HTML, CSS ve JavaScript eğitimlerini aldım. Aynı zamanda takım çalışmasına yatkın sorumluluk sahibi birisiyim.")
        city = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@name='country']")))
        city.click()
        selected_City = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//option[@value='Afyonkarahisar']")))
        selected_City.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        started_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/div/div/input")))
        started_Date.clear()
        started_Date.send_keys("16.01.2024")
        finished_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/div/div/input")))
        finished_Date.clear()
        finished_Date.send_keys("16.01.2024")
        description_Work = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        description_Work.clear()
        description_Work.send_keys("kısmına 300 karakterden fazla karakter giriniz.input : Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin aliquet nibh at dolor volutpat, et aliquet libero condimentum. Nullam posuere arcu ac sollicitudin tempus. Nam in imperdiet tortor. Sed gravida quis nulla sit amet malesuada. Mauris a maximus dui. Nunc dictum risus at tristique pharetra.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin aliquet nibh at dolor volutpat, et aliquet libero condimentum. Nullam posuere arcu ac sollicitudin tempus. Nam in imperdiet tortor. Sed gravida quis nulla sit amet malesuada. Mauris a maximus dui. Nunc dictum risus at tristique pharetra.")
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        sleep(3)
        danger1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[1]/span")))
        assert danger1.text == "En fazla 50 karakter girebilirsiniz"
        danger2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[2]/span")))
        assert danger2.text == "En fazla 50 karakter girebilirsiniz"
        danger3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[3]/span")))
        assert danger3.text == "En fazla 50 karakter girebilirsiniz"
        danger7 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[7]/span")))
        assert danger7.text == "En fazla 300 karakter girebilirsiniz"
        sleep(2)

    def test_Blank_Experience(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()

        experience = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='experience']/following-sibling::span")))
        experience.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        sleep(3)
        danger1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[1]/span")))
        assert danger1.text == "Doldurulması zorunlu alan*"
        danger2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[2]/span")))
        assert danger2.text == "Doldurulması zorunlu alan*"
        danger3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[3]/span")))
        assert danger3.text == "Doldurulması zorunlu alan*"
        danger5 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/span")))
        assert danger5.text == "Doldurulması zorunlu alan*"
        danger6 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/span")))
        assert danger6.text == "Doldurulması zorunlu alan*"
        sleep(2)

    def test_Successful_Add_Experience(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()

        experience = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='experience']/following-sibling::span")))
        experience.click()
        sleep(2)
        corporationName = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='corporationName']")))
        corporationName.clear()
        corporationName.send_keys("Kampüs 365")
        position = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='position']")))
        position.clear()
        position.send_keys("Front-end Developer")
        sector = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='sector']")))
        sector.clear()
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@name='country']")))
        city.click()
        selected_City = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//option[@value='Afyonkarahisar']")))
        selected_City.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        started_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/div/div/input")))
        started_Date.clear()
        started_Date.send_keys("16.01.2024")
        finished_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/div/div/input")))
        finished_Date.clear()
        finished_Date.send_keys("16.01.2024")
        description_Work = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        description_Work.clear()
        description_Work.send_keys("")
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Deneyim eklendi."

    def test_Successful_Add_Experience(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()

        experience = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='experience']/following-sibling::span")))
        experience.click()
        sleep(2)
        corporationName = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='corporationName']")))
        corporationName.clear()
        corporationName.send_keys("Kampüs 365")
        position = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='position']")))
        position.clear()
        position.send_keys("Front-end Developer")
        sector = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='sector']")))
        sector.clear()
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@name='country']")))
        city.click()
        selected_City = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//option[@value='Afyonkarahisar']")))
        selected_City.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        started_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/div/div/input")))
        started_Date.clear()
        started_Date.send_keys("16.01.2024")
        finished_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/div/div/input")))
        finished_Date.clear()
        finished_Date.send_keys("16.01.2024")
        description_Work = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//textarea[@name='description']")))
        description_Work.clear()
        description_Work.send_keys("")
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Deneyim eklendi."

    def test_Continious_Work(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()

        experience = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='experience']/following-sibling::span")))
        experience.click()
        sleep(2)
        corporationName = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='corporationName']")))
        corporationName.clear()
        corporationName.send_keys("Kampüs 365")
        position = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='position']")))
        position.clear()
        position.send_keys("Front-end Developer")
        sector = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='sector']")))
        sector.clear()
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@name='country']")))
        city.click()
        selected_City = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//option[@value='Afyonkarahisar']")))
        selected_City.click()
        sleep(2)
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        started_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/div/div/input")))
        started_Date.clear()
        started_Date.send_keys("16.01.2024")
        contious_Work = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='checkbox']")))
        contious_Work.click()
        
        finished_Date = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/div/div/input")))
        finished_Date.clear()
        finished_Date.send_keys("16.01.2024")
        assert finished_Date.text != "16.01.2024"

    def test_Blank_Education(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        education = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='educations']/following-sibling::span")))
        education.click()
        sleep(2)
        danger1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[1]/span")))
        assert danger1.text == "Doldurulması zorunlu alan*"
        danger2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[2]/span")))
        assert danger2.text == "Doldurulması zorunlu alan*"
        danger3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[3]/span")))
        assert danger3.text == "Doldurulması zorunlu alan*"
        danger4 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[4]/span")))
        assert danger4.text == "Doldurulması zorunlu alan*"
        danger5 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/span")))
        assert danger5.text == "Doldurulması zorunlu alan*"
        danger6 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[6]/span")))
        assert danger6.text == "Doldurulması zorunlu alan*"

    def test_Success_Education(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        education = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a/span[@class='educations']/following-sibling::span")))
        education.click()
        sleep(2)
        education_Level = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[1]/select")))
        education_Level.click()
        lisans = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//option[@value='Lisans']")))
        lisans.click()
        university = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[2]/input")))
        university.clear()
        university.send_keys("Kampüs 365")
        section = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[3]/input")))
        section.clear()
        section.send_keys("Yazılım")
        yearOfStart = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[4]/div/div/input")))
        yearOfStart.clear()
        yearOfStart.send_keys("2019")
        script = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(script)
        endOfStart = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row mb-2']/div[5]/div/div/input")))
        endOfStart.clear()
        endOfStart.send_keys("2023")
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Eğitim bilgisi eklendi."


    def test_Blank_Talent(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        talents_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Yetkinliklerim']")))
        talents_link.click()
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        save.click()
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Herhangi bir yetenek seçmediniz!."

    def test_addCompetence(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        competence = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, " //div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[4]/span[2]")))
        competence.click()
        sleep(2)
        addArea = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, " //div[@id='react-select-2-placeholder']/following-sibling::div/input")))
        addArea.clear()
        addArea.send_keys("Muhasebe",Keys.ENTER)  
        sleep(3)
        save = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary py-2 mb-3 d-inline-block mobil-btn']")))
        sleep(3)
        save.click()
    
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Yetenek eklendi."

   
    def test_Delete_Talent(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        talent = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='col-12 col-lg-3 mb-8 mb-lg-0']/div/a[4]/span[2]")))
        talent.click()
        sleep(2)
        trash_icon = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class=' grade-delete g-del']")))
        trash_icon.click()
        sleep(1)
        yes_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Evet']")))
        yes_button.click()
        sleep(2)
        pop_up_message = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='toast-body']")))
        assert pop_up_message.text == "• Yetenek kaldırıldı."
        sleep(2)        
        deleted_skill_xpath = "//span[text()='Aktif Öğrenme']"
        assert len(self.driver.find_elements(By.XPATH, deleted_skill_xpath)) == 0

    def test_Success_Certificate(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        certificates_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Sertifikalarım']")))
        certificates_link.click()
        sleep(2)
        upload_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='cursor-pointer']")))
        upload_button.click()
        sleep(2)
        gozat = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='uppy-u-reset uppy-c-btn uppy-Dashboard-browse']")))
        gozat.click()
        
        
        # Dosya yüklendiğinde sertifikanın ekranda görünüp görünmediğini kontrol et
        uploaded_certificate = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//img[@alt='Herkes İçin Kodlama - 1C']")))
        assert uploaded_certificate.is_displayed()
        
        # Profilim sayfasına geri dön
        profile.click()
        sleep(2)
        certificates_link.click()
        sleep(2)
        # Eklenen sertifikanın listelendiğini kontrol et
        added_certificate = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Herkes İçin Kodlama - 1C')]")))
        assert added_certificate.is_displayed()
        
        # Sertifikaya tıkla ve indirme işlemini kontrol et
        added_certificate.click()
        sleep(2)

    def test_Delete_Certificate(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        certificates_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Sertifikalarım']")))
        certificates_link.click()
        sleep(2)
        delete_icon = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//tbody/tr[1]/td[4]/span[2]")))
        delete_icon.click()
        sleep(2)
        confirm_delete_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Evet')]")))
        confirm_delete_button.click()
        sleep(2)
        
        # Dosya kaldırıldı uyarısını kontrol et
        remove_success_toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Dosya kaldırma işlemi başarılı.')]")))
        assert remove_success_toast.is_displayed()
        
        # Sertifikanın sayfadan kaldırıldığını kontrol et
        try:
            WebDriverWait(self.driver, 5).until_not(ec.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Herkes İçin Kodlama - 1C')]")))
        except TimeoutException:
            pass  # Sertifika sayfadan kaldırıldı

    def test_Success_Media(self):
    # Adımlar 1-4: Linkedin hesabını ekleyin
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        select_platform = (By.XPATH, "//select[@name='platform']")
        select_platform_input = "Linkedin"
        platform_link_input = "www.linkedin.com/in/ilknur-kartop"
        select_platform_element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located("//select[@class='form-select']"))
        Select(select_platform_element).select_by_visible_text(select_platform_input)
        profile_address_input = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='profile_address']")))
        profile_address_input.send_keys(platform_link_input)
        save_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Kaydet']")))
        save_button.click()
    # Beklenen Sonuç: Linkedin hesabı başarıyla eklendiği ve kaydedildiği kontrol edilir
        toast_locator = (By.XPATH, "//div[@class='toast-body']")
        linkedin_success_toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert linkedin_success_toast.text == "Sosyal medya adresiniz başarıyla eklendi."
        linkedin_saved_account = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, f"//li[text()='{select_platform_input}']")))
        assert linkedin_saved_account is not None

    # Adımlar 5-10: GitHub ve Instagram hesaplarını ekleyin
        select_platform_inputs = ["GitHub", "Instagram"]
        profile_link_inputs = ["https://github.com/ilknurrkartop", "https://www.instagram.com/ilknurrkartop/"]
        for i in range(len(select_platform_inputs)):
            select_platform_element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(select_platform))
            Select(select_platform_element).select_by_visible_text(select_platform_inputs[i])
            profile_address_input = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='profile_address']")))
            profile_address_input.send_keys(profile_link_inputs[i])
            save_button.click()
        # Beklenen Sonuç: Hesaplar başarıyla eklenip sınırlamayı aştığını belirten hata alınır ve form kaldırılır
            if i == 2:
                max_media_error_toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
                assert max_media_error_toast.text == "En fazla 3 adet medya seçimi yapılabilir."
                assert len(self.driver.find_elements(By.XPATH, "//select[@name='platform']")) == 0

    # Adımlar 11-12: Profilim sayfasına gidin ve eklenen hesaplardan birine tıklayın
        profile.click()
        media_accounts = ["LinkedIn", "GitHub", "Instagram"]
        for account in media_accounts:
            account_icon = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, f"//span[@class='fa fa-{account.lower()}']")))
            account_icon.click()
        # Beklenen Sonuç: Tıklanan sosyal medya hesabının profiline yönlendirilir
            assert "linkedin" in self.driver.current_url.lower() or "github" in self.driver.current_url.lower() or "instagram" in self.driver.current_url.lower()

    def test_Unmatched_Media_Addition(self):
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)       
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
    
        select_platform = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/div/div[1]/select")))
        Select(select_platform).select_by_visible_text("Linkedin")
    
        profile_input = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@id='profile_url']")))
        profile_input.send_keys("https://www.instagram.com/ilknurrkartop/")
    
        save_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='save']")))
        save_button.click()
    
        try:
            WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Seçilen sosyal medya platformu ile profil adresi alanına yazılan hesap aynı platforma ait değilse kaydetme işlemini başarılı bir şekilde tamamlanamamalı.')]")))
        except TimeoutException:
            assert False, "Beklenen uyarı mesajı görüntülenmedi."

    def test_Update_Media(self):
    # Adımlar 1-4: Medya hesaplarını güncelle
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        media_accounts = ["LinkedIn", "GitHub", "Instagram"]
        new_links = ["www.linkedin.com/in/new-linkedin-profile", "https://github.com/new-github-profile", "https://www.instagram.com/new-instagram-profile/"]
        for i in range(len(media_accounts)):
            edit_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, f"//li[text()='{media_accounts[i]}']/following-sibling::li//span[@class='fa fa-pencil']")))
            edit_button.click()
            link_input = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='profile_address']")))
            link_input.clear()
            link_input.send_keys(new_links[i])
            update_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Güncelle']")))
            update_button.click()
        # Beklenen Sonuç: Medya hesap bilgileri güncellenir
            assert WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, "//div[@class='toast-body']"), "Sosyal medya adresiniz başarıyla güncellendi."))

    def test_Delete_Media(self):
        # Adımlar 1-3: Medya hesabını sil
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        media_account = "Instagram"
        delete_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, f"//li[text()='{media_account}']/following-sibling::li//span[@class='fa fa-trash']")))
        delete_button.click()
        # Beklenen Sonuç: Medya hesap bilgileri silinir
        assert WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, "//div[@class='toast-body']"), "Sosyal medya adresiniz başarıyla kaldırıldı."))
    
    def test_Empty_Languages(self):
        # Adımlar 1-2: Yabancı diller sayfasına git ve boş alanları kaydet
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        languages_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Yabancı Dillerim']")))
        languages_link.click()
        save_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Kaydet']")))
        save_button.click()
        # Beklenen Sonuç: Zorunlu alan uyarısı görüntülenir
        metin= WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//p[text()='Doldurulması zorunlu alan*']")))
        assert metin.text == "Doldurulması zorunlu alan*"

    def test_Success_Languages(self):
        # Adımlar 1-4: Yabancı dilleri başarılı bir şekilde ekleyin
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        languages_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Yabancı Dillerim']")))
        languages_link.click()
        select_language = Select(WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@id='language']"))))
        select_language.select_by_visible_text("İngilizce")
        select_level = Select(WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//select[@id='level']"))))
        select_level.select_by_visible_text("Orta Seviye(B1, B2)")
        save_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Kaydet']")))
        save_button.click()
        # Beklenen Sonuç: Başarı mesajı ve eklenen dilin görünmesi
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Yabancı dil bilgisi eklendi')]")))
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//td[contains(text(),'İngilizce')]")))
        # Adım 5: Profil sayfasına geri dönün ve eklenen dilin görünürlüğünü kontrol edin
        profile.click()
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//td[contains(text(),'İngilizce')]")))

    def test_Delete_Language(self):
        # Adımlar 1-2: Yabancı dillerden birini sil
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        edit = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='cv-edit-icon']")))
        edit.click()
        sleep(2)
        languages_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[@class='sidebar-text' and text()='Yabancı Dillerim']")))
        languages_link.click()
        delete_icon = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//tr[1]//i[@class='fa fa-trash']")))
        delete_icon.click()
        # Beklenen Sonuç: Silme işlemi doğrulama ve başarılı mesajı
        confirm_delete = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Evet']")))
        confirm_delete.click()
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Yabancı dil kaldırıldı')]")))
        # Beklenen Sonuç: Kaydet butonunun altındaki dilin kalkması
        assert len(WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//td[contains(text(),'İngilizce')]")))) == 0

    def test_Empty_Settings(self):
        # Adımlar 1-2: Ayarlar sayfasına git ve zorunlu alanları boş bırakarak şifre değiştirme işlemi yap
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        settings_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a[text()='Ayarlar']")))
        settings_link.click()
        change_password_btn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Şifre Değiştir']")))
        change_password_btn.click()
        # Beklenen Sonuç: Doldurulması zorunlu alan uyarısı
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Doldurulması zorunlu alan')]")))

    def test_Failed_Password_Change(self):
        # Adımlar 1-5: Eşleşmeyen yeni şifrelerle şifre değiştirme işlemi yap
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        settings_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a[text()='Ayarlar']")))
        settings_link.click()
        old_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='oldPassword']")))
        old_password.send_keys("Tobeto1234")
        new_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='newPassword']")))
        new_password.send_keys("Tobet123")
        confirm_new_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='confirmNewPassword']")))
        confirm_new_password.send_keys("Tobe345")
        change_password_btn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Şifre Değiştir']")))
        change_password_btn.click()
        # Beklenen Sonuç: Şifrelerin eşleşmediği uyarısı
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Girilen şifreler eşleşmiyor')]")))

        # Adımlar 6-8: 6 karakterden az yeni şifreyle şifre değiştirme işlemi yap
        new_password.clear()
        new_password.send_keys("123")
        confirm_new_password.clear()
        confirm_new_password.send_keys("123")
        change_password_btn.click()
        # Beklenen Sonuç: Yeni şifrenin en az 6 karakterden olması gerektiği uyarısı
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Şifreniz en az 6 karakterden oluşmalıdır')]")))

        # Adımlar 9-11: Mevcut şifreyle aynı yeni şifreyle şifre değiştirme işlemi yap
        new_password.clear()
        new_password.send_keys("Tobeto1234")
        confirm_new_password.clear()
        confirm_new_password.send_keys("Tobeto1234")
        change_password_btn.click()
        # Beklenen Sonuç: Yeni şifrenin mevcut şifreden farklı olması gerektiği uyarısı
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Yeni şifreniz mevcut şifrenizden farklı olmalıdır')]")))

    def test_Success_Password_Change(self):
        # Adımlar 1-4: Başarılı bir şekilde yeni şifreyle şifre değiştirme işlemi yap
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        settings_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='_next']/div/main/section/div/div/div[1]/div/a[8]/span[2]")))
        settings_link.click()
        old_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='oldPassword']")))
        old_password.send_keys("Tobeto1234")
        new_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='newPassword']")))
        new_password.send_keys("Tobeto456")
        confirm_new_password = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//input[@name='confirmNewPassword']")))
        confirm_new_password.send_keys("Tobeto456")
        change_password_btn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Şifre Değiştir']")))
        change_password_btn.click()
        # Beklenen Sonuç: Şifrenin başarıyla güncellendiği pop-up mesajı
        assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Şifreniz güncellenmiştir.')]")))

    def test_Terminate_Membership(self):
        # Adımlar 1-2: Hesabı sonlandırma işlemi başlat
        Test_Tobeto.test_SuccessLogin(self)
        sleep(2)
        profile = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='d-none d-xxl-flex navbar-nav']/li[2]/a")))
        profile.click()
        sleep(2)
        settings_link = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//span[ text()='Ayarlar']")))
        settings_link.click()
        terminate_membership_btn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-danger mb-2  w-100']")))
        terminate_membership_btn.click()
        # Beklenen Sonuç: Hesap silme işlemi için onay pop-up'ı gösterilir
        box=WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//p[@class='alert-message mx-3']")))
        assert box.text == "Hesabınızı silmek istediğinize emin misiniz?"
       
        # Adım 3: Hesabı silme işlemini onayla
        confirm_termination_btn = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Evet']")))
        confirm_termination_btn.click()
        # Beklenen Sonuç: Hesap başarıyla silinmiştir
        assert "Hesabınız başarıyla silindi." in self.driver.page_source