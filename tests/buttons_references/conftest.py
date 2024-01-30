import pytest

from framework.page import Page
from time import sleep


@pytest.fixture()
def home_page(driver):
    yield Page(driver)
