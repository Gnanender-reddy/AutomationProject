
#webdriver_locators: ID,class,name, xpath,css selector,link text.
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("jhgj")
driver.find_element_by_css_selector("input[name='name']").send_keys("fd")
driver.find_element_by_name("email").send_keys("jgjg")

driver.find_element_by_id("exampleInputPassword1").send_keys("gmhgbj")
driver.find_element_by_class_name("form-check-input").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)
 #this will grab the txt and return it.

#select class provide methods to handle the options in drop downs.
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))

dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1) #if you want to select according to index.
#dropdown.select_by_value("M") #if value is there for that element use this lline.
message=driver.find_element_by_class_name("alert-success").text
assert "success1233" in message #if it is substring then write this line
#assert "success" == message --> if you are checking full string then write this line

#//*[contains(@class,'alert-success')] -->own xpath