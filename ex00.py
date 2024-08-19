import requests
from bs4 import BeautifulSoup
url=f'https://school.use.go.kr/eonyang-h/M010301/'
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text, 'html.parser')
result=soap.select('td.tch-nme')
print("20122-이재묵")
print(result)
