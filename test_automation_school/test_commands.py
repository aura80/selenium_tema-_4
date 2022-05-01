# import selenium
# from selenium import webdriver
import time

import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


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

def test_browser_commands():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

    #   close()    -    quit()
    driver.find_element(By.LINK_TEXT, 'nopCommerce').click()

    time.sleep(3)

    #driver.close()
    driver.quit()

def test_navigational_commands():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.emag.ro/")
    driver.get("https://www.amazon.com/")

    driver.back()
    driver.forward()
    driver.refresh()

    driver.close()

def test_find_element_elements():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://automationpractice.com/index.php")

    ###  find_element() returns a single webelement !!!

    # locator with one single element   // send_keys("") only for single element find_element(), not for find_elements() !!!!!
    driver.find_element(By.XPATH,'//input[@id="newsletter-input"]').send_keys("abc@yahoo.com")

    # locator with multiple elements
    footer_elem = driver.find_element(By.XPATH, '//section[@id="block_various_links_footer"]//a')
    print("\nOne element from many: ", footer_elem.text)     # printeaza doar un singur element, cel mai rapid

    time.sleep(2)

    ###  find_element() returns multiple webelements, it returns a list of webelements !!!

    # a list of elements containing one element
    list_one_element = driver.find_elements(By.XPATH, '//div[@id="newsletter_block_left"]')
    print("Web elements found with find_elements() for one element locator : ", len(list_one_element))

    print(list_one_element[0].text)

    # a list of elements containing multiple elements
    list_multi_elements = driver.find_elements(By.XPATH, '//div[@class="block_content toggle-footer"]//a')
    print("Web elements found with find_elements() for multiple elements locator : ", len(list_multi_elements))

    print(list_multi_elements[0].text)
    print(list_multi_elements[1].text)
    print(list_multi_elements[2].text)
    print(list_multi_elements[3].text)

    list_all = driver.find_elements(By.XPATH, '//footer[@id="footer"]//a')
    print("\nElements in list: ", len(list_all))
    for i in list_all:
        print(i.text)

    try:
        # it gives error NoSuchElementException
        driver.find_element(By.LINK_TEXT, 'Ecommerce soft')
    except:
        # no error
        dim = driver.find_elements(By.LINK_TEXT, 'Ecommerce ™')
        print("\nElements with exception: ", len(dim))


    driver.close()


def test_text_getattribute():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")

    #     text    -    get_attribute()
    username = driver.find_element(By.XPATH, '//div[@id="divUsername"]')
    print("\nGet_attribute id: ", username.get_attribute('id'))
    print("Get_attribute class: ", username.get_attribute('class'))
    print("Get_attribute value: ", username.get_attribute('value'))

    inner_text_user = driver.find_element(By.CSS_SELECTOR, '#divUsername .form-hint')
    print("\nInner text username: ", inner_text_user.text)

    time.sleep(2)

    driver.get("http://automationpractice.com/index.php")

    item_search = driver.find_element(By.XPATH, '//input[@id="search_query_top"]')
    item_search.send_keys("shirt")

    item_search.clear()

    item_search.send_keys("jeans")

    print("Get_attribute value: ", item_search.get_attribute('value'))
    print("Get_attribute type: ", item_search.get_attribute('type'))
    print("Get_attribute id: ", item_search.get_attribute('id'))
    print("Get_attribute name: ", item_search.get_attribute('name'))
    print("Get_attribute class: ", item_search.get_attribute('class'))
    print("Get_attribute placeholder: ", item_search.get_attribute('placeholder'))

    driver.quit()

def test_implicitly_wait_command():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")

    driver.implicitly_wait(10)     # every element from now till quit affected

    driver.find_element(By.XPATH, "//div[text()='Sunt de acord']").click()

    elem = driver.find_element(By.XPATH, "//input[@name='q']")
    elem.send_keys("Python")
    elem.submit()       # enter on google page in absence of click button

    list_elem = driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb.MBeuO.DKV0Md')
    print("\nElements on the page: ", len(list_elem))
    for el in list_elem:
        print(el.text)

    driver.find_element(By.XPATH, '//h3[text()="Welcome to Python.org"]').click()

    driver.quit()

def test_explicitly_wait_command():
    driver= selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www4.bing.com/?form=DCDN")

    declaration = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                  ElementNotVisibleException,
                                                                                  ElementNotSelectableException,
                                                                                  Exception])

    elem = driver.find_element(By.XPATH, '//input[@id="sb_form_q"]')
    elem.send_keys("Bucuresti")
    elem.submit()

    declaration.until(EC.presence_of_element_located((By.XPATH, '//a[text()="București - Wikipedia"]'))).click()

    driver.quit()






