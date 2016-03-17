import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from __builtin__ import classmethod


# Class callable of checking if the website was deployed and running
class mysite_testCase_deployed(unittest.TestCase):
    # Class method implemented to avoid opening a browser each test in the class
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
		cls.driver.set_window_size(1600,900)
	
	# Checking if the site responds
	def test_site_is_deployed(self):
	# Waiting 10sec for the site to respond
		self.wait = WebDriverWait(self.driver, 10)
		self.driver.get('http://serednytskyi.pro/')
		# Asserting if the title matches (loaded)
		self.title = self.wait.until(EC.title_is("Serednytskyi"), "Page was not deployed")

	# Class method implemented to avoid opening a browser each test in the class
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == "__main__":
	unittest.main()