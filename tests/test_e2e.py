import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# @pytest.mark.usefixtures("setup")
from page_objects.checkout_page import CheckoutPage
from page_objects.checkout_page1 import CheckoutPage1
from page_objects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info(checkoutpage,"some")

        #checkoutpage = CheckoutPage(self.driver)
        cards = checkoutpage.getCardTitles()
        for card in cards:
            product_name = card.text
            if product_name == "Blackberry":
                checkoutpage.getCardTitles().click()
        checkoutpage.getChekout().click()
        log.info(checkoutpage,"soem one")
        checkoutpage1 = CheckoutPage1(self.driver)
        checkoutpage1.getCheckout1().click()

        self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")
        # [xpath='1']
        self.driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[class='btn btn-success btn-lg']").click()
        print(self.driver.find_element_by_class_name("alert-success").text)
        self.driver.get_screenshot_as_file("screen.png")