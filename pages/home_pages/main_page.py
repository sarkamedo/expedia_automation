from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _hotels_button = "#tab-hotel-tab-hp"
    _search_box = "#hotel-destination-hp-hotel"

    def get_hotels_button(self):
        return WW(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self._hotels_button)))

    def get_search_box(self):
        return WW(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self._search_box)))

    def click_hotels_button(self):
        self.get_hotels_button().click()

    def perform_search_by_query(self, search_query):
        self.get_search_box().clear()
        self.get_search_box().send_keys(search_query)
        self.get_search_box().send_keys(Keys.RETURN)
        self.driver.implicitly_wait(2)
        self.get_search_box().send_keys(Keys.RETURN)

    def search_hotels_and_display_results(self, search_query):
        self.click_hotels_button()
        self.perform_search_by_query(search_query)

##############################
    # def search_hotels_and_show_results(self, query):
    #     hotels_button = WW(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, self._hotels_button)))
    #     hotels_button.click()

    #     search_box = WW(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, self._search_box)))
    #     search_box.clear()
    #     search_box.send_keys(query)
    #     self.driver.implicitly_wait(1)
    #     search_box.send_keys(Keys.RETURN)
    #     self.driver.implicitly_wait(1)
    #     search_box.send_keys(Keys.RETURN)
