from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

def test_sort(browserInstance):
    driver = browserInstance
    browserSortedVeggies = []
   # driver = webdriver.Chrome()
    #driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # click on column hrader
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all vegies name - veggielist
    veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
    for veggie in veggieWebElements:
        browserSortedVeggies.append(veggie.text)

    originalBrowserSortedList = browserSortedVeggies.copy()

    # sort veggilist = newsortedlist
    browserSortedVeggies.sort()
    # veggielist = newsortedlist
    assert browserSortedVeggies == originalBrowserSortedList