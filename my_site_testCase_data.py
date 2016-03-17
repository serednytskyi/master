import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

# Simple class capable of testing if particular elements were loaded and displayed.
class mysite_testCase_data(unittest.TestCase):
    # Class method implemented to avoid opening a browser each test in the class
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
		cls.driver.implicitly_wait(30)
		cls.driver.set_window_size(1600,900)
		cls.driver.get('http://serednytskyi.pro/')

	# Checking if "About me" text block is displayed
	def test_if_text_is_in_place(self):
		self.first_text = self.driver.find_element_by_css_selector('#me > div.about_me > p')
		self.assertTrue(self.first_text.is_displayed(), '"About me" text is not displayed')

	# Checking if photo is displayed 
	def test_if_photo_is_in_place(self):
		self.photo = self.driver.find_element_by_css_selector('#me > div.img > img')
		self.photo_height = self.photo.size['height']
		# Asserting the height of the photo to be sure it's not a browser placeholder
		self.assertTrue(self.photo_height > 24, "There is no photo")
	
	# Class method for browser closing
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == "__main__":
	unittest.main()