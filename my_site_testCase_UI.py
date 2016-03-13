import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod


class mysite_testCase_UI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.set_window_size(1600,900)
        cls.driver.get('file:///D:/site/index.html')



    def test_if_text_is_in_place(self):
        self.first_text = self.driver.find_element_by_css_selector('#profile > h1')
        self.assertTrue(self.first_text.is_displayed(), '"Greatings" text is not displayed')

    def test_if_photo_is_in_place(self):
        self.photo = self.driver.find_element_by_css_selector('#profile_table  td:nth-child(2)')
        self.photo_height = self.photo.size['height']
        self.assertTrue(self.photo_height > 24, "There is no photo")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()