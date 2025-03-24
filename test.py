import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize the WebDriver (make sure the driver is correctly installed)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title, "Title does not contain 'Google'"
