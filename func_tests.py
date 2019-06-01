"""
from selenium import webdriver

#browser = webdriver.Firefox()

browser.get('http://127.0.0.1:8000')

assert 'Django Jamie Foxx' in browser.title

from selenium import webdriver

browser = webdriver.Firefox()

assert 'To-Do' in browser.title

browser.quit()
"""

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def tearDown(self):
			self.browser.quit()


	def test_can_start_a_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')	

		self.assertIn('To do lists',self.browser.title)
		self.fail('Finish the test:')

if __name__ == '__main__':
	unittest.main(warnings='ignore')			