import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.common.action_chains import ActionChains

# Class capable of testing JQuery scripts like "jumping" buttons and "Block scroll"
# All the button IDs are represented as lists to avoid spamming variables
class mysite_testCase_JQuery_scripts(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
		cls.driver.implicitly_wait(30)
		cls.driver.set_window_size(1600,900)
		cls.driver.get('http://serednytskyi.pro/')
		
	# TODO Add assertions to make the test actually check something and not just pressing buttons
	def test_top_menu_buttons(self):
		self.top_menu_buttons = ["profile_button", "skills_button", "experience_button" ,"contact_button"]
		for button in self.top_menu_buttons:
			self.top_button = self.driver.find_element_by_id(button)
			self.top_button.click()
			time.sleep(0.2)

	# Checking if JQuery script makes contact_buttons "jump"
	def test_contact_buttons_animate(self):
		# Waiting to avoid interference with previous test
		time.sleep(2)
		self.contact_buttons = ["fb", "ln", "git", "cv"]
		for button in self.contact_buttons:
			self.contact_button = self.driver.find_element_by_id(button)
			# Action chain to perform hower action
			self.hower = ActionChains(self.driver).move_to_element(self.contact_button)
			self.hower.perform()
			time.sleep(0.2)
			self.contact_button_height = self.contact_button.size['height']
			# Asserting button height parameter after 0.2 seconds to give it a time to actually "jump"
			self.assertTrue(self.contact_button_height > 68, "jqery script doesn't work for " + button +" button")
			# Waiting 1 second to let button finish the animation sequence (just to make sure that the following button is isolated)
			time.sleep(1)
	
	# Checking if navigation_buttons changing their color when hower action is performed on them
	def test_navigation_buttons_animate(self):
		self.button_ids = ["profile_button", "skills_button", "experience_button", "contact_button"]
		for button in self.button_ids:
			self.icon = self.driver.find_element_by_id(button)
			# Action chain to perform hower action
			self.hower = ActionChains(self.driver).move_to_element(self.icon)
			self.hower.perform()
			# Asserting if "howered" class was applied to the element
			self.assertTrue(("howered" in self.icon.get_attribute("class")), button + " is not highlighted")
			time.sleep(1)

	# Class method for browser closing
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == "__main__":
	unittest.main()