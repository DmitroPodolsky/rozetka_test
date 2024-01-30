import pytest
from selenium.webdriver import Chrome

@pytest.fixture()
def driver() -> Chrome:
    driver = Chrome()
    yield driver
    driver.quit()
