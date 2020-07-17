from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PivotAndTableHier(unittest.TestCase): #Проверяем иерархию из шапки и значений таблицы и таблицы среза

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
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/169')

    def hierPivot1(self):
        # case_district_name в среза
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(3) > th:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                              'table > thead > tr:nth-child(3) > th:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(3) > th:nth-child(2)')
        result = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                          'table > thead > tr:nth-child(3) > th:nth-child(2)').text
        print(result)
        assert result == 'case_organization_level1_short_name', 'Упало при переходе из шапки hierPivot1'  # проверка появившегося поля
        #case_patient_gender в среза

    def hierPivot2(self):
        #case_patient_gender
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(2) > th:nth-child(2)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                              'table > thead > tr:nth-child(2) > th:nth-child(2)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector('.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(3) > th:nth-child(2)')
        result = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                          'table > thead > tr:nth-child(3) > th:nth-child(2)').text
        print(result)
        assert result == 'возраст кат 1', 'Упало при переходе из шапки hierPivot2' #проверка появившегося поля

    def hierPivot3(self):
        actions = webdriver.ActionChains(self.driver)
        # 10+ female в среза
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(3) > th:nth-child(5)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                              'table > thead > tr:nth-child(3) > th:nth-child(5)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector('.d3-context-menu > ul:nth-child(1) > li:nth-child(3)').click()  # клик по меню
        self.wait_by_css('#slice-container-698 > table > thead > tr:nth-child(3) > th:nth-child(3)')
        result = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                          'table > thead > tr:nth-child(3) > th:nth-child(3)').text
        result1 = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                           'table > thead > tr:nth-child(4) > th:nth-child(2)').text
        print(result)
        assert result == '10+', 'Упало при переходе из значения показателя hierPivot3'  # проверка появившегося поля
        assert result1 == 'case_patient_age', 'Упало при переходе из значения показателя hierPivot3'

    def hierPivot4(self):
        actions = webdriver.ActionChains(self.driver)
        # следуюущий переход по иерархии
        # ГП №28 в среза
        self.wait_by_css('#slice-container-698 > table > tbody > tr:nth-child(2) > th')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                              'table > tbody > tr:nth-child(2) > th')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector('.d3-context-menu > ul:nth-child(1) > li:nth-child(3)').click()  # клик по меню
        self.wait_by_css('#slice-container-698 > table > tbody > tr:nth-child(1) > th:nth-child(3)')
        result = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                          'table > tbody > tr:nth-child(1) > th:nth-child(3)').text
        result1 = self.driver.find_element_by_css_selector('#slice-container-698 > '
                                                           'table > thead > tr:nth-child(5) > th:nth-child(3)').text
        print(result)
        assert result == 'ГП №28 ПО №28', 'Упало при переходе из значения показателя hierPivot4'  # проверка появившегося поля
        assert result1 == 'case_organization_level2_short_name', 'Упало при переходе из значения показателя hierPivot4'

    def hierTable1(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        actions = webdriver.ActionChains(self.driver)
        # следуюущий переход по иерархии
        # case_district_name в таблице
        self.wait_by_css('.dataTables_scrollHeadInner .sorting:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('.dataTables_scrollHeadInner .sorting:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по первому пункту меню
        self.wait_by_css('.dataTables_scrollHeadInner .sorting:nth-child(2)')
        result = self.driver.find_element_by_css_selector('.dataTables_scrollHeadInner .sorting:nth-child(2)').text
        print(result)
        assert result == 'case_organization_level1_short_name', 'Упало при переходе из значения hierTable1'  # проверка появившегося поля

    def hierTable2(self):
        actions = webdriver.ActionChains(self.driver)
        # следуюущий переход по иерархии
        # female в таблице, Красногвардейский, ДГП 68
        self.wait_by_css('tr.odd:nth-child(3) > td:nth-child(3) > span:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('tr.odd:nth-child(3) > '
                                                              'td:nth-child(3) > span:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по первому пункту меню
        self.wait_by_css('tr.odd:nth-child(3) > td:nth-child(4) > span:nth-child(1)')
        result1 = self.driver.find_element_by_css_selector('tr.odd:nth-child(3) '
                                                           '> td:nth-child(4) > span:nth-child(1)').text
        result2 = self.driver.find_element_by_css_selector('tr.odd:nth-child(3) '
                                                           '> td:nth-child(3) > span:nth-child(1)').text
        print(result1)
        assert result1 == '30+', 'Упало при переходе из значения показателя hierTable2'
        assert result2 == 'female', 'Упало при переходе из значения показателя hierTable2'

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.hierPivot1()
        self.hierPivot2()
        self.hierPivot3()
        self.hierPivot4()
        self.hierTable1()
        self.hierTable2()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()
