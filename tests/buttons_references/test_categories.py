

import pytest
from framework.page import Page
from framework import URL

@pytest.mark.parametrize("url", [('https://www.work.ua/jobs/by-category/')])
def test_catigories_success(home_page: Page, url: str) -> None:
    home_page.driver.get(url=URL)
    home_page.find_and_click('//*[@id="center"]/div[2]/ul/li[1]')
    assert url == home_page.driver.current_url
    
@pytest.mark.parametrize("url", [('https://www.work.ua/job')])
def test_catigories_failure(home_page: Page, url: str) -> None:
    home_page.driver.get(url=URL)
    home_page.find_and_click('//*[@id="center"]/div[2]/ul/li[1]')
    assert url != home_page.driver.current_url
    