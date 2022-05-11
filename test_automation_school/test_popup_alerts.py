import time
import selenium
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_simple_alert_ok():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsAlert()"]').click()

    alert_ok = driver.switch_to.alert

    print(f'\n{alert_ok.text}')

    alert_ok.accept()

    text_sent = driver.find_element(By.CSS_SELECTOR, 'p#result')
    print(text_sent.text)

    driver.quit()


def test_confirm_alert_ok_cancel():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.maximize_window()

    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

    alert_box = driver.switch_to.alert
    time.sleep(2)

    print("\n", alert_box.text)

    alert_box.dismiss()

    text_sent = driver.find_element(By.CSS_SELECTOR, 'p#result')
    print(text_sent.text)

    driver.quit()


def test_prompt_alert_ok_cancel():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.maximize_window()

    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

    alerta = driver.switch_to.alert
    print()
    print(alerta.text)

    alerta.send_keys("Hello!!!")

    time.sleep(2)

    alerta.accept()
    #alerta.dismiss()

    text_sent = driver.find_element(By.CSS_SELECTOR, 'p#result')
    print(text_sent.text)

    time.sleep(2)


    driver.quit()


def test_authentification_popups():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    driver.maximize_window()

    titlu = driver.find_element(By.CSS_SELECTOR, '.example h3')
    print()
    print(titlu.text)
    print(driver.title)

    assert titlu.text != driver.title, 'Inner text and the title are not the same'


    time.sleep(2)


    driver.quit()
