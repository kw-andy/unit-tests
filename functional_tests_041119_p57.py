from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# assert 'Django' in browser.title #before page 55

assert 'To-Do' in browser.title

browser.quit()
