from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
try:
	driver.get("https://io-proj.github.io/gamepage/")
	assert "Main page" in driver.title, "Wrong page title"
	time.sleep(2)
	driver.find_elements_by_xpath("//a[contains(text(), 'Log in')]")[0].click()
	elem = driver.find_element_by_name("username")
	elem.send_keys("abc")
	elem = driver.find_element_by_name("pass")
	elem.send_keys("abc")
	elem.send_keys(Keys.RETURN)
	time.sleep(10)
	assert "Main page" in driver.title, "Wrong page title"
	driver.find_elements_by_xpath("//a[contains(text(), 'Profile')]")[0].click()
	time.sleep(2)
	assert "Profile" in driver.title, "Wrong page title"
	username = driver.find_elements_by_tag_name('h2')[0].text
	assert "abc" in username, "Wrong username"
	time.sleep(2)
	driver.find_elements_by_xpath("//div[contains(text(), 'Log out')]")[0].click()
	assert "Main page" in driver.title, "Wrong page title"
except AssertionError:
	raise
except Exception as e:
	print(e)
finally:
	time.sleep(2)
	driver.close()