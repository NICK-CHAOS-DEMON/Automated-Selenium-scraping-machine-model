from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import re
from selenium import webdriver
browser = uc.Chrome()
browser.get('https://coinatmradar.com/country/226/bitcoin-atm-united-states/')
time.sleep(5)
contents = browser.find_elements(By.CSS_SELECTOR,"h5")
cities=[]
for x in contents:
    a=x.text
    cities.append(a)

print(cities)
for l in cities:
    re.findall("\d+",l)

#
# links=browser.find_elements(By.CSS_SELECTOR,".third [href] ")
# for a in links:
#     print(a.get_attribute('href'))


