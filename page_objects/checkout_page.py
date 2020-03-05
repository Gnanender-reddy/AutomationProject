from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']") #tuple, to deserialize a tuple we have to put *.
    cardFooter=(By.XPATH,"div/button")
    checkOut=(By.CSS_SELECTOR,"a[class*='btn-primary']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle) #here we deserailizing the tuple

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def getChekout(self):
        return self.driver.find_element(*CheckoutPage.checkOut)