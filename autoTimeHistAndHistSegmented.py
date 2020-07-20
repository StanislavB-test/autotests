from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



class TimeHistAndHistSegmented(unittest.TestCase): #Проверяем иерархию из круговой и гистограммы. Различные наборы

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
        self.driver.get('http://ss.dev.bnvt.ru/superset/dashboard/180')

    def hierTimeHist1(self): #autoTimeHist1
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-692 > div > div > div:nth-child(3) > div')
        self.wait_by_css('#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector('#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css('#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-1 > rect') #Ждем пока прогрузится диаграмма
        self.wait_by_css('#slice-container-753 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text')

    def hierTimeHist2(self):  # autoTimeHist1
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-1 > rect')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text')

    def hierTimeHist3(self):  # autoTimeHist1
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-692 > div > div > div:nth-child(3) > div')
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-1 > rect')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-legendWrap.nvd3-svg > g > g > g:nth-child(1) > text')

    def hierTimeHist4(self):  # autoTimeHist1
        actions = webdriver.ActionChains(self.driver)
        self.wait_by_css('#slice-container-692 > div > div > div:nth-child(3) > div')
        self.wait_by_css(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-753 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-0 > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-753 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-753 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(4) > g:nth-child(1) > g:nth-child(1) > g:nth-child(1) > text:nth-child(2)')
        self.driver.find_element_by_css_selector('#controls_753 > a.exploreChart > i').click()

    def hierTimeHist5(self): # autoTimeHist1
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_by_css('#slice-header > div > div > button')
        self.driver.find_element_by_css_selector('#slice-header > div > div > button').click()
        self.wait_by_css('.modal-lg > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)')
        district = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(22)').text
        print(district)
        gender = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(25)').text
        print(gender)
        age_bucket = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(28)').text
        print(age_bucket)
        age = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(31)').text
        print(age)
        mo_lvl1 = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(34)').text
        print(mo_lvl1)
        assert district == "'невский район'", 'Упало с временной гистограммы'
        assert gender == "'female'", 'Упало с временной гистограммы'
        assert age_bucket == "'60+'", 'Упало с временной гистограммы'
        assert age == "'63'", 'Упало с временной гистограммы'
        assert mo_lvl1 == "'гп №94'", 'Упало с временной гистограммы'
        self.driver.switch_to.window(self.driver.window_handles[0])

    def hierHistSegmented1(self): # autoHist3
        self.wait_by_css('#slice-container-692 > div > div > div:nth-child(3) > div')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-1 > rect:nth-child(1)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g.nv-group.nv-series-1 > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text')

    def hierHistSegmented2(self): # autoHist3
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(4)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-barsWrap.nvd3-svg > g > g > g > g > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.wait_by_css(
            '#slice-container-750 > svg > g > g > g.nv-x.nv-axis.nvd3-svg > g > g > g:nth-child(1) > text')

    def hierHistSegmented3(self): # autoHist3
        self.wait_by_css(
            '#slice-container-750 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > rect:nth-child(1)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-750 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)

    def hierHistSegmented4(self): # autoHist3
        self.wait_by_css(
            '#slice-container-750 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > rect:nth-child(1)')
        actions = webdriver.ActionChains(self.driver)
        clickPoint = self.driver.find_element_by_css_selector(
            '#slice-container-750 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > rect:nth-child(1)')
        time.sleep(0.5)
        actions.move_to_element(clickPoint).context_click().perform()
        self.driver.find_element_by_css_selector(
            '.d3-context-menu > ul:nth-child(1) > li:nth-child(2)').click()  # клик по меню 2=1 пункт, 4 = 2 пункт
        time.sleep(0.5)
        self.wait_by_css(
            '#slice-container-750 > svg:nth-child(1) > g:nth-child(1) > g:nth-child(1) > g:nth-child(3) > g:nth-child(1) > g:nth-child(2) > g:nth-child(1) > g:nth-child(1) > rect:nth-child(1)')  # Ждем пока прогрузится диаграмма
        self.driver.find_element_by_css_selector('#controls_750 > a.exploreChart > i').click()

    def hierHistSegmented5(self): # autoHist3
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_by_css('#slice-header > div > div > button')
        self.driver.find_element_by_css_selector('#slice-header > div > div > button').click()
        self.wait_by_css(
            '.modal-lg > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > button:nth-child(1)')
        district = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(19)').text
        print(district)
        purpose = self.driver.find_element_by_css_selector('body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(22)').text
        print(purpose)
        gender = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(25)').text
        print(gender)
        age_bucket = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(28)').text
        print(age_bucket)
        age = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(31)').text
        print(age)
        mo_lvl1 = self.driver.find_element_by_css_selector(
            'body > div:nth-child(6) > div > div.fade.in.modal > div > div > div.modal-body > div > pre > code > span:nth-child(34)').text
        print(mo_lvl1)
        assert district == "'невский район'", 'Упало с сегментированной гистограммы'
        assert purpose == "'лечебно-диагностический прием'", 'Упало с сегментированной гистограммы'
        assert gender == "'female'", 'Упало с сегментированной гистограммы'
        assert age_bucket == "'60+'", 'Упало с сегментированной гистограммы'
        assert age == "'63'", 'Упало с сегментированной гистограммы'
        assert mo_lvl1 == "'гп №8'", 'Упало с сегментированной гистограммы'

    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        self.setup()
        self.login()
        self.hierTimeHist1()
        self.hierTimeHist2()
        self.hierTimeHist3()
        self.hierTimeHist4()
        self.hierTimeHist5()
        self.hierHistSegmented1()
        self.hierHistSegmented2()
        self.hierHistSegmented3()
        self.hierHistSegmented4()
        self.hierHistSegmented5()
        self.tearDown()


if __name__ == '__main__':
    unittest.main()
