from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ddPivot(unittest.TestCase): #Проверяем dd из таблицы среза

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

    def ddPivot_Table(self): #со среза на таблицу; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по table
        time.sleep(0.5)
        self.wait_by_css(
            '[data-grid="\[object Object\]"]:nth-of-type(2) [data-sort="Красногвардейский район"]')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('[data-grid="\[object Object\]"]:nth-of-type(2) [role] [tabindex="0"]:nth-of-type(1)')
        result_age = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(2) [title] .like-pre').text
        result_date = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(2) [title="1\,488\,326\,400\,000"]').text
        result_district = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(2) [data-sort="Красногвардейский район"] .like-pre').text
        result_count = self.driver.find_element_by_css_selector(
            '[data-grid="\[object Object\]"]:nth-of-type(2) [title="703"]').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddPivot_Table'
        assert result_date == '01.03.2017', 'Упало при переходе из ddPivot_Table'
        assert result_district == 'Красногвардейский район', 'Упало при переходе из ddPivot_Table'
        assert result_count == '703', 'Упало при переходе из ddPivot_Table'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Pie(self): #со среза на круговую; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)') #ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(3)').click()  # клик по pie
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-755 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по шапке
        print(result)
        assert result == '1,2017-03-01 00:00:00', 'Упало из ddPivot_Pie'
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Line(self): #cо среза на линейную; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')  # ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по line
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-755 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        result_date = self.driver.find_element_by_css_selector('#slice-container-755 > svg > g > g > g.nv-focus > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        # Проверка значения по шапке
        print(result_age_district)
        print(result_date)
        assert result_age_district == '1, Красногвардейский...', 'Упало из ddPivot_Line'
        assert result_date == 'Ср Март 1', 'Упало из ddPivot_Line'
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Hist(self): #переход со среза на гистограмму; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')  # ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(5)').click()  # клик по hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-755 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        # Проверка значения по шапке
        print(result_age_district)
        print(result_date)
        assert result_age_district == '1,Красногвардейский район', 'Упало из ddPivot_Line'
        assert result_date == '2017-03-01 00:00:00', 'Упало из ddPivot_Line'
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Time_Hist(self): #переход со среза на временную гистограмму; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')  # ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(6)').click()  # клик по time_hist
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-755 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result_age_district = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        # Проверка значения по шапке
        print(result_age_district)
        print(result_date)
        assert result_age_district == '1, Красногвардейский...', 'Упало из ddPivot_Time_Hist'
        assert result_date == 'Ср Март 1', 'Упало из ddPivot_Hist'
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Directed(self): #переход со среза на граф; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')  # ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(7)').click()  # клик по directed
        time.sleep(4.5)
        self.wait_by_css(
            '#slice-container-755 > svg > g:nth-child(4)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-755 > svg > g:nth-child(3)')
        result_age = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g:nth-child(3) > text').text
        result_date = self.driver.find_element_by_css_selector(
            '#slice-container-755 > svg > g:nth-child(4) > text').text
        # Проверка значения по шапке
        print(result_age)
        print(result_date)
        assert result_age == '1', 'Упало из ddPivot_Time_Hist'
        assert result_date == 'Ср Март 1', 'Упало из ddPivot_Hist'
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def ddPivot_Speed(self):
        # переход со среза на граф; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-755 > table > tbody > tr:nth-child(16) > td:nth-child(8)')  # ПКМ по точке перехода
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(8)').click()  # клик по speed
        time.sleep(0.5)
        self.wait_by_css('#slice-container-755 > div > div:nth-child(2) > svg > g.pointer')
        self.wait_by_css(
            '#slice-container-755 > div > div:nth-child(2) > svg > g.arc > path:nth-child(3)')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-755 > div > div:nth-child(2) > svg > g:nth-child(4) > text').text
        print(result)
        assert result == '703 Единица измерения', 'Упало при переходе из ddTable_Speed'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddPivot_Table()
        self.ddPivot_Pie()
        self.ddPivot_Line()
        self.ddPivot_Hist()
        self.ddPivot_Time_Hist()
        self.ddPivot_Directed()
        self.ddPivot_Speed()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()