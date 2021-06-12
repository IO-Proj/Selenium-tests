from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pymongo import MongoClient

DATABASE_URL = 'mongodb+srv://user1:passwd1@cluster0.jw6r4.mongodb.net/myDatabase?retryWrites=true&w=majority'

try:
	#connecting to database
	client = MongoClient(DATABASE_URL)
	db = client['myDatabase']
	users = db.users
	found = users.find_one( {'username': 'test'} )
	if(found is not None):
		users.delete_one( {'username': 'test'} )
	#
	driver = webdriver.Firefox()
	driver.get("https://io-proj.github.io/gamepage/")
	assert "Main page" in driver.title, "Wrong page title"
	time.sleep(2)
	driver.find_elements_by_xpath("//a[contains(text(), 'Sign up')]")[0].click()
	assert "Sign up" in driver.title, "Wrong page title"
	elem = driver.find_element_by_name("username")
	elem.send_keys("test")
	elem = driver.find_element_by_name("pass")
	elem.send_keys("testtest")
	elem.send_keys(Keys.RETURN)
	time.sleep(2)
	alert = driver.switch_to.alert
	assert "Bronze badge for logins!" in alert.text, "Wrong alert message"
	time.sleep(2)
	alert.accept()
	#deleting created test user
	users.delete_one( {'username': 'test'} )
except AssertionError:
	raise
except Exception as e:
	print(e)
finally:
	time.sleep(2)
	driver.close()
	#delete user
	found = users.find_one( {'username': 'test'} )
	if(found is not None):
		users.delete_one( {'username': 'test'} )