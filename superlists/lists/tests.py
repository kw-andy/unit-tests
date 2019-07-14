from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
import unittest
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
"""
class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.assertEqual(1+1,3)
"""

#
class HomePageTest(TestCase):
	"""docstring for ClassName"""
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)

	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')

		html = response.content.decode('utf8')
		#request = HttpRequest()
		#response = home_page(request)
		#html = response.content.decode('utf8')
		#expected_html = render_to_string('home.html')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-do lists</title>',html)
		#self.assertEqual(html,expected_html)
		##self.assertTrue(html.endswith('</html>'))
		self.assertTrue(html.strip().endswith('</html>'))

		self.assertTemplateUsed(response,'home.html')

