# js Dom can access any elements on the web page just like how selenium does
# selenium have a method to execute javascript code in it.

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("helloo")
print(driver.find_element_by_name("name").text) #no data printed.
# note : if browser has already a text we can retrieve that text,but we cant retrieve the text which is entered by selenium.
print(driver.find_element_by_name("name").get_attribute("value"))# this get_attribute method is from java script dom model.
print(driver.execute_script('return document.getElementsByName("name")[0].value')) #this line is completely java script, here
#selenium give access on java script methods, actually selenium inherited the java script methods.