#for links we need to install requests package
import time

import requests
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_links1():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demo.nopcommerce.com/")

    driver.find_element(By.LINK_TEXT, 'Electronics').click()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Gift Car').click()
    time.sleep(2)

    links_number = driver.find_elements(By.TAG_NAME, 'a')
    print("\nNumber of links on page: ", len(links_number))
    links_no = driver.find_elements(By.XPATH, '//a')
    for i in links_no:
        if len(links_no) < 100:
            print(" ", i.text)
            print(i.get_attribute('href'))

def test_links2():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://www.deadlinkcity.com/")

    driver.maximize_window()

    links_on_page = driver.find_elements(By.TAG_NAME, 'a')
    print("\nTotal no. of links on page: ", len(links_on_page))

    total_broken, total_ok = 0, 0
    for link in links_on_page:
        url = link.get_attribute('href')

        # we send a request to the server by using requests and calling the function head(url)
        # the answer from the server is stored in request variable
        try:
            request = requests.head(url)
        except:
            None

        if request.status_code >= 400:
            print(url, '    the link is broken')
            total_broken += 1
        else:
            print(url, '    the link is ok')
            total_ok += 1

    print("Total no. of broken links: ", total_broken)
    print("Total no. of ok links: ", total_ok)

    driver.quit()

def test_links3():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.amazon.com/")
    driver.maximize_window()

    all_img = driver.find_elements(By.TAG_NAME, 'img')
    print("\nTotal no. of img on amazon: ", len(all_img))

    broken, ok = 0, 0
    for img in range(len(all_img)):
        url = all_img[img].get_attribute('src')

        try:
            cerere = requests.head(url)
        except:
            None

        if cerere.status_code >= 400:
            print(f'Link {img} broken: ', url)
            broken += 1
        else:
            print(f'Link {img} ok: ', url)
            ok += 1
    print("Total no. of broken amazon links: ", broken)
    print("Total no. of ok amazon links: ", ok)



