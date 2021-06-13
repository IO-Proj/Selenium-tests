from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
try:
	driver.get("https://io-proj.github.io/gamepage/")
	assert "Main page" in driver.title, "Wrong page title"
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
	driver.find_elements_by_xpath("//a[contains(text(), 'About')]")[0].click()
	time.sleep(1)
	assert "About" in driver.title, "Wrong page title"
	tag = driver.find_elements_by_tag_name('h2')[0].text
	assert "About us" in tag, "Wrong tag's text"
except AssertionError:
	raise
except Exception as e:
	print(e)
	raise
finally:
	time.sleep(2)
	driver.close()