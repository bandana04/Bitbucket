from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def setup_driver():
    service = Service('C:/Users/Acer/Downloads/chromedriver-win64/chromedriver.exe')  # specify the full path to chromedriver.exe
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # implicit wait
    return driver

def teardown_driver(driver):
    driver.quit()

def test_checkboxes(driver):
    driver.get("http://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
        assert checkbox.is_selected()

    print("Checkboxes Test Passed")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        test_checkboxes(driver)
    finally:
        teardown_driver(driver)
