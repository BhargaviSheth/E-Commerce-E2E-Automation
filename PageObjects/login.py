from selenium.webdriver.common.by import By

from PageObjects.shop import ShopPage
from uttils.browserUttils import BrowserUtils



class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username") #put self beacause usename_input have scope to this clas only and self has global scope in whole class
        self.password = (By.ID, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        #The find_element expects two arguments and self.username is only one , we can put star & devide it to two
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver)
        return shop_page


