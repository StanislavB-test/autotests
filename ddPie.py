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

    def ddPie_Table(self): #со среза на таблицу; Переход по 703, ДГП №68, 1 год, 2017-03-01
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_by_css('#slice-container-757 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(2)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-757 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(2)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(5)').click()  # клик по pivot
        time.sleep(0.5)
        self.wait_by_css(
            '#DataTables_Table_3 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css('#DataTables_Table_3 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
        result_age = self.driver.find_element_by_css_selector(
            '#DataTables_Table_3 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)]').text
        result_date = self.driver.find_element_by_css_selector(
            '#DataTables_Table_3 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)').text
        result_district = self.driver.find_element_by_css_selector(
            '#slice-container-757 > table > thead > tr:nth-child(2) > th:nth-child(3)').text
        result_count = self.driver.find_element_by_css_selector(
            '#slice-container-757 > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
        # Проверка значения по значениям
        print(result_age, result_date, result_district, result_count)
        assert result_age == '1', 'Упало при переходе из ddPivot_Table'
        assert result_date == '2017-03-01 00:00:00', 'Упало при переходе из ddPivot_Table'
        assert result_district == 'Выборгский район', 'Упало при переходе из ddPivot_Table'
        assert result_count == '25', 'Упало при переходе из ddPivot_Table'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_755 > a:nth-child(1) > i').click()







    #def tearDown(self):
        #self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddPie_Table()

        #self.tearDown()


if __name__ == '__main__':
    unittest.main()