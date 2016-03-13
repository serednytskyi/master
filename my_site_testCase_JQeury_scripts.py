import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.common.action_chains import ActionChains



class mysite_testCase_JQuery_scripts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.set_window_size(1600,900)
        cls.driver.get('file:///D:/site/index.html')

    def test_top_menu_buttons(self):
        self.button1 = self.driver.find_element_by_id('profile_button')
        self.button2 = self.driver.find_element_by_id('skills_button')
        self.button3 = self.driver.find_element_by_id('someshit_button')
        self.button4 = self.driver.find_element_by_id('someothershit_button')
        self.buttons = [self.button1, self.button2, self.button3, self.button4]
        for button in self.buttons:
            button.click()
            time.sleep(0.2)

    def test_contact_buttons_animate(self):
        self.contact_buttons = ["fb", "ln", "sq"]
        for button in self.contact_buttons:
            self.contact_button = self.driver.find_element_by_id(button)
            self.hower = ActionChains(self.driver).move_to_element(self.contact_button)
            self.hower.perform()
            time.sleep(0.2)
            self.contact_button_height = self.contact_button.size['height']
            self.assertTrue(self.contact_button_height > 68, "jqery script doesn't work for " + button +" button")
            time.sleep(1)

    def test_navigation_buttons_animate(self):
        self.button_ids = ["profile_button", "skills_button", "someshit_button", "someothershit_button"]
        for button in self.button_ids:
            self.icon = self.driver.find_element_by_id(button)
            self.hower = ActionChains(self.driver).move_to_element(self.icon)
            self.hower.perform()
            self.assertTrue(("howered" in self.icon.get_attribute("class")), button + " is not highlighted")
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()