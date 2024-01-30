
import pytest
from framework.search_bar import SearchBar
from framework import URL

@pytest.mark.parametrize("url", [('https://www.work.ua/jobs-kyiv/')])
def test_typing_success(search_bar: SearchBar, url: str) -> None:
    search_bar.driver.get(url=URL)
    search_bar.find_and_click('//*[@id="searchform"]/div/div/div[2]')
    search_bar.find_and_click('//*[@id="searchform"]/div/div/div[2]/ul/li[1]')
    search_bar.find_and_click('//*[@id="sm-but"]')
    assert url == search_bar.driver.current_url
    
@pytest.mark.parametrize("url", [('https://www.work.ua/job')])
def test_typing_failure(search_bar: SearchBar, url: str) -> None:
    search_bar.driver.get(url=URL)
    search_bar.find_and_click('//*[@id="searchform"]/div/div/div[2]')
    search_bar.find_and_click('//*[@id="searchform"]/div/div/div[2]/ul/li[1]')
    search_bar.find_and_click('//*[@id="sm-but"]')
    assert url == search_bar.driver.current_url
    