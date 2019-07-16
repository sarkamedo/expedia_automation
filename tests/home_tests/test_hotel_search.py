
import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC

from pages.home_pages.main_page import MainPage


class ExpediaSearchTests(unittest.TestCase):

    # def test_can_search_and_list_results(self):

    #     baseUrl = "https://www.expedia.com"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get(baseUrl)

    #     mp = MainPage(driver)
    #     mp.search_hotels_and_show_results("key west")
    #     list_of_results = WW(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".listing__link.uitk-card-link")))
    #     self.assertEqual(len(list_of_results), 20)
    #     driver.quit()

    def test_can_search_and_display_results(self):

        baseUrl = "https://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        mp = MainPage(driver)
        mp.search_hotels_and_display_results("key west")
        list_of_results = WW(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".listing__link.uitk-card-link")))
        self.assertEqual(len(list_of_results), 20)
        driver.quit()

if __name__ == '__main__':
    unittest.main()