import time

import selenium.webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.opencart.com/index.php?route=account/register")

    driver.maximize_window()

    roma = driver.find_elements(By.XPATH, '//select[@id="input-country"]//option')

    print("\nElements: ", len(roma))

    for i in range(len(roma)):
        print(roma[i].get_attribute('value'),"  ",roma[i].text)

        if roma[i].text == 'Italy' and roma[i].get_attribute('value') == '105' or roma[i].text == 'Austria' and roma[i].get_attribute('value') == '14' :
            print(f' --------- We visited {roma[i].text} recently')
            roma[i].click()

    time.sleep(3)

    driver.quit()

def test_dropdown2():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.opencart.com/index.php?route=account/register")

    driver.maximize_window()

    tari = Select(driver.find_element(By.CSS_SELECTOR, 'select.form-control'))
    all = tari.options
    print("\nNo. of countries to select: ", len(all))

    for i in all:
        print(i.text)
        if i.text == 'American Samoa':
            i.click()

    time.sleep(3)

    driver.quit()

def test_dropdown3():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.opencart.com/index.php?route=account/register")

    driver.maximize_window()

    #   dropdown with Select and built-in functions

    tari = Select(driver.find_element(By.CSS_SELECTOR, 'select#input-country'))
    tari.select_by_visible_text("Andorra")
    time.sleep(2)
    tari.select_by_index(200)
    time.sleep(2)
    tari.select_by_value('175')


    time.sleep(3)

    driver.quit()

def test_dropdown4():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.maximize_window()

    #   move_to_element

    driver.find_element(By.CSS_SELECTOR, '#cookieChoiceDismiss.cookie-choices-button').click()

    speed = driver.find_element(By.CSS_SELECTOR, 'a.home-link')        #'//select[@id="speed"]/option[3]'
    print("\n", speed.text)

    actions = ActionChains(driver)
    print(actions)

    actions.move_to_element(speed).click()
    print(driver.title)

    time.sleep(3)

    driver.quit()