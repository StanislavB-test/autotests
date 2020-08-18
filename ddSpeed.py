from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ddSpeed(unittest.TestCase): #Проверяем dd со спидометра

    def wait_by_css(self, element_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))
        return self

    def wait_by_xpath(self, element_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element_locator)))
        return self

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 5)

    def login(self):
        self.driver.get('http://ss.dev.bnvt.ru/')
        self.driver.find_element_by_css_selector("#username").send_keys("netrika")
        self.driver.find_element_by_css_selector("#password").send_keys("netrika")
        self.driver.find_element_by_css_selector("input.btn").click()
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/181')

    def ClickPoint(self):
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_by_css(
            '#slice-container-761 > div > div:nth-child(2) > svg > g.pointer')
        time.sleep(1.5) #чтоб стрелка поднялась
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-761 > div > div:nth-child(2) > svg > g.pointer')
        actions.move_to_element(clickPoint).context_click().perform()


    def ddSpeed_Pivot(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по pivot
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-761 > table > tbody > tr:nth-child(1) > th:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-761 > table > tbody > tr:nth-child(1) > th:nth-child(2)')
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-761 > table > tbody > tr:nth-child(1) > th:nth-child(1)').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > table > tbody > tr:nth-child(1) > th:nth-child(2)').text
        result_district = self.driver.find_element_by_css_selector(
            '#slice-container-761 > table > thead > tr:nth-child(2) > th:nth-child(3)').text
        result_count = self.driver.find_element_by_css_selector(
            '#slice-container-761 > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '0', 'Упало при переходе из ddSpeed_Pivot'
        assert result_date == '2017-03-01 00:00:00', 'Упало при переходе из ddSpeed_Pivot'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddSpeed_Pivot'
        assert result_count == '178', 'Упало при переходе из ddSpeed_Pivot'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Table(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(3)').click()  # клик по table
        time.sleep(0.5)
        self.wait_by_css(
            "[data-grid='\[object Object\]']:nth-of-type(7) .odd:nth-of-type(1) [title] .like-pre")  # Ждем пока прогрузится диаграмма
        self.wait_by_css("[data-grid='\[object Object\]']:nth-of-type(7) .odd:nth-of-type(1) [title='1\,488\,326\,400\,000']")
        result_age = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(7) .odd:nth-of-type(1) [title] .like-pre").text
        result_date = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(7) .odd:nth-of-type(1) [title='1\,488\,326\,400\,000']").text
        result_district = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(7) .odd:nth-of-type(1) [data-sort='Красногвардейский район'] .like-pre").text
        result_count = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(7) [title='1\,191']").text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '7', 'Упало при переходе из ddSpeed_Table'
        assert result_date == '01.03.2017', 'Упало при переходе из ddSpeed_Table'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddSpeed__Table'
        assert result_count == '1.19k', 'Упало при переходе из ddSpeed_Table'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Hist(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(5)').click()  # клик по hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '7,Красногвардейский район', 'Упало при переходе из ddSpeed_Hist'
        assert result_date == '2017-03-01 00:00:00', 'Упало при переходе из ddSpeed_Hist'
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Time_Hist(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(6)').click()  # клик по time_hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '7, Красногвардейский...', 'Упало при переходе из ddSpeed_Time_Hist'
        assert result_date == 'Ср Март 1', 'Упало при переходе из ddSpeed_Time_Hist'
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Pie(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по pie
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g > path')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_date)
        assert result_date == '7,2017-03-01 00:00:00', 'Упало при переходе из ddSpeed_Pie'
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Directed(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(7)').click()  # клик по directed
        time.sleep(3.5)
        self.wait_by_css(
            '#slice-container-761 > svg > g:nth-child(6) > circle')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-761 > svg > g:nth-child(7) > circle')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g:nth-child(7) > text').text
        result_age = self.driver.find_element_by_css_selector('#slice-container-761 > svg > g:nth-child(4) > text').text
        # Проверка значения по значениям
        print(result_date, result_age)
        assert result_date == 'Пт Март 3', 'Упало при переходе из ddSpeed_Directed'
        assert result_age == '1', 'Упало при переходе ddSpeed_Directed'
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def ddSpeed_Line(self): #со спидометра
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(8)').click()  # клик по line
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-groups > g.nv-group.nv-series-1')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-focus > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(2) > text').text
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-761 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text').text
        # Проверка значения по значениям
        print(result_age, result_date)
        assert result_age == '0, Красногвардейский...', 'Упало при переходе из ddSpeed_Line'
        assert result_date == 'Чт Март 2', 'Упало при переходе из ddSpeed_Line'
        self.driver.find_element_by_css_selector('#controls_761 > a:nth-child(1) > i').click()

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddSpeed_Pivot()
        self.ddSpeed_Table()
        self.ddSpeed_Hist()
        self.ddSpeed_Time_Hist()
        self.ddSpeed_Pie()
        self.ddSpeed_Directed()
        self.ddSpeed_Line()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()