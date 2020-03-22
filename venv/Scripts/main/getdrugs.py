from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://reference.medscape.com/drug-interactionchecker')

array_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',  'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
search_field = chrome.find_element_by_xpath("//input[@id='MDICtextbox']")

for alph in array_alphabet:
    search_field.send_keys(alph)
    search_medicine_suggention = WebDriverWait(chrome, 10).until(EC.visibility_of_all_elements_located((
        By.XPATH, "//div[@id='MDICildruglist']//ul[@id='MDICdrugs']//li//a"
    )))
    for item in search_medicine_suggention:
        print(item.text)

    search_field.clear()
