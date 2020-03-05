import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from page_objects.home_page import HomePage
from test_data.home_page_data import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()

        homepage=HomePage(self.driver)
        log.info("this is the first name",getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])


        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Succesfghdhfs" in alertText)
        self.driver.refresh()

        # //*[contains(@class,'alert-success')] -->own xpath

    @pytest.fixture(params= HomePageData.test_homepage_data)
    def getData(self,request):
        return request.param