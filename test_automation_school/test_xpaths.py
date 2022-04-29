import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.maximize_window()

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input').send_keys("tricou")
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/img')
    span = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/span').text
    print(span)

    time.sleep(2)

def test2():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demo.nopcommerce.com/")

    driver.maximize_window()

    driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').click()
    register = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[1]/h1').text
    print(register)

    time.sleep(3)

def test3():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")

    driver.maximize_window()

    #   FULL XPATH
    driver.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]').send_keys("T-shirts")
    driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

    time.sleep(3)

def test4():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")

    driver.maximize_window()

    #   PARTIAL XPATH
    driver.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys("dresses")
    driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()

    time.sleep(3)

def test5():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")

    driver.maximize_window()

    #   OR
    driver.find_element(By.XPATH, '//input[@name="search_query" or placeholder="Search"]').send_keys("blouse")
    driver.find_element(By.XPATH, '//button[@class="btn btn-default button-search" or name="submit_search"]').click()

    time.sleep(4)
