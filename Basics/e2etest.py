from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
#//div[@class='card h-100']/div/h4/a
products=driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name=product.find_element_by_xpath("div/h4/a").text
    if product_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.XPATH , "//a[contains(text(),'India')]")))
# [xpath='1']
driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[class='btn btn-success btn-lg']").click()
print(driver.find_element_by_class_name("alert-success").text)
driver.get_screenshot_as_file("screen.png")

