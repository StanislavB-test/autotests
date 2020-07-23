from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ddTable(unittest.TestCase): #Проверяем иерархию из круговой и гистограммы. Различные наборы

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

    def ddTable_Pivot(self): #table_dd; Переход по 1.19к
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector('.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по pivot
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > table > tbody > tr:nth-child(1) > th:nth-child(2)') #Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-754 > table > tbody > tr:nth-child(1) > td:nth-child(3)')
        result = self.driver.find_element_by_css_selector('#slice-container-754 > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
        #Проверка значения по шапке
        print(result)
        assert result == '1.19k', 'Упало при переходе из ddTable_Pivot'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_Hist(self): #table_dd; Переход по 1.19к
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(3)').click()  # клик по hist
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect')
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        resultDate = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        resultText = self.driver.find_element_by_css_selector('#slice-container-754 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        print(resultDate)
        print(resultText)
        assert resultDate == '2017-03-01 00:00:00', 'Упало при переходе из ddTable_Hist'  # проверка появившегося поля
        assert resultText == '7,Красногвардейский район', 'Упало при переходе из ddTable_Hist'
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_Pie(self): #table_dd; Переход по 1.19к
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по pid
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-pieWrap.nvd3-svg > g > g > g.nv-pie > g')
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        print(result)
        assert result == '7,2017-03-01 00:00:00', 'Упало при переходе из ddTable_Hist'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_Line(self): #table_dd; Переход по 1.19к
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(5)').click()  # клик по line
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-focus > g.nv-linesWrap.nvd3-svg > g > g > g.nv-scatterWrap.nvd3-svg > g > g:nth-child(2) > g.nv-groups > g')
        resultText = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        resultDate = self.driver.find_element_by_css_selector('#slice-container-754 > svg > g > g > g.nv-focus > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        print(resultText)
        print(resultDate)
        assert resultText == '7, Красногвардейский...', 'Упало при переходе из ddTable_Hist'  # проверка появившегося поля
        assert resultDate == 'Ср Март 1', 'Упало при переходе из ddTable_Hist'
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_Directed(self):
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(6)').click()  # клик по directed
        time.sleep(4) #графу побеситься
        self.wait_by_css('#slice-container-754 > svg > g:nth-child(3)')
        self.wait_by_css(
            '#slice-container-754 > svg > g:nth-child(4)')
        resultText = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g:nth-child(3) > text').text
        resultDate = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g:nth-child(4) > text').text
        print(resultText)
        print(resultDate)
        assert resultText == '7', 'Упало при переходе из ddTable_Hist'  # проверка появившегося поля
        assert resultDate == 'Ср Март 1', 'Упало при переходе из ddTable_Hist'
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_Speed(self):
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(7)').click()  # клик по speed
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > div > div:nth-child(2) > svg > g.pointer')
        self.wait_by_css(
            '#slice-container-754 > div > div:nth-child(2) > svg > g.arc > path:nth-child(3)')
        result = self.driver.find_element_by_css_selector(
            '#slice-container-754 > div > div:nth-child(2) > svg > g:nth-child(4) > text').text
        print(result)
        assert result == '1.19k Единица измерения', 'Упало при переходе из ddTable_Speed'  # проверка появившегося поля
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def ddTable_TimeHist(self):
        self.wait_by_css('#slice-container-762 > div > div > div:nth-child(2) > div > div')
        self.wait_by_css('tr:nth-of-type(1) > td:nth-of-type(3) > .like-pre')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector('td[title="1,191"]')
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(8)').click()  # клик по time_hist
        time.sleep(0.5)
        self.wait_by_css('#slice-container-754 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g')
        self.wait_by_css(
            '#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text')
        resultText = self.driver.find_element_by_css_selector(
            '#slice-container-754 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g > text').text
        resultDate = self.driver.find_element_by_css_selector('#slice-container-754 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g > text').text
        print(resultText)
        print(resultDate)
        assert resultText == '7, Красногвардейский...', 'Упало при переходе из ddTable_TimeHist'  # проверка появившегося поля
        assert resultDate == 'Ср Март 1', 'Упало при переходе из ddTable_TimeHist'
        self.driver.find_element_by_css_selector('#controls_754 > a:nth-child(1) > i').click()

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.ddTable_Pivot()
        self.ddTable_Hist()
        self.ddTable_Pie()
        self.ddTable_Line()
        self.ddTable_Directed()
        self.ddTable_Speed()
        self.ddTable_TimeHist()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()