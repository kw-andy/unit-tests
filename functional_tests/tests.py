from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#P81/P41

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox() #ok

	def tearDown(self):
		self.browser.quit() #ok

	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])	

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.live_server_url) #ok

		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text) #ok

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		inputbox.send_keys('Buy peacock feathers')

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		self.check_for_row_in_list_table('1: Buy peacock feathers')



		#find_element* == methods provided by selenium
		#Keys == class that simulate keys like Enter

		'''
		super important:
		il y'a :

		find_elements_by_tag_name
		find_element_by_tag_name

		Essentiel de faire attention sous peine d'avoir des bugs incompréhesibles.
			
		'''
    	# There is still a text box inviting her to add another item. She
    	# enters "Use peacock feathers to make a fly" (Edith is very
    	# methodical)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)


		# The page updates again, and now shows both items on her list

		self.check_for_row_in_list_table('1: Buy peaock feathers')
		self.check_for_row_in_list_table('2: Use peaock feathers to make a fly')



if __name__ == '__main__':
	unittest.main(warnings='ignore')				
