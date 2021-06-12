from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
try:
	driver.get("https://io-proj.github.io/gamepage/")
	assert "Main page" in driver.title, "Wrong page title"
	time.sleep(2)
	driver.find_elements_by_xpath("//a[contains(text(), 'Sign up')]")[0].click()
	assert "Sign up" in driver.title, "Wrong page title"
	elem = driver.find_element_by_name("username")
	elem.send_keys("abc")
	elem = driver.find_element_by_name("pass")
	elem.send_keys("abcd")
	elem.send_keys(Keys.RETURN)
	time.sleep(2)
	alert = driver.switch_to.alert
	assert "Error 400: Username already exists" in alert.text, "Wrong alert message"
	time.sleep(2)
	alert.accept()
except AssertionError:
	raise
except Exception as e:
	print(e)
finally:
	time.sleep(2)
	driver.close()