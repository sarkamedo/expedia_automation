# if you experience issues with importing local modules try commenting following two lines...
import sys
sys.path.append(".")

from pages.home_pages.main_page import MainPage

import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC



class ExpediaSearchTests(unittest.TestCase):

    def test_can_search_and_display_results(self):

        baseUrl = "https://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        mp = MainPage(driver)
        mp.search_hotels_and_display_results("key west")
        list_of_results = WDW(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".listing__link.uitk-card-link")))
        self.assertEqual(len(list_of_results), 20)
        driver.quit()

if __name__ == '__main__':
    unittest.main()