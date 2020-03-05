from selenium.webdriver.common.by import By


class CheckoutPage1:
    def __init__(self, driver):
        self.driver = driver


    checkOut1=(By.XPATH,"//button[@class='btn btn-success']")

    def getCheckout1(self):
        return self.driver.find_element(*CheckoutPage1.checkOut1) #here we deserailizing the tuple
