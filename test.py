import pytest
from selenium import webdriver

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.tamusa.edu")
    assert "Google" in driver.title, "Title does not contain 'Google'"
