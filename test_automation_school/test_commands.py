# import selenium
# from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_application():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    print()
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)      # html source page content

    driver.close()

def conditional():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/")
    driver.maximize_window()

    search_elem = driver.find_element(By.XPATH, '//input[@id="myText"]')
    print("Dispalyed status: ",search_elem.is_displayed())
    print("Enabled status: ", search_elem.is_enabled())

    driver.close()