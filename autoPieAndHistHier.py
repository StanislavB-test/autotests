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

    def hierPie1(self):
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
        # case_patient_gender в среза



    def test_case(self):
        self.setup()
        self.login()



if __name__ == '__main__':
    unittest.main()