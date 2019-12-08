from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

#P81/P41

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		inputbox = self.browser.find_elements_by_id('id_new_item')
		self.assertEqual(
			inputbox.getattribute('placeholder'),
			'Enter a to-do item'
		)

		inputbox.send_keys('Buy peacock feathers')

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_elements_by_id('id_list_tab')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')				
