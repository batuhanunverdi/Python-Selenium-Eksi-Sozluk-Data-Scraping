from selenium import webdriver
import random
import time
import os


browser = webdriver.Chrome()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
time.sleep(3)
browser.get(url)
lastpages = browser.find_elements_by_class_name("last")
time.sleep(3)
for lastpage in lastpages:
    lastpagecount = int(lastpage.text)

lastpagecount = int(lastpagecount)

time.sleep(1)
pageCount = 1
entries = []
entryCount = 1
while pageCount<=3:
    randomPage = random.randint(1,lastpagecount)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1
    
with open("entries.txt","w",encoding="utf-8") as file:
    for entry in entries:
        file.write(str(entryCount)+ ".\n" + entry + "\n")
        file.write("----------------------------------\n")
        entryCount +=1
browser.close()