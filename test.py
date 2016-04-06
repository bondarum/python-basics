import unittest
from selenium import webdriver

class testSiblmpe(unittest.TestCase):

    def test_simple(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://koncikowski.pl/trainings/playground/')
        self.browser.find_element
        self.browser.quit()

