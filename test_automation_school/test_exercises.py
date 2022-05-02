import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_itera1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://itera-qa.azurewebsites.net/home/automation")
    driver.maximize_window()

    show_text1 = driver.find_element(By.XPATH, '//label[@for="gender"]').text
    print("\n", show_text1)

    driver.find_element(By.XPATH, '//input[@id="female"]').click()

    show_text2 = driver.find_element(By.XPATH, '//label[text()="Which days of the week are best to start something new?"]')
    print("\n", show_text2.text)

    #   select one checkbox
    driver.find_element(By.XPATH, '//input[@id="monday"]').click()

    time.sleep(2)

    driver.quit()

def test_itera2():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://itera-qa.azurewebsites.net/home/automation")

    #   select all the checkboxes for the days of the week
    nr_elem = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
    print("\nWeek days: ", len(nr_elem))

    for i in range(len(nr_elem)):
        nr_elem[i].click()
        print(nr_elem[i].get_attribute('id'))

    nr_tools = driver.find_elements(By.CSS_SELECTOR, "div.form-group div.custom-control.custom-checkbox label.custom-control-label")
    print("\nNumber of tools/frameworks used: ", len(nr_tools))

    for tool in nr_tools:
        tool.click()
        print("Tools/Frameworks used: ", tool.text, end="")
        spec = tool.get_attribute('for')
        print("  ---  ", spec)
        if spec == "selenium" or spec == "cucumber":
            print("     -      this is my speciality")

    time.sleep(2)

    driver.quit()

def test_itera3():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://itera-qa.azurewebsites.net/home/automation")

    week_days = driver.find_elements(By.CSS_SELECTOR, '.form-check input[type="checkbox"]')
    print("\nDays of the week: ", len(week_days))

    print("Days selected: ")
    for day in range(len(week_days) - 5, len(week_days) - 2):
        week_days[day].click()
        print("     ", week_days[day].get_attribute('id').capitalize())

    time.sleep(2)

    driver.quit()

def test_itera4():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://itera-qa.azurewebsites.net/home/automation")

    days = driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id,"day")]')

    print("\nDays selected: ")
    for i in range(len(days)):
        if i > 0 and i < 3 or i >= 4 and i < 6 :
            days[i].click()
            print(days[i].get_attribute('id'))

    time.sleep(2)

    driver.quit()

def test_itera5():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://itera-qa.azurewebsites.net/home/automation")

    zi = driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id,"day")]')

    time.sleep(5)

    for i in zi:
        if i.is_selected():
            i.click()

    time.sleep(2)

    driver.quit()

