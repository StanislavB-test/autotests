from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ddDirected(unittest.TestCase): #Проверяем dd с графа

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
            '#slice-container-760 > svg > g:nth-child(4) > circle')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g:nth-child(4) > circle')
        time.sleep(4)
        actions.move_to_element(clickPoint).context_click().perform()


    def ddDirected_Pivot(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(6)').click()  # клик по pivot
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-760 > table > tbody > tr:nth-child(1) > th:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-760 > table > tbody > tr:nth-child(1) > th:nth-child(2)')
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-760 > table > tbody > tr:nth-child(1) > th:nth-child(1)').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-760 > table > tbody > tr:nth-child(1) > th:nth-child(2)').text
        result_district = self.driver.find_element_by_css_selector(
            '#slice-container-760 > table > thead > tr:nth-child(2) > th:nth-child(3)').text
        result_count = self.driver.find_element_by_css_selector(
            '#slice-container-760 > table > tbody > tr:nth-child(11) > td:nth-child(2)').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddDirected_Pivot'
        assert result_date == '2017-03-01 00:00:00', 'Упало при переходе из ddDirected_Pivot'
        assert result_district == 'Выборгский район', 'Упало при переходе из ddDirected_Pivot'
        assert result_count == '58.0', 'Упало при переходе из ddDirected_Pivot'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Table(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(7)').click()  # клик по table
        time.sleep(0.5)
        self.wait_by_css(
            "[data-grid='\[object Object\]']:nth-of-type(6) .odd:nth-of-type(1) [title] .like-pre")  # Ждем пока прогрузится диаграмма
        self.wait_by_css("[data-grid='\[object Object\]']:nth-of-type(6) .odd:nth-of-type(1) [title='1\,488\,326\,400\,000']")
        result_age = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(6) .odd:nth-of-type(1) [title] .like-pre").text
        result_date = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(6) .odd:nth-of-type(1) [title='1\,488\,326\,400\,000']").text
        result_district = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(6) .odd:nth-of-type(1) [data-sort='Красногвардейский район'] .like-pre").text
        result_count = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(6) [title='703']").text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddPie_Table'
        assert result_date == '01.03.2017', 'Упало при переходе из ddPie_Table'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddDirected_Table'
        assert result_count == '703', 'Упало при переходе из ddDirected_Table'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Hist(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(9)').click()  # клик по hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '1,Красногвардейский район', 'Упало при переходе из ddDirected_Hist'
        assert result_date == '2017-03-01 00:00:00', 'Упало при переходе из ddDirected_Hist'
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Time_Hist(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(10)').click()  # клик по time_hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '1, Красногвардейский...', 'Упало при переходе из ddDirected_Time_Hist'
        assert result_date == 'Ср Март 1', 'Упало при переходе из ddDirected_Time_Hist'
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Pie(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(8)').click()  # клик по line
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g > path')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_date)
        assert result_date == '1,2017-03-01 00:00:00', 'Упало при переходе из ddDirected_Line'
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Speed(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(11)').click()  # клик по speed
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-760 > div > div:nth-child(2) > svg > g.arc > path:nth-child(3)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-760-legend > svg > g > g > g > g:nth-child(2) > text')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-760 > div > div:nth-child(2) > svg > g:nth-child(4) > text').text
        # Проверка значения по значениям
        print(result)
        assert result == '1.40k Единица измерения', 'Упало при переходе из ddDirected_Speed'
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def ddDirected_Line(self):
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(12)').click()  # клик по directed
        time.sleep(4.5)
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-focus > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(2) > text')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(4) > text')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-focus > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(2) > text').text
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-760 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(4) > text').text
        # Проверка значения по значениям
        print(result_age, result_date)
        assert result_age == '1, Красногвардейский...', 'Упало при переходе из dddDirected_Directed'
        assert result_date == 'Чт Март 2', 'Упало при переходе из ddDirected_Directed'
        self.driver.find_element_by_css_selector('#controls_760 > a:nth-child(1) > i').click()

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddDirected_Pivot()
        self.ddDirected_Table()
        self.ddDirected_Hist()
        self.ddDirected_Time_Hist()
        self.ddDirected_Pie()
        self.ddDirected_Speed()
        self.ddDirected_Line()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()