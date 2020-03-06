from selenium import webdriver
import json

chrome = webdriver.Chrome()
chrome.get('http://pythonclub.com.br/')

posts = chrome.find_elements_by_class_name('post')

with open('data.json', 'w') as json_file:
    for post in posts:
        post_title = post.find_element_by_class_name('post-title')
        post_link = post_title.get_attribute('href')
        post_p = post.find_element_by_class_name('post-meta')
        post_subtitle = post_p.get_attribute('p')

        print u"""Titutlo: {titulo}, \nLink: {link}, \nSubtitulo: {subtitle}""".format(titulo = post_title.text, link = post_link, subtitle = post_subtitle)

# chrome.quit()