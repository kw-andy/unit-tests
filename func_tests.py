from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:8000')

assert 'Django Jamie Foxx' in browser.title

#from selenium import webdriver
#
#browser = webdriver.Firefox()
#
#assert 'To-Do' in browser.title
#
#browser.quit()
