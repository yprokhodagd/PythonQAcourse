from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def wait_till_element_is_visible(self, by, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, element)))

    def wait_till_elements_are_visible(self, by, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((by, element)))

    def wait_till_element_is_clickable(self, by, element):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, element)))

    def find_element(self, by, element):
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        return self.driver.find_elements(by, element)

    def find_link(self, link_text):
        self.driver.find_element_by_link_text(link_text)

    def open_url(self, url):
        return self.driver.get(url)

    def move_to_element(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def windows_scroll(self, x, y):
        return self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def type_text(self, webelement, text):
        return webelement.send_keys(text)
