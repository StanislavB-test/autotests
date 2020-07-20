from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class DirectedHierAndDD(unittest.TestCase): #Проверяем иерархию из шапки и значений таблицы и таблицы среза

    def wait_by_css(self, element_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_locator)))
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
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/179')

    def hierDirected1(self):
        # 0+ в графе
        time.sleep(4) #оставил специально, чтобы граф "пробесился"
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(4) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        time.sleep(0.5)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(4) > circle')
        result = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(5) > text').text
        print(result)
        assert result == '2', 'Упало при переходе из hierDirected1'  # проверка появившегося поля

    def hierDirected2(self):
        #Красногвардейский район в графе
        time.sleep(4)  # оставил специально, чтобы граф "пробесился"
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(9) > circle')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(9) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        time.sleep(0.5)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(13) > circle')
        result = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > text').text
        print(result)
        assert result == 'ДГП №68', 'Упало при переходе из hierDirected2'  # проверка появившегося поля

    def ddDirected2(self):
        #Красногвардейский район в графе
        time.sleep(4)
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-740 > svg > g:nth-child(13) > circle')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-740 > svg > g:nth-child(13) > circle')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu ul li:nth-of-type(4)').click()  # клик по меню
        time.sleep(0.5)
        self.wait_by_css('div:nth-of-type(1) > .slice-cell .slice_container.table '
                         '> .dataTables_wrapper.dt-bootstrap.form-inline.no-footer .dataTables_scrollBody '
                         '> table[role="grid"] > tbody > tr:nth-of-type(1) > td:nth-of-type(1) > .like-pre')
        result = self.driver.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table '
                                                          '> .dataTables_wrapper.dt-bootstrap.form-inline.no-footer .'
                                                          'dataTables_scrollBody > table[role="grid"] > tbody > '
                                                          'tr:nth-of-type(1) > td:nth-of-type(1) > .like-pre').text
        result1 = self.driver.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                           '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                           '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                            'tr:nth-of-type(2) > td:nth-of-type(2) > .like-pre').text
        result2 = self.driver.find_element_by_css_selector('div:nth-of-type(1) > .slice-cell .slice_container.table > '
                                                           '.dataTables_wrapper.dt-bootstrap.form-inline.no-footer '
                                                           '.dataTables_scrollBody > table[role="grid"] > tbody > '
                                                           'tr:nth-of-type(3) > td[title="3"] > .like-pre').text
        print(result)
        assert result == 'Красногвардейский район', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result1 == 'ДГП №68', 'Упало при переходе из hierDirected1'  # проверка появившегося поля
        assert result2 == '3', 'Упало при переходе из hierDirected1'  # проверка появившегося поля

    def tearDown(self):
        self.driver.quit()



    def test_case(self):
        self.setup()
        self.login()
        self.hierDirected1()
        self.hierDirected2()
        self.ddDirected2()
        self.tearDown()



if __name__ == '__main__':
    unittest.main()