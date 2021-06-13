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

	driver.find_elements_by_xpath("//a[contains(text(), 'Games')]")[0].click()
	time.sleep(2)
	assert "Games" in driver.title, "Wrong page title"
	time.sleep(1)

	#checking all games
	games_titles = ["Memo", "Sudoku", "Snake"]
	for i in range(len(games_titles)):
		driver.find_element_by_xpath(f"//div//div//div[{i+1}]//a").click()
		time.sleep(1)
		assert games_titles[i] in driver.title, "Wrong page title"
		driver.find_elements_by_xpath("//a[contains(text(), 'Games')]")[0].click()
		time.sleep(1)

	time.sleep(1)
	driver.find_elements_by_xpath("//a[contains(text(), 'Badges')]")[0].click()
	time.sleep(2)
	tag = driver.find_elements_by_tag_name('h2')[0].text
	assert "Badges" in tag, "Wrong tag's text"
	
	driver.find_elements_by_xpath("//a[contains(text(), 'Ranking')]")[0].click()
	time.sleep(2)
	assert "Ranking" in driver.title, "Wrong page title"

	driver.find_elements_by_xpath("//a[contains(text(), 'About')]")[0].click()
	time.sleep(1)
	assert "About" in driver.title, "Wrong page title"
	tag = driver.find_elements_by_tag_name('h2')[0].text
	assert "About us" in tag, "Wrong tag's text"

	driver.find_elements_by_xpath("//div[contains(text(), 'Log out')]")[0].click()
	time.sleep(2)
	assert "Main page" in driver.title, "Wrong page title"
except AssertionError:
	raise
except Exception as e:
	print(e)
	raise
finally:
	time.sleep(2)
	driver.close()