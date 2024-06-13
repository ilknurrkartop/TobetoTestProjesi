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

class Test_Register:
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
    
    #1 Kullanıcı Kayıt Kontrolü 
    def test_UserRegisterControl(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.send_keys("Tobeto")
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.send_keys("Test")
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        password =self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.click()
        password.send_keys("Tobeto1234.")
        passwordAgain =self.driver.find_element(By.XPATH,"//input[@name='passwordAgain']")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")
        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        aydinlatmaMetni = self.driver.find_element(By.XPATH,"//a[text()='Aydınlatma Metni']")
        aydinlatmaMetni.click()
        main_window_handle = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        for handle in all_window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        assert "https://tobeto.com/yasal-metinler/kvkk-aydinlatma-metni" in self.driver.current_url
        self.driver.close()
        
        self.driver.switch_to.window(main_window_handle)

        acikRizaMetni =self.driver.find_element(By.XPATH,"//a[text()='Açık Rıza Metni']")
        acikRizaMetni.click()
        sleep(3)
        main_window_handle = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        for handle in all_window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        assert "https://tobeto.com/yasal-metinler/acik-riza-metni" in self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(main_window_handle)
        
       
        uyelikSozlesmesi =self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/div/div/label[3]/small/a")
        uyelikSozlesmesi.click()
        main_window_handle = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        for handle in all_window_handles:
            if handle != main_window_handle:
                self.driver.switch_to.window(handle)
                break
        
        assert "https://tobeto.com/yasal-metinler/tobeto-uyelik-sozlesmesi" in self.driver.current_url
        sleep(3)
        
        self.driver.close()
    
        
        
        
    #2 Başarılı Kullanıcı Kayıt Kontrolü
    def test_SuccessfulUserRegister(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.send_keys("Tobeto")
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.send_keys("Test")
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.send_keys("tobetotestmail002@gmail.com")
        password =self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.click()
        password.send_keys("Tobeto1234.")
        passwordAgain =self.driver.find_element(By.XPATH,"//input[@name='passwordAgain']")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")
        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()
        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        numara_alani =self.driver.find_element(By.XPATH,"//input[@name='phoneNumber']")
        numara_alani.click()
        numara_alani.send_keys("0505 123 45 67")
        sleep(3)
        
        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
        devam_et =self.driver.find_element(By.XPATH,"//button[text()='Devam Et']")
        devam_et.click()
        _url = self.driver.current_url
        assert _url == "https://tobeto.com/e-posta-dogrulama?registerType=registerForm"
        giris_yap =self.driver.find_element(By.XPATH,"//a[@class='btn btn-success']")
        giris_yap.click()
        email_alani = self.driver.find_element(By.XPATH,"//input[@name='email']")
        email_alani.click()
        email_alani.send_keys("tobetotestmail002@gmail.com")
        password_alani = self.driver.find_element(By.XPATH,"//input[@name='password']")
        password_alani.click()
        password_alani.send_keys("Tobeto1234.")
        girisyap_button = self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        girisyap_button.click()
        
        
        
    #3 Kullanıcı Kayıt Olurken Bilgileri Değiştirme Kontrolü
    def test_InformationChangeControl(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.send_keys("Tobeto")
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.send_keys("Test")
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        password =self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.click()
        password.send_keys("Tobeto1234.")
        passwordAgain =self.driver.find_element(By.XPATH,"//input[@name='passwordAgain']")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")
        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()
        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        numara_alani =self.driver.find_element(By.XPATH,"//input[@name='phoneNumber']")
        numara_alani.click()
        numara_alani.send_keys("0505 123 45 67")
        closeButton =self.driver.find_element(By.XPATH,"//span[@class='alert-close']")
        closeButton.click()
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.clear()
        firstname.send_keys("Tobet")
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.clear()
        lastname.send_keys("Tes")
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.clear()
        email.send_keys("tobetotes@gmail.com")
        password =self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.click()
        password.clear()
        password.send_keys("Tobeto1234.")
        passwordAgain =self.driver.find_element(By.XPATH,"//input[@name='passwordAgain']")
        passwordAgain.click()
        passwordAgain.clear()
        passwordAgain.send_keys("Tobeto1234.")
        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        numara_alani =self.driver.find_element(By.XPATH,"//input[@name='phoneNumber']")
        numara_alani.click()
        input_value = numara_alani.get_attribute("value")
        assert input_value == ""
        sleep(3)
        
   

    #4 Arama izni alanının kontrolü 
    def test_PermitArea(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tobeto1234.")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("12")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
       
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla
        

        warning1 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/label[4]/small/p")))
        assert warning1.text == "En az 10 karakter girmelisiniz."
        permit_area.clear()

        permit_area.send_keys("1234567890126")  # 10 karakterden fazla karakter gir
        warning2 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/label[4]/small/p")))
        assert warning2.text == "En fazla 10 karakter girebilirsiniz."
        sleep(5)
        permit_area.clear()
        warning3 = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/label[4]/small/p")))
        assert warning3.text == "Doldurulması zorunlu alan*"
        sleep(5)
        self.driver.find_element(By.NAME, "phoneNumberCountry").click()
        self.driver.find_element(By.NAME, "phoneNumberCountry").find_element_by_xpath("//option[value()='Japonya']").click()  # Japonya'yı seç
        assert "Japonya" in self.driver.find_element(By.NAME, "phoneNumberCountry").get_attribute("value" in "+81")  
        #Beklenen sonuç: Ülke kodu telefon numarası başına otomatik eklenmelidir.



    #5 Geçersiz telefon numarasıyla kayıt olma 
    def test_InvalidPhone(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tobeto1234.")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("016784523404")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Geçersiz telefon numarası"
        sleep(3)
    
    #6 Kayıtlı e-posta ile kayıt olma kontrolü 
    def test_RegisterbyRegisteredEmail(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tobeto1234.")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("5316855008")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır."
        sleep(3)


    #7 Geçersiz şifre ile kayıt olma kontrolü
    def test_InvalidPassword(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail5@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tob")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tob")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("5316855008")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
       
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Şifreniz en az 6 karakterden oluşmalıdır."
        sleep(3)

    #8: Eşleşmeyen şifre ile kayıt olma kontrolü
    def test_MisMatchedPassword(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail56@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tob")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto123")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("5316855008")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
       
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• Şifreler eşleşmedi"
        sleep(3)

    #9: Birden fazla hata ile kayıt olma kontrolü 
    def test_MultipleErros(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.NAME, 'firstName')
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.NAME, "lastName")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.NAME, "email")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        
        password =self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys("Tob")
        
        passwordAgain =self.driver.find_element(By.NAME, "passwordAgain")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto123")

        registerButton =self.driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100 mt-6']")
        registerButton.click()
        sleep(3)
        announce = self.driver.find_element(By.XPATH,"//p[@class='alert-message mx-3']")
        assert announce.text == "Kayıt oluşturmak için gerekli sözleşmeler"
        acikRizaMetniButton= self.driver.find_element(By.XPATH,"//input[@name='contact']")
        acikRizaMetniButton.click()
        uyelikSozlesmesiButton =self.driver.find_element(By.XPATH,"//input[@name='membershipContrat']")
        uyelikSozlesmesiButton.click()
        email_izin =self.driver.find_element(By.XPATH,"//input[@name='emailConfirmation']")
        email_izin.click()

        arama_izin =self.driver.find_element(By.XPATH,"//input[@name='phoneConfirmation']")
        arama_izin.click()
        permit_area= self.driver.find_element(By.NAME, "phoneNumber")
        permit_area.click()
        permit_area.send_keys("5316855008")

        iframe= WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//iframe[@title='reCAPTCHA']")))
        self.driver.switch_to.frame(iframe)
        captcha=WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH,"//span[@id=\'recaptcha-anchor\']/div")))
        captcha.click()
        self.driver.switch_to.default_content()
       
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div/div/div[3]/button[2]""").click()  # "Devam Et" butonuna tıkla

        toast_locator = (By.CLASS_NAME, "toast-body")
        toast = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(toast_locator))
        assert toast.text == "• 2 errors occurred"
        sleep(3)

    #10 Geçersiz E-posta ile Başarısız Kullanıcı Kayıt Kontrolü
     
    def test_InvalidMail(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.send_keys("Tobeto")
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.send_keys("Test")
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.send_keys("tobetotestmailgmail.com")
        alert= self.driver.find_element(By.XPATH,"//p[text()='Geçersiz e-posta adresi*']")
        assert alert.text =="Geçersiz e-posta adresi*"

    #11 Kullanıcının doldurulması zorunlu alanlara veri yazıp silme işleminin kontrolü
    def test_Mandatory_field_to_be_filled(self):
        Test_Tobeto.test_Register(self)
        firstname = self.driver.find_element(By.XPATH,"//input[@name='firstName']")
        firstname.click()
        firstname.send_keys("Tobeto")
       
        lastname =self.driver.find_element(By.XPATH,"//input[@name='lastName']")
        lastname.click()
        lastname.send_keys("Test")
        
        email =self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.click()
        email.send_keys("tobetotestmail@gmail.com")
        
        password =self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.click()
        password.send_keys("Tobeto1234.")
        
        passwordAgain =self.driver.find_element(By.XPATH,"//input[@name='passwordAgain']")
        passwordAgain.click()
        passwordAgain.send_keys("Tobeto1234.")

        firstname.clear()
        lastname.clear()
        email.clear()
        password.clear()
        passwordAgain.clear()

        alert= self.driver.find_element(By.XPATH,"//p[text()='Doldurulması zorunlu alan*']")
        assert alert.text =="Doldurulması zorunlu alan*" 

        elements = self.driver.find_elements(By.XPATH, "/html/body/div[5]/div/div/div/div/div/label[4]/small/p")
        assert elements.text == "Doldurulması zorunlu alan*"
        element_count = len(elements)
        expected_count = 6  # Sayfadaki beklenen öğe sayısı
        assert element_count == expected_count





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
            
        
        