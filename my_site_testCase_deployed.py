import unittest
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from __builtin__ import classmethod



class mysite_testCase_deployed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        cls.driver.set_window_size(1600,900)

    def test_site_is_deployed(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get('http://serednytskyi.pro/')
        self.title = self.wait.until(EC.title_is("Serednytskyi"), "Page was not deployed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()