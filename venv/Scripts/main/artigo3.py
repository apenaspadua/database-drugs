from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('http://google.com.br/')

chrome.execute_script('alert("codigo javascript sendo executado")')

chrome.execute_async_script('alert("codigo javascript sendo executado")')


