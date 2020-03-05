#implicit waits-
#syntax-->driver.implicitly_wait(5)
#wait until 5 seconds if object is not displayed.
#global wait
#1.5 seconds to reach next page, then execution will resume in 1.5 seconds
#if object do not show uo at all, then max time your test waits for 5 seconds.
#explicit waits

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
driver.find_element_by_css_selector("[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

# driver.find_element_by_css_selector("button.promoBtn").click()
