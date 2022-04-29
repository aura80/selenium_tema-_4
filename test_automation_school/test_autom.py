import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")

    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, "Women").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Wom").click()
    driver.find_element(By.NAME, "search_query").send_keys("dress")
    driver.find_element(By.NAME, "submit_search").click()

    sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
    print(len(sliders))

    links = driver.find_elements(By.TAG_NAME, "a")
    print(len(links))

    time.sleep(2)

    driver.close()

def test2():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    driver.maximize_window()

    driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()

    #    tagname # ID
    #driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")
    #    #ID
    #driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc@gmail.com")

    #    tagname . valueofclass # ID
    #driver.find_element(By.CSS_SELECTOR, ".col-xs-12 .box:nth-child(1) .form_content .form-group #email").send_keys("abc@gmail.com")

    #    tagname [ attribute = value ]
    #driver.find_element(By.CSS_SELECTOR, 'input[id="email"]').send_keys("abc@gmail.com")

    #    tagname . valueofclass [ attribute = value ]   for username
    driver.find_element(By.CSS_SELECTOR, "input.is_required[name='email']").send_keys("abc@gmail.com")

    #    tagname . valueofclass [ attribute = value ]   for password
    driver.find_element(By.CSS_SELECTOR, 'input.is_required[id="passwd"]').send_keys("passwd")

    try:
        driver.find_element(By.CSS_SELECTOR, '.icon-lock.left').click()
    except:
        print("Wrong credentials")

    time.sleep(2)

    driver.close()
