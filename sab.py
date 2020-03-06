import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///home/bridgeit/PycharmProjects/Pythonautomation/hh.html")
driver.maximize_window()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("fdfdf")
time.sleep(5)
driver.close()