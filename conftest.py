import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path=r"C:\Users\galan\PycharmProjects\chromedriver.exe")
    yield driver
    driver.quit()
