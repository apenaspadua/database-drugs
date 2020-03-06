from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from mylistener import MyListener

chrome = webdriver.Chrome()
listener = MyListener()

ef_chrome = EventFiringWebDriver(chrome, listener)

ef_chrome.get('http://pythonclub.com.br')

try:
     """
        Propositalmente ira gerar uma exception pois a classe nao existe.
        O evento "on_exception" deve ser chamado
    """
     post = ef_chrome.find_element_by_class_name('post-title')
except:
    pass

post = ef_chrome.find_element_by_class_name('post-tile')
post.click()

ef_chrome.close()