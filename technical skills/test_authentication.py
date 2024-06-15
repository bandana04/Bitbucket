from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
def setup_driver():
    service = Service('C:/Users/Acer/Downloads/chromedriver-win64/chromedriver.exe')  
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver

def teardown_driver(driver):
    driver.quit()


def test_basic_auth(driver):
    url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
    driver.get(url)


    success_message = driver.find_element(By.CSS_SELECTOR, 'p').text
    assert "Congratulations! You must have the proper credentials." in success_message
    print("Basic Auth Test Passed")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        test_basic_auth(driver)
    finally:
        teardown_driver(driver)
