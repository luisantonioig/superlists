from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'To-do' in browser.title , "El titulo de la página es " + browser.title
browser.quit()