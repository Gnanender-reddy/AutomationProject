import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_css_selector("#username").send_keys("sushmitha") #this css path is generated from id
driver.find_element_by_css_selector(".password").send_keys("sushmitha") # #this css path is generated from type
driver.find_element_by_css_selector(".password").clear() # #this will clear the text
driver.find_element_by_link_text("Forgot Your Password?").click() #when it starts with '<a' tag then it is called link.
driver.find_element_by_xpath("//a[text()='Cancel']").click() #this xpath is by text to click cancel button
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login']label:nth-child(3 )").text)

driver.close()