import requests
from bs4 import BeautifulSoup
ymd=input('원하는 날짜를 입력(20240326):')
url=f'https://school.use.go.kr/eonyang-h/M01030601/list?ymd={ymd}'
response=requests.get(url)
# print(response.text)
soap=BeautifulSoup(response.text, 'html.parser')
result=soap.find('a',href=f"/eonyang-h/M01030601/list?ymd={ymd}")
print("20122-이재묵")
print(result.text)
