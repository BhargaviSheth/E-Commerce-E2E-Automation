#from telnetlib import EC
#pytest -m smoke // tagging to run smoke
#pytest -n 2 //pytest plugin xdist to run parrallel
#pytest -s to display print statement
import json

import pytest
import sys
import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'PageObjectsModel')))

from
test_data_path = 'data/test.eseTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f) #it converts json file to python object
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shop_page=loginpage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()
    print(checkout_confirmation.getTitle())

    #driver.get("https://rahulshettyacademy.com/angularpractice/")


