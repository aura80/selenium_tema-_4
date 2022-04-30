# import selenium
# from selenium import webdriver
import time

import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_get_application():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()

    print()
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)      # html source page content

    driver.close()

def test_conditional():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.orangehrm.com/")
    driver.maximize_window()

    #   is_displayed()   ,    is_enabled()

    search_elem = driver.find_element(By.XPATH, '//input[@id="myText"]')
    print("\nDispalyed status: ",search_elem.is_displayed())
    print("Enabled status: ", search_elem.is_enabled())

    #   is_selected()
    selected_elem_en = driver.find_element(By.XPATH, '//*[@id="header-navbar"]/ul[3]/li[3]/a')
    print("Selected status EN: ", selected_elem_en.is_selected())      # False
    selected_elem_es = driver.find_element(By.XPATH, '//*[@id="header-navbar"]/ul[3]/li[4]/a')
    print("Selected status ES: ", selected_elem_es.is_selected())      # False

    driver.close()

def test_is_selected():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
    driver.maximize_window()

    #   is_selected()   radio buttons
    male = driver.find_element(By.XPATH, '//input[@id="gender-male"]')
    print("\nMale status initial selection: ", male.is_selected())        # False

    female = driver.find_element(By.XPATH, '//input[@id="gender-female"]')
    print("Female status initial selection: ", female.is_selected())    # False

    male.click()

    print("\nMale status selection: ", male.is_selected())
    print("Female status selection: ", female.is_selected())

    female.click()

    print("\nMale status selection: ", male.is_selected())
    print("Female status selection: ", female.is_selected())

    time.sleep(3)

    driver.close()


