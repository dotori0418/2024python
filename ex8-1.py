from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
dr=webdriver.Chrome()
dr.get("https://www.naver.com")
dr.implicitly_wait(0.5)
query_text=f'파묘'
searchbar=dr.find_element(by=By.CSS_SELECTOR,value='#query')
searchbar.send_keys(query_text)
searchbutton=dr.find_element(by=By.ID,value='search-btn')
dr.implicitly_wait(0.5)
searchbutton.click()
temp=dr.find_element(by=By.CSS_SELECTOR,value='.item_title')
print(temp.text)
temp=dr.find_element(by=By.CSS_SELECTOR,value='.item_info')
print(temp.text)
print('20122 leejaemuk')
time.sleep(10)
