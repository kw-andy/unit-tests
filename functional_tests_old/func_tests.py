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
from selenium.webdriver.common.keys import Keys
import time
import unittest

#print('toto')

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def tearDown(self):
			self.browser.quit()


	def test_can_start_a_list_and_retrieve_it(self):
		# Edith has heard about a cool new online to-do app. She goes 
		# to check out its homepage
		self.browser.get('http://localhost:8000')	

		self.assertIn('To-do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		#self.fail('Finish the test:')
		self.assertIn('To-do',header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'	
		)

		inputbox.send_keys('Buy peacock feathers')

#Functional test now checks we can input a to-do item
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr').text
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
			)

		# There is still a text box inviting her to add another item. 
		# She enters "Use peacock to make a fly"
		# Edith is very methodical

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')			