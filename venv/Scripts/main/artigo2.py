from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('http://google.com.br/')

campo_busca = chrome.find_element_by_name('q')
campo_busca.send_keys('Eu pesquiso as coisas sozinho')

campo_busca.send_keys(Keys.ENTER)


