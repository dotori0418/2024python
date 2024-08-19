from selenium import webdriver
from selenium.webdriver.common.by import By
import time
dr=webdriver.Chrome()
dr.get("https://time.navyism.com/?host=www.naver.com")
dr.implicitly_wait(0.5)

while True:
    msg=dr.find_element(by=By.ID,value='time_area')
    servertime=msg.text
    print=(msg.text)
    
    if servertime=='2024년 04월 01일 12시 12분 00초':
        break
print('times up')
time.sleep(10)