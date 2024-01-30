
from time import sleep
import pytest
from framework.page import Page
from framework import URL

@pytest.mark.parametrize("url", [('https://www.work.ua/zsu/')])
def test_zsu_success(home_page: Page, url: str) -> None:
    home_page.driver.get(url=URL)
    home_page.find_and_click('//*[@id="center"]/div[2]/ul/li[4]')
    windows = home_page.driver.window_handles
    home_page.driver.switch_to.window(windows[1])
    assert url == home_page.driver.current_url
    
@pytest.mark.parametrize("url", [('https://www.work.ua/job')])
def test_zsu_failure(home_page: Page, url: str) -> None:
    home_page.driver.get(url=URL)
    home_page.find_and_click('//*[@id="center"]/div[2]/ul/li[4]')
    windows = home_page.driver.window_handles
    home_page.driver.switch_to.window(windows[1])
    assert url != home_page.driver.current_url
    