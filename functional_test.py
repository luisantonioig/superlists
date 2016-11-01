from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'To-do' in browser.title
browser.quit()