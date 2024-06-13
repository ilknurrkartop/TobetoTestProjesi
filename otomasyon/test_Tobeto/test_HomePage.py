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

class Test_HomePage:
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

    def Open_My_Training(self):
        Test_Tobeto.test_SuccessLogin(self)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)
        dene= self.driver.find_element(By.XPATH, "//button[@id='lessons-tab']")
        dene.click()
        divs = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div")))
        div_count = len(divs)
        assert div_count == 4
        self.driver.execute_script("window.scrollTo(0,500)")
        showMore = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='showMoreBtn']")))
        showMore.click()
        sleep(2)
        
        myTrainings = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row']/span")))
        assert myTrainings.text == "Eğitimlerim"
        current_page = self.driver.current_url
        assert current_page == "https://tobeto.com/egitimlerim"
        sleep(2)

    def Open_My_News(self):
        Test_Tobeto.test_SuccessLogin(self)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)
        news= self.driver.find_element(By.XPATH, "//button[@id='notification-tab']")
        news.click()

        divs = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='notification-tab-pane']/div/div[@class='col-md-4 col-12 my-4']")))
        div_count = len(divs)
        assert div_count == 3

        self.driver.execute_script("window.scrollTo(0,500)")
        showMore = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='notification-tab-pane']/div/div[4]")))
        showMore.click()
        sleep(2)

        news_Title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='container']/div/span")))
        assert news_Title.text == "Duyurularım"
        current_page = self.driver.current_url
        assert current_page == "https://tobeto.com/duyurular"

    def test_MyTraining_Filter(self):
        Test_HomePage.Open_My_Training(self)
        sleep(2)
        dropdown = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='row']/div[3]/div[@class=' css-b62m3t-container']/div/div[2]")))
        dropdown.click()
        sleep(1)
        
        new_to_old = self.driver.find_element(By.XPATH, "//div[@class='select__single-value css-1dimb5e-singleValue']")
        new_to_old.click()
        sleep(2)
        trainings = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div")))
        dates = []
        for training in trainings:
            date_element = training.find_element(By.XPATH, "./div/div/div/span[2]").text
            dates.append(date_element)

        sleep(2)
        sorted_dates = sorted(dates) #büyükten küçüğe sırala
        assert dates == sorted_dates, "Tarihler küçükten büyüğe doğru sıralanmamış."

    def test_MyTraining_Going_On_Filter(self):
        Test_HomePage.Open_My_Training(self)
        sleep(2)
        all_List = []

        trainings = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div")))
        for training in trainings:
            date_element = training.find_element(By.XPATH, "./div/div/div/span[1]").text
            all_List.append(date_element)
        for date in all_List:
            print(date)
        # Devam edenler filtresine geçiş yap
        going_on = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='started-tab']")))
        going_on.click()
        sleep(5)
        # Devam edenler listesi ayrı bir diziye kaydedilir.
        self.driver.execute_script("window.scrollTo(0,500)")
        going_On_List = []
        going_On_trainings = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='done-lessons-tab-pane']/div/div")))
        for training in going_On_trainings:
            date_element = training.find_element(By.XPATH, "./div/div/div/span[1]").text
            going_On_List.append(date_element)
        for less in going_On_List:
            print(less)
        # Tamamlananlar filtresine geçiş yap
        compleated = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@id='done-lessons-tab']")))
        compleated.click()

        # Tamamlananlar ayrı bir diziye kaydedilir.
        compleated_List = []
        trainings = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div")))
        for training in trainings:
            date_element = training.find_element(By.XPATH, "./div/div/div/span[1]").text
            compleated_List.append(date_element)

        # Devam edenler listesi ve tamamlananlar listesi farklı mı kontrol edilir
        assert going_On_List != compleated_List ,"Filtreler uygulanamadı"

    def test_MyTrainings(self):
        Test_HomePage.Open_My_Training(self)
        self.driver.execute_script("window.scrollTo(0,500)")
        training_Name = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div[1]/div/div/div/span")))
        sleep(1)
        go_Training = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='all-lessons-tab-pane']/div/div[1]/div/div/a")))
        go_Training.click()
        sleep(8)     
        detail_Page_Training_Name = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//div[@class='activity-info']/h3")))
        # assert training_Name.text == detail_Page_Training_Name.text

        detail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='ant-btn ant-btn-default ant-btn-lg ant-btn-block btn']")))
        detail.click()
        detail_Title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='course-new-content']/div/div[2]/h3")))
        # assert detail_Title.text == training_Name.text
        close_Detail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//a[@class='sg-icon sg-delete close']")))
        close_Detail.click()

        about = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='rc-tabs-0-tab-about']/div/span")))
        about.click()
        about_Info = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@class='info-section']/div/div/strong")))
        assert about_Info[0].text == "Başlangıç"
        assert about_Info[1].text == "Bitiş"

    def test_News_Filtering(self):
        Test_HomePage.Open_My_News(self)
        sleep(2)
        news_List = []
        news = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//main/div[2]/div[2]/div")))
        for new in news:
            element = new.find_element(By.XPATH, "./div/div/span").text
            news_List.append(element)
        filter_button = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='read-hide']")))

        filter_button.click()
        sleep(2)
        filter_List = []
        news = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//main/div[2]/div[2]/div")))
        for new in news:
            element = new.find_element(By.XPATH, "./div/div/span").text
            filter_List.append(element)
        assert news_List != filter_List, "Filtreleme işlemi başarısız!"

    def test_MyAnnouncementAndNews(self):
        Test_HomePage.Open_My_News(self)

        news_Detail = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//main/div[2]/div[2]/div[1]/div/div[2]/span[2]")))
        news_Detail.click()
        sleep(2)

        pop_up = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='modal-dialog modal-lg modal-fullscreen-sm-down']")))
        assert pop_up is not None, "Popup element not found on the page"

    def test_SurveyPage(self):
        Test_Tobeto.test_SuccessLogin(self)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)
        survey= self.driver.find_element(By.XPATH, "//button[@id='mySurvey-tab']")
        survey.click()
        sleep(2)

        self.driver.execute_script("window.scrollTo(0,500)")
        no_data = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class=' noDataCard']")))
        assert no_data is not None, "not found on the page"

    def test_MyExam(self):
        Test_Tobeto.test_SuccessLogin(self)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(3)

        exam_Title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='exam-header']/span[1]")))
        title_text = exam_Title.text
        assert "Sınav" in title_text, "Sınav kelimesi elementin metninde bulunamadı."
        exam_Title.click()
        sleep(2)

        pop_up = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='modal-dialog modal-xl modal-dialog-centered modal-fullscreen-sm-down']")))
        assert pop_up is not None, "Popup element not found on the page"
        report = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary mt-8 ms-auto me-auto']")))
        report.click()
        sleep(2)

        result_items = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@class='result-items']/span")))
        first_item = result_items[0].find_element(By.TAG_NAME, 'a').text
        assert "Doğru" in first_item, "İlk elemanın içinde 'Doğru' kelimesi bulunamadı."

        second_item = result_items[1].find_element(By.TAG_NAME, 'a').text
        assert "Yanlış" in second_item, "İkinci elemanın içinde 'Yanlış' kelimesi bulunamadı."

        third_item = result_items[2].find_element(By.TAG_NAME, 'a').text
        assert "Boş" in third_item, "Üçüncü elemanın içinde 'Boş' kelimesi bulunamadı."
        
        fourth_item = result_items[3].find_element(By.TAG_NAME, 'a').text
        assert "Puan" in fourth_item, "Dördüncü elemanın içinde 'Puan' kelimesi bulunamadı."

    def test_AreaControl(self):
        Test_Tobeto.test_SuccessLogin(self)
        self.driver.execute_script("window.scrollTo(0,700)")
        sleep(3)

        cards = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.XPATH, "//div[@class='new-packs my-10']/div")))
        first_item = cards[0].find_element(By.XPATH, ".//div/h1").text
        assert "Profilini oluştur" in first_item, "İlk elemanın içinde 'Profilini oluştur' kelimesi bulunamadı."

        second_item = cards[1].find_element(By.XPATH, ".//div/h1").text
        assert "Kendini değerlendir" in second_item, "İlk elemanın içinde 'Kendini değerlendir' kelimesi bulunamadı."

        third_item = cards[2].find_element(By.XPATH, ".//div/h1").text
        assert "Öğrenmeye başla" in third_item, "İlk elemanın içinde 'Öğrenmeye başla' kelimesi bulunamadı."