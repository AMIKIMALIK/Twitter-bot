from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver= webdriver.Chrome("chromedriver.exe")
driver.get('https://www.twitter.com/login')
sleep(2)

element= driver.find_element_by_name("session[username_or_email]")
element.send_keys('py_amit')
element= driver.find_element_by_name("session[password]")
element.send_keys('amit1999')
element.send_keys(Keys.RETURN)
element.close()












# element.send_keys(Keys.RETURN)
# element.close()
