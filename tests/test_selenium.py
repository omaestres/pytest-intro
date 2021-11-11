"""
Example of basic selenium tests
"""
from selenium import webdriver
import chromedriver_autoinstaller

# it installs the chromedriver automatically
chromedriver_autoinstaller.install()

# sample selenium test
def test_selenium():  
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    assert "Python"  in driver.title