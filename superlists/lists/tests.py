from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
"""
class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.assertEqual(1+1,3)
"""


class HomePageTest(TestCase):
	"""docstring for ClassName"""
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To do lists</title>',html)
		self.assertTrue(html.endswith('</html>'))