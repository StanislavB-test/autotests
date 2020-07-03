from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PivotAndTableHier(unittest.TestCase): #Проверяем иерархию из круговой и гистограммы. Различные наборы

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
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/178')

    def hierPie1(self):
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-746 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > '
                         'g:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-746 > svg > g > g > '
                                                              'g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > '
                                                              'g:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css('#slice-container-746 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(1)') #Ждем пока прогрузится диаграмма
        result = self.driver.find_element_by_css_selector('#slice-container-746 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > g:nth-child(2) > text:nth-child(2)').text
        #Проверка значения по шапке
        print(result)
        assert result == 'Невский район,ГП №100', 'Упало при переходе из hierPie1'  # проверка появившегося поля

    def hierPie2(self):
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-746 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-746 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css(
            '#slice-container-746 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(2)')  # Ждем пока прогрузится диаграмма
        result = self.driver.find_element_by_css_selector(
            '#slice-container-746 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(2) > text').text
        # Проверка значения по шапке
        print(result)
        assert result == 'Невский район,ГП №8,ГП №8 ДПО №33', 'Упало при переходе из hierPie2'  # проверка появившегося поля

    def hierPie3(self):
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css(
            '#slice-container-747 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-747 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(1)')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню
        self.wait_by_css(
            '#slice-container-747 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g:nth-child(2)')  # Ждем пока прогрузится диаграмма
        result = self.driver.find_element_by_css_selector(
            '#slice-container-747 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text').text
        # Проверка значения по шапке
        print(result)
        assert result == 'Невский район,female,ГП №8', 'Упало при переходе из hierPie2'  # проверка появившегося поля

    def test_case(self):
        self.setup()
        self.login()
        self.hierPie1()
        self.hierPie2()
        self.hierPie3()



if __name__ == '__main__':
    unittest.main()