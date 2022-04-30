import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def test1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.maximize_window()

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input').send_keys("abcd@yahoo.com")
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

    #   OR   -   AND   -   ActionChains
    driver.find_element(By.XPATH, '//input[@name="search_query" or placeholder="Search"]').send_keys("blouse")
    driver.find_element(By.XPATH, '//button[@class="btn btn-default button-search" or name="submit_search"]').click()
    driver.find_element(By.XPATH, '//select[@id="selectProductSort" and @class="selectProductSort form-control"]').click()

    driver.get("http://automationpractice.com/index.php?controller=search&search_query=blouse&submit_search=&orderby=quantity&orderway=desc")

    element = driver.find_element(By.XPATH, '//option[@value="quantity:desc"]')

    actions = ActionChains(driver)

    actions.move_to_element(element).click()

    time.sleep(4)

def test6():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")

    driver.maximize_window()

    #   contains    -    starts-with
    driver.find_element(By.XPATH, '//input[contains(@id,"_query_")]').send_keys("skirt")
    driver.find_element(By.XPATH, '//button[starts-with(@name,"submit_")]').click()

    driver.get("http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=skirt&submit_search=")
    driver.find_element(By.XPATH, "//a[text()='Women']").click()

    time.sleep(4)
