import time
import selenium
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_three_iframes():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

    driver.maximize_window()

    # cadru will be the web element we will use on the next row to switch to the iframe1
    cadru = driver.find_element(By.NAME, 'packageListFrame')

    # here we switch to the iframe1 upon the web element cadru searched by the name
    driver.switch_to.frame(cadru)

    # we also can switch directly by name in this case or by ID or webelement like above or to put 0 in   frame ( 0 )
    #driver.switch_to.frame("packageListFrame")

    # here we make click on the element from the first iframe1
    driver.find_element(By.LINK_TEXT, 'org.openqa.selenium.chrome').click()

    # we go back to the main page
    driver.switch_to.default_content()


    # here we switch to the iframe2 upon the name of the iframe2
    driver.switch_to.frame("packageFrame")

    # here we make click on the element from the iframe2
    driver.find_element(By.LINK_TEXT, 'ChromeDriver').click()

    # we go back to the main page
    driver.switch_to.default_content()


    # here we switch to the iframe3 upon the name of the iframe3
    driver.switch_to.frame("classFrame")

    # here we make click on the element from the iframe3
    driver.find_element(By.CSS_SELECTOR, '.topNav .navList .navBarCell1Rev').click()


    time.sleep(3)

    driver.quit()


def test_two_iframes_contained():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://demo.automationtesting.in/Frames.html")

    driver.maximize_window()

    driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe').click()

    frame1 = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')

    driver.switch_to.frame(frame1)

    frame2 = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')

    driver.switch_to.frame(frame2)

    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("cocos")


    time.sleep(3)

    driver.quit()


def test_single_frame():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://demo.automationtesting.in/Frames.html")

    driver.maximize_window()

    driver.switch_to.frame("singleframe")

    driver.find_element(By.CSS_SELECTOR, '.container .row .col-xs-6 input').send_keys("selenium")


    time.sleep(3)

    driver.quit()