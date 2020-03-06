from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
chrome.get('https://reference.medscape.com/drug-interactionchecker')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

item_list = chrome.find_elements_by_class_name('MDICilfulllist')

search_field = chrome.find_element_by_xpath("//input[@id='MDICtextbox']")
for alph in alphabet:
    search_field.send_keys(alph)

    for item in item_list:
        div = item.find_element_by_class_name('MDICdrugs')
        drug_name = div.get_attribute('a')

        print u"""Nome: {name}""".format(name = drug_name.text)

    search_field.clear()





