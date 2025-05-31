from selenium.webdriver.common.by import By

from PageObjects.checkout_confirmation import Checkout_Confirmation
from uttils.browserUttils import BrowserUtils


class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)

        self.driver = driver

    def add_product_to_cart(self,product_name):
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

        self.driver.find_element(*self.shop_link).click()
        # //a[contains(@href,'Shop')] - regular expression syntax
        # for css a[href*='Shop']
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):

        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation






