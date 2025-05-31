from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from uttils.browserUttils import BrowserUtils

class Checkout_Confirmation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)  # Calls parent constructor, initializes self.driver

        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")  # Ensure correct formatting
        self.checkout_element = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")  # Removed trailing space

    def checkout(self):
        """Clicks the checkout button."""
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, country_name):
        """Fills in the delivery address and submits."""
        self.driver.find_element(*self.country_input).send_keys(country_name)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))  # Fixed issue

        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkout_element).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        """Validates success message after order submission."""
        success_msg = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_msg, "Order success message not found."
