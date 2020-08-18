from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ddLine(unittest.TestCase): #Проверяем dd из таблицы среза

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
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-9.nv-noninteractive > path.nv-point.nv-point-1')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-9.nv-noninteractive > path.nv-point.nv-point-1')
        actions.move_to_element(clickPoint).context_click().perform()


    def ddLine_Pivot(self): #с линейной 2 марта, 1 год
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(6)').click()  # клик по pivot
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-759 > table > tbody > tr:nth-child(1) > th:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-759 > table > tbody > tr:nth-child(1) > th:nth-child(2)')
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-759 > table > tbody > tr:nth-child(1) > th:nth-child(1)').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-759 > table > tbody > tr:nth-child(1) > th:nth-child(2)').text
        result_district = self.driver.find_element_by_css_selector(
            '#slice-container-759 > table > thead > tr:nth-child(2) > th:nth-child(3)').text
        result_count = self.driver.find_element_by_css_selector(
            '#slice-container-759 > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddLine_Line'
        assert result_date == '2017-03-02 00:00:00', 'Упало при переходе из ddLine_Line'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddLine_Line'
        assert result_count == '551', 'Упало при переходе из ddLine_Line'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Table(self): #с линейной 2 марта, 1 год
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(7)').click()  # клик по table
        time.sleep(0.5)
        self.wait_by_css(
            "[data-grid='\[object Object\]']:nth-of-type(5) [title='1\,488\,412\,800\,000']")  # Ждем пока прогрузится диаграмма
        self.wait_by_css('[data-grid="\[object Object\]"]:nth-of-type(5) [title] .like-pre')
        result_age = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(5) [title] .like-pre').text
        result_date = self.driver.find_element_by_css_selector(
            "[data-grid='\[object Object\]']:nth-of-type(5) [title='1\,488\,412\,800\,000']").text
        result_district = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(5) [data-sort="Красногвардейский район"] .like-pre').text
        result_count = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(5) [title="551"]').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddLine_Table'
        assert result_date == '02.03.2017', 'Упало при переходе из ddLine_Table'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddLine_Table'
        assert result_count == '551', 'Упало при переходе из ddLine_Table'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Hist(self): #с линейной 2 марта, 1 год
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(9)').click()  # клик по hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '1,Красногвардейский район', 'Упало при переходе из ddLine_Hist'
        assert result_date == '2017-03-02 00:00:00', 'Упало при переходе из ddLine_Hist'
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Time_Hist(self): #с линейной 1 марта, 0 лет
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-9.nv-noninteractive > path.nv-point.nv-point-1')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-3.nv-noninteractive > path.nv-point.nv-point-0')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(10)').click()  # клик по time_hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text').text
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_age_district, result_date)
        assert result_age_district == '0, Красногвардейский...', 'Упало при переходе из ddLine_Time_Hist'
        assert result_date == 'Ср Март 1', 'Упало при переходе из ddLine_Time_Hist'
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Pie(self): #с линейной 1 марта, 0 лет
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-9.nv-noninteractive > path.nv-point.nv-point-1')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g.nv-group.nv-series-3.nv-noninteractive > path.nv-point.nv-point-0')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(8)').click()  # клик по line
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-759 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g > path')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по значениям
        print(result_date)
        assert result_date == '0,2017-03-01 00:00:00', 'Упало при переходе из ddLine_Pie'
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Speed(self): #с линейной 1 марта, 1 год
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(12)').click()  # клик по speed
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-759 > div > div:nth-child(2) > svg > g.arc > path:nth-child(3)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-759-legend > svg > g > g > g > g:nth-child(2) > text')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-759 > div > div:nth-child(2) > svg > g:nth-child(4) > text').text
        # Проверка значения по значениям
        print(result)
        assert result == '551 Единица измерения', 'Упало при переходе из ddLine_Speed'
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def ddLine_Directed(self): #с линейной 2 марта, 1 год
        self.ClickPoint()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(11)').click()  # клик по directed
        time.sleep(4.5)
        self.wait_by_css(
            '#slice-container-759 > svg > g:nth-child(4)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-759 > svg > g:nth-child(3)')
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g:nth-child(4) > text').text
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-759 > svg > g:nth-child(3) > text').text
        # Проверка значения по значениям
        print(result_age, result_date)
        assert result_age == '1', 'Упало при переходе из ddLine_Directed'
        assert result_date == 'Чт Март 2', 'Упало при переходе из ddLine_Directed'
        self.driver.find_element_by_css_selector('#controls_759 > a:nth-child(1) > i').click()

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddLine_Pivot()
        self.ddLine_Table()
        self.ddLine_Hist()
        self.ddLine_Time_Hist()
        self.ddLine_Pie()
        self.ddLine_Speed()
        self.ddLine_Directed()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()