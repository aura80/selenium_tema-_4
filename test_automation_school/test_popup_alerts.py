import time
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def alert_one():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsAlert()"]').click()

    time.sleep(1)

    driver.quit()