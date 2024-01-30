import pytest

from framework.search_bar import SearchBar


@pytest.fixture()
def search_bar(driver):
    yield SearchBar(driver)
