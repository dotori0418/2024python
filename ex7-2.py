import requests
from bs4 import BeautifulSoup
url='https://time.navyism.com/?host=www.naver.com'
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text, 'html.parser')
result=soap.select('#time_area')
print(result)
