from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class Page:
    """Base class for all pages in the app"""

    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    def click_element(self, element: WebElement) -> None:
        element.click()

    def find_element(self, xpath: str) -> WebElement:
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element

    def send_keys_to_element(self, element: WebElement, text: str) -> None:
        element.send_keys(text)

    def find_and_click(self, xpath: str) -> WebElement:
        element = self.find_element(xpath)
        self.click_element(element)
        return element

