
import pytest
from framework.search_bar import SearchBar
from framework import URL

@pytest.mark.parametrize("url, text", [('https://www.work.ua/jobs-python/', 'Python')])
def test_place_success(search_bar: SearchBar, url: str, text: str) -> None:
    search_bar.driver.get(url=URL)
    text_field = search_bar.find_element('//*[@id="search"]')
    search_bar.send_keys_to_element(text_field,text)
    search_bar.find_and_click('//*[@id="sm-but"]')
    assert url == search_bar.driver.current_url
    
@pytest.mark.parametrize("url, text", [('https://www.work.ua/jobs', 'Python')])
def test_place_failure(search_bar: SearchBar, url: str, text: str) -> None:
    search_bar.driver.get(url=URL)
    text_field = search_bar.find_element('//*[@id="search"]')
    search_bar.send_keys_to_element(text_field,text)
    search_bar.find_and_click('//*[@id="sm-but"]')
    assert url != search_bar.driver.current_url
    