


class BrowserUtils:

    def __init__(self,driver):
        self.driver = driver

    def getTitle(self) -> object:
        return self.driver.title